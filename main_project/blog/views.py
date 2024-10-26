from datetime import date

from django.shortcuts import render
from blog.models import Author, Post

# Create your views here.


post_collection = [
    {'author': 'Me', 'date': date(2024, 3, 20), 'image': 'token.svg', 'slug': 'first-post', 'title': 'First Post', 'post_text': 'Hello! This is a first post. :P Pretty lame.'},
    {'author': 'Me', 'date': date(2024, 3, 21), 'image': 'sort_by_alpha.svg', 'slug': 'the-real-one', 'title': 'The Real One', 'post_text': 'Now that I created a stupid first post, let\'s go write something real fun like...I need to think about it.'},
    {'author': 'Another Me', 'date': date(2024, 3, 23), 'image': 'rule_settings.svg', 'slug': 'xweet', 'title': 'Xweet?', 'post_text': 'I\'m kind of treating this as a tweet. Don\' feel like writing too much.'},
    {'author': 'Me', 'date': date(2024, 3, 26), 'image': 'settings_heart.svg', 'slug': 'junk-food', 'title': 'Junk Food', 'post_text': 'I know that if I\'m really hungry, I crave Mac Donald\'s.'},
    {'author': 'Mi miself', 'date': date(2024, 3, 24), 'image': 'settings_app.svg', 'slug': 'sleepy-me', 'title': 'Sleepy Me', 'post_text': 'You know when you are tired but denied to do something about it? That\'s me.'},
    {'author': 'Me', 'date': date(2024, 3, 25), 'image': 'bottom_app_bar.svg', 'slug': 'keep-posting', 'title': 'Keep Posting!', 'post_text': 'I need to create a few more posts to make this look good. So, here I am. Writing stupid stuff in a blog.'}
]


def get_date(post):
    return post['date']


def index(request):
    post_list = []
    
    # sorted_posts = sorted(post_collection, key=get_date, reverse=True)
    # lastest_posts = sorted_posts[:3]
    
    # for post in lastest_posts:
    #     post_list.append(create_post_render(post))
    
    post_list = Post.objects.all()
    
    if post_list:
        return render(request, 'blog/index.html', {
            'post_list': post_list
        })
        
    return render(request, '404.html', {
        'title': 'Empty :(',
        'msg': 'There is not posts yet!'
    }, status=404)

def posts(request):
    post_list = []

    sorted_posts = sorted(post_collection, key=get_date, reverse=True)
    
    for post in sorted_posts:
        post_list.append(create_post_render(post))
    
    if post_list:
        return render(request, 'blog/posts.html', {
            'post_list': post_list
        })
        
    return render(request, '404.html', {
        'title': 'Empty :(',
        'msg': 'There is not posts yet!'
    }, status=404)
    
def post(request, slug_post):
    
    try:
        required_post = next(post for post in post_collection if post['slug'] == slug_post)
    except:
        return render(request, '404.html', {
            'title': 'Not Found! D:',
            'msg': 'Post not found!'
        }, status=404)

    return render(request, 'blog/post.html', create_post_render(required_post))
    
def create_post_render(post):
    preview = create_preview(post['post_text'])
    
    return {
        'slug': post['slug'],
        'title': post['title'],
        'post_text': post['post_text'],
        'image': post['image'],
        'author': post['author'],
        'date': post['date'],
        'preview': preview
    }
    
def create_preview(text):
    
    min_char = min(len(text), 6)
    split_list = text.split()[:min_char]
    
    if split_list:
        return ' '.join(split_list) + '...'
    
    return ''