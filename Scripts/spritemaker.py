import numpy as np
import matplotlib.pyplot as plt
#does referencing like this work lol
import sys
np.set_printoptions(threshold=sys.maxsize)

image = plt.imread('/Users/liz/Library/CloudStorage/OneDrive-Personal/Desktop/After Glitch/Desktop/385finalproject/Assets/Dog1/AssetsDog.png')

x,y,z = image.shape

bw = np.zeros((x,y))

##BLACK AND WHITE GENERATOR
for i in range(len(image)):
    for j in range(len(image[i])):
        sum = 0
        for k in range(3):
            sum += (image[i][j][k])**2
        sum = sum/3
        bw[i][j] = sum
# print(bw)

# plt.imshow(bw)
# plt.show()

colormap = np.zeros((x,y))

for i in range(len(bw)):
    for j in range(len(bw[i])):
            # print(bw[i][j])
            # colormap [i][j] = bw[i][j]
            if (bw[i][j]) < 0.00001:  #BLACK
                 colormap[i][j] = 0
            if (bw[i][j]) > 0.99 and (bw[i][j]) < 1.001: #WHITE
                 colormap[i][j] = 1
            # if (image[i][j]) == 0: #GREEN
            #      image[i][j] == 2
            # if (image[i][j]) == 0: #PINK
            #      image[i][j] == 3
            if (bw[i][j]) > 0.152 and (bw[i][j]) < .153: #LIGHTBROWN
                 colormap[i][j] = 4
            if (bw[i][j]) > 0.0400 and (bw[i][j]) < 0.0401: #DARKBROWN
                 colormap[i][j] = 5
            # if (image[i][j]) == 0: #TAN
            #      image[i][j] == 6
            if (bw[i][j]) == 0.5369986: #BLUE
                 colormap[i][j] = 7
            # if (image[i][j]) == 0: #LIGHTGREEN
            #      image[i][j] == 8    
            # if (image[i][j]) == 0: #DARKGREEN
            #      image[i][j] == 9
            # if (image[i][j]) == 0: #PALEGREEN
            #      image[i][j] == 10
            # if (image[i][j]) == 0: #RED
            #      image[i][j] == 11

        # sum = sum/3
        # zeros[i][j] = sum
print(colormap)
