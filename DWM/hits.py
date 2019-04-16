import numpy as np
import math

adj_matrix = np.array([[0, 0, 1],
                     [0, 0, 1],
                     [0, 0, 0]])
hub_weight_vector = np.array([1, 1, 1])
adj_matrix_transpose = np.transpose(adj_matrix)
number_of_steps = 3
j = 1
while j <= number_of_steps:
    authority_weight_vector = np.matmul(adj_matrix_transpose, hub_weight_vector)
    auth_norm = (math.sqrt(math.pow(authority_weight_vector[0], 2) + math.pow(authority_weight_vector[1], 2) + math.pow(authority_weight_vector[2], 2)));

    '''For normalization
    authority_weight_vector[0]=authority_weight_vector[0]/auth_norm;
    authority_weight_vector[1]=authority_weight_vector[1]/auth_norm;
    authority_weight_vector[2]=authority_weight_vector[2]/auth_norm;
    Can be generalized using function
    '''

    hub_weight_vector = np.matmul(adj_matrix, authority_weight_vector)
    hub_norm = (math.sqrt(math.pow(hub_weight_vector[0], 2) + math.pow(hub_weight_vector[1], 2) + math.pow(hub_weight_vector[2], 2)));

    '''For normalization
    hub_weight_vector[0]=hub_weight_vector[0]/hub_norm;
    hub_weight_vector[1]=hub_weight_vector[1]/hub_norm;
    hub_weight_vector[2]=hub_weight_vector[2]/hub_norm;
    Cann be generalized using function
    '''

    j = j + 1
print("Authority weight vector: {}".format(authority_weight_vector))
print("Hub weight vector: {}".format(hub_weight_vector))
