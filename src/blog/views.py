from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from .forms import CommentForm
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

class PostTag(generic.ListView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(tag=kwargs['tag'])

        return render(request, self.template_name, {"post_list": posts})


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    print("post objects-->", post)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
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


class AllPosts(generic.ListView):
    template_name = "index.html"
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    paginate_by = 3
