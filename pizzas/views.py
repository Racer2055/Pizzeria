from django.shortcuts import render
from .models import Pizza, Pizza_Image

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizza = Pizza.objects.all()
    context = {'pizzas': pizza}

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)

    toppings = pizza.topping_set.all()
    image = pizza.pizza_image_set.all()
    context = {'pizza': pizza, 'toppings': toppings,'image': image}

    return render(request, 'pizzas/pizza.html', context)
