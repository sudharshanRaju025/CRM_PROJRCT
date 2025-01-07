from django.db import models
from django.utils import timezone

# Create your models here.
class Opportunities(models.Model):

    Name=models.CharField(max_length=100)
    CC=models.BigIntegerField()
    Phone=models.BigIntegerField()
    Email=models.EmailField(max_length=100)
    Fee_Quoted=models.DecimalField(max_digits=12,decimal_places=2,default=0.0)
    Description=models.CharField(max_length=200,default="N/A")
    # Datetime=models.DateTimeField(default=timezone.now)

    LEAD_STATUS_CHOICES=[
        ("Not contacted","Not contacted"),
        ("Attempted","Attempted"),
        ("warm lead","warm lead"),
        ("cold lead","cold lead"),
    ]

    LEAD_SOURCE_CHOICES = [
        ('None', 'None'),
        ('WalkIn', 'WalkIn'),
        ('StudentReferral', 'StudentReferral'),
        ('Demo', 'Demo'),
        ('WebSite', 'WebSite'),
        ('WebsiteChat', 'WebsiteChat'),
        ('InboundCall', 'InboundCall'),
        ('GoogleAdWords', 'GoogleAdWords'),
        ('FacebookAds', 'FacebookAds'),
        ('GoogleMyBusiness', 'GoogleMyBusiness'),
        ('WhatsAppDigitalLync', 'WhatsAppDigitalLync'),
    ]

    
    STACK_CHOICES = [
      ("Life Skills","Life Skills"),
      ("Study Abroad","Study Abroad"),
      ("HR","HR"),
    ]

    CLASS_MODE_CHOICES = [
        ('HYD ClassRoom', 'HYD ClassRoom'),
        ('BLR ClassRoom', 'BLR ClassRoom'),
        ('India Online', 'India Online'),
        ('International Online', 'International Online'),
    ]

    OPPORTUNITY_STATUS=[
        ("Select Opportunity Status","Select Opportunity Status"),
        ("visiting","visiting"),
        ("visited","visited"),
        ("Demo attended","Demo attended")
    ]

    OPPORTUNITY_STAGE=[
        ("None","None"),
        ("Advanced Discussion","Advanced Discussion"),
        ("Ready to join","Ready to join"),
        ("Visiting","Visiting"),
        ("Fees Negotiation","Fees Negotiation"),
        ("Batch allocation","Batch allocation"),
        ("Interested in demo","Interested in demo"),
        ("Need time this week","Need time this week"),
        ("Need time next week","Need time next week"),
        ("Special Requirment","Speceial Requirement"),
        ("Payment Link sent","Payment Link Sent"),
        ("Closed Won(Registered)","Closed Won(Registered)"),
        ("Busy and Asked a call back","Busy and Asked a call back"),
        ("Closed Lost","Closed Lost")

    ]

    DEMO_ATTENDED_STAGE=[
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
    COURSES_CHOICES=[
        ("HR Generalist core HR","HR Generalist core HR"),
        ("HR Analytics","HR Analytics"),
        ("Spoken English","Spoken English"),
        ("Public Speaking","Public Speaking"),
        ("Communication Skills","Communication skills"),
        ("Soft Skills","Soft Skills"),
        ("Personality Development","Personality Development"),
        ("IELTS","IELTS"),
        ("TOEFL","TOEFFL"),
        ("PTE","PTE"),
        ("GRE","GTE"),
        ("GMAT","GMAT"),
        ("Recruitment Specialist","Recruitment Specialist"),
        ("Payroll Specialist","Payroll Specialist"),
        ("Learning and Development","Learning and Development"),
        ("Others","Others"),
        ("Finance","Finance"),
        ("Competitive Exams","Competitive Exams"),
        ("HR Manager","HR Manager")
    ]

    VISITED_STAGE=[
        ("None","None"),
        ("Call not answered","Call not answered"),
        ("Ready to join","Ready to join"),
        ("Fees Negotiation","Fees Negotiation"),
        ("Batch allocation","Batch allocation"),
        ("Interested Demo","Interested Demo"),
        ("Need time this week","Need time this week"),
        ("Need time next week","Need time next week"),
        ("Need time this Month","Need time this Month"),
        ("Need time Next Month","Need time Next Month"),
        ("Special Requirment","Speceial Requirement"),
        ("Closed Won(Registered)","Closed Won(Registered)"),
        ("Closed Lost(Cold Lead)","Closed Lost(Cold Lead)")

    ]
    LOST_OPPORTUNITY_REASON=[
        ("None","None"),
        ("Invalid Number","Invalid Number"),
        ("Not Interested","Not Interested"),
        ("Joined another institute","Joined another institute"),
        ("Asking free course","Asking free course"),
        ("Pay after palcement","Pay after placement")
    ]


    Opportunity_Status=models.CharField(
        max_length=30,
        choices=OPPORTUNITY_STATUS,
        default="Select Opportunity Status",
    )

    Oppportunity_Stage=models.CharField(
        max_length=30,
        choices=OPPORTUNITY_STAGE,
        default="Select Opportunity StaGE"
    )

    Demo_Attended_Stage=models.CharField(
        max_length=30,
        choices=DEMO_ATTENDED_STAGE,
        default="Select Demo Attended Stage"
    )

    Visited_Stage=models.CharField(
        max_length=30,
        choices=VISITED_STAGE,
        default="Select Visited Stage",
    )

    Lost_Opportunity_Reason=models.CharField(
        max_length=30,
        choices=LOST_OPPORTUNITY_REASON,
        default="Select Lost Opportunity Reason",
    )
    

    Lead_Source=models.CharField(
        max_length=20,
        choices= LEAD_SOURCE_CHOICES ,
        default="None",
    )

    Class_Mode=models.CharField(
        max_length=20,
        choices= CLASS_MODE_CHOICES,
        default="HYDclassrrom",
    )

    Lead_Status=models.CharField(
        max_length=20,
        choices= LEAD_STATUS_CHOICES,
        default="None",
    )

    Course=models.CharField(
        max_length=40,
        choices= COURSES_CHOICES,
        default="None",
    )

    Stack=models.CharField(
        max_length=20,
        choices=STACK_CHOICES ,
        default="None",
    )
