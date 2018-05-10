# -*- coding: utf-8 -*-
__author__ = 'admin'
from rest_framework import serializers
from blog.models import blog, Category,Tag
from todolist.models import User
from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.permissions import IsAuthenticated
from blog.models import ShortMessage
from django.conf import settings
import re
from datetime import datetime, timedelta
from rest_framework.response import Response
from blog.utils import yunpian
from random import choice
from api.utils.permissions import IsOwnerOrReadOnly


class UserSerializer(serializers.HyperlinkedModelSerializer):

    #获取当前用户
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )

    class Meta:
        model = User
        #数据唯一对应数据绑定
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=User.objects.all(),
        #         fields=("username", 'qq'),
        #         message="已经存在",
        #     )
        # ]
        fields = ("username", 'qq')


class UserViewSet(CreateModelMixin, ListModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    # queryset = User.objects.filter(pk__gt=10)
    queryset = User.objects.all()
    #验证用户是否登录
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", 'qq')
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(pk__gt=10)
#     serializer_class = UserSerializer

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ("Tag_name",)
class BlogSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    tags = TagSerializer(many=True)
    author = UserSerializer()
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = blog
        fields = "__all__"

class BlogViewSet(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = BlogSerializer


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validated_mobile(self, mobile):
        #验证手机号码
        if re.match(settings.RE_MOBILE, mobile):
            raise serializers.ValidationError("手机号码错误")
        one_min = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if ShortMessage.objects.filter(ShortMessage_created_time__gt=one_min, ShortMessage_mobile=mobile):
            raise serializers.ValidationError("时间间隔太短")
        return mobile

class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = SmsSerializer

    def generate_code(self):

        seeds = "1234567890"
        random_str = []

        for i in range(6):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        code = self.generate_code()

        Yunpian = yunpian.YunPianWang(settings.API_KEY)
        sms_code = Yunpian.single_send(mobile=mobile, code=code)

        if sms_code["code"] != 0:
            return Response({
                "mobile": sms_code["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = ShortMessage.objects.create(ShortMessage_mobile=mobile, ShortMessage_code=code, ShortMessage_type=1)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



