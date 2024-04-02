def start_playing(obj):
    return obj.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


class Piano:
    def play(self):
        return "Playing the piano"


piano = Piano()
guitar = Guitar()
print(start_playing(guitar))
print(start_playing(piano))
