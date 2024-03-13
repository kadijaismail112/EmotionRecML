"""
Utility functions for loading and plotting datasets.
"""

# import matplotlib.pyplot as plt
import numpy as np


# def plot(x, y, theta, save_path, correction=1.0):
#     """Plot dataset and fitted logistic regression parameters.

#     Args:
#         x: Matrix of training examples, one per row.
#         y: Vector of labels in {0, 1}.
#         theta: Vector of parameters for logistic regression model.
#         save_path: Path to save the plot.
#         correction: Correction factor to apply, if any.
#     """
#     # Plot dataset
#     plt.figure()
#     plt.plot(x[y == 1, -2], x[y == 1, -1], 'bx', linewidth=2)
#     plt.plot(x[y == 0, -2], x[y == 0, -1], 'go', linewidth=2)

#     # Plot decision boundary (found by solving for theta^T x = 0)
#     x1 = np.arange(min(x[:, -2]), max(x[:, -2]), 0.01)
#     x2 = -(theta[0] / theta[2] + theta[1] / theta[2] * x1
#            + np.log((2 - correction) / correction) / theta[2])
#     plt.plot(x1, x2, c='red', linewidth=2)
#     plt.xlim(x[:, -2].min()-.1, x[:, -2].max()+.1)
#     plt.ylim(x[:, -1].min()-.1, x[:, -1].max()+.1)

#     # Add labels and save to disk
#     plt.xlabel('x1')
#     plt.ylabel('x2')
#     plt.savefig(save_path)

def preprocess_data(data):
    width, height = 48, 48
    datapoints = data['pixels'].tolist()
    faces = []
    for pixel_sequence in datapoints:
        face = [int(pixel) for pixel in pixel_sequence.split(' ')]
        face = np.asarray(face).reshape(width, height)
        faces.append(face.astype('float32'))
    faces = np.asarray(faces)
    faces = np.expand_dims(faces, -1)
    emotions = data['emotion'].values
    return faces, emotions

# def split_dataset(faces, emotions, validation_ratio=0.1):

#     return X_train_oversampled, y_train_oversampled, X_test, y_test, X_eval, y_eval