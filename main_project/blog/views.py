from datetime import date

from django.shortcuts import render, get_object_or_404
from blog.models import Author, Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


# post_collection = [
#     {'author': 'Me', 'date': date(2024, 3, 20), 'image': 'token.svg', 'slug': 'first-post', 'title': 'First Post', 'post_text': 'Hello! This is a first post. :P Pretty lame.'},
#     {'author': 'Me', 'date': date(2024, 3, 21), 'image': 'sort_by_alpha.svg', 'slug': 'the-real-one', 'title': 'The Real One', 'post_text': 'Now that I created a stupid first post, let\'s go write something real fun like...I need to think about it.'},
#     {'author': 'Another Me', 'date': date(2024, 3, 23), 'image': 'rule_settings.svg', 'slug': 'xweet', 'title': 'Xweet?', 'post_text': 'I\'m kind of treating this as a tweet. Don\' feel like writing too much.'},
#     {'author': 'Me', 'date': date(2024, 3, 26), 'image': 'settings_heart.svg', 'slug': 'junk-food', 'title': 'Junk Food', 'post_text': 'I know that if I\'m really hungry, I crave Mac Donald\'s.'},
#     {'author': 'Mi miself', 'date': date(2024, 3, 24), 'image': 'settings_app.svg', 'slug': 'sleepy-me', 'title': 'Sleepy Me', 'post_text': 'You know when you are tired but denied to do something about it? That\'s me.'},
#     {'author': 'Me', 'date': date(2024, 3, 25), 'image': 'bottom_app_bar.svg', 'slug': 'keep-posting', 'title': 'Keep Posting!', 'post_text': 'I need to create a few more posts to make this look good. So, here I am. Writing stupid stuff in a blog.'}
# ]


class LastPostsView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'post_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date')[:3]


class AllPostsView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'post_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date')

class PostView(DetailView):
    template_name = 'blog/post.html'
    model = Post
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = context['object'].tags.all()
        
        return context
    
# def index(request):
#     post_list = []
    
#     # Django faz o slice do QuerySet no SQL, então essa expressão abaixo é eficiente
#     post_list = Post.objects.all().order_by("-date")[:3]

#     if post_list:
#         return render(request, 'blog/index.html', {
#             'post_list': post_list
#         })
        
#     return render(request, '404.html', {
#         'title': 'Empty :(',
#         'msg': 'There is not posts yet!'
#     }, status=404)

# def posts(request):
#     post_list = Post.objects.all().order_by("-date")
    
#     if post_list:
#         return render(request, 'blog/posts.html', {
#             'post_list': post_list
#         })
        
#     return render(request, '404.html', {
#         'title': 'Empty :(',
#         'msg': 'There is not posts yet!'
#     }, status=404)
  
        
# def post(request, slug_post):
#     required_post = get_object_or_404(Post, slug=slug_post)
    
#     return render(request, 'blog/post.html', {
#         'post': required_post,
#         'post_tags': required_post.tags.all()
#     })