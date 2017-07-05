from django.db import models

from social_django.models import AbstractUserSocialAuth, DjangoStorage, USER_MODEL


class CustomUserSocialAuth(AbstractUserSocialAuth):
    user = models.ForeignKey(USER_MODEL, related_name='custom_social_auth',
                             on_delete=models.CASCADE)
    class Meta:
        """Meta data"""
        app_label = "app"

class CustomDjangoStorage(DjangoStorage):
    user = CustomUserSocialAuth
