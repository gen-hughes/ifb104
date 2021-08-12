
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 2, 2021.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 11000031 # put your student number here as an integer
student_name   = "Genevieve Hughes" # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  LOCKDOWN
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "track_entities".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various symbols, using data stored in a list to
#  determine which symbols to draw and where.  See the various
#  "client briefings" in Blackboard for full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by the client.
#  This single template file will be used for all parts and you will
#  submit your final solution as a single Python 3 file only, whether
#  or not you complete all requirements for the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You must NOT change
# any of the code in this section.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless
# instructed.
cell_size = 100 # pixels (default is 100)
grid_width = 8 # squares (default is 8)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.5 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 5, 'normal') # font for the coords
big_font = ('Arial', cell_size // 4, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 7, 'Grid must be at least 7 squares wide'
assert (grid_height >= 5) and (grid_height % 2 != 0), \
       'Grid must be at least 5 squares high and height must be odd'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          label_spaces = True): # NO! DON'T CHANGE THIS!
    
    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(str(x_label + 1), align = 'right', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 5, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(chr(y_label + ord('A')), align = 'center', font = small_font)

        # Mark the two "special" cells
        goto(-cell_size * grid_width // 2 + 0.5 * cell_size, 0)
        dot(cell_size // 6)
        goto(cell_size * grid_width // 2 - 0.5 * cell_size, 0)
        dot(cell_size // 6)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1.15) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ntwo states of\nyour first\nentity here', align = 'right', font = big_font)    
        # Right side
        goto(((grid_width + 1.15) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ntwo states of\nyour second\nentity here', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "track_entities" function.  ALL of your solution code
#  must appear in, or be called from, function "track_entities".  Do
#  NOT put any of your code in other parts of the program and do NOT
#  change any of the provided code except as allowed in the main
#  program below.
#

# All of your code goes in, or is called from, this function
def track_entities(replace_me):
    #-------------variables-------------------#

    #------------colours----------------#
    # box_one = 'orange'
    box_two = '#a2f1a2'
    # box_three = 'green'
    # box_four = 'blue'
    # cb_shirt = 'yellow'
    outline = 'black'
    cb_body = '#FFDAB9'
    cb_hat = 'white'
    cb_bag = '#a37e5d'
    
    #-------initialising-----------#
    width(3)

    #------------positioning---------------#
    #edge of boxes
    #goes backwards past the four cells horizontally, and adds some extra space
    side_margin = cell_size*4 + cell_size/1.5
    #goes up half a cell
    top_margin = cell_size/2

    #setting the coordinates to be changed easily
    #the x position has the cell_size subtracted so that the turtle ends up in the bottom left hand corner of the square
    x_pos_one = -side_margin - cell_size
    y_pos_one = top_margin
    y_pos_two = -top_margin - cell_size
    x_pos_two = side_margin + cell_size/4

    #----------drawing coordinates----------#
    draw_x_pos_one = x_pos_one + 40
    #where cb body starts
    draw_x_pos_two = x_pos_one + 5
    #head level
    draw_y_pos_one = y_pos_one + 30
    #hat coords
    draw_x_pos_three = x_pos_one + 75
    draw_y_pos_two = y_pos_one + 62

    #text
    text_y_pos_one = y_pos_one + 2*cell_size

    #cb two
    draw_x_pos_four = x_pos_one+15
    #cb hat
    draw_y_pos_three = y_pos_two + 30
    #eyes
    dot_x_pos_one = x_pos_one + 30
    dot_y_pos_one = y_pos_two + 65
    dot_x_pos_two = dot_x_pos_one + 20

    #-----------body dimensions-----------#
    #variables
        #cb one
    cb_body_rad = 35
    cb_head_rad = 32
    cb_hat_rad = 35
        #cb two
    cb_bag_height = 65
    cb_bag_width = 35

    #----------functions----------#
    #square function
    def square(length,colour):
        begin_fill()
        color('black', colour)
        setheading(0)
        for i in range(4):
            forward(length)
            left(90)
        end_fill()

    #ellipse function
    def ellipse(rad,heading):
        setheading(0)
        for i in range(2):
            circle(rad,90)
            circle(rad//2,90)
        #tilting the shape
        seth(heading)

    #little triangles for shirt
    def triangle(num):
        setheading(0)
        for i in range(num):
            left(45)
            forward(10)
            right(90)
            forward(10)
            setheading(0)

    def rectangle(length,width,colour):
        setheading(0)
        begin_fill()
        color(outline,colour)
        for i in range(2):
            forward(length)
            left(90)
            forward(width)
            left(90)
        end_fill()

    #-----------drawing-----------#

    #-----------charlie brown one----------#

    goto(x_pos_one,text_y_pos_one)
    style = ('Courier', 10)
    write('Charlie Brown', font=style, align='center')

    ##first square
    goto(x_pos_one,y_pos_one)
    pendown()
    square(cell_size, 'orange')
    penup()

    #charlie body
    goto(draw_x_pos_two,y_pos_one)
    pendown()
    color('black','yellow')
    begin_fill()
    right(90)
    circle(cb_body_rad,-180)
    end_fill()
    penup()

    #stripes
    goto(draw_x_pos_two,y_pos_one)
    pendown()
    color('black')
    begin_fill()
    triangle(5)
    end_fill()
    penup()

    #head
    goto(draw_x_pos_one,draw_y_pos_one)
    pendown()
    pencolor(outline)
    fillcolor(cb_body)
    begin_fill()
    circle(cb_head_rad)
    end_fill()
    penup()

    #hat
    goto(draw_x_pos_three,draw_y_pos_two)
    right(-90)
    pendown()
    pencolor(outline)
    fillcolor(cb_hat)
    begin_fill()
    circle(cb_hat_rad,180)
    end_fill()
    #hat line
    goto(draw_x_pos_three,draw_y_pos_two)
    penup()
    setheading(180)
    forward(cb_hat_rad*2)
    setheading(0)
    pendown()
    width(3)
    forward(cb_hat_rad*2+20)
    pencolor(outline)
    penup()


    #-----------charlie brown two----------#
    #second square
    goto(x_pos_one,y_pos_two)
    pendown()
    pendown()
    square(cell_size, box_two)
    penup()

    #body (same design but red)
    goto(draw_x_pos_two,y_pos_two)
    pendown()
    color('black','red')
    begin_fill()
    right(90)
    circle(cb_body_rad,-180)
    end_fill()
    penup()

    #stripes
    goto(draw_x_pos_two,y_pos_two)
    pendown()
    color('black')
    begin_fill()
    triangle(5)
    end_fill()
    penup()

    #bag
    color(outline,cb_bag)
    goto(draw_x_pos_two,draw_y_pos_three)
    pendown()
    begin_fill()
    setheading(0)
    left(75)
    forward(cb_bag_height)
    setheading(0)
    forward(cb_bag_width)
    right(75)
    forward(cb_bag_height)
    goto(draw_x_pos_two,draw_y_pos_three)
    end_fill()
    penup()

    #eyes
    goto(dot_x_pos_one,dot_y_pos_one)
    dot(15,outline)
    goto(dot_x_pos_two,dot_y_pos_one)
    dot(15,outline)
    


    #-----------snoopy one----------#
    #third square
    goto(x_pos_two,y_pos_one)
    pendown()
    square(cell_size, 'green')
    penup()

    #plane
    # pendown()
    # rectangle(cell_size,40,'red')
    # penup()

    #plane
    pendown()
    setheading(0)
    begin_fill()
    color(outline,'red')
    forward(cell_size)
    left(90)
    forward(40)
    left(90)
    forward(cell_size/3)
    right(90)
    circle(cell_size/3,-180)
    forward(cell_size/3)
    left(90)
    forward(40)
    end_fill()

    #body


    #-----------snoopy two----------#
    #fourth square
    goto(x_pos_two,y_pos_two)
    pendown()
    square(cell_size, 'blue')
    penup()

#
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  You
# should NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's data generation function if available, but
### otherwise creating a dummy function that returns an empty
### list
if isfile('entity_data.py'):
    print('\nData module found\n')
    from entity_data import entity_actions
    def actions(new_seed = None):
        seed(new_seed)
        return entity_actions(grid_width, grid_height)
else:
    print('\nNo data module available!\n')
    def actions(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas()

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
title("Put a description of your overall theme here")

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "actions" function with a fixed seed for the
# ***** random number generator, but your final solution must
# ***** work with "actions()" as the argument to "track_entities",
# ***** i.e., for any data set that can be returned by
# ***** calling function "actions" with no seed.
track_entities(actions()) # <-- no argument for "actions" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible when the program
# ***** terminates as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
