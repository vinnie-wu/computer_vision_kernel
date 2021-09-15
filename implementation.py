import imageio as io
import numpy        as np
import scipy.signal as sp
from scipy.interpolate import interp1d


def correlate_adjacent_frames( previous_frame, current_frame ):
    # '''
    #     This function takes in two NumPy arrays filled with uint8 (integers between 0 and 255 inclusive) of size 160 by 160 and returns a
    #     NumPy array of uint8 that represents `previous_frame` being cross correlated with a convolutional kernel of size 110 by 110 created
    #     by removing the first and last 25 pixels in each dimension from `current_frame`.
    #
    #     The array returned should be of size 110 by 110 but the elements that are dependent on values "outside" the provided pixels of
    #     `previous_frame` should be set to zero.
    #
    #     Before computing the cross-correlation, you should normalize the input arrays in the range 0 to 1 and then subtracting the mean pixel
    #     value of both inputs (i.e. the mean value of the list created by concatenating all pixel intensities of `current_frame` and all pixel
    #     intensities of `previous_frame`)
    # '''
    # transform [0-255] --> [0-1]
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
    result = sp.correlate2d(a1_normal,b1s,mode='valid')
    # -- converting MOST NEGATIVE number --> 0, and MOST POSITIVE number --> 255
    normalized_result = (255*(result - np.min(result))/np.ptp(result)).astype(np.int)
    return normalized_result

def make_correlation_video( input_filename, output_filename=None ):
    # '''
    #     This function takes in an input filename string of a GIF and an optional output filename string. It should read the video from the input filename
    #     using the mimread function from imageio and then apply correlate_adjacent_frames to each pair of adjacent frames
    #     (i.e. between frame 0 and frame 1 then frame 1 and frame 2, and so on) to create a video (list of frames) with one less frame than the number of
    #     frames in the input GIF.
    #
    #     If the output_filename is present (i.e. is not None), it should then write the resulting frames into a GIF located at the output filename string
    #     using the mimwrite function from imageio, then in either case the function should return the video as a three-dimensional NumPy array.
    #
    #     You may assume the file located at input_filename is in a fact a GIF (you do not need to handle the error condition where it is some other file type)
    #
    #     Note: In this context a 'video' is a three-dimensional NumPy array that can best be thought of as a list of two-dimensional 'frames' which are
    #     NumPy arrays.
    #
    #     While debugging the last function, you can view these GIF outputs using a web browser or image viewer, they are just regular GIFs.

    # ------ reading GIF file ----------#
    gif_file_original = io.mimread(input_filename)
    gif_length = len(gif_file_original)
    newGif = np.zeros((gif_length-1,51,51))
    i = 0
    while i < (gif_length-1):
        previous_frame = gif_file_original[i]
        current_frame = gif_file_original[i+1]
        newGif[i] = correlate_adjacent_frames( previous_frame, current_frame )
        i = i+1
    io.mimwrite("PERSONAL-new-Gif.gif", newGif.astype(np.uint8))
    return newGif

def is_triangular_path( filename ):
    #     1. Use mimread to load filename into GIF file
    #     2. Use make_correlation_video to get a 3D NumPy array,
    #     3. Apply heuristic to determine if this is a triangular path video from a square path video.
    # main_gif_file = io.mimread(filename)
    newGif = np.asarray(make_correlation_video(filename))
    i=0
    white_dot_position = np.zeros((len(newGif)-1,2,2))
    # -- Populate white dots indexes
    while i<(len(newGif)-1):
        white_dot_position[i] = np.unravel_index(np.argmax(newGif[i], axis=None), newGif[i].shape)
        i = i+1
    # -- store and analyze white dot indexes into VERTEXES
    uniqueVertexes = np.unique(white_dot_position)
    if len(uniqueVertexes) <= 4:
        return False
    else:
        return True
