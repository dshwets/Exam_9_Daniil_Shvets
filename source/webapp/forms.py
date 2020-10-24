from django import forms
from webapp.models import Photo
    # , Cart, Order

#
# class SimpleSearchForm(forms.Form):
#     search = forms.CharField(max_length=100, required=False, label="Найти")


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        # exclude = ['created_at', 'author']
        fields  = ['photo_img', 'signature']

# class CartAddForm(forms.ModelForm):
#     class Meta:
#         model = Cart
#         # fields = []
#         fields = ['qty']  # бонус
#
#
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         exclude = ['products', 'user']
