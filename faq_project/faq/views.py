from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')

        # Check if cached data exists
        cached_data = cache.get(f'faqs_{lang}')
        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        faq_list = []

        for faq in faqs:
            translated_question = faq.get_translated_question(lang)
            faq_data = FAQSerializer(faq).data
            faq_data['question'] = translated_question  # Update the question field
            faq_list.append(faq_data)

        # Cache response for 1 hour
        cache.set(f'faqs_{lang}', faq_list, timeout=3600)
        return Response(faq_list)

    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            faq = serializer.save()  # Save will trigger the translation in the model
            return Response(FAQSerializer(faq).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
