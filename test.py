
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
    #universal colours
    outline = 'black'
    #boxes
    box_one = '#87CEEB'
    box_two = '#a2f1a2'
    box_three = '#87CEEB'
    box_four = '#808080'
    #charlie brown colours
    cb_shirt_one = 'yellow'
    cb_shirt_two = 'red'
    cb_body = '#FFDAB9'
    cb_hat = 'white'
    cb_bag = '#a37e5d'
    grass = '#567d46'
    #snoopy colours
    plane = 'red'
    snoopy = 'white'
    ws = 'yellow'
    tear = '#ADD8E6'
    snoopy_hat = '#8B4513'
    goggles = '#3c4d03'
    
    #-------initialising variables-----------#
    width(3)

    #------------positioning---------------#
    #edge of boxes
    #goes backwards past the four cells horizontally, and adds some extra space
    side_margin = cell_size*4 + cell_size/1.5
    #goes up half a cell
    top_margin = cell_size/2

    #setting the coordinates to be changed easily
    #the x position has the cell_size subtracted so that the turtle ends up in the bottom left hand corner of the square
    #left side x coordinates
    x_left = -side_margin - cell_size
    #right side x coordinates
    x_right = side_margin + cell_size/4
    #top y coordinates
    y_top = top_margin
    #bottom y coordinates
    y_bottom = -top_margin - cell_size

    #----------drawing coordinates----------#

    #---charlie brown one coordinates---#
    #cb head
    cb_x_one = x_left + 40
    cb_y_one = y_top + 30
    #cb body
    cb_x_two = x_left + 5
    #hat and face coords
    cb_x_three = x_left + 75
    cb_y_two = y_top + 62
    #eye coords
    cb_eye_x = x_left + 30
    cb_eye_y = y_top + 55
    #mouth coords
    cb_mouth_x = x_left + 27
    cb_mouth_y = y_top + 43

    ##text
    #text_y_top = y_top + 2*cell_size

    #---charlie brown two coordinates---#
    #cb hat
    cb_y_three = y_bottom + 30
    #eyes
    cb_eye_x_one = x_left + 30
    cb_eye_y_one = y_bottom + 65
    cb_eye_x_two = cb_eye_x_one + 20
    #bubble
    bubble_x = x_left + 60
    bubble_y = y_bottom +60
    #sad eye
    sad_eye_x = bubble_x + 14
    sad_eye_y = bubble_y + 10
    sad_eye_x_2 = sad_eye_x + 10
    #sad mouth
    sad_mouth_x = bubble_x + 12
    sad_mouth_y = bubble_y - 5


    #snoopy one
    snoopy_x_one = x_right + 65
    snoopy_y_one = y_top + 10
    #head pos
    snoopy_x_two = x_right + 27
    snoopy_y_two = y_top + 50
    #ear pos
    snoopy_x_three = snoopy_x_two + 45
    snoopy_y_three = snoopy_y_two - 5
    #arm pos
    snoopy_x_four = snoopy_x_one - 10
    snoopy_y_four = snoopy_y_one + 25
    #eye pos
    snoopy_x_five = snoopy_x_two + 10
    snoopy_y_five = snoopy_y_two + 15
    #hat pos
    snoopy_hat_x = snoopy_x_two + 12
    snoopy_hat_y = snoopy_y_two + 25

    #snoopy two
    #feet
    feet_x_one = x_right + 75
    #head pos
    snoopy_x_head = x_right + 29
    snoopy_y_head = y_bottom + 63
    #woodstock
    w_x = x_right + 55
    w_y = y_bottom + 20
    #ear
    snoopy_x_ear = snoopy_x_head + 10
    snoopy_y_ear = snoopy_y_head - 10
    #eye pos
    snoopy_x_eye = snoopy_x_head + 35
    snoopy_y_eye = snoopy_y_head + 10
    #arm pos
    snoopy_x_arm = x_right + 40
    snoopy_y_arm = y_bottom + 30

    #-----------body dimensions-----------#
    #variables
        #cb one
    cb_body_rad = 35
    cb_head_rad = 32
    cb_hat_rad = 35
        #cb two
    cb_bag_height = 65
    cb_bag_width = 35
    #snoopy one
    snoopy_hat_rad = 20
    #snoopy two
    snoopy_foot = cell_size/5.5
    w_size = 20

    #----------functions----------#
    #square function
    def square(length,colour,text):
        pendown()
        begin_fill()
        color('black', colour)
        setheading(0)
        for i in range(4):
            forward(length)
            left(90)
        end_fill()
        penup()
        right(90)
        forward(60)
        write(text, font=('Arial',12, 'bold'))
        setheading(0)

    #ellipse function
    def ellipse(rad,heading,extent):
        seth(heading)
        for i in range(2):
            circle(rad,extent)
            circle(rad//2,extent)

    #little triangles for shirt
    def triangle(num):
        setheading(0)
        for i in range(num):
            left(45)
            forward(10)
            right(90)
            forward(10)
            setheading(0)

    def rectangle(length,width,colour,heading):
        setheading(heading)
        begin_fill()
        color(outline,colour)
        for i in range(2):
            forward(length)
            left(90)
            forward(width)
            left(90)
        end_fill()

    # def hair(num,x,y):
    #     for i in range(num):
    #         goto(x,y)
    #         forward(10)
    #         angle = randint(45,55)
    #         setheading(angle)
    #         forward(40)
            

    # #-----------drawing functions-----------#

    # #-----------charlie brown one----------#

    # # goto(x_left,text_y_top)
    # # style = ('Courier', 10)
    # # write('Charlie Brown', font=style, align='center')

    def charlie_brown_one():
        ##first square
        goto(x_left,y_top)
        pendown()
        square(cell_size, box_one,'"The baseball \nseason starts \ntoday!"')
        penup()

        #mound
        goto(x_left,y_top)
        pendown()
        color(outline,grass)
        begin_fill()
        right(90)
        circle(cell_size/2,-180)
        end_fill()
        penup()

        #charlie body
        setheading(0)
        goto(cb_x_two,y_top)
        pendown()
        color(outline,cb_shirt_one)
        begin_fill()
        right(90)
        circle(cb_body_rad,-180)
        end_fill()
        penup()

        #stripes
        goto(cb_x_two,y_top)
        pendown()
        color(outline)
        begin_fill()
        triangle(5)
        end_fill()
        penup()

        #head
        goto(cb_x_one,cb_y_one)
        pendown()
        pencolor(outline)
        fillcolor(cb_body)
        begin_fill()
        circle(cb_head_rad)
        end_fill()
        penup()

        #hat
        goto(cb_x_three,cb_y_two)
        right(-90)
        pendown()
        pencolor(outline)
        fillcolor(cb_hat)
        begin_fill()
        circle(cb_hat_rad,180)
        end_fill()

        #hat line
        goto(cb_x_three,cb_y_two)
        penup()
        setheading(180)
        forward(cb_hat_rad*2)
        setheading(0)
        pendown()
        width(3)
        forward(cb_hat_rad*2+20)
        pencolor(outline)
        penup()

        #hat stripe right
        goto(cb_x_three,cb_y_two)
        setheading(-180)
        forward(15)
        pencolor(outline)
        pendown()
        setheading(90)
        circle(cb_hat_rad,70)
        penup()

        #hat stripe left
        goto(cb_x_three,cb_y_two)
        setheading(-180)
        forward(55)
        pencolor(outline)
        pendown()
        setheading(90)
        circle(-cb_hat_rad,70)
        penup()

        #hat stripe middle
        goto(cb_x_three,cb_y_two)
        setheading(-180)
        forward(35)
        right(90)
        pendown()
        forward(35)
        penup()

        #eyes and nose
        goto(cb_x_three,cb_y_two)
        setheading(-180)
        goto(cb_eye_x,cb_eye_y)
        dot(7)
        forward(-9)
        left(90)
        forward(7)
        pendown()
        setheading(0)
        circle(5,180)
        penup()
        goto(cb_eye_x,cb_eye_y)
        setheading(0)
        forward(22)
        dot(7)

        #mouth
        goto(cb_mouth_x,cb_mouth_y)
        pendown()
        forward(3)
        setheading(-70)
        circle(cb_head_rad/3.5,140)
        setheading(0)
        forward(3)
        penup()

    #-----------charlie brown two----------#
    def charlie_brown_two():
        #second square
        goto(x_left,y_bottom)
        pendown()
        pendown()
        square(cell_size, box_two, "Our baseball season starts today and we haven't lost yet!")
        penup()

        #body (same design but red)
        goto(cb_x_two,y_bottom)
        pendown()
        color(outline,cb_shirt_two)
        begin_fill()
        right(90)
        circle(cb_body_rad,-180)
        end_fill()
        penup()

        #stripes
        goto(cb_x_two,y_bottom)
        pendown()
        color(outline)
        begin_fill()
        triangle(5)
        end_fill()
        penup()

        #bag
        color(outline,cb_bag)
        goto(cb_x_two,cb_y_three)
        pendown()
        begin_fill()
        setheading(0)
        left(75)
        forward(cb_bag_height)
        setheading(0)
        forward(cb_bag_width)
        right(75)
        forward(cb_bag_height)
        goto(cb_x_two,cb_y_three)
        end_fill()
        penup()

        #eyes
        goto(cb_eye_x_one,cb_eye_y_one)
        dot(15,outline)
        goto(cb_eye_x_two,cb_eye_y_one)
        dot(15,outline)

        #speech bubble
        goto(bubble_x,bubble_y)
        color(outline,snoopy)
        pendown()
        begin_fill()
        circle(20)
        end_fill()
        penup()

            #triangle
        goto(bubble_x,bubble_y)
        color(outline,snoopy)
        pendown()
        begin_fill()
        setheading(275)
        right(60)
        forward(15)
        right(210)
        forward(15)
        end_fill()
        penup()

        #sad face
        goto(sad_eye_x,sad_eye_y)
        color(outline)
        dot(5)
        goto(sad_eye_x_2,sad_eye_y)
        dot(5)
        #mouth
        goto(sad_mouth_x,sad_mouth_y)
        pendown()
        setheading(-90)
        circle(cb_head_rad/5,-180)
        penup()
    
#     #-----------snoopy one----------#

#     def snoopy_one():
#         #third square
#         goto(x_right,y_top)
#         pendown()
#         square(cell_size, box_three)
#         penup()


#         #body
#         goto(snoopy_x_one,snoopy_y_one)
#         pendown()
#         begin_fill()
#         color(outline, snoopy)
#         ellipse(cell_size/4,45,90)
#         end_fill()
#         penup()

#         #plane
#         goto(x_right,y_top)
#         pendown()
#         setheading(0)
#         begin_fill()
#         color(outline,plane)
#         forward(cell_size)
#         left(90)
#         forward(40)
#         left(90)
#         forward(cell_size/4)
#         left(90)
#         setheading(90)
#         circle(cell_size/4,-180)
#         setheading(180)
#         forward(cell_size/4)
#         left(90)
#         forward(40)
#         end_fill()
#         penup()

#         #arm
#         setheading(180)
#         goto(snoopy_x_four,snoopy_y_four)
#         forward(10)
#         pendown()
#         rectangle(15,7,snoopy,180)
#         penup()

#         #head
#         goto(snoopy_x_two,snoopy_y_two)
#         begin_fill()
#         pendown()
#         color(outline,snoopy)
#         ellipse(cell_size/3.5,-45,90)
#         end_fill()
#         penup()

#         #nose
#         goto(snoopy_x_two,snoopy_y_two)
#         setheading(90)
#         forward(10)
#         setheading(180)
#         forward(10)
#         color(outline)
#         dot(15)
#         forward(3)
#         color(snoopy)
#         dot(5)

#         #ear
#         goto(snoopy_x_three,snoopy_y_three)
#         pendown()
#         begin_fill()
#         color(outline, snoopy)
#         ellipse(cell_size/7,45,90)
#         end_fill()
#         penup()

#         #inner ear
#         goto(snoopy_x_three,snoopy_y_three)
#         pendown()
#         begin_fill()
#         color(outline,outline)
#         ellipse(cell_size/9,45,90)
#         end_fill()
#         penup()

#         #hat
#         goto(snoopy_hat_x,snoopy_hat_y)
#         color(outline,snoopy_hat)
#         pendown()
#         begin_fill()
#         setheading(-115)
#         circle(snoopy_hat_rad,-180)
#         goto(snoopy_hat_x,snoopy_hat_y)
#         penup()
#         end_fill()

#         #eye googles
#         goto(snoopy_hat_x+15,snoopy_hat_y+3)
#         color(outline)
#         dot(12)
#         goto(snoopy_hat_x+15,snoopy_hat_y+3)
#         color(goggles)
#         dot(8)
#         setheading(-25)
#         width(5)
#         pendown()
#         forward(25)
#         penup()

#         #eye
#         color(outline)
#         width(3)
#         goto(snoopy_x_five,snoopy_y_five)
#         dot(6)

#     #-----------snoopy two----------#
#     def snoopy_two():
#         #fourth square
#         goto(x_right,y_bottom)
#         pendown()
#         square(cell_size, box_four)
#         penup()

#         #leg
#         goto(feet_x_one+3,y_bottom+15)
#         pendown()
#         rectangle(50,15,snoopy,-180)
#         penup()

#         #body
#         goto(x_right+50,y_bottom+5)
#         setheading(0)
#         pendown()
#         begin_fill()
#         color(outline,snoopy)
#         ellipse(cell_size/2.7,50,80)
#         end_fill()
#         penup()

#         #black part
#         goto(x_right+15,y_bottom+5)
#         setheading(120)
#         pendown()
#         begin_fill()
#         color(outline)
#         circle(-cell_size/2.7,50)

#         goto(x_right+15,y_bottom+5)
#         setheading(60)
#         pendown()
#         begin_fill()
#         circle(cell_size/3, 65)
#         end_fill()
#         penup()


#         #foot
#         goto(feet_x_one,y_bottom)
#         pendown()
#         setheading(5)
#         begin_fill()
#         color(outline,snoopy)
#         circle(snoopy_foot,180)
#         end_fill()
#         goto(feet_x_one,y_bottom+15)
#         penup()
#         #foot line
#         goto(feet_x_one,y_bottom)
#         pendown()
#         setheading(5)
#         circle(snoopy_foot,90)
#         left(85)
#         forward(10)
#         penup()
#         #foot line 2
#         goto(feet_x_one,y_bottom)
#         pendown()
#         setheading(5)
#         circle(snoopy_foot,130)
#         left(70)
#         forward(10)
#         penup()

#         #head
#         goto(snoopy_x_head,snoopy_y_head)
#         begin_fill()
#         pendown()
#         color(outline,snoopy)
#         ellipse(cell_size/3,-60,90)
#         end_fill()
#         penup()

#         #arm
#         goto(snoopy_x_arm,snoopy_y_arm)
#         pendown()
#         rectangle(30,10,snoopy,-45)
#         penup()

#         #nose
#         goto(snoopy_x_head,snoopy_y_head)
#         setheading(90)
#         forward(10)
#         setheading(-15)
#         forward(55)
#         color(outline)
#         dot(15)
#         forward(3)
#         color(snoopy)
#         dot(5)

#         #ear
#         goto(snoopy_x_ear,snoopy_y_ear)
#         pendown()
#         begin_fill()
#         color(outline, snoopy)
#         ellipse(cell_size/5,30,90)
#         end_fill()
#         penup()

#         #inner ear
#         goto(snoopy_x_ear,snoopy_y_ear)
#         pendown()
#         begin_fill()
#         color(outline,outline)
#         ellipse(cell_size/6,30,90)
#         end_fill()
#         penup()

#         #eye
#         goto(snoopy_x_eye,snoopy_y_eye)
#         dot(6)
#         #tear
#         right(135)
#         forward(5)
#         pendown()
#         color(tear)
#         forward(10)
#         penup()

#         #woodstock
#         goto(w_x,w_y)
#         pendown()
#         begin_fill()
#         color(outline,ws)
#         circle(w_size/2.2)
#         goto(w_x,w_y)
#         end_fill()
#         penup()

#         #triangle
#         goto(w_x+23,w_y+23)
#         pendown()
#         begin_fill()
#         color(outline,ws)
#         left(-60)
#         forward(20)
#         right(-105)
#         forward(20)
#         end_fill()
#         penup()

#         #eye
#         goto(w_x-1,w_y+15)
#         setheading(0)
#         forward(15)
#         pendown()
#         color(outline)
#         dot(5)



# #calling drawing functions
    charlie_brown_one()
    charlie_brown_two()
#     # snoopy_one()
#     # snoopy_two()
    


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
create_drawing_canvas(label_spaces=False)

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
title("Peanuts Comics ft. Charlie Brown and Snoopy")

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
