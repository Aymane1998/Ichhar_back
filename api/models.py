from datetime import timezone
from django.db import models

from authentication.models import User


class BaseModel(models.Model):
   created_at = models.DateTimeField(auto_now_add=True, null=True)
   updated_at = models.DateTimeField(auto_now=True)


class Demand(BaseModel):
    DURATION_CHOICES = [
        ('physique', 'Physique'),
        ('digital', 'Digital'),
    ]
    LANGUAGE_CHOICES = [
        ('arabe', 'Arabe'),
        ('français', 'Français'),
        ('anglais', 'Anglais'),
    ]
    GENDER_CHOICES = [
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ]
    demandeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='demandeur', null=True)
    duration = models.FloatField(max_length=300,null=False,blank=True)
    deadline = models.DateField(blank=True)
    description = models.TextField(max_length=500,null=False,blank=True)
    createur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='createurs', null=True, blank=True, default=None)
    type_video = models.CharField(max_length=50, choices=DURATION_CHOICES)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    comments = models.TextField(max_length=500,null=False,blank=True)
    taken = models.BooleanField(default=False,null=False,blank=True)

    def __str__(self):
        return f"Demande - {self.id}"


class Creator(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField(max_length=500, null=True, blank=True)
    integration_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def total_videos(self):
        return self.videos_created.count()
    @property
    def video_links(self):
        return [video.video_link for video in self.videos_created.all()]


class Video(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='videos_created')
    video_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Video by {self.creator}"
