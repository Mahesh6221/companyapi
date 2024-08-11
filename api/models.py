from django.db import models

# Create your models here.

# 2.set up django models  
# creating company model

class Company(models.Model):#extends models.Model class.
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=
                            (('IT','IT'),
                             ('Non IT','Non IT'),
                             ("Mobile Phones",'Mobile Phones')
                            ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '--'+ self.location


# Employee Model
class Employee(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=50)
    address= models.CharField(max_length=200)
    phone= models.CharField(max_length=10)
    about= models.TextField()
    position= models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('Software Developer','sd'),
        ('Project Leader','pl'),
    ))
    # what relation between companies and employee
    # we know that inside company many employees are there.
    # ForeignKey attached to the Company model.
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    # company field is present inside the employee when data comes inside that
    # company field is present inside the Employee class data 
    # is coming inside database company primary key relation between that 
    # foreign key creates the relation states that which employee is in which company.
    # There is one to many relationship.
    # database then inside companies is there primary key