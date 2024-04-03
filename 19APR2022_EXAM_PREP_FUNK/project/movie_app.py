from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        try:
            new_user = next(filter(lambda u: u.username == username, self.users_collection))
            raise Exception("User already exists!")
        except StopIteration:
            pass
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        try:
            user = next(filter(lambda u: u.username == username, self.users_collection))
        except StopIteration:
            raise Exception("This user does not exist!")

        if not user.username == movie.owner.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        try:
            movie = next(filter(lambda m: m.title == movie.title, self.movies_collection))
            raise Exception("Movie already added to the collection!")
        except StopIteration:
            pass

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        pass

    def delete_movie(self, username: str, movie: Movie):
        pass

    def like_movie(self, username: str, movie: Movie):
        pass

    def dislike_movie(self, username: str, movie: Movie):
        pass

    def display_movies(self):
        pass

    def __str__(self):
        message = f"All users: {', '.join(self.users_collection) if self.users_collection else 'All users: No users.'}"
        message1 = f"All movies: {', '.join(self.movies_collection) if self.movies_collection else 'All movies: No movies.'}"

        return message + message1
