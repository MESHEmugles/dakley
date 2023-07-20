from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class AboutMe(models.Model):
    name= models.CharField(max_length=50, null=True, blank=True)
    wahudo = models.CharField(max_length=100, null=True, blank=True)
    aboutyu = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='aboutme', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'AboutMe'
        managed = True
        verbose_name = 'AboutMe'
        verbose_name_plural = 'AboutMe'



class Home(models.Model):
    banner_big = models.CharField(max_length=100, null=True, blank=True)
    banner_sml = models.CharField(max_length=100, null=True, blank=True)
    url_fst =models.URLField(null=True, blank=True)
    url_snd =models.URLField(null=True, blank=True)
    url_trd =models.URLField(null=True, blank=True)

    def __str__(self):
        return self.banner_big

    class Meta:
        db_table = 'home'
        managed = True
        verbose_name = 'Home'
        verbose_name_plural = 'Home'


class Newsletter(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.email

    class Meta:
        db_table = 'newsletter'
        managed = True
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'


