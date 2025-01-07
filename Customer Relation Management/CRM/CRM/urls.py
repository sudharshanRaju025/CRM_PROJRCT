from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="API docs",
      default_version='v1',
      description="student registation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/",include("login.urls")),
    path("api/",include("leads.urls")),
    path("api/",include("Opportunities.urls")),
    path("api/",include("Learner.urls")),
    path("api/",include("Course.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)