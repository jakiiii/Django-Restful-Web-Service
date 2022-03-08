from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField(
        max_length=30
    )
    about = models.CharField(
        max_length=150
    )
    website = models.URLField(
        max_length=250
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Stream Platform"
        verbose_name_plural = "Stream Platform"
        db_table = "stream_platform"


class WatchList(models.Model):
    name = models.CharField(
        max_length=50
    )
    shortline = models.CharField(
        max_length=200
    )
    platform = models.ForeignKey(
        StreamPlatform,
        on_delete=models.SET_NULL,
        null=True,
        related_name='watchlist'
    )
    active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        db_table = "movie"
