from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserDataSeializer
from core.models import UserData

@api_view(["GET"])
def getData(request):
    data = UserData.objects.all()
    serializer = UserDataSeializer(data, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def addData(request):
    serializer = UserDataSeializer(data=request.data)
    name = request.data["name"]
    if serializer.is_valid():
        serializer.save()
    return Response(f"User {name} successfully added")
   