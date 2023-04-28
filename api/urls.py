from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("accounts/users",views.UsersView,basename="users"),
router.register("users/profile",views.UsersView,basename="profile"),


urlpatterns=[

      path("token/",ObtainAuthToken.as_view()),
      # path("token/refresh/",TokenRefreshView.as_view()),

]+router.urls
