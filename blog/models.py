from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField()
    content = models.TextField(null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,name="category")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

