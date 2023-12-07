# Create your models here.

from users.models import CustomUser
from django.db import models


class Clue(models.Model):
    description = models.CharField(max_length=700)
    hints = models.CharField(max_length=700, default='')
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    approved = models.BooleanField()
    point_value = models.IntegerField(default=50)
    bundle = models.CharField(max_length=200, default='E-Way Bundle')

    def __str__(self):
        return self.description


class UserClueScore(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    clue = models.ForeignKey(Clue, on_delete=models.CASCADE)
    attempts = models.IntegerField(default=0)
    solved = models.BooleanField(default=False)
    attempts_left = models.IntegerField(default=5)

    # def increase_attempts(self):
    #     if self.attempts > 0:
    #         self.attempts += 1
    #         self.save()  

    # def reset_attempts(self):
    #     self.attempts = 3  
    #     self.save()

    # def increase_user_score(self):
    #     if self.attempts > 0:
    #         user = self.user
    #         user.score += (self.clue.point_value-self.attempts*2)
    #         user.save()
