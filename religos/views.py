from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

from .forms import PlaceForm
from .forms import PhotoForm
from .models import Place
from .models import Photo
from .google_vision import do_ocr


class IndexView(generic.ListView):
    model = Place
    template_name = 'religos/index.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        place_list = Place.objects.all()
        paginator = Paginator(place_list, self.paginate_by)

        page = self.request.GET.get('page')
        if page is None:
            page = 1

        try:
            places = paginator.page(page)
        except PageNotAnInteger:
            places = paginator.page(page)
        except EmptyPage:
            places = paginator.page(paginator.num_pages)

        context = super(IndexView, self).get_context_data(**kwargs)
        context['places'] = places
        return context


class DetailView(generic.DetailView):
    model = Place
    template_name = 'religos/detail.html'


class EditView(generic.UpdateView):
    model = Place
    template_name = 'religos/edit.html'
    form_class = PlaceForm
    success_url = '/religos'


class AddView(generic.CreateView):
    model = Place
    template_name = 'religos/add.html'
    form_class = PlaceForm
    success_url = '/religos'


def upload_file(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = Photo(file=request.FILES['file'])
            new_photo.ocr_text = 'dummy'
            new_photo.save()
            new_photo.ocr_text = do_ocr(new_photo.file.path)
            new_photo.save()
            return HttpResponseRedirect(
                reverse(
                    'religos:complete_upload', args=(new_photo.id,)
                )
            )
    else:
        form = PhotoForm()
    return render(request, 'religos/upload_file.html', {'form': form})


def complete_upload(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(
        request,
        'religos/complete_upload.html',
        {'photo': photo}
    )
