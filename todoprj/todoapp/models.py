from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('NS', 'Not Started'),
        ('IP', 'In Progress'),
        ('D', 'Done'),
        ('C', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='NS',
    )

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
