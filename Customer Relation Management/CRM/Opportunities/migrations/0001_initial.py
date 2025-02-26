# Generated by Django 5.1.1 on 2024-10-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Opportunities",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=100)),
                ("CC", models.BigIntegerField()),
                ("Phone", models.BigIntegerField()),
                ("Email", models.EmailField(max_length=100)),
                (
                    "Fee_Quoted",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
                ),
                ("Description", models.CharField(default="N/A", max_length=200)),
                (
                    "Opportunity_Status",
                    models.CharField(
                        choices=[
                            ("Select Opportunity Status", "Select Opportunity Status"),
                            ("visiting", "visiting"),
                            ("visited", "visited"),
                            ("Demo attended", "Demo attended"),
                        ],
                        default="Select Opportunity Status",
                        max_length=30,
                    ),
                ),
                (
                    "Oppportunity_Stage",
                    models.CharField(
                        choices=[
                            ("None", "None"),
                            ("Advanced Discussion", "Advanced Discussion"),
                            ("Ready to join", "Ready to join"),
                            ("Visiting", "Visiting"),
                            ("Fees Negotiation", "Fees Negotiation"),
                            ("Batch allocation", "Batch allocation"),
                            ("Interested in demo", "Interested in demo"),
                            ("Need time this week", "Need time this week"),
                            ("Need time next week", "Need time next week"),
                            ("Special Requirment", "Speceial Requirement"),
                            ("Payment Link sent", "Payment Link Sent"),
                            ("Closed Won(Registered)", "Closed Won(Registered)"),
                            (
                                "Busy and Asked a call back",
                                "Busy and Asked a call back",
                            ),
                            ("Closed Lost", "Closed Lost"),
                        ],
                        default="Select Opportunity StaGE",
                        max_length=30,
                    ),
                ),
                (
                    "Demo_Attended_Stage",
                    models.CharField(
                        choices=[
                            ("None", "None"),
                            ("Advanced Discussion", "Advanced Discussion"),
                            ("Call not answered", "Call not answered"),
                            ("Ready to join", "Ready to join"),
                            ("Visiting", "Visiting"),
                            ("Fees Negotiation", "Fees Negotiation"),
                            ("Batch allocation", "Batch allocation"),
                            ("Need time this week", "Need time this week"),
                            ("Need time next week", "Need time next week"),
                            ("Need time this Month", "Need time this Month"),
                            ("Need time Next Month", "Need time Next Month"),
                            ("Special Requirment", "Speceial Requirement"),
                            ("Closed Won(Registered)", "Closed Won(Registered)"),
                            ("Closed Lost(Cold Lead)", "Closed Lost(Cold Lead)"),
                        ],
                        default="Select Demo Attended Stage",
                        max_length=30,
                    ),
                ),
                (
                    "Visited_Stage",
                    models.CharField(
                        choices=[
                            ("None", "None"),
                            ("Call not answered", "Call not answered"),
                            ("Ready to join", "Ready to join"),
                            ("Fees Negotiation", "Fees Negotiation"),
                            ("Batch allocation", "Batch allocation"),
                            ("Interested Demo", "Interested Demo"),
                            ("Need time this week", "Need time this week"),
                            ("Need time next week", "Need time next week"),
                            ("Need time this Month", "Need time this Month"),
                            ("Need time Next Month", "Need time Next Month"),
                            ("Special Requirment", "Speceial Requirement"),
                            ("Closed Won(Registered)", "Closed Won(Registered)"),
                            ("Closed Lost(Cold Lead)", "Closed Lost(Cold Lead)"),
                        ],
                        default="Select Visited Stage",
                        max_length=30,
                    ),
                ),
                (
                    "Lost_Opportunity_Reason",
                    models.CharField(
                        choices=[
                            ("None", "None"),
                            ("Invalid Number", "Invalid Number"),
                            ("Not Interested", "Not Interested"),
                            ("Joined another institute", "Joined another institute"),
                            ("Asking free course", "Asking free course"),
                            ("Pay after palcement", "Pay after placement"),
                        ],
                        default="Select Lost Opportunity Reason",
                        max_length=30,
                    ),
                ),
                (
                    "Lead_Source",
                    models.CharField(
                        choices=[
                            ("None", "None"),
                            ("WalkIn", "WalkIn"),
                            ("StudentReferral", "StudentReferral"),
                            ("Demo", "Demo"),
                            ("WebSite", "WebSite"),
                            ("WebsiteChat", "WebsiteChat"),
                            ("InboundCall", "InboundCall"),
                            ("GoogleAdWords", "GoogleAdWords"),
                            ("FacebookAds", "FacebookAds"),
                            ("GoogleMyBusiness", "GoogleMyBusiness"),
                            ("WhatsAppDigitalLync", "WhatsAppDigitalLync"),
                        ],
                        default="None",
                        max_length=20,
                    ),
                ),
                (
                    "Class_Mode",
                    models.CharField(
                        choices=[
                            ("HYD ClassRoom", "HYD ClassRoom"),
                            ("BLR ClassRoom", "BLR ClassRoom"),
                            ("India Online", "India Online"),
                            ("International Online", "International Online"),
                        ],
                        default="HYDclassrrom",
                        max_length=20,
                    ),
                ),
                (
                    "Lead_Status",
                    models.CharField(
                        choices=[
                            ("Not contacted", "Not contacted"),
                            ("Attempted", "Attempted"),
                            ("warm lead", "warm lead"),
                            ("cold lead", "cold lead"),
                        ],
                        default="None",
                        max_length=20,
                    ),
                ),
                (
                    "Course",
                    models.CharField(
                        choices=[
                            ("HR Generalist core HR", "HR Generalist core HR"),
                            ("HR Analytics", "HR Analytics"),
                            ("Spoken English", "Spoken English"),
                            ("Public Speaking", "Public Speaking"),
                            ("Communication Skills", "Communication skills"),
                            ("Soft Skills", "Soft Skills"),
                            ("Personality Development", "Personality Development"),
                            ("IELTS", "IELTS"),
                            ("TOEFL", "TOEFFL"),
                            ("PTE", "PTE"),
                            ("GRE", "GTE"),
                            ("GMAT", "GMAT"),
                            ("Recruitment Specialist", "Recruitment Specialist"),
                            ("Payroll Specialist", "Payroll Specialist"),
                            ("Learning and Development", "Learning and Development"),
                            ("Others", "Others"),
                            ("Finance", "Finance"),
                            ("Competitive Exams", "Competitive Exams"),
                            ("HR Manager", "HR Manager"),
                        ],
                        default="None",
                        max_length=40,
                    ),
                ),
                (
                    "Stack",
                    models.CharField(
                        choices=[
                            ("Life Skills", "Life Skills"),
                            ("Study Abroad", "Study Abroad"),
                            ("HR", "HR"),
                        ],
                        default="None",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
