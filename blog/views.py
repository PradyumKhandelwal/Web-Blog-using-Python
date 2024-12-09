from http.client import HTTPResponse
from msilib.schema import ListView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone
from blog.forms import PostForm


#Login
@login_required
def home(request):
    if (request.user.is_authenticated):
        return render ('home')
    else: 
        return render ('login')

    return render(request, "blog/base.html", {})


def post_list(request):

    posts = Post.objects.all()
    return render(request, 'blog/navbar.html', {'posts': posts})


# Post.objects.get(pk=pk)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def User_registration1(request):
    context = {}
    
    context["form"] = GeeksModel()
    if request.method == "POST":
       
        a = request.POST.get('first_name')
        b = request.POST.get('last_name')
        c = request.POST.get('roll_number')
        d = request.POST.get('password')
        query_set = Post(author =request.user, title=b, text=c)
        query_set.save()
        print(request.POST)
    # elif request.method == "GET":
        # a = request.GET['first_name']
        # b = request.GET['last_name']
        # c = request.GET['roll_number']
        # d = request.GET['password']
        # print(request.GET)

    
    # query_set= Post(title= a, description=b)
    # query_set.save()

    return render(request, "blog/post_edit.html", context)
    # print({name: a, surname: b, roll_no: c, password: d})

def post_create(request):
    if request.POST:
        form = PostForm(request.POST)
    
        if form.is_valid():
            print("not working")
            # data = form.cleaned_data()
            # print(data)
            form.save()
            # return HTTPResponse("great")
        else:
            print("else working")    
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

    # def post_class()
from django.views.generic import ListView

class AcmeBookListView(ListView):

    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing') #fk
    template_name = 'books/acme_list.html'

{{ book_list.title}}