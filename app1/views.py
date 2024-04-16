from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import loader
import datetime
from .forms import myForm
from .models import customerPurchaseInfo
from django.http import HttpResponseRedirect

def book(request):
    if request.method == 'POST':

        # you can access form data using request.POST.get('')
        success = False
        form = myForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            return HttpResponseRedirect("/success?success=True")

        if not success:
            return render(request, 'error.html', {'success': success})
        else:
            return render(request, 'success.html', {'success': success})
    else:
        form = myForm
        return render(request, 'booking.html', {'success': False,"form":form})

def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Login error")
            return redirect('log_in')
    else:
        return render(request, 'log_in.html', {})
  
def log_out(request):
  logout(request)
  messages.success(request, "Logged out")
  return redirect('log_in')

def home(request):
  return render(request, 'home.html', {}) 

def tenniscourts(request):
  return render(request, 'tcourt.html') 

def success(request):
    bookingStuff = customerPurchaseInfo.objects.all()
    return render(request, 'success.html', {"bookingstuff": bookingStuff})

def deleteBooking(request,name):
    try:
        comment = customerPurchaseInfo.objects.get(name=name)
        comment.delete()
    except customerPurchaseInfo.DoesNotExist:
        comment = None
    return redirect('success')

def viewCakes(request):
    if request.method == 'POST' and 'BreadPudding' in request.POST:
        return render(request, 'Cakes/breadpudding.html', {})
    elif request.method == 'POST' and 'cupcake' in request.POST:
        return render(request, 'Cakes/cupcake.html', {})
    elif request.method == 'POST' and 'pancake' in request.POST:
        return render(request, 'Cakes/pancakes.html', {})
    elif request.method == 'POST' and 'waffles' in request.POST:
        return render(request, 'Cakes/waffles.html', {})
    return render(request, 'cakesInfo.html')

def editBooking(request, name):
    bookingStuff = customerPurchaseInfo.objects.get(name=name)
    form = myForm(request.POST or None, instance=bookingStuff)

    if form.is_valid():
        form.save()
        return redirect('success')
    
    return render(request, 'editBooking.html', {'order': bookingStuff, 'form':form})