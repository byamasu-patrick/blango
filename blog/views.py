from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.shortcuts import redirect
from blog.forms import CommentForm, PostForm
# Create your views here.

class PostView(View):
    post_form = PostForm()
    
    def get(self, request):        
        posts = Post.objects.filter(published_at__lte=timezone.now())    
        
        return render(request, "blog/index.html", {
            "posts": posts,
            "post_form": self.post_form
        })
        
    def post(self, request):
        if request.method == "POST":
            self.post_form = PostForm(request.POST)        
            if self.post_form.is_valid():
                post = self.post_form.save(commit=False)
                post.author = request.user
                post.save()
                
                return redirect(request.path_info)  
            else:
                return redirect(request.path_info)        
   
class PostDetailView(View):
    comment_form = CommentForm()
    
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        
        return  render(request, "blog/post-detail.html", {
            "post": post,
            "comment_form": self.comment_form
        })
        pass
    
    def post(self, request, slug):        
        post = get_object_or_404(Post, slug=slug)
        
        if request.user.is_active:
            if request.method == "POST":
                self.comment_form = CommentForm(request.POST)

                if self.comment_form.is_valid():
                    comment = self.comment_form.save(commit=False)
                    comment.content_object = post
                    comment.creator = request.user
                    comment.save()

                    return redirect(request.path_info)
        else:
            return redirect(request.path_info)
        pass
    pass

    