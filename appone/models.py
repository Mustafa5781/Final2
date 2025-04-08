from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    owner = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    due_date = models.DateField()
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=50)
    
    def __str__(self):
        return self.title