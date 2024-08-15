from django.shortcuts import render, redirect
from .models import Bill, Item

def home_view(request):
    return render(request, 'bills/home.html')

def create_bill_view(request):
    if request.method == "POST":
        ...
        return redirect('bill_list')
    return render(request, 'bills/create_bill.html')

def bill_list_view(request):
    bills = Bill.objects.all()
    return render(request, 'bills/bill_list.html', {'bills': bills})

def bill_detail_view(request, bill_id):
    bill = Bill.objects.get(id=bill_id)
    items = bill.items.all()
    return render(request, 'bills/bill_detail.html', {'bill': bill, 'items': items})

def add_item_view(request, bill_id):
    if request.method == "POST":
      
        return redirect('bill_detail', bill_id=bill_id)
    return render(request, 'bills/add_item.html', {'bill_id': bill_id})
