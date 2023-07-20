

from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from . address import Address

from hitcount.models import HitCountMixin, HitCount
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse ('pages/all_stories.html', kwargs=(self.pk))





class Tutorial(models.Model):
    Tutorial_id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=90, null=True, blank=True)
    slug = models.SlugField(unique=True)
    description = RichTextField(null=True, blank=True)
    cover_img = models.ImageField(upload_to='cover_img',default='images/blog-1.jpg', blank= True, null= True)
    video = EmbedVideoField(blank=True, null=True)
    no_of_comments = models.IntegerField(default=0, null=True, blank=True)
    like = models.ManyToManyField(Address, related_name='likes', blank=True)
    like_count = models.BigIntegerField(default= 0, null=True, blank=True)
    # hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    tags = TaggableManager()


    def __str__(self):
        return '%s - %s' % (self.author, self.title)



    class Meta:
        verbose_name_plural = 'Tutorials'
        


class TutorialNumber(models.Model):
    created_tutorials = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_tutorials.title

    




class TutorialComment(models.Model):
    comment_tuto = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name= "comments")
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '%s - %s' % (self.name, self.comment_tuto.title)