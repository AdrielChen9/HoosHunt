from django.shortcuts import render
from .models import CustomUser
from operator import attrgetter
from django.http import JsonResponse
# Create your views here.

# Create your views here.
def LeaderBoard(request):
    users = CustomUser.objects.all()
    sorted_users = sorted(users, key=attrgetter('score'), reverse=True)
    top_users = sorted_users[:20]
    context = {'users': top_users}
    return render(request, 'leaderboard.html', context)

def increase_user_score(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        clue_point_value = request.POST.get('clue_point_value')
        
        user = CustomUser.objects.get(id=user_id)
        user.score += clue_point_value
        user.save()
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})