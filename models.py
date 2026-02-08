from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('LEAD', 'Leadership'),
        ('FIN', 'Finance'),
        ('MKT', 'Social Marketing'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Initiative(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="initiatives")
    title = models.CharField(max_length=200)

    # Vision Step
    problem = models.TextField()

    solution = models.TextField()

    # Audience Step
    beneficiaries = models.TextField()

    # Plan Step
    activities = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Progress
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
