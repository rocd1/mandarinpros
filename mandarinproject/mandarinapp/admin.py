from django.contrib import admin
from .models import Lesson, Flashcard, Quiz


# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'pinyin', 'translation', 'lesson')
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'options', 'answer', )


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Flashcard, FlashcardAdmin)
admin.site.register(Quiz, QuizAdmin)
