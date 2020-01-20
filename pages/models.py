from django.db import models



### CONTACT FORM MODEL #######

class NewContact(models.Model):
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=100,blank=True, null=True)
    tell_us_more = models.TextField()

    def __str__(self):
        return self.first_name


# BLOG RSS FEED MODEL

class Subscriber(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name
