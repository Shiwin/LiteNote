from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80,null=False)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=80)
    note = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    is_favorite = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    author = models.ForeignKey(User, null=False)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/note/{0}/'.format(self.id)

    def is_favorite(self):
        return self.is_favorite

    def make_favorite(self):
        self.is_favorite = True

    def make_usual(self):
        self.is_favorite = False

    def is_public(self):
        return self.is_public

    def make_public(self):
        self.is_public = True

    def make_private(self):
        self.is_favorite = False

    def publish(self):
        self.make_public()
        return self.get_absolute_url()

