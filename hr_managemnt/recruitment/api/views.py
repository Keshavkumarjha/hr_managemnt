from rest_framework.viewsets import ModelViewSet

from hr_managemnt.core.permissions import IsHRAdminOrReadOnly
from hr_managemnt.recruitment.models import Application
from hr_managemnt.recruitment.models import Candidate
from hr_managemnt.recruitment.models import JobOpening

from .serializers import ApplicationSerializer
from .serializers import CandidateSerializer
from .serializers import JobOpeningSerializer


class JobOpeningViewSet(ModelViewSet):
    queryset = JobOpening.objects.active().select_related("department")
    serializer_class = JobOpeningSerializer
    permission_classes = [IsHRAdminOrReadOnly]


class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.active()
    serializer_class = CandidateSerializer
    permission_classes = [IsHRAdminOrReadOnly]


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.active().select_related("opening", "candidate")
    serializer_class = ApplicationSerializer
    permission_classes = [IsHRAdminOrReadOnly]
