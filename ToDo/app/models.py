from django.db import models

class Todo(models.Model):
    Name = models.CharField(max_length=100, default='')
    Category = models.CharField(max_length=100, default='')
    Note = models.CharField(max_length=200, default='')
    attached_file = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.Name
