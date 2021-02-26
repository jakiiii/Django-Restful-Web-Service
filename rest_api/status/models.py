from django.db import models
from django.conf import settings


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_status')
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='status/%Y/%m/%d/', null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:50] or "---------- Blank Content ----------"

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Status Post'
        verbose_name_plural = 'Status Posts'
