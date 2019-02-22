from django import forms
course_choices=(
    ('diploma','Diploma'),
    ('Btech','BTech'),
    ('Mtech','MTech'),
    ('Bsc','Bsc'),
    ('Msc','Msc'),
    ('Bca','Bca'),
)
event_choices=(
    ('colorcarnival','ColorCarnival'),
    ('langaming','LanGaming'),
    ('crossinghurdles','CrossingHurdles'),
    ('dance','Dance'),
    ('tehzeeb','Tehzeeb'),
    ('skit','Skit'),
)
college_choices=(
    ('bcet','BCET GURDASPUR'),
    ('other','Others'),
)
class RegForm(forms.Form):
    name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your name'
            }
        )
    )
    course=forms.CharField(
        widget=forms.Select(choices=course_choices)
    )
    college=forms.CharField(
        widget=forms.Select(choices=college_choices)
    )
    email=forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your e-mail'
            }
        )
    )
    contact_no=forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter mobile no.'
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'place-holder':'Enter strong password'
            }
        )
    )
class LoginForm(forms.Form):
    email=forms.EmailField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())
class EventForm(forms.Form):
    participant=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter participant name'
            }
        )
    )
    event=forms.CharField(
        widget=forms.Select(choices=event_choices)
    )
class QuerryForm(forms.Form):
    mobile_no=forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter mobile no'
            }
        )
    )
    query=forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your query'
            }
        )
    )