from .models import Question
import django_filters

class QuestionFilter(django_filters.FilterSet):
    question_text = django_filters.CharFilter(lookup_expr='icontains',label=False,)
    class Meta:
        model = Question
        fields = ['question_text', ]


