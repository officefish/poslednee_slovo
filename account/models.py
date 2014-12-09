from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):


    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    models.signals.post_save.connect(create_user_profile, sender=User)



