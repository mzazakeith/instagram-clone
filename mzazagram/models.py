from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.CharField(max_length=300)
    user = models.ForeignKey(User)

    @classmethod
    def search_by_username(cls, search_term):
        user = cls.objects.filter(user__username__icontains=search_term)
        return user

    def __str__(self):
        return self.bio


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_caption = models.CharField(max_length=300)
    owner = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_caption

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls, self=image_caption):
        self.update()



class Comments(models.Model):
    comment = models.CharField(max_length=250)
    commenter = models.ForeignKey(User)
    image_id = models.ForeignKey(Image)

    def __str__(self):
        return self.comment
