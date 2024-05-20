from django.shortcuts import render

# Create your views here.


post_collection = [
    {'slug': 'first-post', 'title': 'First Post', 'post_text': 'Hello! This is a first post. :P Pretty lame.'},
    {'slug': 'the-real-one', 'title': 'The Real One', 'post_text': 'Now that I created a stupid first post, let\'s go write something real fun like...I need to think about it.'},
    {'slug': 'xweet', 'title': 'Xweet?', 'post_text': 'I\'m kind of treating this as a tweet. Don\' feel like writing too much.'},
    {'slug': 'junk-food', 'title': 'Junk Food', 'post_text': 'I know taht if I\'m really hungry, I crave Mac Donald\'s.'}
]

def index(request):
    post_list = []

    firsts_posts = min(3, len(post_collection))

    for index in range(0, firsts_posts):
        post = post_collection[index]
        post_list.append({
            'slug': post['slug'],
            'title': post['title'],
            'post_text': post['post_text']
        })
    
    return render(request, 'blog/index.html', {
        'post_list': post_list
    })

def posts(request):
    post_list = []

    firsts_posts = min(3, len(post_collection))

    for post in post_collection:
        post_list.append({
            'slug': post['slug'],
            'title': post['title'],
            'post_text': post['post_text']
        })
    
    return render(request, 'blog/posts.html', {
        'post_list': post_list
    })