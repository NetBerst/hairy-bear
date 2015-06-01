from blog.models import Post, Comment, CommentForm
from django.views.generic import ListView, DetailView
from django.utils import timezone
# Create your views here.

class PostsListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.order_by('-datetime')

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['comment_list']  = Comment.objects.filter(post = self.kwargs['pk'])
         
        if self.request.method == 'POST':
            cf = CommentForm(self.request.POST).save(commit=False)
            cf.datetime = timezone.now()
            cf.save()
        else:
            context['form'] = CommentForm()
        return context

   # def get(self,request):
    #    super().get(self,request,*args,**kwargs)

