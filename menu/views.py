from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from menu.models import Category, Dish


def hello(request, name):
    return HttpResponse(f"Hello {name}!")


def add(request, a, b):
    return HttpResponse(f"{a}+{b}={a+b}!")


def about(request):
    return render(request, 'about.html', {})


def dishes_all(request):
    categories = Category.objects.all()
    my_dishes = Dish.objects.all()

    ctx = {
        "categories": categories,
        "dishes": my_dishes,

    }
    return render(request, 'menu.html', ctx)


def dishes_by_category(request, category_id):
    categories = Category.objects.all()

    category = Category.objects.get(id=category_id)
    my_dishes = Dish.objects.filter(category=category)

    ctx = {
        "categories": categories,
        "dishes": my_dishes,

    }

    return render(request, 'menu.html', ctx)
