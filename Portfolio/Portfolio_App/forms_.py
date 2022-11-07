from django import forms
class Response(forms.Form):
    name = forms.CharField(label ='',widget=forms.TextInput(attrs={'id': 'name','placeholder':'Name','class':'form-control'}))
    email = forms.EmailField(label ='',widget=forms.EmailInput(attrs={'id': 'email','placeholder':'E-mail address','class':'form-control'}))
    comment = forms.CharField(label ='',widget=forms.Textarea(attrs={'id': 'comment','placeholder':'Your message','class':'form-control', 'rows':'5'}))
    def clean_name(self):
        print('Validating name field')
        inputname = self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError('The minimum number of characters in the name field should 4')
        print('Validating for name field completed')
        print(inputname)
        return inputname

    def clean_email(self):
        print('Validating email field')
        inputemail = self.cleaned_data['email']
        x = '.'
        y ='@'
        if x not in inputemail and y not in inputemail:
            raise forms.ValidationError('Enter Valid email address')
        print('Validating email field done')
        return inputemail

    def clean_comment(self):
        print('Validating comment field')
        inputcomment = self.cleaned_data['comment']
        l=inputcomment.split()
        print(l)
        print(len(l))
        if len(l)<10:
            raise forms.ValidationError('Minimum 10 words required')
        print('Validating comment field done')
        return inputcomment
