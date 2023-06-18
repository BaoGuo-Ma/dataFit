import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import cdist



def kriging_interpolation(x, y, z, new_x, new_y, nugget=0, sill=1, range_=1):
    """
    Kriging interpolation function

    Parameters:
    x: the x coordinate of a known point, of the shape (n,)
    y: The y coordinate of a known point of shape (n,)
    z: The value of a known point of shape (n,)
    new_x: The x-coordinate of the new point to be predicted, of the shape (m,)
    new_y: The y coordinate of the new point to be predicted, of the shape (m,)
    nugget: nugget effect. The default value is 0
    sill: The sill effect, or variance, defaults to 1
    range_: range argument of the interpolation function, default is 1

    Back:
    new_z: The value of the predicted new point with the shape (m,)
    """

    # n = len(x)
    # m = len(new_x)

    # Computed distance matrix
    dist_matrix = cdist(np.column_stack((x, y)), np.column_stack((x, y)))

    # Calculate the semi-variance function
    cov_matrix = sill - sill * (1 - np.exp(-3 * dist_matrix / range_))

    # Add nugget effect
    np.fill_diagonal(cov_matrix, sill + nugget)

    # Calculate the semi-variance function between the known point and the new point
    dist_new = cdist(np.column_stack((x, y)), np.column_stack((new_x, new_y)))

    # 计算已知点与新点的半方差函数
    cov_new = sill - sill * (1 - np.exp(-3 * dist_new / range_))

    # Calculate the inverse of the semi-variance function matrix
    inv_cov_matrix = np.linalg.inv(cov_matrix)

    # Computed weight matrix
    weights = np.dot(inv_cov_matrix, cov_new)

    # Calculated predicted value
    new_z = np.dot(weights.T, z)

    return new_z


def KrigingPredict(x, y, value, newX, newY):
    z = value

    new_x = np.array(newX)  # The x coordinate of the new point to predict
    new_y = np.array(newY)  # The y coordinate of the new point to predict

    new_z = kriging_interpolation(x, y, z, new_x, new_y)


    plt.scatter(x, y, c=z, cmap='jet', s=6, label='Known Points')
    plt.scatter(new_x, new_y, c=new_z, cmap='jet', s=6, marker='s', label='Predicted Points')
    plt.colorbar(label='Value')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Kriging Interpolation')
    plt.savefig('img.png')
    plt.show()
    return new_z
