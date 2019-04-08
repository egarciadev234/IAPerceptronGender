from django.db import models

class Gender(models.Model):
    height = models.FloatField(null=True)
    weight = models.IntegerField(null=True)
    GENDERS = (
        (0, 'HOMBRE'),
        (1, 'MUJER'),
    )
    options = models.IntegerField(max_length=2, choices=GENDERS, null=False)

    def __unicode__(self):
        return self.options

    