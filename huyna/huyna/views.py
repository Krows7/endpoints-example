from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from huyna.models import Workout

@csrf_exempt
def get_workouts(request, workout_id=None):
    if request.method == 'GET':
        if workout_id:
            try:
                return HttpResponse(Workout.objects.get(id=workout_id))
            except:
                return HttpResponse('Workout entity does not exist')
            # return specific row
        else:
            result = Workout.objects.all()
            return HttpResponse(result)
            # return all rows
    elif request.method == 'POST':
        try:
            name = request.POST['name']
            description = request.POST['description']
            duration = request.POST['duration']
            sensei = request.POST['sensei']

            workout = Workout(name=name, description=description, duration=duration, sensei=sensei
            workout.save()
            return HttpResponse(workout)
            # Create new workout
        except:
            return HttpResponse('One of the arguments is missing or incorrect')
    elif request.method == 'PUT':
        PUT = QueryDict(request.body)
        if not workout_id: return HttpResponse('Workout ID is required to edit')
        try:
            workout = Workout.objects.get(id=workout_id)
        except:
            return HttpResponse('Workout entity does not exist')
        try:
            if PUT.get('name'): workout.name = PUT['name']
            if PUT.get('description'): workout.description = PUT['description']
            if PUT.get('duration'): workout.duration = PUT['duration']
            if PUT.get('sensei'): workout.sensei = PUT['sensei']
            workout.save()
            return HttpResponse(workout)
            # Update workout
        except:
            return HttpResponse('Input data invalid')
    elif request.method == 'DELETE':
        try:
            workout = Workout.objects.get(id=workout_id)
        except:
            return HttpResponse('Workout entity does not exist')
        workout.delete()
        return HttpResponse('Row deleted.')
        # Delete workout