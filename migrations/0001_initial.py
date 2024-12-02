# Generated by Django 5.1.3 on 2024-11-28 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project24',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('urn', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_uuid', models.CharField(max_length=255)),
                ('flow_name', models.CharField(blank=True, max_length=255, null=True)),
                ('flow_uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('borrower_fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('borrower2_fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('civil_servant_response', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_employment', models.CharField(blank=True, max_length=255, null=True)),
                ('dob', models.CharField(blank=True, max_length=255, null=True)),
                ('dept_code', models.CharField(blank=True, max_length=255, null=True)),
                ('ec_number', models.CharField(blank=True, max_length=255, null=True)),
                ('from_date', models.CharField(blank=True, max_length=255, null=True)),
                ('to_date', models.CharField(blank=True, max_length=255, null=True)),
                ('loan_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('monthly_installment', models.CharField(blank=True, max_length=255, null=True)),
                ('loan_tenure', models.CharField(blank=True, max_length=255, null=True)),
                ('reference', models.CharField(blank=True, max_length=255, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=255, null=True)),
                ('employer_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('employment_location', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('application_type', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('home_address', models.CharField(blank=True, max_length=255, null=True)),
                ('id_number', models.CharField(blank=True, max_length=255, null=True)),
                ('job_position', models.CharField(blank=True, max_length=255, null=True)),
                ('permanent_employee', models.CharField(blank=True, max_length=255, null=True)),
                ('runout_date', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_engagement', models.CharField(blank=True, max_length=255, null=True)),
                ('ministry_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_num1', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile_num2', models.CharField(blank=True, max_length=20, null=True)),
                ('gross_salary', models.CharField(blank=True, max_length=255, null=True)),
                ('net_salary', models.CharField(blank=True, max_length=255, null=True)),
                ('nok_fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('nok_id', models.CharField(blank=True, max_length=255, null=True)),
                ('nok_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('nok_relationship', models.CharField(blank=True, max_length=255, null=True)),
                ('nok_address', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_id', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_address', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_selection', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, default='Pending', max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('client_signature', models.CharField(blank=True, max_length=255, null=True)),
                ('representative_signature', models.CharField(blank=True, max_length=255, null=True)),
                ('approvedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('lastEditedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('lastEditedDate', models.CharField(blank=True, max_length=255, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=255, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('user_sent_feedback', models.TextField(blank=True, null=True)),
                ('id_picture', models.FileField(blank=True, null=True, upload_to='Project24')),
                ('proof_of_residence', models.FileField(blank=True, null=True, upload_to='Project24')),
                ('pay_slip', models.FileField(blank=True, null=True, upload_to='Project24')),
                ('employment_letter', models.FileField(blank=True, null=True, upload_to='Project24')),
                ('sized_photo', models.FileField(blank=True, null=True, upload_to='Project24')),
                ('selecttenure_package', models.CharField(blank=True, max_length=255, null=True)),
                ('tenure_package', models.CharField(blank=True, max_length=255, null=True)),
                ('ssb_state', models.CharField(blank=True, max_length=255, null=True)),
                ('payeecode', models.CharField(blank=True, max_length=255, null=True)),
                ('pin', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project24EditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urn', models.CharField(blank=True, max_length=20, null=True)),
                ('field_edited', models.CharField(blank=True, max_length=255, null=True)),
                ('from_data', models.CharField(blank=True, max_length=255, null=True)),
                ('to_data', models.CharField(blank=True, max_length=255, null=True)),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
                ('edited_by', models.CharField(blank=True, max_length=255, null=True)),
                ('edit_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project24Resubmit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urn', models.CharField(blank=True, max_length=20, null=True)),
                ('id_picture', models.FileField(blank=True, null=True, upload_to='Project24')),
                ('proof_of_residence', models.FileField(blank=True, null=True, upload_to='Project24')),
                ('pay_slip', models.FileField(blank=True, null=True, upload_to='Project24')),
                ('employment_letter', models.FileField(blank=True, null=True, upload_to='Project24')),
                ('sized_photo', models.FileField(blank=True, null=True, upload_to='Project24')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project24FeedBackLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_sent_feedback', models.TextField(blank=True, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project24')),
            ],
        ),
        migrations.CreateModel(
            name='Project24NoteLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_note', models.TextField(blank=True, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project24')),
            ],
        ),
    ]
