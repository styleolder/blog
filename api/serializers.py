# -*- coding: utf-8 -*-
__author__ = 'admin'
from rest_framework import serializers
from blog.models import blog, Category
from todolist.models import User
from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin
from blog.models import ShortMessage
from django.conf import settings
import re
from datetime import datetime, timedelta
from rest_framework.response import Response
from blog.utils import yunpian
from random import choice


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'user_icon')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(pk__gt=10)
    serializer_class = UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
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



