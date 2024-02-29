from django.shortcuts import render, redirect, get_object_or_404
from portfolio_app.forms import CommentForm
from .models import Comment, Post

def post_detailview(request, id):
    post = get_object_or_404(Post, id=id)
    posts = Post.objects.all()

    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
            content = cf.cleaned_data['content']
            Comment.objects.create(post=post, user=request.user, content=content)
            return redirect('post_detail', id=id)

    else:
        cf = CommentForm()

    comments = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'posts': posts,
        'comment_form': cf,
        'comments': comments,
    }

    return render(request, 'post_detail.html', context)