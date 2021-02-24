from django.db import models

# Create your models here.
class NewsHeadline(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()


    def _str_(self):
        return self.title
