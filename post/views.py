from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from post.models import Post, Stream


# Create your views here.
@login_required
def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)

    groups_id = []

    for post in posts:
        groups_id.append(post.post_id)

    post_items = Post.objects.filter(id__in=groups_id).all().order_by('-posted')
    template = loader.get_template('index.html')
    context = {
        'post_items': post_items,
    }
    return HttpResponse(template.render(context, request))