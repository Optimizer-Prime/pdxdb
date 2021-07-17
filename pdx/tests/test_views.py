from django.test import TestCase
from django.urls import reverse_lazy


class HomePageViewTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('submit/')
        print(response.templates)
        self.assertTemplateUsed(response, 'submit.html')
