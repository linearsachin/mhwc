from .models import Question
import django_filters

class QuestionFilter(django_filters.FilterSet):
    question_text = django_filters.CharFilter(lookup_expr='icontains',label=False,)
    class Meta:
        model = Question
        fields = ['question_text', ]
        
        def __init__(self, *args, **kwargs):
            super(UserFilter, self).__init__(*args, **kwargs)
            # You need to override the label_from_instance method in the filter's form field
            self.filters['question_text'].field.label_from_instance = ''