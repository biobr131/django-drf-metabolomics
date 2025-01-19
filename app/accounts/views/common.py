from rest_framework.generics import ListAPIView, RetrieveAPIView

from accounts.models import CustomUser
from accounts.serializers import UserListSerializer, UserDetailSerializer


class UserListView(ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = "username"
