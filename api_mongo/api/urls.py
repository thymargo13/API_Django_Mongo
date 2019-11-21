from django.urls import path,include
from .api import  CompanyViewSet, UserViewSet
from rest_framework import routers

# urlpatterns = [
#     #path('UserView/', UserView),
#     path('company', CompanyView.as_view({'get': 'list'}), name='company'),
#     path('user', UserView.as_view({'get': 'list'}), name='user'),
# ]

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/company', CompanyViewSet, 'company')

urlpatterns = router.urls