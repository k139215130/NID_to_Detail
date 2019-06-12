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