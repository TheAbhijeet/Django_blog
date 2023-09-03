from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from .models import Post



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            user = request.user  # Get the logged-in user

            # Check if the provided first_name and email match the logged-in user's data
            if (
                user.first_name == comment_form.cleaned_data['name']
                and user.email == comment_form.cleaned_data['email']
            ):
                new_comment = 'success'  # Comment successfully created
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
            else:
                # Provided first_name or email do not match the logged-in user's data
                new_comment = 'mismatch'

    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

