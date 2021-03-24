from django.db import models


# Create your models here.

class Question(models.Model):
    enunciatedQuestion = models.TextField()
    alternatives = models.JSONField()
    trueOrFalse = models.BooleanField(default=False)
    rightAnswer = models.IntegerField(choices=[
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
    ])

    def __str__(self):
        return self.enunciatedQuestion
