from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from friendship.exceptions import AlreadyExistsError
from friendship.models import Follow

from .models import Image, Profile, Comments
from .forms import NewImageForm, CreateProfileForm, CommentForm


@login_required(login_url='signup')
def index(request):
    comments = Comments.objects.all()
    form = CommentForm()
    mine = Profile.objects.get(user=request.user.id)
    profiles = Profile.objects.all()
    user = request.user
    following = Follow.objects.following(user)
    images =[]
    for follower in following:
        wenyewe = follower.id
        images+=Image.objects.filter(owner=wenyewe).order_by('-pub_date')
    return render(request, 'index.html',{'following':following,'images':images,"profiles":profiles, "mine":mine,"comment":form, "comments":comments, 'user':user})


@login_required
def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = current_user
            image.save()
            return redirect(index)
    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})


@login_required
def profile(request):
    current_user = request.user.id
    user = request.user
    profile = Profile.objects.get(user=current_user)
    images = Image.objects.filter(owner=current_user).order_by('-pub_date')
    followers = len(Follow.objects.followers(user))
    following = len(Follow.objects.following(user))
    posts = len(Image.objects.filter(owner=user))
    return render(request, 'profile.html', {"images": images, 'user': request.user, "profile": profile,"followers":followers,"following":following,"posts":posts})


@login_required
def explore(request):
    images = Image.objects.all().order_by('-pub_date')
    return render(request, 'explore.html', {"images": images})


@login_required
def userprofile(request, user_id):
    users = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=users)
    images = Image.objects.filter(owner=users).order_by('-pub_date')
    followers = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    posts = len(Image.objects.filter(owner=users))
    people_following = Follow.objects.following(request.user)
    return render(request, 'profile/userprofile.html', {"user": users, "profile": profile, "images": images,"followers":followers, "following":following, "posts":posts, "people_following":people_following})


def follow(request, user_id):
    users = User.objects.get(id=user_id)
    try:
        follow = Follow.objects.add_follower(request.user, users)
    except AlreadyExistsError:
        return render(request, "followed.html")
    # return render(request, 'profile/userprofile.html', {"follow": follow})
    return redirect('/userprofile/'+user_id)

@login_required
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('/profile')
    else:
        form = CreateProfileForm()
    return render(request, 'registration/activated.html', {"form": form})


@login_required
def comment(request,image_id):
   if request.method == 'POST':
       image = get_object_or_404(Image, pk = image_id)
       form = CommentForm(request.POST, request.FILES)
       if form.is_valid():
           comment = form.save(commit=False)
           comment.commenter = request.user
           comment.image_id = image
           comment.save()
           return redirect(index)
   else:
       form = CommentForm()
   return render(request, 'index.html',{'comment':form})



