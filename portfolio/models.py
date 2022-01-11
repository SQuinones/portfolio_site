from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100) #How many characters we want
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'portfolio/images/')
    url = models.URLField(blank=True)
    
    #return the name in more scripting way
    def __str__(self):
        return self.title
    
    
