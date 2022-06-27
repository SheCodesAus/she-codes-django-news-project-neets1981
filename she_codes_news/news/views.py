from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stories = NewsStory.objects.all().order_by('-pub_date') # ordering from newest to oldest
        context['latest_stories'] = stories[:4]
        context['all_stories'] = stories
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class=StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

class EditStoryView(UpdateView):
    model = NewsStory
    template_name: str= 'news/editstory.html'
    fields =['title','content','place_image']
    context_object_name = 'storyedit'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  

class DeleteStoryView(DeleteView):
    model = NewsStory
    template_name: str= 'news/deletestory.html'
    context_object_name = 'deletestory'
    success_url = reverse_lazy('news:index')

# class AuthorListView(ListView):
class StoriesByAuthor(generic.ListView):
    model = NewsStory
    # form_class = StoryForm
    context_object_name = 'author_list'
    template_name = 'news/author.html'
    paginate_by = 50


    def get_queryset(self):
        author_id = self.kwargs['author_id']
        return self.model.objects.filter(author = author_id,)
        

    def get_context_data(self, **kwargs):
        context = super(StoriesByAuthor, self).get_context_data(**kwargs)
        context['author'] = self.get_queryset()
        return context
        

