#import reqiure packages
import tkinter as tk
import time
import math

# creating a root window to work on it
root = tk.Tk()
root.geometry('400x400')
root.title("Analog clock")
root.iconphoto(False, tk.PhotoImage(file='clock2.png'))

# defining our function to update the clock value
def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

	# change the ending co-ordinates from we have (295,295)
	# putting the formula x = r * sin(radians(t)) 
	# and y = r * cos(radians(t))
	# 360/60 sec = 6 radian

    seconds_x = second_line_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * second_line_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(second_line, center_x, center_y, seconds_x, seconds_y)
	
		# doing same thing for hour and minutes
    minutes_x = minute_line_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minute_line_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minute_line, center_x, center_y, minutes_x, minutes_y)
	

    hours_x = hours_line_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_x
    hours_y = -1 * hours_line_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_y
    canvas.coords(hour_line, center_x, center_y, hours_x, hours_y)

	
	# update the clock value
    root.after(1000, update_clock)



# create a canvas to draw clock on the window size
canvas = tk.Canvas(root,width=400,height=400,bg="black")
canvas.pack(expand=True,fill='both')

# create a background clock image in background
bg = tk.PhotoImage(file="analog.png")
# add bg to canvas container and this point in center of the clock to rotate lines
canvas.create_image(200,200,image=bg)

# creating mid point of the clock using variable
center_x = 200
center_y = 200
second_line_len = 95
minute_line_len = 80
hours_line_len = 50

# Moving our seconds_line in the clock
# create line take 4 perameter center and length of perameter 
second_line = canvas.create_line(200,200,200+second_line_len,200+second_line_len,width=1.5,fill='red')
minute_line = canvas.create_line(200,200,200+minute_line_len,200+minute_line_len,width=2.5,fill='white')
hour_line = canvas.create_line(200,200,200+hours_line_len,200+hours_line_len,width=4,fill='yellow')



update_clock()

root.mainloop()
