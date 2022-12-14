from django.db import models

    
class CustomUser(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=20, blank=False, null=False)
    u_password = models.CharField(max_length=255, blank=False, null=False)
    user_email = models.EmailField(max_length=255, blank=False,null=False)
    user_address = models.CharField(max_length=255,blank=False, null=False)
    user_profile_img = models.ImageField(blank=True, null=False, upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    isRemoved = models.BooleanField(default=False)
    
    objects = models.Manager()
    all_entries = objects.all()
    
    class Meta:
        verbose_name = 'Appstore User'