import numpy as np
def get_matrix(alpha, beta, gamma, num_points):
    """Return the matrix for the internal energy minimization.
    # Arguments
        alpha: The alpha parameter.
        beta: The beta parameter.
        gamma: The gamma parameter.
        num_points: The number of points in the curve.
    # Returns
        The matrix for the internal energy minimization. (i.e. A + gamma * I)
    """
    # Construct a pentadiagonal matrix, A.
    A = np.zeros((num_points, num_points))

    # Fill the main diagonal
    np.fill_diagonal(A, 2 * alpha + 6 * beta)

    # Complete the two adjacent diagonals next to the central diagonal.
    A[np.arange(1, num_points), np.arange(0, num_points - 1)] = -alpha - 4 * beta
    A[np.arange(0, num_points - 1), np.arange(1, num_points)] = -alpha - 4 * beta

    # Fill the second diagonals on either side of the main diagonal
    A[np.arange(2, num_points), np.arange(0, num_points - 2)] = beta
    A[np.arange(0, num_points - 2), np.arange(2, num_points)] = beta

    # Adjust both the first and last rows.
    A[0, -2], A[0, -1], A[1, -1], A[-1, 0], A[-1, 1], A[
        -2, 0] = beta, -alpha - 4 * beta, beta, -alpha - 4 * beta, beta, beta

    # Add gamma * I to A
    A += gamma * np.eye(num_points)

    # Return the inverse of A + gamma * I
    return np.linalg.inv(A)





