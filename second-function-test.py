import imageio as io
import numpy        as np
import scipy as sp
from scipy import signal
from scipy.interpolate import interp1d

def correlate_adjacent_frames( previous_frame, current_frame ):
    a1 = previous_frame/255
    b1 = current_frame/255
    # average of a1 & b1
    a1b1 = np.concatenate((a1,b1))
    average = np.mean(a1b1)
    # normalized arrays
    a1_normal = a1 - average
    b1_normal = b1 - average
    # -----CLEANUP FINISHED-----------------------------
    # Convolutional Kernel
    b1s = b1_normal[25:135, 25:135]
    result = sp.signal.correlate2d(a1_normal,b1s,mode='valid')
    # -- converting MOST NEGATIVE number --> 0, and MOST POSITIVE number --> 255
    normalized_result = (255*(result - np.min(result))/np.ptp(result)).astype(np.uint8)
    return normalized_result

def make_correlation_video(file_path):
    gif_file_original = io.mimread(file_path)
    i = 0
    gif_length = len(gif_file_original)
    print(gif_length)
    newGif = np.zeros((gif_length-1,51,51))
    while i < (gif_length-1):
        previous_frame = gif_file_original[i]
        current_frame = gif_file_original[i+1]
        newGif[i] = correlate_adjacent_frames( previous_frame, current_frame ).astype(np.uint8)
        # print("Loop: ",i)
        i = i+1
    io.mimwrite("PERSONAL-new-Gif.gif", newGif.astype(np.uint8))
    return newGif

GIF_file_name = "assets/tree-cover-square-path-1.gif"
newGif = np.asarray(make_correlation_video(GIF_file_name))
# Now time to find vertexes of white dots!
i=0
white_dot_position = np.zeros((len(newGif)-1,2,2))
# -- Populate white dots indexes
while i<(len(newGif)-1):
    white_dot_position[i] = np.unravel_index(np.argmax(newGif[i], axis=None), newGif[i].shape)
    print("White dot position: ", white_dot_position[i])
    i = i+1
uniqueVertexes = np.unique(white_dot_position)
print(unique)
# -- store and analyze white dot indexes into VERTEXES
