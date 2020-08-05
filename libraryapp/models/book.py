from django.db import models
from .library import Library
from .librarian import Librarian

class Book(models.Model):

    title = models.CharField(max_length=50)
    isbn = models.IntegerField()
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()
    location = models.ForeignKey(Library, on_delete=models.CASCADE, null=True, default=None)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
    #    INSERT INTO libraryapp_librarian (id, location_id, user_id)
    #    VALUES (
    #        id:integer,
    #        location_id:integer,
    #        user_id:integer
    #      ); 
         return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
