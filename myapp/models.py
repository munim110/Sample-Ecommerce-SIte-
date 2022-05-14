from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100) # VARCHAR(100)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class_name = models.CharField(max_length=100)
    roll = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name