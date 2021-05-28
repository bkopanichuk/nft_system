from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Create your models here.

class BaseToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tokenId = models.CharField(max_length=200, unique=True, null=True, blank=True)
    address = models.CharField(max_length=42, null=True, blank=True)

    def __str__(self):
        return self.tokenId

class Metadata(models.Model):
    token = models.OneToOneField(BaseToken, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, help_text="Identifies the asset to which this NFT represents", null=True, blank=True)
    description = models.CharField(max_length=255, help_text="Describes the asset to which this NFT represents", null=True, blank=True)
    content = models.CharField(max_length=255, help_text="A URI pointing to a resource with mime type image/* representing the asset to which this NFT represents. Consider making any images at a width between 320 and 1080 pixels and aspect ratio between 1.91:1 and 4:5 inclusive.", null=True, blank=True)


    def __str__(self):
        return self.title