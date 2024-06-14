from django.contrib import admin

from gamification.models import Achievements, UserAchievements

admin.site.register(Achievements)
admin.site.register(UserAchievements)
