from datetime import timezone
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, Meeting, Venue, Minutes
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


#meeting form


class MeetingForm(forms.ModelForm):
    # fields we want to include and customize in our form
    venue = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Meeting Venue',
                                                               'class': 'form-control',
                                                               }))
    name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Meeting_Title',
                                                              'class': 'form-control',
                                                              }))
   
    
    meeting_date = forms.DateField(widget=DatePickerInput)

    
              
    description = forms.CharField(max_length=400,
                             required=True,
                             widget=forms.Textarea(attrs={'placeholder': 'Meeting description',
                                                           'class': 'form-control',
                                                           }))
                                                            

    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Meeting
        fields = ['venue', 'name', 'meeting_date','description','avatar']
         
        widgets = {
            'my_date_field' : DatePickerInput(),
            'my_time_field' : TimePickerInput(),
            'my_date_time_field' : DateTimePickerInput(),
        }


        #### DATE VALIDATION
        
    def validate_date(meeting_date):
        if meeting_date < timezone.now().date():
            raise forms.ValidationError("Date cannot be in the past")

#/end of meeting form
 
class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name','address',  'phone', 'web', 'email_address')
    


class MinutesForm(forms.ModelForm):
    class Meta:
        model = Minutes
        fields = ('org_name','date',  'opening', 'members_present', 'members_absent', 'business_from_the_previous_meeting','new_business',
        'additions_to_the_agenda', 'adjournment', 'minutes_submitted_by', 'minutes_approved_by')      




class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
