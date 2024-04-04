class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) == 0:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        msg_liked_movies = f"\n".join([movie.details() for movie in self.movies_liked])
        msg_if_not_liked = f"No movies liked."
        message1 = f"Username: {self.username}, Age: {self.age}\n"
        message1 += f"Liked movies:\n"
        if self.movies_liked:
            message1 += msg_liked_movies
        else:
            message1 += msg_if_not_liked

        message1 += "Owned movies:\n"
        msg_owned = f"\n".join([movie.details() for movie in self.movies_owned])
        msg_if_not_owned = f"No movies owned."
        if self.movies_owned:
            message1 += msg_owned
        else:
            message1 += msg_if_not_owned

        return message1
