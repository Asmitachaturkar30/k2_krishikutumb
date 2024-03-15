from .NotificationAppDBOperations import *
from django.http import JsonResponse


def createDevice_fn(profileId, mobileNumber, deviceToken, Notes, Description):
    if (
        profileId and
        mobileNumber and
        deviceToken and
        Notes and
        Description 
    ):

        response = createDevice_db(profileId, mobileNumber, deviceToken, Notes, Description)

        return response
    else:
        response = ({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
#-----------------------------------------------------------------------------------------

def getUserNotification_fn(profileId):
    result = getUserNotification_db(profileId)

    data_list = []

    if result:
        response = {
            "result": "success",
            "message": "success",
            "userList": []
        }

        for item in result:
            notification_text = item[3]

            # Check if notification_text is a string, not JSON
            if isinstance(notification_text, str):
                notification_text_str = notification_text
            else:
                # Convert JSON to string
                notification_text_str = json.dumps(notification_text)

            data = {
                "notification_id": item[0],
                "profileId": item[1],
                "userId": item[2],
                "notification_text": notification_text_str,
                "notification_type": item[4],
                "is_read": item[5]
            }
            data_list.append(data)

        response["userList"] = data_list

        return response
    else:
        response = {
            "result": "error",
            "message": "No data found"
        }
        return response
