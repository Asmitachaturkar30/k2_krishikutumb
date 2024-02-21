from .manageK2appDbOperation import *
from django.http import JsonResponse

 # ------------------------------------------------------------------------------------------
def getMsgParamNotEmpty():
    return {'result': 'failure','message': 'JSON Invalid Parameters.'}

 # ------------------------------------------------------------------------------------------
def getPrimarySecondaryFunctions_fn(state, district):
    result = getPrimarySecondaryFunctions_db(state, district)

    response = {} 
    if result is not None:
        user_list = []
        for item in result:
            data = {
                "priSecId": item[0],
                "primaryFunction": item[1],
                "secondaryFunction": item[2],
                "primaryFunctionImageName": item[3],
                "secondaryFunctionImageName": item[4],
                "canRegister": item[5],
                "canDemandSecondaryFunction": item[6],
                "isAvailableSecondaryFunction": item[7],
                "areFunctionInUse": item[8],
                "primaryFunctionLocal": item[9],
                "secondaryFunctionLocal": item[10],
                "functionUnit": item[11],
                "functionType": item[12]
            }
            user_list.append(data)  # Append the data to the user_list

        response = {
            "result": "success",
            "message": "success",
            "userList": user_list  # Set the user list in the response
        }
    elif result is None:
        response = {
            "result": "error",
            "message": "No data found"
        }
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }

    return response

# ------------------------------------------------------------------------------------------
def getLanguages_fn(language, k2Type):
    result = getLanguages_db(language, k2Type)
    english_result = getLanguages_db('ENGLISH', k2Type)  # Pass k2Type to the second call
    response = {} 
    
    if result is not None:
        user_list = []
        
        for item, english_item in zip(result, english_result):
            data = {
                "englishName": english_item[0],
                "localName": item[1]
            }
            
            user_list.append(data)  # Append the data to the user_list

        response = {
            "result": "success",
            "message": "success",
            "userList": user_list  # Set the user list in the response
        }
    elif result is None:
        response = {
            "result": "error",
            "message": "No data found"
        }
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }

    return response

 # ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# def getk2support_fn(state, district):
#     result = getk2support_db(state, district)

#     data = []
#     if result is not None:
#         response = {
#             "result": "success",
#             "message": "success",
#             "userList": []
#         }

#         for item in result:
#             data = {
#                 "id": item[0],
#                 "vedioLink": item[1],
#                 "vedioType": item[2],
#                 "vediok2Page": item[3],
#                 "vedioLinkHindi": item[4],
#                 "vedioLinkLocal": item[5]

#             }
#             response["userList"].append(data)

#         return response
#     elif result is None:
#         Jresponse = JsonResponse({
#             "result": "error",
#             "message": "No data found"
#         })
#         return Jresponse
#     else:
#         response = {
#             "result": "failure",
#             "message": "Get Request Failure"
#         }
#         return response

def getk2support_fn(state, district):
    result = getk2support_db(state, district)
    response = {}  # Create an empty response dictionary

    if result is not None:
        user_list = []  # Create an empty list for user data

        for item in result:
            data = {
                "id": item[0],
                "vedioLink": item[1],
                "vedioType": item[2],
                "vediok2Page": item[3],
                "vedioLinkHindi": item[4],
                "vedioLinkLocal": item[5]
            }
            user_list.append(data)  # Append the data to the user_list

        response = {
            "result": "success",
            "message": "success",
            "userList": user_list  # Set the user list in the response
        }
    elif result is None:
        Jresponse = JsonResponse({
            "result": "error",
            "message": "No data found"
        })
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }

    return response


# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


def getStateDistrictList_fn():
    result = getStateDistrictList_db()

    response = {}  # Create an empty response dictionary

    if result is not None:
        user_list = [] 

        for item in result:
            data = {
                "id": item[0],
                "state": item[1],
                "state_hindi": item[2],
                "district": item[3],
                "district_hindi": item[4],
                "latitude":item[5],
                "longitude":item[6]

            }
            user_list.append(data)  # Append the data to the user_list

        response = {
            "result": "success",
            "message": "success",
            "userList": user_list  # Set the user list in the response
        }
    elif result is None:
        Jresponse = JsonResponse({
            "result": "error",
            "message": "No data found"
        })
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }

    return response
# ------------------------------------------------------------------------------------------


def getVillageList_fn(state, district):
    result = getVillageList_db(state, district)

    response = {} 
    if result is not None:
        user_list = []
        for item in result:
            data = {
                "id": item[0],
                "tehsil": item[1],
                "village": item[2],
                "tehsil_hindi": item[3],
                "village_hindi": item[4],
                "latitude":item[5],
                "longitude":item[6]

            }
            user_list.append(data)  # Append the data to the user_list

        response = {
            "result": "success",
            "message": "success",
            "userList": user_list  # Set the user list in the response
        }
    elif result is None:
        Jresponse = {
            "result": "error",
            "message": "No data found"
        }
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }

    return response
# ------------------------------------------------------------------------------------------
def getTertiaryFourthFunctions_fn(priSecId):
    result = getTertiaryFourthFunctions_db(priSecId)

    response = {}  # Create an empty response dictionary

    if result is not None:
        user_list = [] 

        for item in result:
            data = {
                "id": str(item[0]),
                "priSecId": str(item[1]),
                "tertiaryFunction": str(item[2]),
                "fourthFunction": str(item[3]),
                "tertiaryFunctionVariety": str(item[4]),
                "fourthFunctionVariety": str(item[5]),
                "tertiaryFunctionImageName": str(item[6]),
                "fourthFunctionImageName": str(item[7]),
                "tertiaryFunctionLocal": str(item[8]),
                "fourthFunctionLocal": str(item[9]),
                "tertiaryFunctionVarietyLocal": str(item[10]),
                "fourthFunctionVarietyLocal": str(item[11]),
                "canDemandtertiaryFunction": str(item[12]),
                "isAvailabletertiaryFunction": str(item[13]),
                "areFunctionInUse": str(item[14]),
                "functionUnit": str(item[15]),
                "description": str(item[16])
            }
            user_list.append(data)  # Append the data to the user_list

        response = {
            "result": "success",
            "message": "success",
            "userList": user_list  # Set the user list in the response
        }
    elif result is None:
        Jresponse = JsonResponse({
            "result": "error",
            "message": "No data found"
        })
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }

    return response
# ------------------------------------------------------------------------------------------