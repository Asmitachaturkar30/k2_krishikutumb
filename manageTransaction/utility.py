# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)


# from firebase_admin import messaging

# def send_notification(provider_token, title, body):
#     message = messaging.Message(
#         token=provider_token,
#         notification=messaging.Notification(
#             title=title,
#             body=body,
#         ),
#     )

#     # Send the FCM notification
#     result = messaging.send(message)
#     return result
