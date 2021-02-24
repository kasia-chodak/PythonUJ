input_height = int(input("Wpisz ile pól na wysokość ma mieć prostokąt: "))
input_width = int(input("Wpisz ile pól na szerokość ma mieć prostokąt: "))

line_height = '|'
line_width = '+'

input_width_2 = input_width


# konstrukcja linii budujących prostokąt
def linia_width(robocze_width):
    global line_width
    while robocze_width > 0:
        line_width += '---+'
        robocze_width -= 1
    return line_width


def linia_height(number):
    global line_height
    while number > 0:
        line_height += '   |'
        number -= 1
    return line_height


constructed_line_width = linia_width(input_width)
constructed_line_height = linia_height(input_width_2)


# konstrukcja prostokąta
def rectangle(height, width):
    print(constructed_line_width)
    while height > 0:
        print(constructed_line_height)
        print(constructed_line_width)
        height -= 1


rectangle(input_height, input_width)
