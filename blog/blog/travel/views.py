from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Entry,Comment
from django.urls import reverse,reverse_lazy
class HomeView(ListView,LoginRequiredMixin):
    model=Entry
    template_name='travel/index.html'
    context_object_name="blog_travel"
    ordering=['-entry_date']
    paginate_by= 2 
class EntryView(DetailView,LoginRequiredMixin):
    model=Entry
    template_name='travel/travel_detail.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        comments=Comment.objects.filter(entry=self.kwargs['pk'])
        context['comments']=comments
        return context

class CreateEntryView(CreateView,LoginRequiredMixin):
    model=Entry
    template_name='travel/create_entry.html'
    fields=['entry_title','entry_text']
    def form_valid(self,form):
        form.instance.entry_author=self.request.user
        return super().form_valid(form)

def home(request):
    return render(request,'travel/home.html',{})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    template_name = "travel/post_confirm_delete.html"
    success_url = "/"

    def test_func(self):
        # get current working post
        post = self.get_object()
        if self.request.user == post.entry_author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    template_name = "travel/postmodel_form.html"
    fields = ["entry_title", "entry_text"]

    # method to assign username to author for updating author name in post
    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)

    # function to permit editing post based on their ownership
    def test_func(self):
        # get current working post
        post = self.get_object()
        if self.request.user == post.entry_author:
            return True
        return False

def profile(request):
    return render(request, "travel/profile.html")
class CommentCreate(LoginRequiredMixin,CreateView):

    model=Entry
    fields=['entry_text']
    template_name='travel/create_comment.html'
    login_url=reverse_lazy('login')

    def form_valid(self,form):
         form.instance.user=self.request.user
         form.instance.post=Entry.objects.get(id=self.kwargs['pk'])
         return super().form_valid(form)
    def get_success_url(self):
        return reverse('travel:blog-travel-detail',kwargs={'pk':self.kwargs[pk]})

# Create your views here.

