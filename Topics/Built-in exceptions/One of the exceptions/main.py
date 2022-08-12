value = int(input())

exception_list = dir(locals()['__builtins__'])

print(exception_list[value])