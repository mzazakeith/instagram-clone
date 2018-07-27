
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


