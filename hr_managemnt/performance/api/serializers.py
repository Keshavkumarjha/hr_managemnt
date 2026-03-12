from rest_framework import serializers

from hr_managemnt.performance.models import PerformanceReview


class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = ["id", "employee", "reviewer", "review_period", "rating", "comments", "created_at"]

    def validate_rating(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value
