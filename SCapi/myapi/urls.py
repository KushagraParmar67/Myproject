from . import views 
from django.urls import path,re_path
from myapi.views import Payment_api


urlpatterns=[
    path(r'home/',views.home,name='home'),
    path(r'course/<int:id>',views.Course,name='Course'),
    path(r'Inquerry',views.CallRequest,name='INQUERRY'),
    path(r'register',views.register,name='register'),
    path(r'login',views.Login,name='login'),
    path(r'',views.test),
    path(r'payment/',Payment_api.as_view()),
    path(r'abc',views.check,name='abc'),
    re_path(r'tes',views.tes),
]