from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel


class Contact(
        TimeStampedModel,
        ActivatorModel,
        TitleSlugDescriptionModel,
        Model):

    class Meta:
        verbose_name_plural = "Contacts"

    email = models.EmailField(verbose_name="Email")

    def __str__(self) -> str:
        return f'{self.title}'
