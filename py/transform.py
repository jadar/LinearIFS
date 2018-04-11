import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

def applyTransformation(input_points, a, b, c, d, e, f):
    output_points = []
    coeffMatrix = np.array([[a, b], 
                            [c, d]])
    additive = np.array([[e], [f]])
    
    for point in input_points:
        paramMatr = point.transpose()
        transformedParams = np.add(coeffMatrix.dot(paramMatr), additive)
        output_points.append([transformedParams[0][0], transformedParams[0][1]])
    return np.array(output_points)

start_rect = np.array([
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0]
    ])

reps = 4

fig = plt.figure()
ax = fig.add_subplot(111)

fix, ax = plt.subplots()

rect = start_rect

for i in range(0,reps):
    rect = applyTransformation(rect, 0.86, 0.03, -0.03, 0.86, 0, 1.5)
    poly = patches.Polygon(rect, lw=2, fc='none')
    ax.add_patch(poly)

ax.set_xlim(auto=True)
ax.set_ylim(auto=True)
plt.show()
