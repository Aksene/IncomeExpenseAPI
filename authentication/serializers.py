from rest_framework import fields, serializers
from .models import User

class RegisterSerialezer(serializers.ModelSerializer):
    password=serializers.CharField(
        max_length=68,min_length=6, write_only=True)

    # Model for data
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    # Validate user submited information 
    # (Called by serializers.is_valid in Views).
    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs

    # Create the user submited infromation 
    # (Called by serializers.save in Views).
    def create(self, validated_data):
        # Calls create_user method from models.py
        # No ** only passes username
        return User.object.create_user(**validated_data)