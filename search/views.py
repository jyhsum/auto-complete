from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FrequencyTable
from .utils import get_auto_complete_suggestions
from .serializers import AutoCompleteSuggestionsSerializer


class SearchView(APIView):
    def get(self, request):
        keyword = request.query_params.get('q')
        suggestions = get_auto_complete_suggestions(keyword)
        records = FrequencyTable.objects(query=keyword)
        if not records:
            new_record = FrequencyTable(query=keyword, frequency=1)
            new_record.save()
        else:
            record = records.first()
            record.frequency = record.frequency + 1
            record.save()
        serializer = AutoCompleteSuggestionsSerializer(data=suggestions, many=True)
        serializer.is_valid(raise_exception=True)
        return Response({'data': serializer.data})
