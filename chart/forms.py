from django import forms


class SingleForm(forms.Form):
    username = forms.CharField(required=True, 
                                error_messages={'required': '此欄位必須填寫'},
                                widget=forms.TextInput(attrs={'class': 'form-control', 
                                                            'placeholder': '請輸入您的 NID 帳號'}))
    password = forms.CharField(required=True, 
                                error_messages={'required': '此欄位必須填寫'}, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 
                                                                'placeholder': '請輸入您的 NID 密碼'}))
    nid = forms.CharField(required=True, 
                                error_messages={'required': '此欄位必須填寫'},
                                widget=forms.TextInput(attrs={'class': 'form-control', 
                                                            'placeholder': '請輸入欲查詢之學號'}))


from .models import ActivityTag

class ActivityTagForm(forms.ModelForm):
    class Meta:
        model = ActivityTag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入欲新增之活動標籤'})
        }
        error_messages = {
            'name': {
                'required': '此欄位必須填寫'
            }
        }
