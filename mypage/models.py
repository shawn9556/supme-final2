from multiprocessing.sharedctypes import Value
from django.db import models
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)
    GENDER =[
        ('M', '남성'),
        ('W', '여성'),
    ]
    gender = models.CharField(max_length=4, choices=GENDER)
    email = models.CharField(max_length=32)
    age = models.CharField(max_length=16)
    # alien_type = models.CharField(max_length=32)

    alien_type = models.ImageField(
        upload_to = "static/alien/%y"
    )
    alien_name = models.CharField(max_length=32)
    alien_content = models.TextField()
    for_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.for_user.username

class Select(models.Model):
    selector = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    people = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    TRAVEL_PURPOSE=[
        ('힐링', '힐링'),
        ('아웃도어', '아웃도어'),
        ('맛집투어', '맛집투어'),
        ('자연감상', '자연감상'),
    ]

    PLACE_START = [
        ('강동구', '강동구'),
        ('강남구', '강남구'),
        ('강북구', '강북구'),
        ('강서구', '강서구'),
    ]

    SELECT_STATE = [
        ("preparing", "여행 준비 중"),
        ("prepared", "여행 준비 끝"),
        ("on_travel", "여행 중"),
        ("finished", "여행 완료"),
    ]
    travel_purpose = models.CharField(max_length=30, choices=TRAVEL_PURPOSE, default='자연감상')
    selection_state = models.CharField(max_length=32, choices=SELECT_STATE, default=SELECT_STATE[0][0])
    def state_name(self):
        for state in self.SELECT_STATE:
            if state[0] == self.selection_state:
                return state[1]
    place_start = models.CharField(max_length=10, choices=PLACE_START, default='강동구')
    create_date = models.DateTimeField()

    def __str__(self):
        return self.selector.for_user.username


