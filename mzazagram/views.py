

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


