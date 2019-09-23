from .models import *
from .serializers import *

from rest_framework import viewsets
from django.shortcuts import render

# @action처리
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

'''
# ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 조회만 가능
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''
# ModelViewSet은 ListView와 DetailView에 대한 CRUD가 모두 가능

class CafeViewSet(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

    for cafe in queryset:
        cafe_id = cafe.id
        likes_count = Cafe_Like.objects.filter(cafe=cafe_id).count()
        # unlikes_count = Cafe_Unlike.objects.filter(cafe=cafe_id).count()

        cafe.likes_count = likes_count
        #cafe.unlikes_count = unlikes_count
        cafe.save()

    # @action(method=['post'])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 얍을 띄우는 custom api
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍")

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    for review in queryset:
        review_id = review.id
        likes_count = Review_Like.objects.filter(review=review_id).count()
        unlikes_count = Review_Unlike.objects.filter(review=review_id).count()

        review.likes_count = likes_count
        review.unlikes_count = unlikes_count
        review.save()


@csrf_exempt
def cafe_detail(request, pk):
    print('cafe detail function !!')
    try : 
        cafe = Cafe.objects.get(pk=pk)
    except Cafe.DoesNotExist:
        return HttpResponse(status=404)
    
    if (request.method == 'GET'):
        serializers = CafeDetailSerializer(Cafe, context={'request':request})
        return JsonResponse(serializers.data)

class Cafe_LikeViewSet(viewsets.ModelViewSet):
    queryset = Cafe_Like.objects.all()
    serializer_class = Cafe_LikeSerializer
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 얍을 띄우는 custom api
    def Like(self, request, *args, **kwargs):
        return HttpResponse("좋아요를 눌렀습니다.")

class Cafe_UnlikeViewSet(viewsets.ModelViewSet):
    queryset = Cafe_Unlike.objects.all()
    serializer_class = Cafe_UnlikeSerializer

class Review_LikeViewSet(viewsets.ModelViewSet):
    queryset = Review_Like.objects.all()
    serializer_class = Review_LikeSerializer

class Review_UnlikeViewSet(viewsets.ModelViewSet):
    queryset = Review_Unlike.objects.all()
    serializer_class = Review_UnlikeSerializer
