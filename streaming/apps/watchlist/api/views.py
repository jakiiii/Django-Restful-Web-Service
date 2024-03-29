from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, mixins, status
from rest_framework.validators import ValidationError
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.watchlist.api.permissions import AdminOrReadOnly, IsReviewUserOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.watchlist.api.throttling import ReviewCreateThrottling, ReviewListThrottling
from apps.watchlist.models import WatchList, StreamPlatform, Review
from apps.watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from apps.watchlist.api.pagination import WatchListPagination, WatchListLOPagination, WatchListCRPagination


class UserReviewFiltering(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReviewSerializer

    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(reviewer__username=username)

    def get_queryset(self):
        queryset = Review.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(reviewer__username=username)
        return queryset


class ReviewCreateAPI(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    throttle_classes = (ReviewCreateThrottling, AnonRateThrottle)

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        reviewer = self.request.user
        watchlist = WatchList.objects.get(pk=pk)
        reviewer_qs = Review.objects.filter(reviewer=reviewer, watchlist=watchlist)
        if reviewer_qs.exists():
            raise ValidationError("You already reviewed")
        if watchlist.number_ratting == 0:
            watchlist.avt_ratting = serializer.validate_data['ratting']
        else:
            watchlist.avt_ratting = (watchlist.avt_ratting + serializer.validated_data['ratting'])/2
        watchlist.number_ratting = watchlist.number_ratting + 1
        watchlist.save()
        serializer.save(reviewer=reviewer, watchlist=watchlist)


class ReviewListAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReviewSerializer
    # throttle_classes = (ReviewListThrottling, AnonRateThrottle)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('reviewer__username', 'ratting', 'active')

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsReviewUserOrReadOnly,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # throttle_classes = (UserRateThrottle, AnonRateThrottle)
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = 'review-detail'


# class ReviewListAPI(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class ReviewDetailAPI(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class WatchListListAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = WatchListSerializer
    queryset = WatchList.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    search_fields = ('^name', '=platform__name')
    ordering_fields = ('avt_ratting', 'created_at')
    filterset_fields = ('name', 'platform__name', 'avt_ratting', 'number_ratting', 'created_at')
    # pagination_class = WatchListPagination
    pagination_class = WatchListLOPagination
    # pagination_class = WatchListCRPagination


class WatchListListAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchlist, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response({'msg': 'Content is Deleted!'}, status=status.HTTP_204_NO_CONTENT)


class StreamPlatformListAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response({'msg': 'Content is Deleted!'})

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#
#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response({'msg': 'Content is Deleted!'})
