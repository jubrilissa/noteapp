from django.db import models


class Note(models.Model):
    """Model representation of the Note class"""

    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='modified')

    def __str__(self):
        """
        String representation of model
        :return:
        """
        return self.title
