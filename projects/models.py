from django.db import models
from portfolio.settings import MEDIA_ROOT

def user_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, filename) 

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    gitLink = models.TextField(default='')
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
