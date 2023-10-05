from rest_framework import viewsets, decorators, response, permissions, decorators
from . import models, serializers
from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ViewSet):
    authentication = []  # Do not verify authentication
    permission_classes = []  # Do not verify permissions
    serializer_class = serializers.UserModelSerializer

    def create(self, request):
        """Create New User Action"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response(
            {"Detail": f'User:{user.username} created'}, status=201
        )

    def retrieve(self, request, pk):
        """List User Action"""
        queryset = models.Contact.objects.filter(user= pk)
        model_contact = []
        for value in queryset:
            model_contact += [{
                "first_name": value.first_name,
                "middle_name" : value.middle_name,
                "email": value.email,
                "phone": value.phone,
                "mobile": value.mobile,
                "user": value.user
            }]
        serializer = []
        output = []
        for contact in model_contact:
            serializer = serializers.ContactModelSerializer(contact)
            print("serializer")
            print(serializer.data)
            output.append(serializer.data)
        return response.Response(output)





class ContactViewSet(viewsets.ModelViewSet):
    """Contac Viewset"""
    authentication = []  # Do not verify authentication
    permission_classes = []  # Do not verify permissions
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactModelSerializer

