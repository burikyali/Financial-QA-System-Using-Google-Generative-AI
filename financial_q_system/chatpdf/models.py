from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(
        choices=[
            (1, "Very Poor"),
            (2, "Poor"),
            (3, "Average"),
            (4, "Good"),
            (5, "Excellent"),
        ]
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name} - Rating: {self.rating}"
