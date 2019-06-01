from django.db import models
from django.contrib import auth
# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return self.username

# Incomplete
# class Profile(models.Model):
#     name = models.CharField(max_length = 100)
#     varsity_id = models.CharField(max_length = 20, unique = True)
#     sheet_id = models.IntegerField(default = 0)
#
#     def __str__(self):
#         return self.name + ' ( ' + self.varsity_id + ' ) '

# from django.db import models
from django.contrib.auth.models import User as us
from PIL import Image
# # Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(us, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, default='No Name')
	status = models.CharField(max_length=100, default='No Status')
	varsity_id = models.CharField(max_length=15, default='000-000-0000')
	image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	# def save(self, **kwargs):
	# 	super().save()

	# 	img = Image.open(self.image.path)

	# 	if img.height > 300 or img.width > 300:
	# 		output_size = (300,300)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.path)