import numpy as np
import matplotlib.pyplot as plt
#does referencing like this work lol
import sys
np.set_printoptions(threshold=sys.maxsize)

image = plt.imread('/Users/liz/Library/CloudStorage/OneDrive-Personal/Desktop/After Glitch/Desktop/385finalproject/Assets/Dog1/AssetsDog.png')

x,y,z = image.shape

zeros = np.zeros((x,y))

##BLACK AND WHITE GENERATOR
# for i in range(len(image)):
#     for j in range(len(image[i])):
#         sum = 0
#         for k in range(3):
#             sum += (image[i][j][k])**2
#         sum = sum/3
#         zeros[i][j] = sum
# print(zeros)

# plt.imshow(zeros,'gray')
# plt.show()

for i in range(len(image)):
    for j in range(len(image[i])):
        for k in range(3):
            if (image[i][j][k]) = 
        sum = sum/3
        zeros[i][j] = sum
print(zeros)