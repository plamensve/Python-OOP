class reverse_iter:
    def __init__(self, reversed_list):
        self.reversed_list = reversed_list
        self.start_idx = len(reversed_list)
        self.end_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start_idx -= 1
        if self.start_idx > self.end_idx:
            return self.reversed_list[self.start_idx]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
