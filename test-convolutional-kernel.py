
import numpy as np
import imageio as io
import scipy as sp
from scipy import signal
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

original_gif = io.mimread("assets/tree-cover-square-path-0.gif")

previous_frame = original_gif[0]
current_frame = original_gif[1]
a1 = previous_frame/255
b1 = current_frame/255
a1b1 = np.concatenate((a1,b1))
average = np.mean(a1b1)

# normalized arrays
a1_normal = a1 - average
b1_normal = b1 - average
print("a1_normal: ", a1_normal)
print("b1_normal: ", b1_normal)
# Convolutional Kernel
b1s = b1_normal[25:135, 25:135]
result = sp.signal.correlate2d(a1_normal,b1s,mode='valid')
print("result: ", result)
# -- converting MOST NEGATIVE number --> 0, and MOST POSITIVE number --> 255
normalized_result = (255*(result - np.min(result))/np.ptp(result)).astype(int)
print("Normalized (0-255) Result: ", normalized_result)
white_dot_position = np.unravel_index(np.argmax(normalized_result, axis=None), normalized_result.shape)
print("White dot position: ", white_dot_position)
print("White dot value: ", normalized_result[white_dot_position])
io.imwrite("PERSONAL-test-image-kernel-NORMALIZED-RESULT.jpg",normalized_result)
