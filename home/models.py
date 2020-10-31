from django.db.models import (
    Model, 
    
    CharField, 
    TextField,
    EmailField,
    ImageField,
    FileField,
    DateTimeField,

    ForeignKey,
    OneToOneField,
    ManyToManyField,
    
    CASCADE
)

from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator
from django.utils import timezone

class Author(Model):
    date_created = DateTimeField(default=timezone.now)
    profilePic = ImageField(upload_to='images/profilepics/')
    name = CharField(max_length=100)
    penName = CharField(max_length=100)
    email = EmailField()
    phoneNo = PhoneNumberField()

    def __str__(self):
        return self.name

class Single(Model):
    date_created = DateTimeField(default=timezone.now)
    title = CharField(max_length=100)
    author = ForeignKey(Author, related_name='author' ,on_delete=CASCADE)
    collabs = ManyToManyField(Author, related_name='collabs', blank=True)
    coverPhoto = ImageField(upload_to='images/singles/')
    songFile = FileField(upload_to='songs/', validators=[FileExtensionValidator(allowed_extensions=['mp3'])]) 

    def __str__(self):
        return self.title

class Album(Model):
    date_created = DateTimeField(default=timezone.now)
    title = CharField(max_length=100)
    coverPhoto = ImageField(upload_to='images/albums/')
    author = ForeignKey(Author, on_delete=CASCADE)
    songs = ManyToManyField(Single)

    def __str__(self):
        return self.title