from pyfcm import FCMNotification

def send_fcm_notification(registration_id, title, body, data):
    fcm_api_key = ''  # Replace with your actual FCM API key

    push_service = FCMNotification(api_key=fcm_api_key)

    message = {
        "to": registration_id,
        "notification": {
            "title": title,
            "body": body
        },
        "data": data
    }

    # Send the FCM notification
    result = push_service.notify_single_device(registration_id=registration_id, message_body=body, data_message=message)

    return result
