class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner', 'pub_date']


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

