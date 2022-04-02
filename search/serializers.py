from pkg_resources import require
from rest_framework.serializers import Serializer, CharField, IntegerField, FloatField


class AutoCompleteSuggestionsSerializer(Serializer):
    query = CharField(required=True, allow_null=False, allow_blank=False)
    frequency = IntegerField(required=True, allow_null=False)
    score = FloatField(required=True, allow_null=False)
