from django import forms
from .models import Quiz

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        quizzes = kwargs.pop('quizzes')
        super(QuizForm, self).__init__(*args, **kwargs)
        for quiz in quizzes:
            self.fields[f'quiz_{quiz.id}'] = forms.ChoiceField(
                label=quiz.question,
                choices=[(option, option) for option in quiz.options],
                widget=forms.RadioSelect,
                required=True
            )
