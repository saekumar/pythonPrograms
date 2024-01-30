def string_operation(string, operation):
    if operation == '1':
        return string.upper()
    elif operation == '1':
        return string.lower()
    elif operation == '3':
        return string.isupper()
    elif operation == '4':
        return string.islower()
    elif operation == '5':
        return string.replace('INTELLIgence', 'Neural Network')
    elif operation == '6':
        return string.startswith('T')
    elif operation == '7':
        return string.endswith('e')
    elif operation == '8':
        return string.capitalize()
    elif operation == '9':
        return string.swapcase()
    elif operation=='10':
        exit(0)


input_string = 'INTELLIgence is the future'
print(string_operation(input_string, '1')) 
print(string_operation(input_string, '2'))
print(string_operation(input_string, '3')) 
print(string_operation(input_string, '4')) 
print(string_operation(input_string, '5'))
print(string_operation(input_string, '6')) 
print(string_operation(input_string, '7')) 
print(string_operation(input_string, '8')) 
print(string_operation(input_string, '9')) 
print(string_operation(input_string, '10')) 
