# put your python code here
def multiply(*args):
    product = 1
    for number in args:
        product *= number
    return product
