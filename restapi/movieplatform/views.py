from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status, generics, mixins, permissions

from rest_framework.views import APIView

from movieplatform.permissions import AdminOrReadOnly, ReviewOwnerOrReadOnly
from movieplatform.serializers import StreamPlatformSerializer, WatchListSerializer, ReviewsSerializer
from movieplatform.models import StreamPlatform, WatchList, Reviews


class ReviewCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def perform_create(self, serializer):
        id = self.kwargs.get('id')
        watchlist = WatchList.objects.get(id=id)
        reviewer = self.request.user
        reviewer_queryset = Reviews.objects.filter(reviewer=reviewer, watchlist=watchlist)
        if reviewer_queryset.exists():
            raise ValidationError("You are already reviewed this object")
        if watchlist.number_ratting == 0:
            watchlist.avg_ratting = serializer.validated_data['ratting']
        else:
            watchlist.avg_ratting = (watchlist.avg_ratting + serializer.validated_data['ratting'])/2
        watchlist.number_ratting = watchlist.number_ratting + 1
        watchlist.save()
        serializer.save(reviewer=reviewer, watchlist=watchlist)


class ReviewList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Reviews.objects.filter(watchlist=id)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReviewOwnerOrReadOnly]
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    lookup_field = 'id'


# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StreamPlatformAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAV(APIView):
    def get(self, request, id):
        try:
            platform = StreamPlatform.objects.get(id=id)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'Object Not Found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        platform = StreamPlatform.objects.get(id=id)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = StreamPlatform.objects.get(id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request):
        watch_list = WatchList.objects.all()
        serializer = WatchListSerializer(watch_list, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailAV(APIView):

    def get(self, request, id):
        try:
            movie = WatchList.objects.get(id=id)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Object Not Found!'}, status=status.HTTP_404_NOT_FOUND)
        serializers = WatchListSerializer(movie, context={'request': request})
        return Response(serializers.data)

    def put(self, request, id):
        movie = WatchList.objects.get(id=id)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = WatchList.objects.get(id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
