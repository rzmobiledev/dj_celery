from functools import partial
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
# from drf_spectacular.types import OpenApiTypes

from app.models import (User, Article)
from app.serializer import (
    UserSerializer, UserSerializerDetail, ArticleSerializer, )


class UserView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserSerializer

    @extend_schema(
        request=UserSerializer,
        responses={201: UserSerializer},
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        # extra parameters added to the schema
        # override default docstring extraction
        description='More descriptive text',
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id="get_all_users",
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
        examples=[
            OpenApiExample(
                'Example 1',
                description='longer description',
                value=[{
                    "username": "kiran",
                    "email": "kiran@gmail.com",
                }],
            ),

        ],
    )
    def get(self, request):
        user = User.objects.all()
        serializer = self.serializer_class(instance=user, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserViewDetail(APIView):

    serializer_class = UserSerializerDetail
    permission_classes = [IsAuthenticated, IsAdminUser]

    @extend_schema(
        request=UserSerializerDetail,
        responses={200: UserSerializerDetail},
    )
    def put(self, request, pk):
        instance = User.objects.get(pk=pk)
        serializer = self.serializer_class(
            instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        # override default docstring extraction
        description='More descriptive text',
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id="get_one_user",
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
        examples=[
            OpenApiExample(
                'Example 1',
                description='longer description',
                value=""
            ),

        ],
    )
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ArticleView(APIView):

    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=ArticleSerializer,
        responses={201: ArticleSerializer},
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        # override default docstring extraction
        description='More descriptive text',
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id="get_all_articles",
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
        examples=[
            OpenApiExample(
                'Example 1',
                description='longer description',
                value=""
            ),

        ],
    )
    def get(self, request):
        article = Article.objects.all()
        serializer = self.serializer_class(instance=article, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ArticleViewDetailAndUpdate(APIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=ArticleSerializer,
        responses={200: ArticleSerializer},
    )
    def put(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = self.serializer_class(
            instance=article, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        # override default docstring extraction
        description='More descriptive text',
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id="get_one_article",
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
        examples=[
            OpenApiExample(
                'Example 1',
                description='longer description',
                value=""
            ),

        ],
    )
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = self.serializer_class(instance=article)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
