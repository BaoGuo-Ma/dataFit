from OtherFile import P, V, CenterPoint, UyAndMagU
from KrigingModel import KrigingPredict
import time

start_time = time.time()
pointFile = 'point'
pFile = 'P'
vFile = 'v'

x, y = CenterPoint(pointFile)
v = V(vFile)
p = P(pFile)

uy = UyAndMagU('Uy')
ux = [0] * len(uy)
newX = ux
newY = uy
newValue = KrigingPredict(x, y, v, newX, newY)
Area = 2.726523199e-8
PressureDrop = ((newValue[0] * 10e-7) / Area) * 1.225
print(PressureDrop)

end_time = time.time()
total_time = end_time - start_time
print(f"The code execution time is：{total_time}s")
