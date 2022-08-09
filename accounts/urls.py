from django.urls import path,include

from accounts import views
urlpatterns = [
    path('signin',views.SigninView.as_view(),name='signin'),
    path('user/home',views.userhome,name='userhome'),
    path('signout',views.logout_,name='logout')
]
