from datetime import date

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import CommentForm
from blog.models import Author, Post, Comment

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
    template_name = 'blog/posts.html'
    model = Post
    context_object_name = 'post_list'
    ordering = ['-date']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        
        return data


class AllPostsView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    context_object_name = 'post_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date')

class PostView(View):
    
    def get(self, request, slug):
        context = self.create_default_context(request, slug)
        context['comment_form'] = CommentForm()
        
        return render(request, 'blog/post.html', context)
        
    def post(self, request, slug):
        context = self.create_default_context(request, slug)
        post = context.get('post')
        
        comment_form = CommentForm(request.POST)
        context['comment_form'] = comment_form
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            
            return HttpResponseRedirect(reverse('post', args=[slug]))
        
        # Esse return ocorre apenas se o comentário inserido for inválido.
        return render(request, 'blog/post.html', context)
        
    def create_default_context(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_list = post.comments.all().order_by("-id")
        
        read_later_list = request.session.get('read-later-list')
        read_later = read_later_list is not None and post.id in read_later_list
        
        return {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_list': comment_list,
            'read_later': read_later
        }
    

class AllCommentsView(ListView):
    template_name = 'blog/comments.html'
    model = Comment
    context_object_name = 'comment_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-id')


class ReadLaterPostView(View):
    def get(self, request):
        read_later_list = request.session.get('read-later-list')
        post_list = []
        
        if read_later_list is not None:
            post_list = Post.objects.filter(id__in=read_later_list)
            
        return render(request, 'blog/read_later.html', {
            'post_list': post_list
        })
        
    def post(self, request):
        post_id = request.POST.get('post_id', 0)
        
        if post_id:
            post_id = int(post_id)
            
            read_later_list = request.session.get('read-later-list')
            
            if read_later_list is None:
                read_later_list = []
            
            if post_id not in read_later_list:
                read_later_list.append(post_id)
            else:
                read_later_list.remove(post_id)
                
            request.session['read-later-list'] = read_later_list
            
        return HttpResponseRedirect(reverse('blog-home'))


class RemoveReadLaterView(View):
    def post(self, request, id):
        read_later_list = request.session.get('read-later-list')
        
        if read_later_list is not None and id in read_later_list:
            read_later_list.remove(id)
            
        request.session['read-later-list'] = read_later_list
            
        return HttpResponseRedirect(reverse('read-later'))

    
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