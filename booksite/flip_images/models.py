from django.db import models
from datetime import datetime
datetime.now()

class FlipbookImage(models.Model):
    image = models.ImageField(upload_to='flipbook/')
    caption = models.CharField(max_length=100, blank=True, null=True)

    title = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
  
    is_front = models.BooleanField(default=False)   # ✅ NEW

    uploaded_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.is_front:
            return f"Front: {self.title}"
        return f"Page: {self.caption}"

