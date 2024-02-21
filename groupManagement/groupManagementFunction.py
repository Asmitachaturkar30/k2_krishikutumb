from .groupManagementDbOperation import *
from django.http import JsonResponse

def getUserGroups_fn(groupId):
    result = getUserGroups_db(groupId)

    data = []
    if result is not None:
        response = {
                "result": "success",
                "message": "success",
                "userList": []
        }

        for item in result:
            data = {
                "id": item[0],
                "profileId": item[1],
                "activitySequence": item[2],
                "activityName": item[3],
                "activityNameLocal": item[4],
                "activityExpectedInDays": item[5],
                "needHelp": item[6],
                "expenses": item[7],
                "doneorSkip": item[8],
                "activityExpectedStartdate": item[9],
                "activityCompletedDate": item[10],
                "activityreScheduledDate": item[11],
                "memberFirstName": item[12],
                "memberLastName": item[13],
                "groupName": item[14],
                "groupId": item[15]
            }
            response["userList"].append(data)

        return response 
    
    elif result is None:
        Jresponse = {
            "result": "failure",
            "message": "No data found"
        }
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }
        return response