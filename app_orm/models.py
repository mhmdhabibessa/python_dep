from django.db import models



class Actor(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # movies = []   



class MovieManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 5:
            errors["title"] = "Movie title should be at least 5 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Movie description should be at least 10 characters"
        if len(postData['image_url']) < 6 :
            errors['image_url'] = "The Image must be a link"
        if int(postData['duration']) < 30:
            errors['duration'] = "The Duration at least must be 30 min"
        return errors

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    image_url = models.TextField(default="")    
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    actors= models.ManyToManyField(Actor,related_name="movies")
    objects= MovieManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


