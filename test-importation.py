import numpy as np
import imageio as io
import scipy as sp
from scipy import signal

import matplotlib.pyplot as plt

np.random.seed(0)


previous_frame = np.random.randint(255, size=6)
current_frame = np.random.randint(255, size=6)

print("\n\nPrevious Frame: ", previous_frame)
print("Current Frame: ", current_frame)

a1 = previous_frame/255
b1 = current_frame/255

print("\n\nA1: ", a1)
print("B1: ", b1)

# average of a1 & b1
a1b1 = np.concatenate((a1,b1))
average = np.mean(a1b1)

print("Average: ", average)
# normalized arrays
a1_normal = a1 - average
b1_normal = b1 - average

print("Normalized A1: ", a1_normal)
print("Normalized B1: ", b1_normal)
kernel = b1_normal[0:2]
# temp = np.zeros(4)
i=0
temp=np.zeros((4,4))
while i < 3:
    a1_temp = a1_normal[i:(i+3)]
    print(a1_temp)
    temp[i] = sp.signal.correlate(a1_temp, kernel)
    print("Temp: ", temp)

    i = i+1
