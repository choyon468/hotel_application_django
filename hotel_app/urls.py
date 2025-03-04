from django.urls import path, include
from .views import HomePageView, RoomCreateView, RoomListView, RoomDetailView, RoomUpdateView, RoomDeleteView, RoomReserveView
from django.contrib.auth import views as auth_views
from .views import register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Homepage shows available rooms
    path('reserve/<int:pk>/', RoomReserveView.as_view(), name='reserve'),
    path('create/', RoomCreateView.as_view(), name='roomcreate'),
    path('roomlist/', RoomListView.as_view(), name='roomlist'),
    path('roomdetail/<int:pk>', RoomDetailView.as_view(), name='roomdetail'),
    path('roomupdate/<int:pk>', RoomUpdateView.as_view(), name='roomupdate'),
    path('roomdelete/<int:pk>', RoomDeleteView.as_view(), name='roomdelete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]