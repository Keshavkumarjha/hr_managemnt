from rest_framework import serializers

from hr_managemnt.recruitment.models import Application
from hr_managemnt.recruitment.models import Candidate
from hr_managemnt.recruitment.models import JobOpening


class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = ["id", "title", "department", "location", "is_open", "created_at"]


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "full_name", "email", "phone", "created_at"]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "opening", "candidate", "stage", "created_at"]
