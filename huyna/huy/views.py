from django.http import HttpResponse

from huyna.models import Workout


def get_workouts(request):
    if request.method == 'GET':
        if request.GET.get('id', None):
            return HttpResponse(Workout.objects.get(id=request.GET.get('id')))
            # return specific row
        else:
            result = Workout.objects.all()
            return HttpResponse(result)
            # return all rows
    elif request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        duration = request.POST['duration']
        sensei = request.POST['sensei']
        workout = Workout(name, description, duration, sensei)
        workout.save()
        return HttpResponse(workout)
        # Create new workout
    elif request.method == 'PUT':
        workout = Workout.objects.get(id=request.PUT.get('id'))
        workout.name = request.PUT['name']
        workout.description = request.PUT['description']
        workout.duration = request.PUT['duration']
        workout.sensei = request.PUT['sensei']
        workout.save()
        return HttpResponse(workout)
        # Update workout
    elif request.method == 'DELETE':
        workout = Workout.objects.get(id=request.DELETE.get('id'))
        workout.delete()
        return HttpResponse('Row deleted.')
        # Delete workout