from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=16, null=True)
  
  class Meta:
    ordering = ['name']
    verbose_name_plural = 'Categories'

  def __str__(self):
    return f"{self.name}"



class Post(models.Model):
  title = models.CharField("Title", max_length=64)
  content = models.TextField("Content",)
  image = models.ImageField(upload_to='images/blog',)
  publish_date = models.DateTimeField(auto_now_add=True, null=True)
  last_updated = models.DateTimeField(auto_now=True)
  status = models.CharField("Status", max_length=2, null=True)
  slug = models.IntegerField(null=True)
  category = models.ForeignKey(Category, on_delete=models.PROTECT)

  def __str__(self):
    return f"{self.title}"

  class Meta:
    ordering = ['publish_date']
  


