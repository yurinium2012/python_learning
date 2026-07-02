def calculate(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2
    

result = calculate(200, 370)
print("the result is: ", result)

result = calculate(40, 30)
print("the result is: ", result)
