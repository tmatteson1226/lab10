##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=800, background='white')
drawpad.grid(row=0, column=1)
#creating the house
square = drawpad.create_rectangle(200,200,600,600, fill='red')
#creating the roof
line1 = drawpad.create_line(200,200,400,0)
line2 = drawpad.create_line(400,0,600,200)
#making door
square2 = drawpad.create_rectangle(375,600,425,500, fill='brown')
#making windows
window1 = drawpad.create_rectangle(250,250,350,350, fill='white')
window2 = drawpad.create_rectangle(450,250,550,350, fill='white')
root.mainloop()