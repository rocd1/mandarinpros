import json
from django.core.management.base import BaseCommand
from mandarinapp.models import Lesson, Flashcard, Quiz

class Command(BaseCommand):
    help = 'Load JSON data into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_data', type=str, help='D:\mandarinpros\mandarinproject\json_data.json')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_data']
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for lesson_data in data['lessons']:
            lesson = Lesson.objects.create(category=lesson_data['category'])

            for flashcard_data in lesson_data['flashcards']:
                Flashcard.objects.create(
                    lesson=lesson,
                    word=flashcard_data['word'],
                    pinyin=flashcard_data['pinyin'],
                    translation=flashcard_data['translation']
                )

            for quiz_data in lesson_data['quizzes']:
                quiz = Quiz.objects.create(
                    lesson=lesson,
                    question=quiz_data['question'],
                    options=quiz_data['options'],
                    answer=quiz_data['answer']
                )

                
        self.stdout.write(self.style.SUCCESS('Successfully loaded JSON data into the database'))
