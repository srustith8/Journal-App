from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=40,unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_DRAFT = 1
    STATUS_PUBLISHED = 2
    STATUS_ARCHIVED = 3
    STATUSES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_ARCHIVED, 'Archived'),
    )

    title = models.CharField(max_length=2000)
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    status = models.SmallIntegerField(choices=STATUSES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()

    def __str__(self):
        return self.name
