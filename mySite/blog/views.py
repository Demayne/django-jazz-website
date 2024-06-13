from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    """
    View to display a list of all blog posts.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered blog.html template with a list of all posts
        and the 5 most recent posts.
    """
    posts = Post.objects.all()
    recent_posts = Post.objects.order_by('-date')[:5]
    return render(request, 'blog.html', {'posts': posts, 'recent_posts': recent_posts})

def post_detail(request, post_id):
    """
    View to display the details of a single blog post.

    Args:
        request: The HTTP request object.
        post_id (int): The id of the post to display.

    Returns:
        HttpResponse: The rendered post.html template with the details of the specified post.
    """
    post = get_object_or_404(Post, pk=post_id)
    print(post.body)  # Debugging output to print the body content in the terminal
    return render(request, 'post.html', {'post': post})

def header(request):
    """
    View to display the header.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered header.html template.
    """
    return render(request, 'header.html')
