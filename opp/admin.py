from django.contrib import admin
from .models import UserProfile,Opportunites,Vote
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Opportunites)
admin.site.register(Vote)
