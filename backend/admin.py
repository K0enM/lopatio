from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from backend.models import Nickname, Quote, LeaderbordPosition
# Register your models here.
class NicknameInline(admin.StackedInline):
  model = Nickname
  can_delete = False
  verbose_name_plural = 'nickname'
  
class LeaderboardPositionInline(admin.StackedInline):
  model = LeaderbordPosition
  can_delete = False
  verbose_name_plural = 'mongolen_board_position'

class UserAdmin(BaseUserAdmin):
  inlines = (NicknameInline, LeaderboardPositionInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Quote)