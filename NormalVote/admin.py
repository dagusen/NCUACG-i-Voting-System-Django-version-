from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_title', 'question_describe']}),
        ('Date', {'fields': ['pub_date', 'expire_date']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)
