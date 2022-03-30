from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoApi.urls')),
]
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
