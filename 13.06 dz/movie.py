class Movie:
    def __init__(self, title, director, genre, release_year, duration, rating):
        self.title = title
        self.director = director
        self.genre = genre
        self.release_year = release_year
        self.duration = duration
        self.rating = rating

    def show_info(self):
        return f"{self.title} ({self.release_year}) directed by {self.director}"

    def rate_movie(self, new_rating):
        self.rating = new_rating
        return f"Movie rated as {new_rating} stars."

    def is_short(self):
        return self.duration <= 120

    def watch(self, minutes_watched):
        if minutes_watched <= self.duration:
            self.duration -= minutes_watched
            return f"Watched {minutes_watched} minutes. {self.duration} minutes left."
        else:
            return "Movie finished."
