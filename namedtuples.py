# from collections import namedtuple
# Color=namedtuple('color',['red', 'green', 'blue'])
# color=Color(55,125.155)

# print(color.red)


from collections import namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 125, 155)

# Accessing 'red' from the instance 'color'
print(color.red)
