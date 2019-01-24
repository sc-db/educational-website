from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/')
    text = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return '{message:{fill}{align}{width}}'.format(message=self.text[:100],fill=' ',align='<',width=100)
