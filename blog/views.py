from blog.models import Post, Comment, CommentForm
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

class PostsListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.order_by('-datetime')

def post_detail_func_view(request,pk):
    #Получа объект или ошибку 404 
    postForComment = get_object_or_404(Post,id = pk)
    context = {}
    context['post'] = postForComment
    context['comment_list'] = Comment.objects.filter(post = pk)
    template_name = 'blog/post_detail.html'
        
    if  request.method == 'POST':
        
        cf = CommentForm(request.POST)
        context['form']= cf

        if cf.is_valid():
            new_cf = cf.save(commit=False)
            new_cf.post = postForComment
            new_cf.save()
            return HttpResponseRedirect(reverse('detail',args=pk))
    else:
        context['form']=CommentForm()

    return render(request,template_name,context)

 
