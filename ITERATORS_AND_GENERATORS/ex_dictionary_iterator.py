class dictionary_iter:

    def __init__(self, dictionary):  # {1: "1", 2: "2"}
        self.items = list(dictionary.items())  # dictionary.items() => dict_items([(1, "1"), (2, "2")])
        self.index: int = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items) - 1:
            raise StopIteration

        self.index += 1

        return self.items[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
