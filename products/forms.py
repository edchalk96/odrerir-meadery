from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        
        self.fields['mead_type'].queryset = categories
        self.fields['mead_type'].label = 'Category / Mead Type'

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ('')
        self.helper.attrs = {'enctype': 'multipart/form-data'}

        self.helper.layout = Layout(
            Row(
                Column('sku', css_class='col-md-6 mb-3'),
                Column('name', css_class='col-md-6 mb-3'),
            ),
            Row(
                Column('mead_type', css_class='col-md-6 mb-3'),
                Column('abv', css_class='col-md-6 mb-3'),
            ),
            Row(
                Column('price', css_class='col-md-6 mb-3'),
                Column('stock_level', css_class='col-md-6 mb-3'),
            ),
            'ingredients',
            'description',
            Row(
                Column('clearance', css_class='col-md-6 mb-3'),
                Column('most_popular', css_class='col-md-6 mb-3'),
            ),
            Row(
                Column('image_url', css_class='col-md-6 mb-3'),
                Column('image', css_class='col-md-6 mb-3'),
            ),
            Row(
                Column(
                    HTML(
                        '<a class="btn me-2" href="{% url \'products\' %}">Cancel</a>'
                    ),
                    Submit('submit', 'Add Product', css_class='btn'),
                    css_class='col-12 mt-4',
                )
            ),
        )

        for field_name, field in self.fields.items():
            if field_name != 'image' and not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating']
        widgets = {'rating': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),}