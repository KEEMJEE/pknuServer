from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# Register your models here. 모델 데이터를 등록해라
admin.site.register(Question, QuestionAdmin)

