from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from employees.serializers.user_info import UserFullSerializer

User = get_user_model()


class UserInfoHookAPIView(APIView):
    """
    GET /api/employees/user-info/              -> текущий пользователь
    GET /api/employees/user-info/<pk>/         -> пользователь по pk (только staff/superuser,
                                                 или если pk == request.user.pk)
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None, *args, **kwargs):
        # Если pk не передан — возвращаем текущего пользователя
        if pk is None:
            try:
                target = (
                    User.objects.select_related("passport", "workplace__storage", "workplace__main_office_filial")
                    .prefetch_related("groups")
                    .get(pk=request.user.pk)
                )
            except User.DoesNotExist:
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Если запрошен чужой пользователь — требуем is_staff/is_superuser
            if int(pk) != request.user.pk and not (request.user.is_staff or request.user.is_superuser):
                return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)

            try:
                target = (
                    User.objects.select_related("passport", "workplace__storage", "workplace__main_office_filial")
                    .prefetch_related("groups")
                    .get(pk=pk)
                )
            except User.DoesNotExist:
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserFullSerializer(target, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)