from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    '''A topic the user is learning about.'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of the model'''
        return self.text
    
#Creating Entry class for storing entries regarding topics
class Entry(models.Model):
    '''A entry where user can write about topic'''
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''Diplaying the text of topic'''
        return self.text[:50] + "..."
