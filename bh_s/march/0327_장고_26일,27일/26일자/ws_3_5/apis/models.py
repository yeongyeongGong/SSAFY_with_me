from django.db import models
from django.core.validators import URLValidator, MinLengthValidator, MaxLengthValidator

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(
        validators=[MinLengthValidator(10), MaxLengthValidator(60)]
    )
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
