from django.db import models

class WebhookPayload(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    payload = models.JSONField()  # Requires Django 3.1+

    def __str__(self):
        return f"WebhookPayload {self.id} at {self.timestamp}"

class Project24(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    urn = models.CharField(max_length=20, blank=True, null=True)
    contact_uuid = models.CharField(max_length=255)
    flow_name = models.CharField(max_length=255, blank=True, null=True)
    flow_uuid = models.CharField(max_length=255, blank=True, null=True)
    borrower_fullname = models.CharField(max_length=255, blank=True, null=True)
    borrower2_fullname = models.CharField(max_length=255, blank=True, null=True)
    civil_servant_response = models.CharField(max_length=255, blank=True, null=True)
    date_of_employment = models.CharField(max_length=255, blank=True, null=True)
    dob = models.CharField(max_length=255, blank=True, null=True)
    dept_code = models.CharField(max_length=255, blank=True, null=True)
    ec_number = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.CharField(max_length=255, blank=True, null=True)
    to_date = models.CharField(max_length=255, blank=True, null=True)
    loan_amount = models.CharField(max_length=255, blank=True, null=True)
    monthly_installment = models.CharField(max_length=255, blank=True, null=True)
    loan_tenure = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.EmailField(max_length=255, blank=True, null=True)
    employer_contact = models.CharField(max_length=255, blank=True, null=True)
    employment_location = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    application_type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    id_number = models.CharField(max_length=255, blank=True, null=True)
    job_position = models.CharField(max_length=255, blank=True, null=True)
    permanent_employee = models.CharField(max_length=255, blank=True, null=True)
    runout_date = models.CharField(max_length=255, blank=True, null=True)
    date_of_engagement = models.CharField(max_length=255, blank=True, null=True)
    ministry_name = models.CharField(max_length=255, blank=True, null=True)
    mobile_num1 = models.CharField(max_length=20, blank=True, null=True)
    mobile_num2 = models.CharField(max_length=20, blank=True, null=True)
    gross_salary = models.CharField(max_length=255, blank=True, null=True)
    net_salary = models.CharField(max_length=255, blank=True, null=True)
    nok_fullname = models.CharField(max_length=255, blank=True, null=True)
    nok_id = models.CharField(max_length=255, blank=True, null=True)
    nok_phone = models.CharField(max_length=255, blank=True, null=True)
    nok_relationship = models.CharField(max_length=255, blank=True, null=True)
    nok_address = models.CharField(max_length=255, blank=True, null=True)
    spouse_fullname = models.CharField(max_length=255, blank=True, null=True)
    spouse_id = models.CharField(max_length=255, blank=True, null=True)
    spouse_address = models.CharField(max_length=255, blank=True, null=True)
    spouse_selection = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, default="Pending", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    client_signature = models.CharField(max_length=255, blank=True, null=True)
    representative_signature = models.CharField(max_length=255, blank=True, null=True)
    approvedBy = models.CharField(max_length=255, blank=True, null=True)
    lastEditedBy = models.CharField(max_length=255, blank=True, null=True)
    lastEditedDate = models.CharField(max_length=255, blank=True, null=True)
    createdBy = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    user_sent_feedback = models.TextField(blank=True, null=True)
    id_picture = models.FileField(upload_to="Project24", blank=True, null=True)
    proof_of_residence = models.FileField(upload_to="Project24", blank=True, null=True)
    pay_slip = models.FileField(upload_to="Project24", blank=True, null=True)
    employment_letter= models.FileField(upload_to="Project24", blank=True, null=True)
    sized_photo= models.FileField(upload_to="Project24", blank=True, null=True)
    selecttenure_package = models.CharField(max_length=255, blank=True, null=True)
    tenure_package = models.CharField(max_length=255, blank=True, null=True)
    ssb_state = models.CharField(max_length=255, blank=True, null=True)
    payeecode= models.CharField(max_length=255, blank=True, null=True)
    pin = models.IntegerField(blank=True, null=True)
    

    def __str__(self):
        return self.full_name
    
    
class Project24FeedBackLog(models.Model):
    client = models.ForeignKey(Project24, on_delete=models.CASCADE)
    user_sent_feedback = models.TextField(blank=True, null=True)
    createdBy = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.user_sent_feedback
    
    
class Project24NoteLog(models.Model):
    client = models.ForeignKey(Project24, on_delete=models.CASCADE)
    internal_note = models.TextField(blank=True, null=True)
    createdBy = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.internal_note    
    
    

class Project24Resubmit(models.Model):
    urn = models.CharField(max_length=20, blank=True, null=True)
    id_picture = models.FileField(upload_to="Project24", blank=True, null=True)
    proof_of_residence = models.FileField(upload_to="Project24", blank=True, null=True)
    pay_slip = models.FileField(upload_to="Project24", blank=True, null=True)
    employment_letter= models.FileField(upload_to="Project24", blank=True, null=True)
    sized_photo= models.FileField(upload_to="Project24", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
class Project24EditLog(models.Model):
    urn = models.CharField(max_length=20, blank=True, null=True)
    field_edited = models.CharField(max_length=255, blank=True, null=True)   
    from_data = models.CharField(max_length=255, blank=True, null=True)
    to_data = models.CharField(max_length=255, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    edited_by = models.CharField(max_length=255, blank=True, null=True)
    edit_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
        