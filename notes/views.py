
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from django.http import Http404

from notes.serializers import NoteSerializer
from notes.models import Note
from notes.mixins import NotePaginationMixin


class NotePagination(PageNumberPagination):
    page_size = 2
    max_page_size = 2


class NoteListView(APIView, NotePaginationMixin):
    """List all notes or create a new note"""
    pagination_class = NotePagination
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request):
        page = self.paginate_queryset(self.queryset)

        if page is not None:
            serializer = NoteSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = NoteSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetailView(APIView):
    """Retrieve, update or delete a single note"""

    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
