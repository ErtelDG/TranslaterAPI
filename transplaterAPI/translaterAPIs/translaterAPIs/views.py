from rest_framework.response import Response
from rest_framework import viewsets, status, response
from rest_framework.views import APIView
import deepl
from django.http import JsonResponse
from dotenv import load_dotenv
import os

load_dotenv()  # loads the configs from .env

class DeeplView(APIView):
  
  def post(self, request, format=None):
    message_to_translate = request.data.get('message')
    print(message_to_translate)
  
    auth_key = str(os.getenv('deepl_auth_key'))
    translator = deepl.Translator(auth_key)

    result = translator.translate_text(message_to_translate, target_lang="EN-US")
    print(result.text)  # "Bonjour, le monde !"
    return Response({"message":result.text})
