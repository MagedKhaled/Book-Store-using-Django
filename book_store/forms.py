from django import  forms
from book_store.models import Book
from django.core.exceptions import ValidationError
from category.models import Category




class BookForm(forms.Form):
    class Meta:
        model = Book
        fields = ['name','description','image','price','inStock','category']


    def clean_name(self):

        found = Book.objects.filter(name=self.cleaned_data['name']).exists()
        if found:
            raise ValidationError("Track name already exists")
        return self.cleaned_data['name']




class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    # def clean_name(self):

    #     found = Book.objects.filter(name=self.cleaned_data['name']).exists()
    #     if found:
    #         raise ValidationError("Track name already exists")
    #     return self.cleaned_data['name']
    

