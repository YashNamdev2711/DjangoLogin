from django.db import models

# Create your models here.
class InsertMarks(models.Model):
    URNO=models.IntegerField()
    UNAME=models.CharField(max_length=30)
    UPHY=models.IntegerField()
    UCHE=models.IntegerField()
    UMATHS=models.IntegerField()
    def __str__(self):
        return str(self.URNO)

class Qaa(models.Model):
    la=(('j','java'),('p','python'),('c','c_prog'))
    lang=models.CharField(max_length=1,choices=la)
    question=models.CharField(max_length=300)
    ans=models.TextField()
    def __str__(self):
        return self.question