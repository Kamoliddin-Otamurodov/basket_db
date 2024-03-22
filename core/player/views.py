from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

from .models import Player , City , Coach , Team , User

from .serializers import PlayerSerializer , CitySerializer , CoachSerializer , TeamSerializer , UserSerializer


class UserView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request) -> Response:
        customer = User.objects.all()

        serializer = UserSerializer(customer, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(self, request: Request, user_id: int) -> Response:
        customer = User.objects.get(id=user_id)

        serializer = UserSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, user_id: int) -> Response:
        data = request.data

        task = User.objects.get(id=user_id)

        serializer = UserSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, user_id: int) -> Response:
        task = User.objects.get(id=user_id)
        task.delete()

        return Response({'message': 'deleted.'})
    

class PlayerView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request) -> Response:
        tasks = Player.all()

        serializer = PlayerSerializer(tasks, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = PlayerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayerDetailView(APIView):
    def get(self, request: Request, todo_id : int) -> Response:
        customer = Player.objects.get(id = todo_id)

        serializer = PlayerSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, todo_id : int) -> Response:
        data = request.data

        task = Player.objects.get(id = todo_id)

        serializer = PlayerSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, todo_id : int) -> Response:
        task = Player.objects.get(id = todo_id)
        task.delete()

        return Response({'message': 'deleted.'})
    

class CityView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request , todo_id : int) -> Response:
        customer = City.objects.filter(todo_id = todo_id)

        serializer = CitySerializer(customer, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request , todo_id : int) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = CitySerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityDetailView(APIView):
    def get(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        customer = City.objects.get(todo_id = todo_id , id=task_id)

        serializer = CitySerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        data = request.data

        task = City.objects.get(todo_id = todo_id , id=task_id)

        serializer = CitySerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
    def patch(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        data = request.data

        task = City.objects.get(todo_id = todo_id , id=task_id)

        serializer = CitySerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        task = City.objects.get(todo_id = todo_id , id=task_id)
        task.delete()

        return Response({'message': 'deleted.'})
    
    from rest_framework.views import APIView


class CoachView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request , todo_id : int) -> Response:
        customer = Coach.objects.filter(todo_id = todo_id)

        serializer = CoachSerializer(customer, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request , todo_id : int) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = CoachSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoachDetailView(APIView):
    def get(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        customer = Coach.objects.get(todo_id = todo_id , id=task_id)

        serializer = CoachSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        data = request.data

        task = Coach.objects.get(todo_id = todo_id , id=task_id)

        serializer = CoachSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
    def patch(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        data = request.data

        task = Coach.objects.get(todo_id = todo_id , id=task_id)

        serializer = CoachSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        task = Coach.objects.get(todo_id = todo_id , id=task_id)
        task.delete()

        return Response({'message': 'deleted.'})
    


class TeamView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request , todo_id : int) -> Response:
        customer = Team.objects.filter(todo_id = todo_id)

        serializer = TeamSerializer(customer, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request , todo_id : int) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = TeamSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetailView(APIView):
    def get(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        customer = Team.objects.get(todo_id = todo_id , id=task_id)

        serializer = TeamSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        data = request.data

        task = Team.objects.get(todo_id = todo_id , id=task_id)

        serializer = TeamSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
    def patch(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        data = request.data

        task = Team.objects.get(todo_id = todo_id , id=task_id)

        serializer = TeamSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        task = City.objects.get(todo_id = todo_id , id=task_id)
        task.delete()

        return Response({'message': 'deleted.'})