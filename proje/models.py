from django.db import models

# Create your models here.



class Mansets(models.Model):
    resim=models.ImageField(upload_to="static/assets/images/%Y/%m/%d/", )
    ustyazi= models.CharField(max_length=100)
    yazi= models.TextField()



    def __str__(self):
        return self.ustyazi
    


class Sample(models.Model):
    baslik= models.CharField(max_length=100)
    blog = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='sample')


    def __str__(self):
        return self.baslik
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    

class Comment(models.Model):
    post = models.ForeignKey(Mansets, related_name="comments", on_delete=models.CASCADE)  
    name = models.CharField(max_length= 255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
       return '%s - %s' % (self.post.ustyazi, self.name)    
    
