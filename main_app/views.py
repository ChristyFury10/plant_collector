from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Plant, Garden
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gardens"] = Garden.objects.all()
        return context
    

class About(TemplateView):
    template_name = "about.html"
    
# class Plant:
#     def __init__(self, name, image, habitat, bio):
#         self.name = name
#         self.image = image
#         self.habitat = habitat
#         self.bio = bio

# plants = [
# Plant("lily", "https://www.gardendesign.com/pictures/images/675x529Max/site_3/asiatic-lily-cappuccino-lily-creative-commons_11653.jpg", "garden", "lily bio"),
# Plant("basil", "https://www.marthastewart.com/thmb/Yhu57XTilZFA3rJum_lgTE-4T2E=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/fresh-basil-getty-0421-d35ca06fec1a4cb596615eed5aa57335.jpg", "herb garden", "yummy" ),
# Plant("black eyed susan", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Rudbeckia_hirta_kz03.jpg/1200px-Rudbeckia_hirta_kz03.jpg", "Maryland", "Maryland state flower" ),
# ]

class PlantList(TemplateView):
    template_name = "plant_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["plants"] = Plant.objects.filter(name__icontains=name)
            context["header"] = f"searching for {name}"
        else:
            context["plants"] = Plant.objects.all()
            context["header"] = "All Plants"

        context["gardens"] = Garden.objects.all()
        return context
    
        return context
    
class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'image', 'habitat','bio']
    template_name = "plant_create.html"
    
    def get_success_url(self):
        return reverse('plant_detail', kwargs={'pk': self.object.pk})

class PlantDetail(DetailView):
    model = Plant
    template_name = "plant_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gardens"] = Garden.objects.all()
        return context

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['name', 'image', 'habitat', 'bio']
    template_name = "plant_update.html"
    def get_success_url(self):
        return reverse('plant_detail', kwargs={'pk': self.object.pk})
    
class PlantDelete(DeleteView):
    model = Plant
    template_name = "plant_delete_confirmation.html"
    success_url = "/plants/"

class GardenPlantAssoc(View):
    def get(self, request, pk, plant_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Garden.objects.get(pk=pk).plants.remove(plant_pk)
        if assoc == "add":
            Garden.objects.get(pk=pk).plants.add(plant_pk)
        return redirect("home")