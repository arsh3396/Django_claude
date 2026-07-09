from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
        
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, default='Unknown')
    is_published = models.BooleanField(default=False)
    
    category = models.ForeignKey(
        Category,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    def __str__(self):
        return self
  
    
