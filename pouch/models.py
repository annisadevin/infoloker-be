from django.db import models

class Pouch(models.Model):
    no_account = models.CharField(max_length=100)
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type_pouch = models.IntegerField()
    goal = models.FloatField()
    expected = models.IntegerField()
    need = models.FloatField()
    saving =  models.FloatField()
    
    def __str__(self) -> str:
        return self.name + self.no_account
