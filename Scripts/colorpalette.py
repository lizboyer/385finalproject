import math

with open("colorscripty.txt", "r") as colorfile:    #imports color r g b file
    colortext = colorfile.read()

colortext = colortext.split("\n")   #formats color r g b file
for i in range(len(colortext)):
    colortext[i] = colortext[i].split(" ")

for i in range(len(colortext)): #strings into ints, rounds to 12-bit coloration rather than 24-bit
    for j in range(len(colortext[i])):
        if (j>0):
            colortext[i][j] = int(colortext[i][j])
            colortext[i][j] = math.floor(colortext[i][j] / 16)


# colors = {}

# black = 0
# white = 1
# green = 2
# pink = 3
# lightbrown = 4
# darkbrown = 5
# tan = 6
# blue = 7
# lightgreen = 8
# darkgreen = 9
# palegreen = 10
# red = 11

# colors[0] = ()
# colors[1] = ()
# colors[2] = ()
# colors[3] = ()
# colors[4] = ()
# colors[5] = ()
# colors[6] = ()
# colors[7] = ()
# colors[8] = ()
# colors[9] = ()
# colors[10] = ()
# colors[11] = ()

# black = {255,255,255}
# white = {R:,G:,B:}
# green = {R:,G:,B:}
# pink = {R:,G:,B:}
# lightbrown = {R:,G:,B:}
# darkbrown = {R:,G:,B:}
# tan = {R:,G:,B:}
# blue = {R:,G:,B:}
# lightgreen = {R:,G:,B:}
# darkgreen = {R:,G:,B:}
# palegreen = {R:,G:,B:}
# red = {R:,G:,B:}

# Green: 
# 	R:21 0001 
# 	G:58 0011 
# 	B:10 0000 
# Pink:
# 	R:240
# 	G:120
# 	B:103
# Brown(Light): 
# 	R:146 
# 	G:78
# 	B:27
# Brown(Dark): 
# 	R:76
# 	G:35
# 	B:8
# Tan:
# 	R:242
# 	G:215
# 	B:171
# Blue:
# 	R:115
# 	G:173
# 	B:171
# Light Green:
# 	R:157
# 	G:211
# 	B:65
# Dark Green:
# 	R:33
# 	G:80
# 	B:18
# Green Score Text: 
# 	R:146
# 	G:204
# 	B:35
# Red Duck Meter:
# 	R:167
# 	G:59
# 	B:43
