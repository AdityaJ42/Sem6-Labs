import numpy as np
transition_matrix = np.array([[0, 0, 0, 0.25, 1, 0.33],
                           [0.33, 0, 0, 0, 0, 0.33],
                           [0.33, 0.25, 0, 0.25, 0, 0],
                           [0, 0.25, 0.5, 0, 0, 0],
                           [0, 0.25, 0.5, 0.25, 0, 0.33],
                           [0.33, 0.25, 0, 0.25, 0, 0]])
temp1 = transition_matrix
page_rank_vector = np.array([0.167, 0.167, 0.167, 0.167, 0.167, 0.167])
var = np.array([])
temp = transition_matrix
j = 1
while(j <= 5):
    page_rank_vector = transition_matrix.dot(page_rank_vector)
    page_rank_vector = np.around(page_rank_vector, decimals=3)
    transition_matrix = np.matmul(transition_matrix, temp1)
    transition_matrix = np.around(transition_matrix, decimals=3)
    if np.array_equal(page_rank_vector, var):
        break
    var = page_rank_vector
    j = j + 1
print("Page Rank Vector:")
print(page_rank_vector)
