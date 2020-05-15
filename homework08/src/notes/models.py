from django.db import models
from django.utils import timezone
# Create your models here.

from django.contrib.auth import get_user_model
import html2text

User = get_user_model()
html_t = html2text.HTML2Text()

class Note(models.Model):
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    tags = models.CharField(max_length=200)
    
    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.pub_date <= now
    
    def __str__(self):
        return self.title
    
    def tags_list(self):
        return self.tags.split(',')
  
    def content(self):
        return "\t".join([self.title, html_t.handle(self.body)])
