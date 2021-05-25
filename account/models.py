from django.db import models
from django.conf import settings


# Custom user profile
class Profile(models.Model):
    # The user one-to-one field allows you to associate profiles with users.
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True,
                                     null=True)
    photo = models.ImageField(upload_to='users/%y/$m/4d/',
                              blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
