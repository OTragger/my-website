import random as r
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from slugify import slugify



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    


class Contributor(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(default='default_contributor.png')
    
    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    tag = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tag
    
    
class Project(models.Model):
    def main_image_upload(instance, filename):
        #this should return the os.path.join('media/projects/userxx')
        new_pp = '{}_{}_{}.{}'.format(instance.client,instance.title,'main_image','jpg')
        return 'projects/{}/{}'.format(instance.title, new_pp)
    
    def head_image_upload(instance, filename):
        #this should return the os.path.join('media/projects/userxx')
        new_pp = '{}_{}_{}.{}'.format(instance.client,instance.title,'head_image','jpg')
        return 'projects/{}/{}'.format(instance.title, new_pp)
    
    title = models.CharField(max_length=100)
    summary = models.TextField()
    client = models.CharField(max_length= 50)
    category = models.ManyToManyField(Category)
    date = models.DateField()
    projectMainColor = models.CharField(max_length=20, blank=True)
    website = models.URLField(max_length= 50, blank=True)
    contributors = models.ManyToManyField(Contributor)
    mainImage = models.ImageField(upload_to = main_image_upload, blank = True)
    headImage = models.ImageField(upload_to = head_image_upload, blank = True)
    slug = models.SlugField(default='link')
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    

  
class ProjectImages(models.Model):
    def image_upload(instance,filename):
        #this should return the os.path.join('media/projects/userxx')
        #how to generate a random integer number within a range?
        num = r.randint(0, 10)
        myfilename = '{}_{}.{}'.format(instance.project.title,num,'jpg')
        return 'projects/{}/{}'.format(instance.project.title, myfilename)
    
    
    name = models.CharField(max_length =50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    thumb = models.ImageField(upload_to = image_upload,blank = True)
    
    def __str__(self):
        return self.name
    

    
  
#this is to handle the deletion action on video model
#in case an object is deleted, the file associated with it is too
@receiver(pre_delete, sender = ProjectImages)
def ProjectImages_delete(sender, instance, **kwargs):
    #we pass False so that FileField does not save the model
    instance.thumb.delete(False)
    
    
@receiver(pre_delete,sender=Project)
def Project_delete(sender, instance, **kwargs):
    #we pass False so that FileField does not save the model
    instance.mainImange.delete(False)

