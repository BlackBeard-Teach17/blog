from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.generic import ListView

from .models import Post, Comment
from .forms import EmailPostForm, CommentForm

def post_list(request):
    posts_list = Post.published.all()
    paginator = Paginator(posts_list, 3) # 3 posts in each page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page':page, 'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    #List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create comment obj but not saved to DB
            new_comment = comment_form.save(commit=False)
            # Associate comment with the current post
            new_comment.post = post

            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'post': post, 'comments':comments, 'new_comment': new_comment,
                                                     'comment_form': comment_form})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.changed_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd[0]} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n {cd[0]}\'s comments: {cd[3]}"
            send_mail(subject, message, 'admin@myblog.com', [cd[2]])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, sent:'sent' })

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/post_list.html'