from django import forms
from blogs.models import myBlogs

class formBlogs(forms.ModelForm):
	class Meta:
		model = myBlogs
		fields = "__all__"

		widgets = {
			'title': forms.TextInput(attrs={
				'class':'form-control border border-warning',
				'required':'required',
				}),
			'body': forms.Textarea(attrs={
				'class':'form-control border border-warning',
				'required':'required',
				'max_length':'990'
				}),
			'gambar': forms.FileInput(attrs={
				'class':'form-control border border-warning',
				'required':'required'
				}),
			'created_at': forms.TextInput(attrs={
				'class':'form-control border border-warning',
				'readonly':'readonly'
				})
		}