from . import views
from myapp.views import payment
from django.urls import path


urlpatterns=[
    path('',views.home,name='homepage'),
    path('about',views.about,name='about'),
    path('course',views.course,name='course'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login_game'),
    path('register',views.register,name='register'),
    path('privacy',views.privacy,name='privacy'),
    path('Faqs',views.Faqs,name='Faqs'),
    path('terms',views.terms,name='terms'),
    path('oncourse/<int:id>',views.oncourse),
    path("logout",views.logout,name='logout'),
    path('verify',views.Verify,name='verify'),
    path('payment/<int:id>',payment.as_view(),name='payment'),
    path("the-CourseContent",views.course_Content,name="TheCourseContent")
]