from django.db import models
from django.contrib import admin
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.user",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "body",
    )

