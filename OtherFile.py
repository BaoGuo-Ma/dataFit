import math

import matplotlib.pyplot as plt
import numpy as np


def CenterPoint(file):
    # Reads the file containing the coordinates
    point=[]
    with open(file, 'r') as f:
        for line in f:
            x, y, _ = line.split()
            x = float(x[1:])
            y = float(y)
            point.append((x, y))
    center_x = [coord[0] for coord in point]
    center_y = [coord[1] for coord in point]

    return center_x,center_y

def V(file):
    v = []
    with open(file, 'r') as f:
        for line in f:
            x = float(line.split()[0])
            v.append(x)
    return v

def P(file):
    p = []
    with open(file, 'r') as f:
        for line in f:
            x = line.split()
            p.append(float(x[0]))
    return p

def UyAndMagU(file):
    with open(file,'r')as f:
        MagU=[]
        for line in f:
            data=float(line.split()[0])
            MagU.append(data)
    return MagU

