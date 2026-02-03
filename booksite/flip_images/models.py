from django.db import models
from datetime import datetime
datetime.now()

class FlipbookImage(models.Model):
    image = models.ImageField(upload_to='flipbook/')
    caption = models.CharField(max_length=100, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_front = models.BooleanField(default=False)           # front page flag
    is_back = models.BooleanField(default=False)            # back page flag
    title = models.CharField(max_length=100, blank=True)    # for front page
    date = models.DateField(null=True, blank=True)          # for front page

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        if self.is_front:
            return f"Front: {self.title}"
        return f"Page: {self.caption}"
