from django.db import models


status = [("Draft", "Draft"),("Published", "Published")]

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255, default="General")
  
  class Meta:
    ordering = ['name']
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField("Title", max_length=255)
  content = models.TextField("Content")
  image = models.ImageField(upload_to='images/blog', default="default.jpg")
  publish_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)
  status = models.CharField("Status",max_length=16, choices=status, default="Draft")
  category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', default="General")
 

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['publish_date']
  

class Comment(models.Model):
  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
  name = models.CharField("Title",max_length=255)
  content = models.TextField("Comment")
  time_stamp = models.DateTimeField(auto_now_add=True)
  def __str__(self):
        return self.name