from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField( max_length=300)
    Zip_code = models.CharField('Zip Code', max_length=20)
    phone = models.CharField('Contact Phone', max_length=10)
    web = models.URLField('Web Address')
    email_address = models.EmailField('Email Address')
    

    def __str__(self):
        return self.name


class Minutes(models.Model):
    org_name = models.CharField('Organization Name', max_length=15)
    date = models.DateTimeField( 'Date', blank=True, null=True )
    opening = models.TextField()
    members_present = models.TextField()
    members_absent = models.TextField()
    business_from_the_previous_meeting= models.TextField()
    new_business = models.TextField()
    additions_to_the_agenda= models.TextField()
    adjournment= models.TextField()
    minutes_submitted_by = models.CharField('Organization Name', max_length=15)
    minutes_approved_by = models.CharField('Organization Name', max_length=15)

    def __str__(self):
        return self.org_name


class Meeting(models.Model):
    name = models.CharField('Meeting Name', max_length=120)
    meeting_date = models.DateTimeField( 'Meeting Date', blank=True, null=True )
    venue = models.CharField('Name ', max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    
    def __str__(self):
        return self.name

    @property
    def Due_date(self):
        today = date.today()
        Due_date = self.meeting_date.date() - today
        Due_date_stripped = str(Due_date).split(",", 1)[0]
        return Due_date_stripped

    @property
    def Past_Time(self):
        today = date.today()
        if self.meeting_date.date() < today:
            time = "Past"
        elif self.meeting_date.date() == today:
            time = "Due"
        else:
            time = "Forthcoming"
        return time



