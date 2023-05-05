from django.db import models


# Create your models here.
class salesAgent(models.Model):
    agent_serialNo = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField(max_length=10)
    assigned_area = models.CharField(max_length=80)
    team_leader = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return f'salesAgent: {self.first_name} {self.surname}'
