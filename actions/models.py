from django.db import models


# User activities stream
class Action(models.Model):
    # The user who performed the action; this is a ForeignKey to the Django User model
    user = models.ForeignKey('auth.User',
                             related_name='actions',
                             db_index=True,
                             on_delete=models.CASCADE)
    # The verb describing the action that the user has performed
    verb = models.CharField(max_length=255)
    # The date and time when this action was created
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('created',)
