from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
  """Test API VIEW"""
  def get(self, request, format=None):
    an_apiview = [
      'Use HTTP mnethods as function',
      'Is similar asdasdasdas',
      'hello babe',
      'you are handsome'
    ]
    return Response({'message': 'Hello', 'an_apiview': an_apiview})