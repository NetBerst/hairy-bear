from blog.models import Post, Comment, CommentForm
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.template.response import TemplateResponse
from blog.forms  import UserForm

# Create your views here.

class PostsListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-datetime')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authForm'] = AuthenticationForm()
        return context


def post_detail_func_view(request, pk):
    # Получа объект или ошибку 404
    postForComment = get_object_or_404(Post, id=pk)
    context = {}
    context['post'] = postForComment
    context['comment_list'] = Comment.objects.filter(post=pk)
    template_name = 'blog/post_detail.html'

    if not request.user.is_authenticated():
        context['authForm'] = AuthenticationForm()

    if request.method == 'POST':

        cf = CommentForm(request.POST)
        context['form'] = cf

        if cf.is_valid():
            new_cf = cf.save(commit=False)
            new_cf.post = postForComment
            new_cf.save()
            return HttpResponseRedirect(reverse('blog:detail', args=pk))
    else:
        context['form'] = CommentForm()

    return render(request, template_name, context)


def list_of_page(request):
    return TemplateResponse(request, "blog/index.html", {})


def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('blog:list'))
        else:
            return HttpResponse("Your account is disabled.")
    else:
        # print "Invalid login details: {0}, {1}".format(username, password)
        return HttpResponse("Invalid login details supplied.")


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:list'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,
                  'blog/register.html',
                  {'user_form': user_form, 'registered': registered})