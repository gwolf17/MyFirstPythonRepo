from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)

    #Return description so you can see it in Admin interface
    def __str__(self):
        return (self.description)

    #Tells django to reference the category table in our database
    class Meta:
        db_table = "category"

#Ratings class
class Rating(models.Model):
    rating = models.CharField(max_length=4)
    description = models.CharField(max_length=1000)
    movie_id = models.ManyToManyField(Category, through='Movie')

    #Return description so you can see it in Admin interface
    def __str__(self):
        return (self.description)
    
    #Tells django to reference the ratin table in our database
    class Meta:
        db_table = "rating"

#linking table for category and rating
class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.DateField
    #Foerign keys linking to Category and Rating tables
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

    #Return title so you can see it in Admin interface
    def __str__(self):
        return (self.title)

    #Tells django to reference the movie table in our database
    class Meta:
        db_table = "movie"