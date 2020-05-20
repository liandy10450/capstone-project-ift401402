from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import orderForm

# Create your views here.
def index(request):
    
    return render(request, 'JIT/index.html')

def vendor(request):
    new_orders = Order.objects.filter(order_status_id='1').order_by('published_date')
    current_orders = Order.objects.filter(order_status_id='2').order_by('published_date')
    return render(request, 'JIT/vendor.html',{'new_orders':new_orders, 'current_orders':current_orders})

def receiving(request):
    current_orders = Order.objects.filter(order_status_id='2').order_by('published_date')
    being_delivered_orders = Order.objects.filter(order_status_id='3').order_by('published_date')
    completed_orders = Order.objects.filter(order_status_id='4').order_by('published_date')
    return render(request, 'JIT/receiving.html',{'current_orders':current_orders, 'being_delivered_orders':being_delivered_orders, 'completed_orders':completed_orders})

def CRUD_template(request):
    return render(request, 'JIT/CRUD_template.html')

#def post_new(request):
#    form = changeStatus()
#    return render(request, 'JIT/process_selected.html', {'form': form})

#Create orders
def order_create(request):
    form = orderForm()
    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'JIT/order_create.html', context)

#update existing order by reusing order_create and pre-filling field
def order_update(request, pk):

    order = Order.objects.get(order_id=pk)
    form = orderForm(instance=order)

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = orderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('index')

    context={'form':form}
    return render(request, 'JIT/order_create.html', context)

#delete order
def order_delete(request, pk):
    order = Order.objects.get(order_id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('index')
    context = {'item':order}
    return render(request, 'JIT/order_delete.html', context)