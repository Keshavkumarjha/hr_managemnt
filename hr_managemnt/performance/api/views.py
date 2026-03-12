from rest_framework.viewsets import ModelViewSet

from hr_managemnt.core.permissions import IsHRAdminOrReadOnly
from hr_managemnt.performance.models import PerformanceReview

from .serializers import PerformanceReviewSerializer


class PerformanceReviewViewSet(ModelViewSet):
    queryset = PerformanceReview.objects.active().select_related("employee", "reviewer")
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsHRAdminOrReadOnly]
