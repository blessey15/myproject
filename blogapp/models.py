

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.author.username + ', ' + self.title[:40]

    def get_absolute_url(self):
        return reverse('blogpost-detail', kwargs={'pk': self.pk})




class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    ...

    def number_of_comments(self):
        return BlogComment.objects.filter(blogpost_connected=self).count()

class BlogComment(models.Model):
    blogpost_connected = models.ForeignKey(
        BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blogpost_connected.title[:40]
