from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()


class StreamPlatform(models.Model):
    name = models.CharField(
        max_length=30,
    )
    about = models.CharField(
        max_length=150
    )
    website = models.URLField(
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Stream Platform"
        verbose_name_plural = "Stream Platform"
        db_table = "stream_platform"


class WatchList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='watchlist_user'
    )
    platform = models.ForeignKey(
        StreamPlatform,
        on_delete=models.CASCADE,
        related_name='watchlist'
    )
    title = models.CharField(
        max_length=50
    )
    description = models.CharField(
        max_length=200
    )
    active = models.BooleanField(
        default=True
    )
    avg_ratting = models.FloatField(
        default=0,
        null=True,
        blank=True
    )
    number_ratting = models.IntegerField(
        default=0,
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Watch List"
        verbose_name_plural = "Watch List"
        db_table = "watch_list"


class Reviews(models.Model):
    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviewer'
    )
    watchlist = models.ForeignKey(
        WatchList,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    ratting = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    description = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )
    active = models.BooleanField(
        default=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    update = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return "{} - Ratting: {}".format(self.watchlist.title, self.ratting)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        db_table = "reviews"
