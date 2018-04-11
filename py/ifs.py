import numpy as np
import matplotlib.pyplot as plt
import math
import argparse

# Applies an affine transformation and returns the result as a tuple.
def applyIFSTransformation(a, b, c, d, e, f, x, y):
    coeffMatrix = np.array([[a, b], 
                            [c, d]])
    additive = np.array([[e], [f]])
    paramMatr = np.array([[x], [y]])
    transformedParams = np.add(coeffMatrix.dot(paramMatr), additive)
    return (transformedParams[0][0], transformedParams[1][0])
    
# The typical IFS producing the fern fractal as described by Williams 136.
def barnsleyFernIFS(x, y):
    T1 = [
        (0.86, 0.03, -0.03, 0.86),
        (0.2, -0.25, 0.21, 0.23),
        (-0.15, 0.27, 0.25, 0.26),
        (0, 0, 0, 0.17)
        ]
    T2a = [
        (0, 1.5),
        (0, 1.5),
        (0, 0.45),
        (0, 0)
        ]

    P = [0.83, 0.08, 0.08, 0.01]
    choice = np.random.choice(4, p = P)
    coeff = T1[choice]
    tranls = T2a[choice]
    return applyIFSTransformation(coeff[0], coeff[1], coeff[2], coeff[3], tranls[0], tranls[1], x, y)

# The other typical IFS producing the classic Sierpinski Triangle as described by Larry Riddle at
# 
def sierpinskiTriangleIFS(x, y):
    T1 = [
        (0.5, 0, 0, 0.5),
        (0.5, 0, 0, 0.5),
        (0.5, 0, 0, 0.5),
        ]
    T2a = [
        (0, 0),
        (0.5, 0),
        (0.25, 0.433)
        ]

    P = [0.33, 0.33, 0.34]
    choice = np.random.choice(3, p = P)
    coeff = T1[choice]
    add = T2a[choice]
    return applyIFSTransformation(coeff[0], coeff[1], coeff[2], coeff[3], add[0], add[1], x, y)

# And IFS producing the Koch curve fractal as described by Larry Riddle at
# http://ecademy.agnesscott.edu/~lriddle/ifs/kcurve/kcurve.htm
def kochCurveIFS(x, y):
    T1 = [
        (0.33, 0, 0, 0.33),
        (0.166, -0.287, 0.287, 0.166),
        (0.166, 0.287, -0.287, 0.166),
        (0.33, 0, 0, 0.33)
        ]
    T2a = [
        (0, 0),
        (.333, 0),
        (0.5, .287),
        (.666, 0)
        ]

    P = [0.25, 0.25, 0.25, 0.25]
    choice = np.random.choice(len(T1), p = P)
    coeff = T1[choice]
    add = T2a[choice]
    return applyIFSTransformation(coeff[0], coeff[1], coeff[2], coeff[3], add[0], add[1], x, y)

# An IFS producing our Arrow fractal as described in our paper.
def arrowIFS(x, y):
    T1 = [
        (0.75, 0, 0, 0.75),
        (0, -0.375, 0.375, 0),
        (0, 0.375, -0.375, 0),
        ]
    T2a = [
        (0.125, 0.125),
        (0.5, 0.125),
        (0.5, 0.5)
        ]

    P = [0.33, 0.33, 0.34]
    choice = np.random.choice(len(T1), p = P)
    coeff = T1[choice]
    add = T2a[choice]
    return applyIFSTransformation(coeff[0], coeff[1], coeff[2], coeff[3], add[0], add[1], x, y)

# Unused attempt at making the binary tree IFS as described by Larry Riddle at 
# http://ecademy.agnesscott.edu/~lriddle/ifs/pythagorean/symbinarytree.htm.
def binTreeIFS(x, y, r, theta):
    T1 = [
        (r * math.cos(theta), r * -math.sin(theta), r * math.sin(theta), r * math.cos(theta)),
        (r * math.cos(theta), r * math.sin(theta), r * -math.sin(theta), r * math.cos(theta)),
        (1, 0, 0, 1),
        ]
    T2a = [
        (0, 1),
        (0, 1),
        (0, 0),
        ]

    P = [0.5, 0.25, 0.25]
    choice = np.random.choice(len(T1), p = P)
    coeff = T1[choice]
    add = T2a[choice]
    return applyIFSTransformation(coeff[0], coeff[1], coeff[2], coeff[3], add[0], add[1], x, y)

# Routine for plotting a given IFS for a given amount of rounds.
def plotIFS(ifs, rounds):
    fun = None
    if ifs == 'fern':
        fun = barnsleyFernIFS
    elif ifs == 'triangle':
        fun = sierpinskiTriangleIFS
    elif ifs == 'koch':
        fun = kochCurveIFS
    elif ifs == 'arrow':
        fun = arrowIFS
    else: return
    
    x = 0
    y = 0
    
    for _ in range(0, rounds):
        x, y = fun(x, y)
    #     x, y = binTreeIFS(x, y, 0.7, 1.047)
        plt.plot(x, y, 'r.', markersize=1, antialiased=False)
    
    try: plt.show()
    except: pass

# Main function parses arguments and hands them off to `plotIFS`.
def main():
    parser = argparse.ArgumentParser(description="Plot iterated function system (IFS).")
    parser.add_argument('function', metavar='IFS', type=str, nargs=1, choices=['fern', 'triangle', 'koch', 'arrow'],
                   help='the function to plot. options: {fern, triangle, square, koch, arrow}')
    parser.add_argument('--rounds', dest='R', type=int, default=20000,
                   help='the number of iterations to complete (default: 20000)')
    args = parser.parse_args()
    plotIFS(args.function[0], args.R)
    
if __name__ == "__main__":
    main()