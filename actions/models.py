from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# User activities stream
class Action(models.Model):
    # The user who performed the action; this is a ForeignKey to the Django User model
    user = models.ForeignKey('auth.User',
                             related_name='actions',
                             db_index=True,
                             on_delete=models.CASCADE)
    # The verb describing the action that the user has performed
    verb = models.CharField(max_length=255)
    # ForeignKey field that points to the ContentType model
    target_ct = models.ForeignKey(ContentType,
                                  blank=True,
                                  null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE)
    # PositiveIntegerField for storing the primary key of the related object
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True,
                                            db_index=True)
    # A GenericForeignKey field to the related object based on the combination of the two previous fields
    target = GenericForeignKey('target_ct', 'target_id')
    # The date and time when this action was created
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('created',)
