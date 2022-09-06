from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField("Title", max_length=64)
  content = models.TextField("Content")
  image = models.ImageField(upload_to='media/blog_pics')
  publish_date = models.DateTimeField(auto_now_add=True, null=True)
  last_updated = models.DateTimeField(auto_now=True)
  status = models.CharField("Status", max_length=2, null=True)
  slug = models.IntegerField(null=True)

  def __str__(self):
    return f"{self.title}"

  class Meta:
    ordering = ['publish_date']
    verbose_name_plural = 'Post'


class Category(models.Model):
  name = models.CharField(max_length=16)
  post = models.ForeignKey(Post, on_delete=models.PROTECT)


  def __str__(self):
    return f"{self.name}"