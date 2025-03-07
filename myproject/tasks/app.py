from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

@api_view(["GET"])
def get_task_list(request):
    """Получить список всех задач"""
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_task_detail(request, pk):
    """Получить одну задачу по ID"""
    try:
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

@api_view(["POST"])
def create_task(request):
    """Создать новую задачу"""
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["PUT"])
def update_task(request, pk):
    """Обновить существующую задачу"""
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(["DELETE"])
def delete_task(request, pk):
    """Удалить задачу"""
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response({"message": "Task deleted"}, status=204)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)
