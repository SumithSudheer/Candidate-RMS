from django.contrib import admin
from .models import *
# Register your models here
if admin.site.is_registered(Profile):
    admin.site.unregister(Profile)
    
class UserProfileAdmin(admin.ModelAdmin):
    # Customize the display in the admin panel if needed
    list_display = ['user', 'is_hr', 'is_teamlead', 'is_manager', 'is_mainHr', 'is_teamMember', 'is_onboardingHr']

admin.site.register(Profile, UserProfileAdmin)
admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(MeetingSchedule)
admin.site.register(MeetingReview)
admin.site.register(TeamLeadDecision)

admin.site.register(ManagerDecision)
admin.site.register(EmailLog)