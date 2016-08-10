from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50, default="forename")
    last_name = models.CharField(max_length=30, default="surname")

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)



