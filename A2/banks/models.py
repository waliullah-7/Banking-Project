from django.db import models
from django.contrib.auth.models import User

class BankModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bankname = models.CharField(max_length=100)
    swift_code = models.IntegerField()
    inst_num = models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.bankname

class BranchModel(models.Model):
    bank = models.ForeignKey(BankModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    transit_num = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(default='admin@enigmatix.io')
    capacity = models.IntegerField(null=True)
    last_modified = models.DateTimeField(auto_now=True)
    