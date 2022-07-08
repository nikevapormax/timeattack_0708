from rest_framework import serializers
from user.models import UserApply as UserApplyModel

class UserApplySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    def get_username(self, obj):
        return obj.user_set.username
    
    
    class Meta:
        model = UserApplyModel
        fileds = ['user', 'username', 'jobpost']