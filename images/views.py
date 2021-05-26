from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ImageCreateForm


# Submit image form
@login_required
def image_create(request):
    if request.method == 'POST':
        # Form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # Form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # Assign current user to the item
            new_item.user = request.user
            # Save to db
            new_item.save()
            messages.success(request, 'Images added successfully')
            # Redirect to new created item detail_view
            return redirect(new_item.get_absolute_url())
    else:
        # Build our form with data provided via GET
        form = ImageCreateForm(data=request.GET)
    return render(request,
                  'images/image/create.html',
                  {
                      'section': 'images',
                      'form': form
                  })
