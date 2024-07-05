# community/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Accountapp.models import Follow, Member
from .models import Archive
import random

@login_required
def community_home(request):
    # Randomly select an archive from other users
    other_users_archives = Archive.objects.exclude(user=request.user)
    random_archive = random.choice(other_users_archives) if other_users_archives.exists() else None

    # Get user profile data
    user = request.user
    followers = Follow.objects.filter(following=user)
    following = Follow.objects.filter(follower=user)

    context = {
        'random_archive': random_archive,
        'user': user,
        'followers_count': followers.count(),
        'following_count': following.count(),
    }
    return render(request, 'community/home.html', context)

@login_required
def follower_list(request):
    user = request.user
    followers = Follow.objects.filter(following=user)
    return render(request, 'community/follower_list.html', {'followers': followers})

@login_required
def following_list(request):
    user = request.user
    following = Follow.objects.filter(follower=user)
    return render(request, 'community/following_list.html', {'following': following})
