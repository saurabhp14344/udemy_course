from django.db import models

class ProfileViewSet(models.Model):
    """Create a custom fields for user """

    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User Info"
        verbose_name_plural = " Users "

