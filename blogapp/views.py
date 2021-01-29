from django.shortcuts import render

# Create your views here.
from .models import BlogPost, BlogComment
from .forms import NewCommentForm

class BlogPostDetailView(DetailView):
    model = BlogPost
    # template_name = MainApp/BlogPost_detail.html
    # context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = BlogComment.objects.filter(
            blogpost_connected=self.get_object()).order_by('date_posted')
        data['comments'] = comments_connected
        data['comment_form'] = NewCommentForm( )

        return data

    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content=request.POST.get('content'),
                                  author=request.POST.get('author'),
                                  blogpost_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
