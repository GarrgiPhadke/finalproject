from django.db import models

class Review(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.author}'