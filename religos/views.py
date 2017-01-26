from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PlaceForm, PhotoForm, LoginForm, SignupForm
from .models import Place, Photo
from .google_vision import do_ocr
from django.contrib.auth.models import User


class NameSearchMixin(object):

    def get_queryset(self):
        queryset = super(NameSearchMixin, self).get_queryset()

        queryset = queryset.filter(user=self.request.user).order_by('update_date')

        q = self.request.GET.get("q")

        if q:
            return queryset.filter(name=q)

        return queryset


class IndexView(LoginRequiredMixin, NameSearchMixin, ListView):
    model = Place
    template_name = 'religos/index.html'
    paginate_by = 5
    login_url = '/religos/home/'
    raise_exception = False

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            print('Logined')
        else:
            print('Logout')

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


class DetailView(LoginRequiredMixin, DetailView):
    model = Place
    template_name = 'religos/detail.html'
    login_url = '/religos/home/'


class EditView(LoginRequiredMixin, UpdateView):
    model = Place
    template_name = 'religos/edit.html'
    form_class = PlaceForm
    success_url = '/religos'
    login_url = '/religos/home/'


class AddView(LoginRequiredMixin, CreateView):
    model = Place
    template_name = 'religos/add.html'
    form_class = PlaceForm
    success_url = '/religos'
    login_url = '/religos/home/'

    def form_valid(self, form):
        place = form.save(commit=False)
        place.user = self.request.user
        place.save()

        return HttpResponseRedirect(
            reverse(
                'religos:index'
            )
        )


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
            login(self.request, user)
        else:
            print('Login faild!!')

        return HttpResponseRedirect(
            reverse(
                'religos:index'
            )
        )


class LogoutView(LoginRequiredMixin, TemplateView):
    template_name = 'religos/logout.html'
    login_url = '/religos/home/'


class SignupView(FormView):
    template_name = 'religos/signup.html'
    form_class = SignupForm
    success_url = '/religos'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password_first = form.cleaned_data['password_first']

        user = User.objects.create_user(
            username=username, password=password_first
        )
        user.save()

        return HttpResponseRedirect(
            reverse(
                'religos:signup_complete'
            )
        )


class SignupCompleteView(TemplateView):
    template_name = 'religos/signup_complete.html'


class HomeView(TemplateView):
    template_name = 'religos/home.html'
