import numpy as np
import matplotlib.pyplot as plt

toplist = np.array([
    0, 0, 1, 3, 5,
    7, 9, 12, 14, 18,
    20, 23, 27, 30, 33,
    37, 41, 43, 46, 50,
    54, 57, 60, 64, 68,
    72, 76, 81, 85, 89,
    93
    ])

def get_vertices(beam_coefficients) -> np.ndarray:
    global bases
    return np.array(beam_coefficients@bases.T)

def compute_adjMatrix(beam_coefficients) -> np.ndarray:
    return np.isclose(np.abs(get_vertices(beam_coefficients)[None,:] - get_vertices(beam_coefficients)[:,None]), 1)

def draw(beam_coefficients) -> None:
    # def compute_adjMatrix(beam_coefficients):
    #     return np.isclose(np.abs(get_vertices(beam_coefficients)[None,:] - get_vertices(beam_coefficients)[:,None]), 1)
    
    def compute_num_of_edges(beam_coefficients) -> int:
        return int(np.sum(compute_adjMatrix(beam_coefficients)) / 2)
    
    vertices = get_vertices(beam_coefficients)
    adjMatrix = compute_adjMatrix(beam_coefficients)
    size = len(adjMatrix)
    plt.rcParams["figure.figsize"] = (6,6)
    plt.title(f"Number of vertices = {len(beam_coefficients)}. Number of edges = {compute_num_of_edges(beam_coefficients)}.\nLargest known number of edges = {toplist[len(beam_coefficients)]}.")

    # draw edges
    for i in range(size):
        for j in range(i+1, size):
            if adjMatrix[i][j]:
                plt.plot([vertices[i].real, vertices[j].real],
                [vertices[i].imag, vertices[j].imag], c='black', linewidth = 0.3)

    # draw vertices
    x_axis = [x.real for x in vertices]
    y_axis = [x.imag for x in vertices]
    plt.plot(x_axis, y_axis, '.', color='red', ms=10)
    plt.xlim(min(x_axis)-0.5, max(x_axis)+0.5)
    plt.ylim(min(y_axis)-0.5, max(y_axis)+0.5)
    plt.show()