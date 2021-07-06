from django.db import models

class Work(models.Model):
    OFFICE_CHOICE = (('Gerente', 'Gerente'), ('Dev Back-End','Dev Back-End'), ('Dev Front-End','Dev Front-End'), ('Estagiario','Estagiario'))

    name = models.CharField(max_length=200)
    years = models.IntegerField()
    wage = models.FloatField()
    office = models.CharField(max_length=50, choices=OFFICE_CHOICE, default='Estagiario')

    def __str__(self):
        return self.name
        