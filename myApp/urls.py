from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
    path('luxury/', views.luxury, name='luxury'),
    path('new-construction/', views.new_construction, name='new-construction'),
    path('communities/', views.communities, name='communities'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    path('join/', views.join, name='join'),
]
