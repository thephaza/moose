from django.shortcuts import render, redirect
import requests
from .models import Post, Comment, Contact, Tag
from .paginator import Pagination


def home_view(request):

    posts = Post.objects.filter(is_published = True).order_by('-created_at')
    qwe = Pagination(posts,4)
    d = {
        'posts':qwe.get_page(1)
    }
    return render(request, 'index.html',context=d)

def blog_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    paginator = Pagination(posts, 3)
    data = request.GET

    print("="*50)
    print(data.get('page'))
    print("=" * 50)
    page_numba = int(data.get('page', 1))

    d = {
        'posts': paginator.get_page(page_numba),
        'prev': page_numba - 1,
        'next': page_numba + 1,
        'nimadir': page_numba,
        'pages': range(1,paginator.pager + 1),
        'last' : paginator.the_last(page_numba),
        'first': paginator.the_first(page_numba)
    }
    return render(request, 'blog.html', context=d)

def blog_detail_view(request, pk):
    post = Post.objects.get(id = pk)
    comments = Comment.objects.filter(post = post)
    data = request.POST
    name = data.get('name')
    email = data.get('email')
    website = data.get('website')
    message = data.get('message')

    if request.method == 'POST':
        obj = Comment.objects.create(name = name, email = email, website = website, message = message, post = post)
        obj.save()

        return redirect(f'/blog/{pk}')
    d = {
        'post': post,
        'comments': comments,
        'comments_count': len(comments)
    }
    return render(request, 'blog-single.html', context = d)

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    TELEGRAM_BOT_TOKEN = "8062810091:AAH9T1c64eNnr0vLiSVJJpPppd0oOi6e_FI"
    BASE_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
    CHAT_ID = '-1001660431368'


    if request.method == 'POST':
        data = request.POST
        full_name = data.get('full_name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        print(data)
        obj = Contact.objects.create(full_name=full_name, email=email, subject=subject, message=message)
        obj.save()
        response = requests.get(BASE_URL.format(TELEGRAM_BOT_TOKEN, CHAT_ID, f'Project: Moose\nType:ContactUs\nId:{obj.id}\nMessage:{obj.message}\nEmail:{obj.email}'))
        print(response.json())
        return redirect('/contact')


    return render(request, 'contact.html')

def tag_view(request, pk):
    tag = Tag.objects.get(id = pk)
    tag_name = tag.name
    posts = Post.objects.filter(is_published=True, tag = tag).order_by('-created_at')
    paginator = Pagination(posts, 2)
    data = request.GET
    page_numba = int(data.get('page',1))

    d = {
        'posts': paginator.get_page(page_numba),
        'prev': page_numba - 1,
        'tag_name': tag_name,
        'qanaqadir': page_numba,
        'next': page_numba + 1,
        'pages': range(1, paginator.pager + 1),
        'last': paginator.the_last(page_numba),
        'first': paginator.the_first(page_numba),
        'tag':tag
    }
    return render(request, 'tag-blog.html',context=d)





def all_view(request):
    posts = Post.objects.filter(is_published = True)
    return render(request, 'all-blogs.html', {'posts':posts})