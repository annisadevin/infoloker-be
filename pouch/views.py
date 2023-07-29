from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Pouch
from .serializers import PouchSerializer
import requests
import math


def count_expected(goal, current_balance, remainder, token):
    user_account = requests.post('http://34.101.154.14:8175/hackathon/bankAccount/info/all', headers={'Authorization': f"Bearer {token}"}).json()
    print("ACCOUNT", user_account)
    pouch_len = len(user_account)
    saving = remainder / pouch_len
    expected = math.ceil((goal - current_balance)/saving)

    return saving, expected

class PouchListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        pouches = Pouch.objects.all()
        serializer = PouchSerializer(pouches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        goal = request.data.get('goal')
        remainder = request.data.get('remainder')
        token = request.data.get('token')
        saving, expected = count_expected(goal, 0, remainder, token)
        data = {
            'no_account': request.data.get('account'), 
            'user_id': request.data.get('user'), 
            'name': request.data.get('name'), 
            'type_pouch': request.data.get('type'),
            'goal': goal, 
            'expected': expected, 
            'need': request.data.get('need'),
            'saving': saving
        }
        serializer = PouchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PouchDetailApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 3. Retrieve
    def get(self, request, pouch_id, *args, **kwargs):
        '''
        Retrieves the Pouch with given Pouch_id
        '''
        try:
            pouch_instance =Pouch.objects.get(id=pouch_id)
            serializer = PouchSerializer(pouch_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Pouch.DoesNotExist:
            return Response(
                {"res": "Object with Pouch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
class PouchByUserApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 3. Retrieve
    def get(self, request, user_id, *args, **kwargs):
        '''
        Retrieves the Pouch with given Pouch_id
        '''
        pouch_list =Pouch.objects.filter(user_id=user_id)
        serializer = PouchSerializer(pouch_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

