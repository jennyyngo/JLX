from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class FoodVendor(models.Model):
	key = models.CharField(max_length=128, unique=True)
	latitude = models.DecimalField(max_digits=18, decimal_places=15, null=True)
	longitude = models.DecimalField(max_digits=18, decimal_places=15, null=True)
	vendorType = models.CharField(max_length=128)
	open = models.BooleanField(default=False)
	businessName = models.CharField(max_length=128, null=True)
	address = models.CharField(max_length=128)
	description = models.CharField(max_length=128)
	
	def __unicode__(self):      #For Python 2, use __str__ on Python 3
		return self.key