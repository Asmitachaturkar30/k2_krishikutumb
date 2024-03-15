from django.db import IntegrityError, DatabaseError, connection
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pyfcm import FCMNotification
from .NotificationAppFunction import *
from .utils import send_fcm_notification
from django.db import connection


@csrf_exempt
def send_notification(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            if 'operation' in data:
                operation = data['operation']

                if operation == 'createDevice':
                    if (
                        'user' in data and
                        'profileId' in data['user'] and
                        'mobileNumber' in data['user'] and
                        'deviceToken' in data['user'] and
                        'Notes' in data['user'] and
                        'Description' in data['user']
                    ):
                        user = data['user']
                        profileId = user['profileId']
                        mobileNumber = user['mobileNumber']
                        deviceToken = user['deviceToken']
                        Notes = user['Notes']
                        Description = user['Description']

                        response = createDevice_fn(profileId, mobileNumber, deviceToken, Notes, Description)

                        print("Response from create_device:", response)

                        if response['result'] == 'success':
                            if "Device created" in response.get("message", ""):
                                print("Condition met for device creation. Proceeding to notification.")
                                notification_result = send_fcm_notification(deviceToken, "New Device Created", "Your new device is ready!", response)
                                print("Notification result:", notification_result)

                                if notification_result and notification_result.get('success'):
                                    print("Notification success. Returning success response.")
                                    return JsonResponse({'result': 'success', 'message': 'Device created, and notification sent successfully'})
                                else:
                                    print("Notification failed. Returning failure response.")
                                    return JsonResponse({'result': 'failure', 'message': 'Device created, but failed to send notification'})
                            elif "Device updated" in response.get("message", ""):
                                print("Condition met for device update. Returning success response.")
                                return JsonResponse({'result': 'success', 'message': 'Device updated successfully'})
                            else:
                                print("Unexpected response message. Returning original response.")
                                return JsonResponse(response)
                        else:
                            print("Device creation/update failed. Returning failure response.")
                            return JsonResponse(response)
                    else:
                        return JsonResponse({'result': 'failure', 'message': 'Missing parameter'})
                    
                elif operation == 'getUserNotification':
                    if 'profileId' in data:
                        profileId = data['profileId']
                        response = getUserNotification_fn(profileId)
                        return JsonResponse(response)
                    else:
                        return JsonResponse({'message': 'Invalid parameters'})
                        
                else:
                    return JsonResponse({'result': 'failure', 'message': 'Invalid operation'})
        except json.JSONDecodeError:
            return JsonResponse({'result': 'failure', 'message': 'Invalid JSON data'})















































































































































































































































# @csrf_exempt
# def send_notification(request):
#     if request.method == 'POST':
#         if request.data:
#             data = request.data

#             if 'operation' in data:
#                 operation = data['operation']

#                 if operation == 'createDevice':
#                     if (
#                         'user' in data and
#                         'profileId' in data['user'] and
#                         'mobileNumber' in data['user'] and
#                         'Notes' in data['user'] and
#                         'Description' in data['user'] and
#                         'deviceToken' in data['user']  # Add this line to check for deviceToken
#                     ):
#                         user = data['user']
#                         profileId = user['profileId']
#                         mobileNumber = user['mobileNumber']
#                         Notes = user['Notes']
#                         Description = user['Description']
#                         deviceToken = user['deviceToken']  # Get the device token from the request

#                         response = createDevice_fn(profileId, mobileNumber, Notes, Description, deviceToken)

#                         # Check if the device creation was successful
#                         if response.get('result') == 'success':
#                             # Send push notification
#                             notification_result = send_fcm_notification(deviceToken, "New Device Created", "Your new device is ready!")

#                             # Handle the result of the notification
#                             if notification_result and notification_result.get('success'):
#                                 return JsonResponse({'result': 'success', 'message': 'Device created, and notification sent successfully'})
#                             else:
#                                 return JsonResponse({'result': 'success', 'message': 'Device created, but failed to send notification'})
#                         else:
#                             return JsonResponse({'result': 'failure', 'message': 'Failed to create device'})
#                     else:
#                         return JsonResponse({'result': 'failure', 'message': 'Missing parameter'})