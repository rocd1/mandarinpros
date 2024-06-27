from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Lesson, Flashcard, Quiz
from .forms import QuizForm

def home(request):
    categories = Lesson.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'mandarinapp/home.html', context)

def flashcards(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    flashcards = lesson.flashcards.all()
    quizzes = lesson.quizzes.all()
    categories = Lesson.objects.all()
    
    form = QuizForm(quizzes=quizzes)

    context = {
        'lesson': lesson,
        'flashcards': flashcards,
        'form': form,
        'categories': categories,
    }

    if request.method == 'POST':
        form = QuizForm(request.POST, quizzes=quizzes)
        if form.is_valid():
            results = []
            for quiz in quizzes:
                selected_answer = form.cleaned_data[f'quiz_{quiz.id}']
                correct = selected_answer == quiz.answer
                results.append({
                    'question': quiz.question,
                    'selected_answer': selected_answer,
                    'correct_answer': quiz.answer,
                    'correct': correct,
                })
            context['results'] = results

    return render(request, 'mandarinapp/flashcards.html', context)
