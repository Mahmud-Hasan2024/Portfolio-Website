from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tech_stack = models.CharField(max_length=255, blank=True)
    live_url = models.URLField(blank=True)
    api_url = models.URLField(blank=True)
    swagger_url = models.URLField(blank=True)
    repo_frontend = models.URLField(blank=True)
    repo_backend = models.URLField(blank=True)
    screenshot = CloudinaryField('screenshot', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # newest first

    def __str__(self):
        return self.title

    def _generate_unique_slug(self):
        base = slugify(self.title)[:200] or "project"
        slug = base
        counter = 1
        while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base}-{counter}"
            counter += 1
            # ensure max length
            if len(slug) > 220:
                slug = slug[:220]
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', args=[self.slug])


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} <{self.email}> at {self.created_at:%Y-%m-%d %H:%M}"
