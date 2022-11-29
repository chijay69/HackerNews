from rest_framework.response import Response
from rest_framework.decorators import api_view
from HN.models import *
from .serializers import ItemSerializer


# views goes here

@api_view(['GET'])
def getData(request):
    # person = {'name': 'victor', 'age': 22}
    items = BaseModel.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
