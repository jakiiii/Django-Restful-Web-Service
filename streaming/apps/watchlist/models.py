from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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


class Review(models.Model):
    ratting = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.CharField(
        max_length=200,
        null=True
    )
    watchlist = models.ForeignKey(
        WatchList,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.ratting}"

    class Meta:
        ordering = ('created_at',)
        verbose_name = "Review"
        verbose_name_plural = "Review"
        db_table = "review"
