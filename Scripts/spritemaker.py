import numpy as np
import matplotlib.pyplot as plt
#does referencing like this work lol
import sys

##CLEAR SPRITE FILE
with open('/Users/liz/OneDrive/Desktop/After Glitch/Desktop/385finalproject/Sprites/sprites.sv', 'w') as spritefile:
    spritefile.write(" \n")
    spritefile.close

##WRITE MODULE DECLARATION
with open('/Users/liz/OneDrive/Desktop/After Glitch/Desktop/385finalproject/Sprites/sprites.sv', 'a') as spritefile:
    spritefile.write("\n module font_rom ( input [10:0]	addr, \n output [7:0]	data \n); \n \n	parameter ADDR_WIDTH = 11; \n   parameter DATA_WIDTH =  8; \n	logic [ADDR_WIDTH-1:0] addr_reg; \n				 \n	// ROM definition				 \n	parameter [0:2**ADDR_WIDTH-1][DATA_WIDTH-1:0] ROM = ")
    spritefile.close

## ITERATE THROUGH SPRITE FILES (change if file order changes)
folder = np.array = ["Dog","Duck","Background"]
numfolders = 2  #number of folders zero indexed
numfiles = [21,3,3] #how many files are in each folder

for i in range(2): #looping through general asset folders (DOG, DUCK, BACKGROUND)
     for j in range(numfiles[i]): #looping through numbered asset files (ASSETDOGn) (THIS HAS TO CHANGE FOR DOG, DUCK, BACKGROUND)
        # print(('/Users/liz/Library/CloudStorage/OneDrive-Personal/Desktop/After Glitch/Desktop/385finalproject/Assets/{}/Assets{}{}.png'.format(folder[i],folder[i],j) ))
        print(j)
        # image = plt.imread('/Users/liz/Library/CloudStorage/OneDrive-Personal/Desktop/After Glitch/Desktop/385finalproject/Assets/{}/Assets{}{}.png'.format(folder[i],folder[i],j))
        image = plt.imread('/Users/liz/Library/CloudStorage/OneDrive-Personal/Desktop/After Glitch/Desktop/385finalproject/Assets/{}/Assets{}{}.png'.format(folder[i],folder[i],j))

        x,y,z = image.shape
        np.set_printoptions(threshold=sys.maxsize, linewidth = y*4)

        bw = np.zeros((x,y))

        ##BLACK AND WHITE GENERATOR
        for i in range(len(image)):
            for j in range(len(image[i])):
                sum = 0
                for k in range(3):
                    sum += (image[i][j][k])**2
                sum = sum/3
                bw[i][j] = sum

        ##COLORMAP GENERATOR
        colormap = np.zeros((x,y))

        for i in range(len(bw)):
            for j in range(len(bw[i])):
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
                    if (bw[i][j]) > 0.536 and (bw[i][j]) < .537: #BLUE
                        colormap[i][j] = 7
                    # if (image[i][j]) == 0: #LIGHTGREEN
                    #      image[i][j] == 8    
                    # if (image[i][j]) == 0: #DARKGREEN
                    #      image[i][j] == 9
                    # if (image[i][j]) == 0: #PALEGREEN
                    #      image[i][j] == 10
                    # if (image[i][j]) == 0: #RED
                    #      image[i][j] == 11
        print(colormap)
        colormapstr = np.array2string(colormap)
        with open('/Users/liz/OneDrive/Desktop/After Glitch/Desktop/385finalproject/Sprites/sprites.sv', 'a') as spritefile:
            spritefile.write(colormapstr)
            spritefile.close


with open('/Users/liz/OneDrive/Desktop/After Glitch/Desktop/385finalproject/Sprites/sprites.sv', 'a') as spritefile:
    spritefile.write("}; \n \n	assign data = ROM[addr]; \n \n endmodule  ")
    spritefile.close