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
        try:
            current_movie = next(filter(lambda m: m.title == movie.title, movie.owner.movies_owned))
        except StopIteration:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k, v in kwargs.items():
            movie.title = v
            return f"{username} successfully edited {v} movie."

    def delete_movie(self, username: str, movie: Movie):
        try:
            movie = next(filter(lambda m: m.title == movie.title, self.movies_collection))
        except StopIteration:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        movie.owner.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        current_user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie.owner.username == current_user.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        try:
            current_movie = next(filter(lambda m: m.title == movie.title, current_user.movies_liked))
            raise Exception(f"{username} already liked the movie {movie.title}!")
        except StopIteration:
            pass

        movie.likes += 1
        current_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        current_user = next(filter(lambda u: u.username == username, self.users_collection))
        try:
            current_movie = next(filter(lambda m: m.title == movie.title, current_user.movies_liked))
            current_user.movies_liked.remove(current_movie)
            current_movie.likes -= 1
            return f"{username} disliked {current_movie.title} movie."
        except StopIteration:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda n: (-n.year, n.title))
        if not self.movies_collection:
            return "No movies found."
        final_msg = []
        for m in sorted_movies:
            final_msg.append(m.details())
        return '\n'.join(final_msg)

    def __str__(self):
        message = f"All users: {(', '.join([u.username for u in self.users_collection])) if self.users_collection else 'All users: No users.'}"
        message1 = f"All movies: {(', '.join([m.title for m in self.movies_collection])) if self.movies_collection else 'All movies: No movies.'}"

        return message + '\n' + message1
