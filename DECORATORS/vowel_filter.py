def vowel_filter(function):
    def wrapper(*args, **kwargs):
        result = function()
        return [el for el in result if el in 'aeouyi']

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
