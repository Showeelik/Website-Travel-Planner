from django import forms
from django.core.exceptions import ValidationError
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

    def clean(self):
        cleaned_data = super().clean()
        user = self.instance.user if self.instance.pk else self.initial.get('user')
        route = self.instance.route if self.instance.pk else self.initial.get('route')

        if user and route and Review.objects.filter(user=user, route=route).exists():
            raise ValidationError("Вы уже оставили отзыв на этот маршрут.")

        return cleaned_data