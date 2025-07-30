from django import forms
from .models import FoodHistory

class AddItemForm(forms.ModelForm):
    class Meta:
        model = FoodHistory
        fields = ['product_name', 'manufacturing_date', 'expiry_date']  # 👈 Removed purchase_date
        widgets = {
            'manufacturing_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }
