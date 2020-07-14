from rest_framework.serializers import ModelSerializer
from .models import Result

class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = ['id','aris', 'stoic', 'epic', 'skep', 'cyr']