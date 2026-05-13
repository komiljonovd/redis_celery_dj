from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import News
from .serializers import NewsSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page,never_cache
from rest_framework.generics import ListAPIView
# Create your views here.




# class NewsAPiView(APIView):
#     def get(self,request):
#         cache_key = 'news_list_cache_15min'
#         data = cache.get(cache_key)

#         if data is not None:
#             print('данные из Redis:',data)

#             return Response(data)
        
#         queryset = News.objects.filter(is_published=True)
#         serializer = NewsSerializer(queryset,many=True)

#         cache.set(cache_key,serializer.data,timeout=60*15)

#         return Response(serializer.data)

# class NewsAPiView(APIView):
#     @method_decorator(cache_page(60 * 15,key_prefix='news_15min'))
#     def get(self, request):
#         print('DB')
#         queryset = News.objects.filter(is_published=True)
#         serializer = NewsSerializer(queryset, many=True)
#         return Response(serializer.data)
                

class NewsAPiView(ListAPIView):
    queryset = News.objects.filter(is_published=True).order_by('-created_at')
    serializer_class = NewsSerializer
    
    @method_decorator(cache_page(60 * 15, key_prefix='news_api_list'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)