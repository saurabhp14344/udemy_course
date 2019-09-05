from django.urls import path,include
from profile_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile-viewset', views.ProfileApi_ViewSet)


urlpatterns = [
    path('user_info', views.HelloApi.as_view()),
    path('', include(router.urls))
]
