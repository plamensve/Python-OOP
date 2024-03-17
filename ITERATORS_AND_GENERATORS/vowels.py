class vowels:
    def __init__(self, my_string):
        self.my_string = my_string
        self.vowels = ['a', 'e', 'i', 'u', 'y', 'o']
        self.vowels_values = [c for c in self.my_string if c.lower() in self.vowels]
        self.start_idx = -1
        self.end_idx = len(self.vowels_values)

    def __iter__(self):
        return self

    def __next__(self):
        self.start_idx += 1
        if self.start_idx < self.end_idx:
            return self.vowels_values[self.start_idx]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
