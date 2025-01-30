from django.db import models
# Create your models here.
class Buyer(models.Model):
    #Buyer - модель представляющая покупателя
    name = models.CharField(max_length=60, help_text='username аккаунта')
    ballance=models.DecimalField(max_digits=8,decimal_places=2)
    age=models.IntegerField()
    def __str__(self):
        return self.name

class Games(models.Model):
    #Game - модель представляющая игру
    title=models.CharField(max_length=100,help_text='title игры' )
    #Название игры
    cost= models.DecimalField(max_digits=7,decimal_places=2)
    #цена(DecimalField)
    size=models.DecimalField(max_digits=10, decimal_places=2)
    #размер файлов игры(DecimalField)
    description=models.TextField()
    #описание(неограниченное кол - во текста)
    age_limited = models.BooleanField(default=False)
    #ограничение возраста 18 + (BooleanField, по умолчанию False)
    buyer=models.ManyToManyField(Buyer,related_name='buyers')
    # покупатель обладающий игрой(ManyToManyField).У каждого покупателя может
    # быть игра и у каждой игры может быть несколько обладателей.

    def __str__(self):
        return self.title
