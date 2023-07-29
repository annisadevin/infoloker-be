from django.urls import path

from .views import *

app_name = 'main'

urlpatterns = [
    path('pouch', PouchListApiView.as_view(), name='pouch-api-list'),
    path('pouch/info/<int:pouch_id>/', PouchDetailApiView.as_view(), name='pouch-api-detail'),
    path('pouch/user/<int:user_id>/', PouchByUserApiView.as_view(), name='pouch-api-user'),
]
