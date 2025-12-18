from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegisterSerializer,UserListSerializer

# PUBLIC: Register user
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"})
        return Response(serializer.errors, status=400)


# PROTECTED: Profile APIs
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email
        })

    def put(self, request):
        user = request.user
        user.email = request.data.get("email", user.email)
        user.save()
        return Response({"message": "Profile updated"})

    def delete(self, request):
        request.user.delete()
        return Response({"message": "User deleted"})
    
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserListSerializer

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

