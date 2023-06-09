from django.db import models


class Employer(models.Model):
    name = models.CharField(max_length=60, null=False)
    pass_number = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'Сотрудник: {self.name} ({self.pass_number})'

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
# Create your models here.
