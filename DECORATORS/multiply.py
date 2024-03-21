def multiply(times):
    def decorator(ref_func):
        def wrapper(*args, **kwargs):
            result = ref_func(*args, **kwargs)
            return result * times

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
