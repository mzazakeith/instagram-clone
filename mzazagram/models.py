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

