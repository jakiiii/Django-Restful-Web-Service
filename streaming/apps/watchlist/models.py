from django.db import models


class Movie(models.Model):
    name = models.CharField(
        max_length=50
    )
    description = models.CharField(
        max_length=200
    )
    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        db_table = "movie"
