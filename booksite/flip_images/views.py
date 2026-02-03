from django.views import View
from django.shortcuts import render, redirect
from .models import FlipbookImage
from .forms import FlipbookImageForm
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
# def index(request):
#     return render(request,'index.html')


MAX_IMAGES = 15

def upload_images(request):
    images = FlipbookImage.objects.all().order_by('id')

    if request.method == "POST":
        files = request.FILES.getlist('images')  # get multiple uploaded files

        if not files:
            return render(request, 'upload_images.html', {
                'images': images,
                'error': 'No files selected'
            })

        if images.count() + len(files) > MAX_IMAGES:
            return render(request, 'upload_images.html', {
                'images': images,
                'error': f'Maximum {MAX_IMAGES} images allowed'
            })

        # Save each uploaded file
        for f in files:
            FlipbookImage.objects.create(image=f)

        return redirect('upload')  # reload page after upload

    return render(request, 'upload_images.html', {'images': images})


def index(request):
    images = FlipbookImage.objects.all()

    if request.method == 'POST':
        files = request.FILES.getlist('image')

        if images.count() + len(files) > 15:
            return render(request, 'flipbook.html', {
                'images': images,
                'error': 'Maximum 15 images allowed'
            })

        for file in files:
            FlipbookImage.objects.create(image=file)

        return redirect('flipbook')

    return render(request, 'index.html', {'images': images})


def delete_image(request, img_id):
    img = get_object_or_404(FlipbookImage, id=img_id)
    img.delete()
    return redirect('upload')
