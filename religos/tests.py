import io

from PIL import Image

from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import PhotoForm
from django.core.files.uploadedfile import SimpleUploadedFile


from .models import Photo


class AddTests(TestCase):
    def test_get(self):
        response = self.client.get(reverse('religos:add'))
        self.assertEqual(response.status_code, 200)


class UploadFileTests(TestCase):
    def test_get(self):
        response = self.client.get(reverse('religos:upload_file'))
        self.assertEqual(response.status_code, 200)


class CompleteUploadTests(TestCase):
    def test_get(self):
        response = self.client.get(reverse('religos:complete_upload'))
        self.assertEqual(response.status_code, 200)


class PhotoFormTests(TestCase):
    class UploadFormTest(TestCase):
        def _get_form_class(self):
            from .forms import PhotoForm
            return PhotoForm

        def _make_dummy_image(self):
            file_obj = io.BytesIO()
            im = Image.new('RGBA', size=(10, 10), color=(256, 0, 0))
            im.save(file_obj, 'png')
            file_obj.name = 'test.png'
            file_obj.seek(0)
            return file_obj

        def test_it(self):
            img = self._make_dummy_image()
            Form = self._get_form_class()
            form = Form(
                data={'title': 'test title'},
                files={'img': SimpleUploadedFile(
                    img.name,
                    img.read(),
                    content_type='image/png',
                )},
            )
            self.assertTrue(form.is_valid())
