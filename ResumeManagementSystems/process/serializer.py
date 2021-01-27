from rest_framework import serializers
from process.models import RegistrationModel,ProfileModel

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationModel
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'