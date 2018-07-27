

@login_required
def explore(request):
    images = Image.objects.all().order_by('-pub_date')
    return render(request, 'explore.html', {"images": images})
