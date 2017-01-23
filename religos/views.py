from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login

from .forms import PlaceForm, PhotoForm, LoginForm
from .models import Place, Photo
from .google_vision import do_ocr


class NameSearchMixin(object):

    def get_queryset(self):
        queryset = super(NameSearchMixin, self).get_queryset()

        queryset.order_by('update_date')

        q = self.request.GET.get("q")

        if q:
            print('do filtering')
            return queryset.filter(name=q)

        return queryset


class IndexView(NameSearchMixin, ListView):
    model = Place
    template_name = 'religos/index.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # queryset = super(NameSearchMixin, self).get_queryset()
        queryset = self.get_queryset()
        place_list = queryset.all()

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

    # def get(self, request, *args, **kwargs):
    #     form = SearchForm()
    #     return render(request, self.template_name, {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     return HttpResponseRedirect('/religos/')


class DetailView(DetailView):
    model = Place
    template_name = 'religos/detail.html'


class EditView(UpdateView):
    model = Place
    template_name = 'religos/edit.html'
    form_class = PlaceForm
    success_url = '/religos'


class AddView(CreateView):
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


class LoginView(FormView):
    template_name = 'religos/login.html'
    form_class = LoginForm
    success_url = '/religos'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('Login success!!')
            # login(request, user)
        else:
            print('Login faild!!')

        return HttpResponseRedirect(
            reverse(
                'religos:index'
            )
        )
