
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm



def index(request):
    # If the mothod is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Save (if yes)
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')
            
        else:
            # Error (if no)
            return HttpResponseRedirect(form.errors.as_json())

    

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form = PostForm()

    # Show
    return render(request, 'posts.html', 
                    {'posts': posts})
    

def delete(request, post_id):
    # Find user
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    # If the method is POST
    post = Post.objects.get(id=post_id)
    # if request file is there return tweets
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # save and reddirect to home page
            return HttpResponseRedirect('/')
    # if we want to update then it will redirect back to the update.html it will display to user
        else:
            return HttpResponseRedirect("not valid")
    form = PostForm
    return render(request, 'edit.html', {'post': post, 'form':form})

def like(request, post_id):
    post = Post.objects.get(id = post_id)
    new_like = post.likes + 1
    post.likes = new_like
    post.save()
    return HttpResponseRedirect('/')