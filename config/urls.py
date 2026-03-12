from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from config.views import healthz
from drf_spectacular.views import SpectacularAPIView
from hr_managemnt.dashboard_views import attendance_page
from hr_managemnt.dashboard_views import dashboard
from hr_managemnt.dashboard_views import departments_page
from hr_managemnt.dashboard_views import employees_page
from hr_managemnt.dashboard_views import leave_page
from hr_managemnt.dashboard_views import payroll_page
from hr_managemnt.dashboard_views import profile_page
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("healthz/", healthz, name="healthz"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path("dashboard/", dashboard, name="dashboard"),
    path("employees/", employees_page, name="employees-page"),
    path("departments/", departments_page, name="departments-page"),
    path("attendance/", attendance_page, name="attendance-page"),
    path("leaves/", leave_page, name="leave-page"),
    path("payroll/", payroll_page, name="payroll-page"),
    path("profile/", profile_page, name="profile-page"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("hr_managemnt.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    # ...
    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/", TemplateView.as_view(template_name="docs/api_home.html"), name="api-home"),
    path("api/", include("config.api_router")),
    path("api/auth/jwt/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="home",
    ),
    path("api/reference/", TemplateView.as_view(template_name="docs/api_reference.html"), name="api-reference"),
]

if settings.DEBUG:

    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
            *urlpatterns,
        ]
