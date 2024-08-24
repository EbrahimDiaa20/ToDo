from django.db import models

class Todo(models.Model):
    text = models.TextField(max_length=500)
    attached_file = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.text
