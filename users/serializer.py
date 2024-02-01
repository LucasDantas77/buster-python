from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(max_length=127)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(required=False, default=False)
    is_superuser = serializers.BooleanField(read_only=True, source="user.is_superuser")

    def validate_email(self, value):
        email = User.objects.filter(email=value).first()

        if email:
            raise serializers.ValidationError("email already registered.")
        return value

    def validate_username(self, value):
        username = User.objects.filter(username=value).first()
        if username:
            raise serializers.ValidationError("username already taken.")

        return value

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["is_superuser"] = instance.is_employee
        if instance.is_employee:
            rep["is_superuser"] = True
        else:
            rep["is_superuser"] = instance.is_superuser
        return rep

    def create(self, validated_data):
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        password = validated_data.get("password", None)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
