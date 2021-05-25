from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Image model
class Image(models.Model):
    # User that bookmarked the image
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='images_created',
        on_delete=models.CASCADE
    )
    # Title, slug, url, file, descr., created at date for image
    title = models.CharField(max_length=200),
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y%m%d')
    description = models.TextField(blank=True)
    # Database indexes improve query performance
    created = models.DateField(auto_now_add=True, db_index=True)

    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='images_liked',
        blank=True
    )

    # Auto generate slug from title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)