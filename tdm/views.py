from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer

import os
from os.path import isfile, join
#from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings
from django.http import HttpResponse, Http404
from wsgiref.util import FileWrapper


    
class TDFileManagerView(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request):
      
      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        filename = self.request.query_params.get('filename')

        # folder path
        dir_path = settings.MEDIA_ROOT

        if filename == None:
            # reference: https://pynative.com/python-list-files-in-a-directory/
            """Returns list of file names within directory"""
            
            # list to store files
            res = []

            # Iterate directory
            for path in os.listdir(dir_path):
                # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    res.append(path)
            return Response(res)
        
        else:
            file_path = os.path.join(dir_path, filename)
            if os.path.exists(file_path):
                document = open(file_path, 'rb')
                response = HttpResponse(FileWrapper(document), 'application/file: ' + filename)
                return response
            raise Http404