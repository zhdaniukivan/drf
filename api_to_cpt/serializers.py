import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


# def encode():
#     model = WomenModel('Angelina Jolie', 'Content: Angeline Jolie')
#     model_str = WomenSerializer(model)
#     print(model_str.data, type(model_str.data), sep='\n')
#     json = JSONRenderer().render(model_str.data)
#     print(json, type(json), sep='\n')
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angeline Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)



# class WomenSerializer(serializers.ModeSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')
