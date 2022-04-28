# Shortes path on a height map

## Brief

The algorithm finds the curve with minimal length between two points on a given map.


## Problem Formulation

The height map is given in the form of two dimensional array of nonnegative values. It is convenient to represent it as grey-scaled 8-bit image of dimension $N_x\times N_y$ where black color corresponds zero height while white corresponds the maximal height 255.

A continuius curve $\gamma$ on the map $w$ is a finite sequence of points
$$
    \gamma = (p_1, p_2, \dots, p_{N-1}), \quad p_k = (x_k, y_k)
$$
such that the distance between its neightbour elements equals one:
$$
    |x_{k+1} - x_k| + |y_{k+1} - y_k| = 1.
$$

The algorithm finds the curve $\gamma$ which minimizes the cost function
$$
    \Phi[\gamma] = \sum_{p\in\gamma} w(p) + \sum_{p\in\gamma} 1
$$
unser the assumtion, that the curve never turns back, i.e. 
$$
    y_{k+1} - y_k \geq 0.
$$
The cost function $\Phi[\gamma]$ is composed of two terms. The first one gives the sum of pixels of the height map $w$ the curve $\gamma$ goes through. The second represents the curve length.

Optionally, the initial and final points can be fixed as
$$
    p_0 = (x_0, 0), p_{N-1} = (x_{N-1}, N-1)
$$
Otherwise, the algorithm finds an optimal curve which connects the top side of the image and its bottom.

## Solution
The solution to the formulated problem is based on the Bellman's principle of optimality, so it needs just $O(N_x\times N_y)$ computational operations and about $O(N_x\times N_y)$ additional memory.

# Examples

1. The shortest path with free ends 

    <img src="./doc/map2-l1.svg" width="200"/>

2. The shortest path with fixed ends

    <img src="./doc/map1-l1.svg" width="200"/>

3. The shortest path for randomly generated image

    <img src="./doc/map3-l1.svg" width="200"/>

After little modifications the algorithm can find curves with diagonal junctions. In this case the optimality criteria turns into
$$
    \Phi[\gamma] = \sum_{p\in\gamma} w(p) + \sum_{k=1^{N-1}} \mathbf{dist}(p_k, p_{k-1})
$$
where the distance operator is defined as
$$
    \mathbf{dist}(p_k, p_{k-1}) \equiv \sqrt{(x_k - x_{k-1})^2 + (y_k - y_{k-1})^2} \in \{1, \sqrt{2}\}.
$$
The following examples demonstrate results of the modified algorithm.

4. The shortest path with free ends when diagonal connections allowed

    <img src="./doc/map2-l2.svg" width="200"/>

5. The shortest path with fixed ends when diagonal connections allowed

    <img src="./doc/map1-l2.svg" width="200"/>

6. The shortest path for randomly generated image when diagonal connections allowed

    <img src="./doc/map3-l2.svg" width="200"/>
