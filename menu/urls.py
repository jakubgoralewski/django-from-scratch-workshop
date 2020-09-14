from django.urls import path

from menu import views

urlpatterns = [
    path('hello/<str:name>', views.hello),
    path('add/<int:a>/<int:b>', views.add),
    path('about/', views.about, name="about"),
    path('dishes/', views.dishes_all, name='dishes'),
    path('dishes/<int:category_id>', views.dishes_by_category, name="dishes_by_category"),
]