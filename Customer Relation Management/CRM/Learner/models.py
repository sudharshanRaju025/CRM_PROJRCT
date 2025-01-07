from django.db import models
from django.utils import timezone



class Learner(models.Model):

    First_Name=models.CharField(max_length=200)
    Last_Name=models.CharField(max_length=100)
    Id_Proof=models.BigIntegerField()
    Phone=models.BigIntegerField()
    Date_of_Birth=models.DateField()
    Email=models.EmailField()
    Registered_Date=models.DateField(default=timezone.now)
    Batch_Id=models.IntegerField()
    Alternate_Phone=models.BigIntegerField()
    Description=models.TextField(max_length=300)
    Exchange_Rate=models.BigIntegerField()
    Source=models.CharField(max_length=20)
    Learner_Owner=models.IntegerField()
    Currency=models.DecimalField(max_digits=12,decimal_places=2)
    Lead_created_time=models.DateField(default=timezone.now)
    Counselling_Done_BY=models.IntegerField()
    Registered_Course=models.CharField(max_length=20)
    Preferable_Time=models.DateField(default=timezone.now)
    Tech_Stack=models.CharField(max_length=50)
    Batch_Timing=models.DateField(default=timezone.now)
    Course_Commnets=models.CharField(max_length=100)
    Mode_Of_Class=models.CharField(max_length=100)
    Slack_Access=models.CharField(max_length=100)
    Comment=models.CharField(max_length=100)
    LMS_Access=models.CharField(max_length=100)

    LOCATION=[
        ("None","None"),
        ("Advanced Discussion","Advanced Discussion"),
        ("Call not answered","Call not answered"),
        ("Ready to join","Ready to join"),
        ("Visiting","Visiting"),
        ("Fees Negotiation","Fees Negotiation"),
        ("Batch allocation","Batch allocation"),
        ("Need time this week","Need time this week"),
        ("Need time next week","Need time next week"),
        ("Need time this Month","Need time this Month"),
        ("Need time Next Month","Need time Next Month"),
        ("Special Requirment","Speceial Requirement"),
        ("Closed Won(Registered)","Closed Won(Registered)"),
        ("Closed Lost(Cold Lead)","Closed Lost(Cold Lead)")

    ]
    
    ATTENDED_DEMO_CHOICES=[
        ("None","None"),
        ("Advanced Discussion","Advanced Discussion"),
        ("Call not answered","Call not answered"),
        ("Ready to join","Ready to join"),
        ("Visiting","Visiting"),
        ("Fees Negotiation","Fees Negotiation"),
        ("Batch allocation","Batch allocation"),
        ("Need time this week","Need time this week"),
        ("Need time next week","Need time next week"),
        ("Need time this Month","Need time this Month"),
        ("Need time Next Month","Need time Next Month"),
        ("Special Requirment","Speceial Requirement"),
        ("Closed Won(Registered)","Closed Won(Registered)"),
        ("Closed Lost(Cold Lead)","Closed Lost(Cold Lead)")
    ]

    LEARNER_STAGE_CHOICES=[
        ("None","None"),
        ("Advanced Discussion","Advanced Discussion"),
        ("Call not answered","Call not answered"),
        ("Ready to join","Ready to join"),
        ("Visiting","Visiting"),
        ("Fees Negotiation","Fees Negotiation"),
        ("Batch allocation","Batch allocation"),
        ("Need time this week","Need time this week"),
        ("Need time next week","Need time next week"),
        ("Need time this Month","Need time this Month"),
        ("Need time Next Month","Need time Next Month"),
        ("Special Requirment","Speceial Requirement"),
        ("Closed Won(Registered)","Closed Won(Registered)"),
        ("Closed Lost(Cold Lead)","Closed Lost(Cold Lead)")
    ]
    
    Learner_Stage=models.CharField(
        max_length=50,
        choices=LEARNER_STAGE_CHOICES,
        default="None",
    )

    Attended_Demo=models.CharField(
        max_length=50,
        choices=ATTENDED_DEMO_CHOICES,
        default="None",
    )

    Location=models.CharField(
        max_length=50,
        choices=LOCATION,
        default="None",
    )