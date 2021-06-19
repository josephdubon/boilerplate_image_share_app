from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


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


# Contact
class Contact(models.Model):
    user_from = models.ForeignKey('auth.User',
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User',
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)  # this will create a db index for the created field

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


# Add the following fields to User dynamically
# Retrieve the user model
user_model = get_user_model()
# Monkey patch to the User model with add_to_class
# **never alter the existing Django User Model, this is just for practice
user_model.add_to_class('following',
                        models.ManyToManyField('self',
                                               through=Contact,
                                               related_name='followers',
                                               symmetrical=False))
