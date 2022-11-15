from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["name", "content", "category"]

        labels = {
            "name": "상품명",
            "content": "문의내용",
            "category": "문의유형",
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
        labels = {
            "답변": "문의내용",
        }
