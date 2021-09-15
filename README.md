# Project: Computer Vision Kernel
Kernel written fully in Python (with NumPy & SciPy libraries). This is a project based in Signals and Processing Course (ELEC 221) in UBC, Vancouver. See ***project-doc.pdf*** for the framework of this project. Aim of the project is to use Fast Fourier Transform (FFT) to determine the direction of video sweep for a sample GIF file.

## Installing Required Libraries

To install the NumPy, SciPy and Imageio libraries you can run `python -m pip install numpy scipy imageio`

## Running Test Cases Locally

To run the four provided test cases you can run `python test.py`.

## Generating Cross Correlation Images

To generate a cross correlation GIF, run `python make_correlation_video.py <filename of gif>`. This depends on your implementation of the `make_correlation_video` function so if you haven't done that yet it will not do anything.
