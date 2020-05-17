from django.db import models

# Create your models here.

class Customer(models.Model):
    # model containing Customer's Profile and Geolocation (lat,lng)

    name = models.CharField(max_length=20)  # character field with max length of 20

    age = models.IntegerField() # Integer Value for the age

    lat = models.FloatField()   # A float value for latitude

    lng = models.FloatField()   # A float value for longitude

    def __str__(self):
        return self.name


class Bookmarks(models.Model):
    # model containing Bookmarks info : title, url, source_name, date

    title = models.CharField(max_length=50) # character value with max length of 50 characters

    url = models.URLField() # value vaidated by URLValidator, default max length is 200 characters

    source_name = models.CharField(max_length=50)   # character value for name of the publication source with max length of 50

    date = models.DateField(auto_now=True)  # date will be automatically saved when a Bookmark will be created

    customer = models.ManyToManyField(Customer, through='customer_bookmark', through_fields=('bookmark', 'customer'))

    def __str__(self):
        return self.title


class customer_bookmark(models.Model):
    # model to connect Customers to Bookmarks

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')    # connect customer model

    bookmark = models.ForeignKey(Bookmarks, on_delete=models.CASCADE, related_name='bookmark')   # connect bookmark model

    def __str__(self):
        return self.customer.name + ' - ' + self.bookmark.title

    class Meta:

        unique_together = ['customer','bookmark']   # to have uniques customer-bookmark relation