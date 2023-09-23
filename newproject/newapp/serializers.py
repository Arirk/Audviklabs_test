from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def get_user_email(self,obj):
        if obj.created_by:
            return obj.created_by.email
        return None
    
    def get_user_name(self,obj):
        if obj.created_by:
            return obj.created_by.username
        return None
        
