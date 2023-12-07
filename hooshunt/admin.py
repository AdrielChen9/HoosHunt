from django.contrib import admin
from .models import Clue, UserClueScore
# Register your models here.
admin.site.register(Clue)
admin.site.register(UserClueScore)

class ClueAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        return Clue.objects.filter(active=True)
