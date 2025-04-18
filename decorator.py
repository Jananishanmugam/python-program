#A decorator in Python is a function that modifies another function without changing its actual code

def decorator_func(sub_func):
    def wrapper(arg):
        print("inner_decorator")
        # sub_func(arg)
        return arg
    return wrapper

@decorator_func
def sub_function(a):
    print("actual_function")
    a = a-2
    print(f"value of a {a}")
    return a

print(sub_function(5))
