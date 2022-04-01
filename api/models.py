from django.db import models


class Book(models.Model):
    title = models.TextField(max_length=32, blank=False, null=False)

    def __str__(self):
        return self.title

    def create_book(self, title):
        book = self.create(title=title)
        # do something with the book
        return book
