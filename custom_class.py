'''
Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

'''

# Solution

class Rectangle:
          
    def __init__(self, length:int, width:int):
        # instance attributes
        self.length = length
        self.width = width

    # __iter__() method - used for iteration over class object.
    def __iter__(self):
        yield{'length': self.length}
        yield{'width': self.width }
            
#object instatiation
rect = Rectangle(10,20)

#iteration over object to generate output as per desired format.
for dimensions in rect:
    print(dimensions)