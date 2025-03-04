from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Room

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, RoomForm, RoomUpdateForm, RoomCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


class HomePageView(LoginRequiredMixin, ListView):
    model = Room
    template_name = 'hotel_app/home_page.html'
    context_object_name = 'rooms'
    # success_url = '/roomlist/'

class RoomReserveView(LoginRequiredMixin, UpdateView):
    model = Room
    template_name = 'hotel_app/room_reserve.html'
    fields = ['occupant_name']
    success_url = '/roomlist/'

class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    template_name = 'hotel_app/room_create.html'
    # fields = ['room_number', 'bed_type', 'smoking', 'rate']
    form_class = RoomCreateForm
    success_url = '/create/'

class RoomListView(ListView):
    model = Room
    template_name = 'hotel_app/room_list.html'
    context_object_name = 'rooms'

class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
    template_name = 'hotel_app/room_detail.html'
    context_object_name = 'room'

class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = Room
    template_name = 'hotel_app/room_update.html'
    # fields = ['occupant_name','room_number', 'bed_type', 'smoking', 'rate']
    form_class = RoomForm
    success_url = '/roomlist/'

class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = 'hotel_app/room_delete.html'
    success_url = '/roomlist/'
