## Setup
1. Git clone this repository onto your computer, under your `make` Folder.
2. Open VS Code. 
2. Create a new file called `vars_make.py` in this repository.
3. Follow the instructons.

## Instructions
Your task is going to be to write a program to calculate the area and perimeter of a circle, rectangle, and octagon.

Begin by writing header comments, and three comments below the header comments, labelled # Input, # Processing, and # Output.

### Input
Here is where you are going to ask the user to **input** 4 values:

- The radius of the circle
- The length of the rectangle
- The width of the rectangle
- A side length of the octagon

You may use any prompt you wish, but they should make sense.

__Hint__: Don't forget that to have the user input a number, you must use the `int(input("Prompt here: "))` command.

### Processing
For each shape (circle, rectangle, octagon) calculate, then store in variables with good names, the area and perimeter.

### Output
For each shape, output the following line:

f"The <insert-shape-name-here> has an area of {shape_area} and a perimeter of {shape_perimeter}"
