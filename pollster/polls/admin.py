from django.contrib import admin

# Register your models here.
from .models import Question, Choic
#admin.site.register(question)
#admin.site.register(Choice)

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster"


class ChoicInLine(admin.TabularInline):
    model = Choic
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', { 
        'fields': ['pub_date'], 'classes': ['collapse']}), ] 
    inlines = [ChoicInLine] 
  
  
admin.site.register(Question, QuestionAdmin) 
