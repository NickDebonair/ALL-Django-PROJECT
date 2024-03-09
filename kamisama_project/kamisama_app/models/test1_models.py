from django.db import models


CUSTOMER_CHOICES = (
(0, u'法人'),
(1, u'個人')
)

class Company(models.Model):
# """法人情報"""
    name = models.CharField(max_length=30) # 法人名

    def __str__(self):
        return self.name

class Person(models.Model):
# """個人情報"""
    name = models.CharField(max_length=30) # 個人名

    def __str__(self):
        return self.name

class Customer(models.Model):
# """顧客"""
    customer_type = models.IntegerField(choices=CUSTOMER_CHOICES)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.customer_type)

class Work(models.Model):
# """案件情報"""
    name = models.CharField(max_length=50) # 案件名
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

