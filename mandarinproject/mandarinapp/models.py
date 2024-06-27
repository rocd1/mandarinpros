from django.db import models


# Create your models here.

class Lesson(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Flashcard(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='flashcards', on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    pinyin = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)

    def __str__(self):
        return self.word

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='quizzes', on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    options = models.JSONField()
    answer = models.CharField(max_length=500, default=0)

    def __str__(self):
        return self.question
    


