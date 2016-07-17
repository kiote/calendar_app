from django.test import TestCase, RequestFactory
from event_template.views import SingleView


class GoogleAuthTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_event(self):
        request = self.factory.get('/event/1')
        # response = SingleView.as_view()(request, 1)
