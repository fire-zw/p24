#from django.shortcuts import render

#def home(request):
#    if request.method == "POST":
#        # Handle POST data here
 #       post_data = request.POST.get("example", "")  # Example of getting form data
 #       
 #       # You can process the POST data here
 #       context = {"message": f"Received: {post_data}"}
  #  else:
   #     # Handle GET requests here (default case)
    #    context = {}

    #template = "index.html"
    #return render(request, template, context)


#from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#import json

#@csrf_exempt  # Disable CSRF protection for webhook requests (ensure security otherwise)
#def webhook_handler(request):
#    if request.method == "POST":
#        try:
#            payload = json.loads(request.body)
#            # Process the payload
#            print("Webhook received:", payload)
#            # Perform any specific action with the payload here
#            return JsonResponse({"status": "success", "message": "Webhook processed successfully!"})
#        except json.JSONDecodeError:
#            return JsonResponse({"status": "error", "message": "Invalid JSON payload"}, status=400)
#    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

from django.views.decorators.csrf import csrf_exempt
from .models import WebhookPayload
from django.shortcuts import render
import json
from django.http import JsonResponse

def dashboard(request):
    payloads = WebhookPayload.objects.all().order_by('-timestamp')
    return render(request, 'dashboard.html', {'payloads': payloads})

@csrf_exempt
def webhook_handler(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            # Save payload to database
            WebhookPayload.objects.create(payload=payload)
            return JsonResponse({"status": "success", "message": "Webhook processed successfully!"})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON payload"}, status=400)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)
