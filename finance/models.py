from django.db import models
from users.models import CustomUser
from django.db.models import Sum

# Create your models here.


class CostCenter(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Share(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    costcenter = models.ForeignKey(CostCenter, on_delete=models.CASCADE, related_name='share')
    share = models.DecimalField(max_digits=3, decimal_places=0, default=100)

    class Meta:
        unique_together = ('user', 'costcenter')

    def __str__(self):
        return str(self.user) + ' - ' + self.costcenter.name  + ' - ' + str(self.share)
  
    
class Expense(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null = True)
    costcenter = models.ForeignKey(CostCenter, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return str(self.user) + ' - ' + self.name if self.name != None else str(self.user) + ' - ' + str(self.id)


