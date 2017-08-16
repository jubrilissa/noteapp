
from django.test import TestCase

from notes.models import Note


class NoteModelsTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(title='D3 assessment', description='D3 assessment ')

    def test_can_retrieve_note(self):
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, self.note.title)
        self.assertEqual(note.description, self.note.description)
