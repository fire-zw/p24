from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
#from weasyprint import HTML
from django.conf import settings
import requests
from datetime import datetime
import random


#@login_required(login_url="/project24/login")
def project24_dashboard(request):
    client_data = Project24.objects.all()
    pending_reg = Project24.objects.filter(status="Pending")
    in_progress = Project24.objects.filter(status="InProgress")
    processed = Project24.objects.filter(status="Approved")
    rejected = Project24.objects.filter(status="Rejected")
    webhook_entries = Project24.objects.exclude(contact_uuid="").count()  # Assuming webhook entries have a `contact_uuid`

    template = "pages/main.html"
    context = {
        "client": client_data,
        "pending_reg": pending_reg.count(),
        "prog": in_progress.count(),
        "proc": processed.count(),
        "rej": rejected.count(),
        "webhook_count": webhook_entries,
    }

    return render(request, template, context)



@csrf_exempt
def user_registration(request):
    PIN = ""
    if request.method == "POST":
        data = json.loads(request.body)
        PIN=str(random.randint(100000, 999999))

        # Extract the contact, flow, and results data from the JSON object
        contact = data.get("contact", {})
        flow = data.get("flow", {})
        results = data.get("results", {})
        urn=contact.get("urn", "").replace("tel:+", "")
        
        check_urn = Project24.objects.filter(urn=urn).exists()
        if not check_urn:
            project = Project24(
                name=contact.get(
                    "name", ""
                ), 
                urn=urn,
                contact_uuid=contact.get("uuid", ""),  # Extract 'uuid' from 'contact'
                flow_name=flow.get("name", ""),  # Extract 'name' from 'flow'
                flow_uuid=flow.get("uuid", ""),  # Extract 'uuid' from 'flow'
                borrower_fullname=results.get("borrowerfullname", {}).get(
                    "value", ""
                ),  # Extract 'borrowerfullname'
                borrower2_fullname=results.get("borrower2fullname", {}).get(
                    "value", ""
                ),  # Extract 'borrower2fullname'
                civil_servant_response=results.get("civil_servant_response", {}).get(
                    "value", ""
                ),  # Extract 'civil_servant_response'
                first_name=results.get("first_name", {}).get(
                    "value", ""
                ),
                last_name=results.get("last_name", {}).get(
                    "value", ""
                ),
                date_of_employment=results.get("dateofemployment", {}).get(
                    "value", ""
                ),  # Extract 'dateofemployment'
                dept_code=results.get("deptcode", {}).get(
                    "value", ""
                ),  # Extract 'deptcode'
                ec_number=results.get("ecnumber", {}).get(
                    "value", ""
                ),  # Extract 'ecnumber'
                email_address=results.get("emailaddress", {}).get(
                    "value", ""
                ),  # Extract 'emailaddress'
                employer_contact=results.get("employercontact", {}).get(
                    "value", ""
                ),  # Extract 'employercontact'
                employment_location=results.get("employmentlocation", {}).get(
                    "value", ""
                ),  # Extract 'employmentlocation'
                full_name=results.get("fullname", {}).get(
                    "value", ""
                ),  # Extract 'fullname'
                gender=results.get("gender", {}).get("category", ""),  # Extract 'gender'
                home_address=results.get("homeaddress", {}).get(
                    "value", ""
                ),  # Extract 'homeaddress'
                id_number=results.get("idnumber", {}).get(
                    "value", ""
                ),  # Extract 'idnumber'
                job_position=results.get("jobposition", {}).get(
                    "value", ""
                ),  # Extract 'jobposition'
                ministry_name=results.get("ministryname", {}).get(
                    "value", ""
                ),  # Extract 'ministryname'
                mobile_num1=results.get("mobilenum1", {}).get(
                    "value", ""
                ),  # Extract 'mobilenum1'
                mobile_num2=results.get("mobilenum2", {}).get(
                    "value", ""
                ),  # Extract 'mobilenum2'
                net_salary=results.get("netsalary", {}).get(
                    "value", ""
                ),  # Extract 'netsalary'
                nok_fullname=results.get("nokfullname", {}).get(
                    "value", ""
                ),  # Extract 'nokfullname'
                nok_id=results.get("nokid", {}).get(
                    "value", ""
                ), 
                     # Extract 'nokid'
                nok_phone=results.get("nokphone", {}).get(
                    "value", ""
                ),  # Extract 'nokphone'
                nok_relationship=results.get("nokrelationship", {}).get(
                    "value", ""
                ),  # Extract 'nokrelationship'
                nok_address=results.get("nokaddress", {}).get(
                    "value", ""
                ),  # Extract 'nokaddress'
                spouse_fullname=results.get("spousefullname", {}).get(
                    "value", ""
                ),  # Extract 'spousefullname'
                spouse_id=results.get("spouseid", {}).get(
                    "value", ""
                ),  # Extract 'spouseid'
                spouse_address=results.get("spouseaddress", {}).get(
                    "value", ""
                ),  # Extract 'spouseaddress'
                spouse_selection=results.get("spouseselecetion", {}).get(
                    "value", ""
                ),  # Extract 'spouseselecetion'
                selecttenure_package=results.get("selecttenure", {}).get(
                    "category", ""
                ), 
                tenure_package=results.get("package", {}).get(
                    "category", ""
                ),
                pin=PIN
            )
            project.save()
            
            resub = Project24Resubmit(
                urn=contact.get("urn", "").replace("tel:+", "")
            )
            resub.save()
            params = {"pin": PIN}
        else:
            Project24.objects.get(urn=urn).update(
                name=contact.get("name", ""),
                urn=urn,
                contact_uuid=contact.get("uuid", ""),
                flow_name=flow.get("name", ""),
                flow_uuid=flow.get("uuid", ""),
                first_name=results.get("first_name", {}).get("value", ""),
                last_name=results.get("last_name", {}).get("value", ""),
                borrower_fullname=results.get("borrowerfullname", {}).get("value", ""),
                borrower2_fullname=results.get("borrower2fullname", {}).get("value", ""),
                next_of_kin_fullname=results.get("next_of_kin_fullname", {}).get("value", ""),
                next_of_kin_id=results.get("next_of_kin_id", {}).get("value", ""),
                next_of_kin_phone=results.get("next_of_kin_phone", {}).get("value", ""),
                relationship_with_next_of_kin=results.get("relationship_with_next_of_kin", {}).get("value", ""),
                next_of_kin_address=results.get("next_of_kin_address", {}).get("value", ""),
                civil_servant_response=results.get("civil_servant_response", {}).get("value", ""),
                date_of_employment=results.get("dateofemployment", {}).get("value", ""),
                dept_code=results.get("deptcode", {}).get("value", ""),
                ec_number=results.get("ecnumber", {}).get("value", ""),
                email_address=results.get("emailaddress", {}).get("value", ""),
                employer_contact=results.get("employercontact", {}).get("value", ""),
                employment_location=results.get("employmentlocation", {}).get("value", ""),
                full_name=results.get("fullname", {}).get("value", ""),
                gender=results.get("gender", {}).get("category", ""),
                home_address=results.get("homeaddress", {}).get("value", ""),
                id_number=results.get("idnumber", {}).get("value", ""),
                job_position=results.get("jobposition", {}).get("value", ""),
                ministry_name=results.get("ministryname", {}).get("value", ""),
                mobile_num1=results.get("mobilenum1", {}).get("value", ""),
                mobile_num2=results.get("mobilenum2", {}).get("value", ""),
                net_salary=results.get("netsalary", {}).get("value", ""),
                nok_fullname=results.get("nokfullname", {}).get("value", ""),
                nok_id=results.get("nokid", {}).get("value", ""),
                nok_phone=results.get("nokphone", {}).get("value", ""),
                nok_relationship=results.get("nokrelationship", {}).get("value", ""),
                nok_address=results.get("nokaddress", {}).get("value", ""),
                spouse_fullname=results.get("spousefullname", {}).get("value", ""),
                spouse_id=results.get("spouseid", {}).get("value", ""),
                spouse_address=results.get("spouseaddress", {}).get("value", ""),
                spouse_selection=results.get("spouseselecetion", {}).get("value", ""),
                selecttenure_package=results.get("selecttenure", {}).get("category", ""),
                tenure_package=results.get("package", {}).get("category", ""),
                pin=PIN
            )
            
        
    return JsonResponse(params, safe=False)


@login_required(login_url="/")
def user_details(request, pk):
    message = ""
    feedback_log_list = None
    feedBack_log = None
    internal_log_list = ''
    internal_log = ''
    change_log = None
    user = Project24.objects.get(pk=pk)  
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        # Updating the user data from the form
        note = request.POST.get('note')
        user.urn = request.POST.get('urn')
        if user.first_name == request.POST.get('first_name'):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="First name",
                from_data=user.first_name,
                to_data=request.POST.get('first_name', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.first_name = request.POST.get('first_name', '')
            user.save()
        if user.last_name == request.POST.get('last_name'):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Last name",
                from_data=user.last_name,
                to_data=request.POST.get('last_name', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.last_name = request.POST.get('last_name', '')
            user.save()    
        if user.gender == request.POST.get('gender', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Gender",
                from_data=user.gender,
                to_data=request.POST.get('gender', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.gender = request.POST.get('gender', '')
            user.save()
        
        if user.date_of_employment == request.POST.get('date_of_employment', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Employment date",
                from_data=user.date_of_employment,
                to_data=request.POST.get('date_of_employment', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.date_of_employment = request.POST.get('date_of_employment')
            user.save()
            
        if user.dept_code == request.POST.get('dept_code', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Department code",
                from_data=user.dept_code,
                to_data=request.POST.get('dept_code', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.dept_code = request.POST.get('dept_code')
            user.save()
            
        if user.ec_number == request.POST.get('ec_number', ''):
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="EC Number",
                from_data=user.ec_number,
                to_data=request.POST.get('ec_number', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.ec_number = request.POST.get('ec_number')
            user.save()
            
        if user.ssb_state == request.POST.get('ssb_state', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="SSB Status",
                from_data=user.ssb_state,
                to_data=request.POST.get('ssb_state', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.ssb_state = request.POST.get('ssb_state')
            user.save()   
            
        if user.payeecode == request.POST.get('payeecode', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Payee code",
                from_data=user.payeecode,
                to_data=request.POST.get('payeecode', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.payeecode = request.POST.get('payeecode')
            user.save()      
        if user.email_address == request.POST.get('email_address', ''):
            pass
        else:    
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Email",
                from_data=user.email_address,
                to_data=request.POST.get('email_address', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.email_address = request.POST.get('email_address', '')
            user.save() 
            
        if user.id_number == request.POST.get('id_number', ''):
            pass
        else:    
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="ID Number",
                from_data=user.id_number,
                to_data=request.POST.get('id_number', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.id_number = request.POST.get('id_number', '')
            user.save()   
            
        if user.home_address == request.POST.get('home_address', ''):
            pass
        else:    
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Home Address",
                from_data=user.home_address,
                to_data=request.POST.get('home_address', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.home_address = request.POST.get('home_address', '')
            user.save()     
            
        if user.ec_number == request.POST.get('ec_number', ''):
            pass
        else:    
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="EC Number",
                from_data=user.ec_number,
                to_data=request.POST.get('ec_number', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.ec_number = request.POST.get('ec_number', '')
            user.save()    
            
        if user.job_position == request.POST.get('job_position', ''):
            pass
        else:    
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Job Position",
                from_data=user.job_position,
                to_data=request.POST.get('job_position', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.job_position = request.POST.get('job_position', '')
            user.save()     
            
        if user.ministry_name == request.POST.get('ministry_name', ''):
            pass
        else:    
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Ministry name",
                from_data=user.ministry_name,
                to_data=request.POST.get('ministry_name', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.ministry_name = request.POST.get('ministry_name', '')
            user.save()
            
        if user.net_salary == request.POST.get('net_salary', ''):
            pass
        else:    
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Net Salary",
                from_data=user.net_salary,
                to_data=request.POST.get('net_salary', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.net_salary = request.POST.get('net_salary', '')
            user.save()  
            
        if user.gross_salary == request.POST.get('gross_salary', ''):
            pass
        else:    
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Gross Salary",
                from_data=user.gross_salary,
                to_data=request.POST.get('gross_salary', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.gross_salary = request.POST.get('gross_salary', '')
            user.save()                      
            
        if user.employer_contact == request.POST.get('employer_contact', ''):
            pass
        else:    
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Gross Salary",
                from_data=user.employer_contact,
                to_data=request.POST.get('employer_contact', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.employer_contact = request.POST.get('employer_contact')
            user.save()
        
        user.borrower_fullname = request.POST.get('borrower_fullname')
        user.borrower2_fullname = request.POST.get('borrower2_fullname')
        


        user.employment_location = request.POST.get('employment_location')
        user.dob = request.POST.get('dob', '')
        user.title = request.POST.get('title', '')
        
        user.spouse_fullname = request.POST.get('spouse_fullname')
        user.spouse_id = request.POST.get('spouse_id')
        user.spouse_address = request.POST.get('spouse_address')
        
        if user.status == request.POST.get('status', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Status",
                from_data=user.status,
                to_data=request.POST.get('status', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            if request.POST.get('status', '') == "Approved":
                user.status = request.POST.get('status', '')
                user.lastEditedDate = formatted_datetime
                user.approvedBy = request.user.username
                user.save()
            else:
                user.status = request.POST.get('status', '')
                user.save()
                    
        user.lastEditedBy = request.user.username
        if user.from_date == request.POST.get('from_date', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="From Date",
                from_data=user.from_date,
                to_data=request.POST.get('from_date', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.from_date = request.POST.get('from_date')
            user.save()
        if user.to_date == request.POST.get('to_date', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="To Date",
                from_data=user.to_date,
                to_data=request.POST.get('to_date', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.to_date = request.POST.get('to_date')
            user.save()
            
        if user.loan_amount == request.POST.get('loan_amount', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Loan Amount",
                from_data=user.loan_amount,
                to_data=request.POST.get('loan_amount', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.loan_amount = request.POST.get('loan_amount', '')
            user.save()
            
        if user.monthly_installment == request.POST.get('monthly_installment', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Monthly Installment",
                from_data=user.monthly_installment,
                to_data=request.POST.get('monthly_installment', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.monthly_installment = request.POST.get('monthly_installment', '')
            user.save()  
            
            
        if user.loan_tenure == request.POST.get('loan_tenure', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Loan tenure",
                from_data=user.loan_tenure,
                to_data=request.POST.get('loan_tenure', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.loan_tenure = request.POST.get('loan_tenure', '')
            user.save() 

        if user.nok_fullname == request.POST.get('nok_fullname', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Next Of Kin Fullname",
                from_data=user.nok_fullname,
                to_data=request.POST.get('nok_fullname', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.nok_fullname = request.POST.get('nok_fullname', '')
            user.save()

        if user.nok_id == request.POST.get('nok_id ', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Next Of Kin ID",
                from_data=user.nok_id,
                to_data=request.POST.get('nok_id', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.nok_id = request.POST.get('nok_id', '')
            user.save()

        if user.nok_phone == request.POST.get('nok_phone ', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Next Of Kin Phone",
                from_data=user.nok_phone,
                to_data=request.POST.get('nok_phone', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.nok_phone= request.POST.get('nok_phone', '')
            user.save()

        if user.nok_relationship == request.POST.get('nok_relationship ', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Relationship With Next Of Kin",
                from_data=user.nok_relationship,
                to_data=request.POST.get('nok_relationship', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.nok_relationship= request.POST.get('nok_relationship', '')
            user.save()

        if user.nok_address == request.POST.get('nok_address ', ''):
            pass
        else:
            edit_log = Project24EditLog(
                urn=user.urn,
                field_edited="Next Of Kin Address",
                from_data=user.nok_address,
                to_data=request.POST.get('nok_address', ''),
                reason=note,
                edited_by=request.user.username
            )
            edit_log.save()
            user.nok_address= request.POST.get('nok_address', '')
            user.save()
     
        
        # Save the updated user details to the database
        user.save()
        
        save_internal_log = Project24NoteLog(
            client=user,
            internal_note=request.POST.get('note', ''),
            createdBy=request.user.username,
            
        )
        save_internal_log.save()

        # Show a success message
        messages.success(request, 'User details have been successfully updated.')
        return redirect('user_details', pk=user.pk)
    feedBack_log = Project24FeedBackLog.objects.filter(client=user.pk).exists()
    if feedBack_log:
        feedback_log_list = Project24FeedBackLog.objects.filter(client=user.pk)
    else:
        pass    
    
    internal_log = Project24NoteLog.objects.filter(client=user.pk).exists()
    if internal_log:
        internal_log_list = Project24NoteLog.objects.filter(client=user.pk)
    else:
        pass   
    template = "website/project24/pages/user_details.html"
    context = {
        "user": user,
        "msg": message,
        "id_pic": "https://2waychat.com/media/" + str(user.id_picture),
        "id_pic1": "https://2waychat.com/media/" + str(user.proof_of_residence),
        "id_pic2": "https://2waychat.com/media/" + str(user.pay_slip),
        "id_pic3": "https://2waychat.com/media/" + str(user.employment_letter),
        "id_pic4": "https://2waychat.com/media/" + str(user.sized_photo),
        
        # "r1": "https://2waychat.com/media/" + str(user_r.id_picture),
        # "r2": "https://2waychat.com/media/" + str(user_r.proof_of_residence),
        # "r3": "https://2waychat.com/media/" + str(user_r.pay_slip),
        # "r4": "https://2waychat.com/media/" + str(user_r.employment_letter),
        # "r5": "https://2waychat.com/media/" + str(user_r.sized_photo),
        
        "flog": feedback_log_list,
        "nlog": internal_log_list,
        "clog": change_log,
    }
    return render(request, template, context)


@login_required(login_url="/")
def send_note(request):
    token = settings.P24_WHATSAPP_TOKEN
    print(token)
    phone_number_id = settings.PHONENUMBER_ID_P24
    print(phone_number_id)
    if request.method == "POST":
        note = request.POST.get("feedback_note", "")
        mobile_number = request.POST.get("mobile_number", "")
        print(note)
        print(mobile_number)
        URL = "https://graph.facebook.com/v20.0/" + phone_number_id + "/messages?access_token=" + token
        data = {
            "messaging_product": "whatsapp",
            "to": mobile_number,
            "text": {"body": note},
        }
        headers = {"Content-Type": "application/json"}
        p = requests.post(URL, data=json.dumps(data), headers=headers)
        print(p.text)
        if p.status_code == 200:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            get_user = Project24.objects.get(urn=mobile_number)
            get_user.user_sent_feedback = note
            get_user.lastEditedBy = request.user.username
            get_user.lastEditedDate = formatted_datetime
            get_user.save()
            
            # Save to Feedback log
            save_log = Project24FeedBackLog(
                client=get_user,
                user_sent_feedback=note,
                createdBy=request.user.username,
            )
            save_log.save()
            return redirect('user_details', pk=get_user.pk)
    return HttpResponse("200")    
       


def generate_loan_application_pdf(request, pk):
    project = Project24.objects.get(id=pk)
    templates = "pages/loan_application.html"
    context = {
        'user': project
    }
    
    html_string = render(request, template, context).content.decode('utf-8')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{project.full_name}-{project.urn}-{project.id}.pdf"'

    # Use WeasyPrint to generate the PDF
    HTML(string=html_string).write_pdf(response)

    return response


def generate_p24_pdf(request, pk):
    project = Project24.objects.get(id=pk)
    template = "website/project24/pages/project_24_form.html"
    context = {
        'project': project
    }
    html_string = render(request, template, context).content.decode('utf-8')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{project.full_name}-P24-{project.urn}-{project.id}.pdf"'
    HTML(string=html_string).write_pdf(response)
    return response


def generate_ssb_pdf(request, pk):
    # Get the project data
    project = Project24.objects.get(id=pk)

    context = {
        'project': project
    }
    templates = "pages/ssb_form.html"
    html_string = render(request, template, context).content.decode('utf-8')
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{project.full_name}-SSB-{project.urn}-{project.id}.pdf"'

    # Use WeasyPrint to generate the PDF
    HTML(string=html_string).write_pdf(response)

    return response

def login_user_project24(request):
    msg = ""
    if request.user.is_authenticated:
        try:
            return HttpResponseRedirect(redirect_to='/project-24/dashboard')
        except Exception as e:
            print(e)

    if request.method == "POST":
        try:
            name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            new_user = authenticate(username=name, password=password)
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(redirect_to='/project-24/dashboard')

            else:
                msg = "Access denied! Invalid credentials, please try again!"
                context = {"msg": msg}
                return render(request, 'website/project24/auth/login.html', context)
        except Exception as e:
            print(e)
    return render(request, 'website/project24/p24Auth/login.html')


@login_required(login_url='/')
def user_logout_project24(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/project24/login')
