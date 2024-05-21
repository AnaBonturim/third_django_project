from django.shortcuts import render

# Create your views here.


post_collection = {
    'first-post': {'slug': 'first-post', 'title': 'First Post', 'post_text': 'Hello! This is a first post. :P Pretty lame.'},
    'the-real-one': {'slug': 'the-real-one', 'title': 'The Real One', 'post_text': 'Now that I created a stupid first post, let\'s go write something real fun like...I need to think about it.'},
    'xweet': {'slug': 'xweet', 'title': 'Xweet?', 'post_text': 'I\'m kind of treating this as a tweet. Don\' feel like writing too much.'},
    'junk-food': {'slug': 'junk-food', 'title': 'Junk Food', 'post_text': 'I know taht if I\'m really hungry, I crave Mac Donald\'s.'},
    'sleepy-me': {'slug': 'sleepy-me', 'title': 'Sleepy Me', 'post_text': 'You know when you are tired but denied to do something about it? That\'s me.'}
}

def index(request):
    post_list = []
    
    posts = list(post_collection.values())

    last = len(posts) - 1
    first = max(last - 3, 0)

    for index in range(last, first, -1):
        post = posts[index]
        post_list.append({
            'slug': post['slug'],
            'title': post['title'],
            'post_text': post['post_text']
        })
    
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

    posts = list(post_collection.values())
    
    for post in reversed(posts):
        post_list.append({
            'slug': post['slug'],
            'title': post['title'],
            'post_text': post['post_text']
        })
    
    if post_list:
        return render(request, 'blog/posts.html', {
            'post_list': post_list
        })
        
    return render(request, '404.html', {
        'title': 'Empty :(',
        'msg': 'There is not posts yet!'
    }, status=404)
    
def post(request, slug):
    
    required_post = post_collection.get(slug, None)
    
    if (required_post is None):
        return render(request, '404.html', {
            'title': 'Not Found! D:',
            'msg': 'Post not found!'
        }, status=404)

    return render(request, 'blog/post.html', {
        'slug': required_post['slug'],
        'title': required_post['title'],
        'post_text': required_post['post_text']
    })