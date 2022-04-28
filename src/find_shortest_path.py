import numpy as np
import cv2
import matplotlib.pyplot as plt


def find_shortest_path(weights, x0=None, xf=None):
    '''
        Find the shortest path on the image
            `weight` is an image of type 'uint8' which represents the height map
    '''
    h,w = weights.shape
    S = np.zeros((h,w), dtype=int)
    R = np.zeros((h,w), dtype=int)

    if x0 is None:
        S[0,:] = weights[0,:]
    else:
        S[0,x0+1:] = weights[0,x0] + np.cumsum(weights[0,x0+1:] + 1)
        S[0,0:x0] = np.cumsum(weights[0,0:x0][::-1] + 1)[::-1] + weights[0,x0]
        S[0,x0] = weights[0,x0]

    for y in range(1, h):
        # from left to tight
        prev_x = 0
        weight = S[y-1, prev_x]

        for x in range(w):
            weight = weight + weights[y,x] + 1
            new_weight = S[y-1, x] + weights[y,x] + 1

            if new_weight < weight:
                weight = new_weight
                prev_x = x

            S[y,x] = weight
            R[y,x] = prev_x

        # from right to left
        prev_x = w - 1
        weight = S[y-1, prev_x]

        for x in range(w-1, -1, -1):
            weight = weight + weights[y,x] + 1
            new_weight = S[y-1, x] + weights[y,x] + 1

            if new_weight < weight:
                weight = new_weight
                prev_x = x
            
            if weight < S[y, x]:
                S[y,x] = weight
                R[y,x] = prev_x
    
    if xf is None:
        xfrom = np.argmin(S[-1,:])
    else:
        xfrom = xf

    path = [xfrom]

    for y in range(h-1, 0, -1):
        xfrom = R[y, xfrom]
        path.append(xfrom)

    path = path[::-1]
    return path, S, R

def plot_path(path, **kwargs):
    n = len(path)
    xx = np.zeros(2 * n - 1)
    xx[0::2] = path
    xx[1::2] = path[:-1]
    yy = np.zeros(2 * n - 1)
    yy[0::2] = np.arange(0, n)
    yy[1::2] = np.arange(1, n)
    plt.plot(xx, yy, **kwargs)


def test1():
    '''
        Shortest path with the given initial and final points
    '''
    im = cv2.imread('data/map1.png', 0)
    x0 = 3
    xf = 7
    y0 = 0
    yf = im.shape[0] - 1
    path,S,R = find_shortest_path(im, x0, xf)

    h,w = im.shape
    fig = plt.figure('map1', figsize=(2, 2*h/w), dpi=90)

    plt.imshow(im, cmap='gray', interpolation='nearest')
    plot_path(path, color='red')
    plt.plot([x0, xf], [y0, yf], '*')
    plt.grid(True)
    fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
    fig.savefig('doc/map1-l1.svg')


def test2():
    '''
        Shortest path with free ends
    '''
    im = cv2.imread('data/map2.png', 0)
    path,S,R = find_shortest_path(im)

    h,w = im.shape
    fig = plt.figure('map2', figsize=(2, 2*h/w), dpi=90)
    plt.imshow(im, cmap='gray', interpolation='nearest')
    plot_path(path, color='red')
    plt.grid(True)
    fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
    fig.savefig('doc/map2-l1.svg')


def test3():
    '''
        Shortest path with free ends
    '''
    im = cv2.imread('data/map3.png', 0)
    path,S,R = find_shortest_path(im)

    h,w = im.shape
    fig = plt.figure('map3', figsize=(2, 2*h/w), dpi=90)

    plt.imshow(im, cmap='gray', interpolation='nearest')
    plot_path(path, color='red')
    plt.grid(True)
    fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
    fig.savefig('doc/map3-l1.svg')


if __name__ == '__main__':
    test1()
    test2()
    test3()
    plt.show()