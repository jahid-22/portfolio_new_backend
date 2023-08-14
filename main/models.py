from django.db import models

# Create your models here.

class Services(models.Model):
    main_title      = models.CharField(max_length = 80)
    sub_title         = models.CharField(max_length= 80)
    text                = models.CharField(max_length=130)
    
    def __str__(self):
        return self.main_title

# Project Category
class Category(models.Model):
    name    = models.CharField(max_length=200, unique=True)
    slug       = models.SlugField(unique=True, max_length=200)
    
    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

# Portfolio
class Portfolio(models.Model):
    name    = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    github_link     = models.CharField(max_length=300)
    live_link     = models.CharField(max_length=300)
    project_img = models.CharField(max_length=400)
    