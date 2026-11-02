# import functions_2 as f2
# import functions_2
# print(functions_2.my_function(200, 23.2233)
# from functions_2 import my_function
import math

import functions_2
# f2.my_function(100, 22.11)

# from functions_2 import my_function

# print(my_function(22, 2.19))

from my_package import shapes
print(shapes.triangle_area(3,4,5))

from my_package.shapes import triangle_area
print(triangle_area(3,4,5))

from my_package.shapes import triangle_area as area
print(area(3,4,5))


print(dir(math))
print(dir(functions_2))









