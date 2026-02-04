from django.views import View
from django.shortcuts import render, redirect
from .models import FlipbookImage
from .forms import FlipbookImageForm
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
# def index(request):
#     return render(request,'index.html')


MAX_IMAGES = 15

# def upload_images(request):
#     images = FlipbookImage.objects.all().order_by('id')

#     if request.method == "POST":
#         files = request.FILES.getlist('images')  # get multiple uploaded files

#         if not files:
#             return render(request, 'upload_images.html', {
#                 'images': images,
#                 'error': 'No files selected'
#             })

#         if images.count() + len(files) > MAX_IMAGES:
#             return render(request, 'upload_images.html', {
#                 'images': images,
#                 'error': f'Maximum {MAX_IMAGES} images allowed'
#             })

#         # Save each uploaded file
#         for f in files:
#             FlipbookImage.objects.create(image=f)

#         return redirect('upload')  # reload page after upload

#     return render(request, 'upload_images.html', {'images': images})


def upload_images(request):
    images = FlipbookImage.objects.all().order_by('id')

    front_page = FlipbookImage.objects.filter(is_front=True).first()
    pages = FlipbookImage.objects.filter(is_front=False).order_by('id')
    print("UPLOAD VIEW → front_page:", front_page)

    if request.method == "POST":
        files = request.FILES.getlist('images')

        is_front = 'is_front' in request.POST  # ✅ SAFE checkbox check
        title = request.POST.get('title') or None
        caption = request.POST.get('caption') or None

        raw_date = request.POST.get('date')
        date = raw_date if raw_date else None

        if not files:
            return render(request, 'upload_images.html', {
                'images': images,
                'front_page': front_page,
                'pages': pages,
                'error': 'No images selected'
            })

        # 🔥 FRONT PAGE LOGIC
        if is_front:
            image = files[0]   # only ONE front page image allowed

            # delete old front page
            FlipbookImage.objects.filter(is_front=True).delete()

            FlipbookImage.objects.create(
                image=image,
                title=title,
                date=date,
                caption=caption,
                is_front=True
            )
            print("🔥 SAVING FRONT PAGE")

        # 🔥 NORMAL PAGES LOGIC
        else:
            print("🔥 SAVING NORMAL PAGES")

            for f in files:
                FlipbookImage.objects.create(
                    image=f,
                    caption=caption,
                    is_front=False
                )
        front_page = FlipbookImage.objects.filter(is_front=True).first()

        print("DEBUG front_page object:", front_page)
        print("DEBUG front_page exists:", bool(front_page))
        return redirect('upload')

    return render(request, 'upload_images.html', {
        'images': images,
        'front_page': front_page,
        'pages': pages,
    })



def index(request):
    images = FlipbookImage.objects.all()
    front_page = FlipbookImage.objects.filter(is_front=True).first()
    pages = FlipbookImage.objects.filter(is_front=False).order_by('id')

    if request.method == 'POST':
        files = request.FILES.getlist('image')

        if images.count() + len(files) > 15:
            return render(request, 'index.html', {
                'images': images,
                'error': 'Maximum 15 images allowed'
            })

        for file in files:
            FlipbookImage.objects.create(image=file)

        return redirect('flipbook')

    return render(request, 'index.html', {'images': images,       
    'front_page': front_page,
    'pages': pages,})


def delete_image(request, img_id):
    img = get_object_or_404(FlipbookImage, id=img_id)
    img.delete()
    return redirect('upload')

def flipbook_view(request):
    front_page = FlipbookImage.objects.filter(is_front=True).first()
    pages = FlipbookImage.objects.filter(is_front=False).order_by('id')
    print("DEBUG front_page:", front_page)

    return render(request, 'index.html', {
        'front_page': front_page,
        'pages': pages,
    })
