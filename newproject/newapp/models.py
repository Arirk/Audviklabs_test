from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey('self', on_delete= models.SET_NULL, null= True, blank = True, related_name = 'created_users')
    updated_by = models.ForeignKey('self', on_delete= models.SET_NULL, null= True, blank = True, related_name = 'updated_users')
    
    class Meta:
        app_label = 'newapp'