class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        pass

    def get_time(self):
        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        pass


time = Time(9, 30, 59)
print(time.next_second())
