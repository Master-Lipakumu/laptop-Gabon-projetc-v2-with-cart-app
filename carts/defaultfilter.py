from django import template

def mult(value, arg):
    "Multiplies the arg and the value"
    return float(value) * float(arg)

def sub(value, arg):
    "Subtracts the arg from the value"
    return float(value) - float(arg)

def div(value, arg):
    "Divides the value by the arg"
    return float(value) / float(arg)

template.register_filter('mult', mult, True)
template.register_filter('sub', sub, True)
template.register_filter('div', div, True)