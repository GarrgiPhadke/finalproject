from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def review(request):
    reviews = Review.objects.all()
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review')
    return render(request, 'review/review.html', {'reviews': reviews, 'form': form})
