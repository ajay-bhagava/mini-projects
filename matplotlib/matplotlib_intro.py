import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])
ypoints_1 = np.array([6,10,3,15,1])
'''
plt.plot(xpoints, ypoints)
plt.show()

# use 'o' to plot without lines
plt.plot(xpoints, ypoints)
plt.show()

# x points default to [0,1,2,3,....]
# marker argument allows each point to have a specified marker
plt.plot(ypoints_1, marker = '*')
plt.show()


# formatted strings provide a shorthand way to format the plot
# format is: "marker|line_style|color"
# in this case, marker is o, line is : (dashed), and color is red

plt.plot(ypoints_1, "o:r")
plt.show()
'''

# marker size (shorthand ms)
# marker edge color (shorthand mec)
# marker face color (shorthand mfc)
# can also use hex codes for the colors

# line style (shorthand ls)
# line color (shorthand c)
# line width (shorthand lw)

# plot multiple lines on the same graph using multiple plt plots and using plt.show() after
plt.plot(ypoints_1, ls="--",c="#000000",lw="4",ms=20, mec="b", mfc="g")
plt.plot(ypoints, '*--',c="#f791ca")
plt.show()

# example with more lines
# plt.plot will take pairs and plot them as x and y values
# can create labels using xlabel and ylabel
# use title() to create a title
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Title")

plt.plot(x1, y1, x2, y2)
plt.show()


# to specify fonts, create a dictionary with the font, color, and size
# then add the "fontdict=" tag to a label
# use loc to specify the position of the labels
font1 = {'family':'serif','color':'blue','size':20}
plt.title("Sports Watch Data", fontdict = font1, loc = "left")
plt.plot(x1, y1, x2, y2)
# add gridlines, can specify which axis, no input will do both axes, 
# can also style gridlines
plt.grid(axis="y",color="green",linestyle="--",linewidth=0.5)
plt.show()



	
