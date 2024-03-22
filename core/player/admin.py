from django.contrib import admin
from .models import Player , City , Coach , Team


@admin.register(Player)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'born_date' , "height" , "weight" , "team" , "city" , "position" , "coach"]


@admin.register(Coach)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'city', 'team']


@admin.register(City)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Team)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']