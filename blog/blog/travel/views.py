from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView
from .models import Entry
class HomeView(ListView,LoginRequiredMixin):
    model=Entry
    template_name='travel/index.html'
    context_object_name="blog_travel"
    ordering=['-entry_date']
    paginate_by= 2 
class EntryView(DetailView,LoginRequiredMixin):
    model=Entry
    template_name='travel/travel_detail.html'
class CreateEntryView(CreateView,LoginRequiredMixin):
    model=Entry
    template_name='travel/create_entry.html'
    fields=['entry_title','entry_text']
    def form_valid(self,form):
        form.instance.entry_author=self.request.user
        return super().form_valid(form)


# Create your views here.

