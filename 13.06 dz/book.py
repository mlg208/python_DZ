class Book:
    def __init__(self, title, author, genre, pages, publication_year, rating):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.publication_year = publication_year
        self.rating = rating

    def get_info(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

    def rate(self, new_rating):
        self.rating = new_rating
        return f"Book rated as {new_rating} stars."

    def is_classic(self):
        return self.publication_year <= 1900

    def read(self, pages_to_read):
        self.pages -= pages_to_read
        return f"{pages_to_read} pages read. {self.pages} pages left."
