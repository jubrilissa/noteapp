from rest_framework.test import APIClient, APITestCase
from django.core.urlresolvers import reverse
from notes.models import Note


class NoteViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.note1 = Note.objects.create(title="Bla bla bla1", description="Oshey1")
        self.note2 = Note.objects.create(title="Bla bla black2", description="Oshey2")
        self.note3 = Note.objects.create(title="Bla bla black3", description="Oshey3")

    def test_retrieve_all_note(self):
        url = reverse('list_note')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_can_create_note(self):
        url = reverse("list_note")
        data = {"title": "created from here", 'description': "created oshey"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_can_delete_note(self):
        url = reverse("single_note", kwargs={"pk": self.note1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_can_edit_note(self):
        url = reverse("single_note", kwargs={"pk": self.note2.id})
        data = {"title": "The updated note", "description": "updated description"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        Note.objects.all().delete()
