from rest_framework.response import Response
from rest_framework import status

def post(self, request):
    user = request.data
    serializer = UserSerializer(data=user)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"user": serializer.data, "status": status.HTTP_200_OK})