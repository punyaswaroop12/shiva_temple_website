from django.db import models


class PageSection(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "Page Section"
        verbose_name_plural = "Page Sections"

    def __str__(self):
        return self.title
