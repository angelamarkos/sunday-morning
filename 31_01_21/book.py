class Book:
    def __init__(self, title, author, date_published):
        self.title = title
        self.author = author
        self.date_published = date_published

    def to_string(self):
        return f'{self.title} - {self.author}'

