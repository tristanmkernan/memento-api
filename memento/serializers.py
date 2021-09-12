from rest_framework import serializers

from .models import Memento, MementoCategory


class MementoCategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MementoCategory
        fields = "__all__"


class MementoCategoryRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return self.context["request"].user.mementocategory_set


class MementoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    category = MementoCategorySerializer(read_only=True)
    category_id = MementoCategoryRelatedField(write_only=True)

    notes = serializers.CharField(allow_blank=True)
    location = serializers.CharField(allow_blank=True)

    class Meta:
        model = Memento
        fields = "__all__"

    def create(self, validated_data):
        category = validated_data.pop("category_id")
        return Memento.objects.create(**validated_data, category=category)

    def update(self, instance, validated_data):
        category = validated_data.pop("category_id")
        changes = {
            **validated_data,
            "category": category
        }
        for key, value in changes:
            setattr(instance, key, value)

        instance.save()

        return instance
