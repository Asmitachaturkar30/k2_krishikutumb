#!/usr/bin/python
from .managTransationDbOperation import *
from django.http import JsonResponse
from firebase_admin import messaging
import firebase_admin
from firebase_admin import credentials

 # ------------------------------------------------------------------------------------------
def registerAvailabilityDemand_fn(mobileNumber, demandType, demandPrimaryFunction, demandSecondaryFunction, demandTertiaryFunction, demandTertiaryFunctionVarity,
                                       demandFourthFunction, demandFourthFunctionVarity, demandInUnit, demandDate, demandNote, village, tehsil, district, state):

    if (mobileNumber and
        demandType and
        demandPrimaryFunction and
        demandSecondaryFunction and
        demandTertiaryFunction and
        demandTertiaryFunctionVarity and
        demandFourthFunction and
        demandFourthFunctionVarity and
        demandInUnit and
        demandDate and
        demandNote and
        village and
        tehsil and
        district and
        state
        ):

        response = registerAvailabilityDemand_db(mobileNumber, demandType, demandPrimaryFunction, demandSecondaryFunction, demandTertiaryFunction, demandTertiaryFunctionVarity,
                                                demandFourthFunction, demandFourthFunctionVarity, demandInUnit, demandDate, demandNote, village, tehsil, district, state)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
# ----------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
def doBooking_fn(consumerMobileNumber, providerMobileNumber, bookingType, isBookingExpired, bookingStatus, bookingPrimaryFunction,
                      bookingSecondaryFunction, bookingTertiaryFunction, bookingTertiaryFunctionVarity, bookingFourthFunction,
                      bookingFourthFunctionVarity, bookingInUnit, bookingDate, bookingNote, village, tehsil, district, state):

    if (consumerMobileNumber and
        providerMobileNumber and
        bookingType and
        isBookingExpired and
        bookingStatus and
        bookingPrimaryFunction and
        bookingSecondaryFunction and
        bookingTertiaryFunction and
        bookingTertiaryFunctionVarity and
        bookingFourthFunction and
        bookingFourthFunctionVarity and
        bookingInUnit and
        bookingDate and
        bookingNote and
        village and
        tehsil and
        district and
        state
        ):

        response = doBooking_db(consumerMobileNumber, providerMobileNumber, bookingType, isBookingExpired, bookingStatus, bookingPrimaryFunction,
                                       bookingSecondaryFunction, bookingTertiaryFunction, bookingTertiaryFunctionVarity, bookingFourthFunction, bookingFourthFunctionVarity,
                                       bookingInUnit, bookingDate, bookingNote, village, tehsil, district, state)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
# ----------------------------------------------------------------------------------
def getBooking_fn(providerMobileNumber, bookingPrimaryFunction, bookingSecondaryFunction, bookingTertiaryFunction):
    result = getBooking_db(providerMobileNumber, bookingPrimaryFunction, bookingSecondaryFunction, bookingTertiaryFunction)
    data = []
    if result is not None:
        response = {
            "result": 'success',
            "message": 'success',
            "userList": []
        }
        for row in result:
            data = {
                "firstName": row[0],
                "lastName": row[1],
                "mobileNumber": row[2],
                "village": row[3],
                "tehsil": row[4],
                "last_updated_at": row[5],
                "bookingType": row[6],
                "bookingStatus": row[7],
                "bookingDate": row[8],
                "bookingNote": row[9],
                "bookingInUnit": row[10],
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
# --------------------------------------------------------------------------------------------
    
def getTertiaryContacts_fn(primaryFunction, secondaryFunction, tertiaryFunction, tertiaryFunctionVariety, fourthFunction, fourthFunctionVariety, village, tehsil):
        response = getTertiaryContacts_db(primaryFunction, secondaryFunction, tertiaryFunction, tertiaryFunctionVariety, fourthFunction, fourthFunctionVariety, village, tehsil)
        data = []
        # Check if the result is a list of tuples
        if response is not None:
            response = {
            "result": 'success',
            "message": 'success',
            "userList": []
            }
            for item in response:
                data = {
                    "profileid": item[0],
                    "firstname": item[1],
                    "lastname": item[2],
                    "mobilenumber": item[3],
                    "village": item[4],
                    "last_updated_at": item[5],
                    "priority": item[6],
                    "demandtype": item[7],
                    "functionunit": item[8],
                    "description": item[9]
                }
                response["userList"].append(data)
            return response 
        
        elif response is None:
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
# ------------------------------------------------------------------------------------------


def getContacts_fn(mobileNumber, primaryFunction, secondaryFunction, village, tehsil):
    result = getContacts_db(
        mobileNumber, primaryFunction, secondaryFunction, village, tehsil)

    data = []
    if result is not None:
        response = {
            "result": "success",
            "message": "success",
            "userList": []
        }

        for item in result:
            data = {
                "profileId": item[0],
                "firstName": item[1],
                "lastName": item[2],
                "mobileNumber": item[3],
                "village": item[4],
                "last_updated_at": item[5],
                "priority": item[6],
                "demandType": item[7]
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
# # ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

def createDevice_fn(profileId, mobileNumber, Notes, Description):
    if (profileId and mobileNumber and Notes and Description):
        response = createDevice_db(profileId, mobileNumber, Notes, Description)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
# ------------------------------------------------------------------------------------------



def getDeviceDetails_fn(profileId, mobileNumber):
    result = getDeviceDetails_db(profileId, mobileNumber)
    if result is not None:
        response = {
                "result": "success",
                "message": "success",
                "userList": []
        }

        for item in result:
            data = {
				"deviceId":item[0],
                "profileId":item[1],
                "mobileNumber":item[2],
				"token" : item[3],
                "Notes":item[4],
                "Description":item[5]
            }
            response["userList"].append(data)

        return (response)
    elif result is None:
        response = {
            "result": "error",
            "message": "No data found"
        }
        return (response)
    else:
        return response({
            "result": "error",
            "message": "get failuer"
        })
#----------------------------------------------------------------------------

def UpdateBooking_fn(bookingId,bookingType,isBookingExpired,bookingStatus,
                                    bookingInUnit,bookingDate,bookingNote):

    if (bookingId and bookingType and isBookingExpired and bookingStatus and bookingInUnit and bookingDate and bookingNote):
        response = UpdateBooking_db(bookingId,bookingType,isBookingExpired,bookingStatus,
                                    bookingInUnit,bookingDate,bookingNote)

        return response
    else:
        response = ({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response

# -------------------------------------------------------------------------------
import firebase_admin
from firebase_admin import credentials, messaging
from django.http import JsonResponse

cred = credentials.Certificate("I:\k2krishikutumb-firebase-adminsdk-klb7k-aa3e78dcde.json")
firebase_admin.initialize_app(cred)

# def send_notification(providerToken, title, body, data):
#     # print("Inside send_notification function...")
#     message = messaging.Message(
#         data=data,  # 'data' should be a dictionary with key-value pairs
#         notification=messaging.Notification(
#             title=title,
#             body=body,
#         ),
#         token=providerToken
#     )
#     result = messaging.send(message)
#     print("Result from send fcm:", result)  # Add this print statement
#     return result


# def send_notification(providerToken, title, body, data):
#     message = messaging.Message(
#         data=data,
#         notification=messaging.Notification(
#             title=title,
#             body=body,
#         ),
#         token=providerToken
#     )
#     try:
#         result = messaging.send(message)
#         print("Result from send FCM:", result)
#         return result
#     except firebase_admin._messaging_utils.UnregisteredError as e:
#         print(f"UnregisteredError: {e}")
#         # Handle unregistered error, e.g., update the token in your database or remove it
#         return {"error": "UnregisteredError", "message": str(e)}
#     except Exception as e:
#         print(f"Error sending FCM: {e}")
#         return {"error": "UnknownError", "message": str(e)}


import logging

logger = logging.getLogger(__name__)

# def doBookingNotific_fn(consumerMobileNumber, providerMobileNumber, bookingType, isBookingExpired, bookingStatus,
#                       bookingPrimaryFunction, bookingSecondaryFunction, bookingTertiaryFunction, bookingTertiaryFunctionVarity, bookingFourthFunction,
#                       bookingFourthFunctionVarity, bookingInUnit, bookingDate, bookingNote, village, tehsil, district, state, providerToken):

#     if (
#         consumerMobileNumber and providerMobileNumber and bookingType and isBookingExpired and bookingStatus and
#         bookingPrimaryFunction and bookingSecondaryFunction and bookingTertiaryFunction and
#         bookingTertiaryFunctionVarity and bookingFourthFunction and bookingFourthFunctionVarity and
#         bookingInUnit and bookingDate and bookingNote and village and tehsil and district and state and providerToken
#     ):

#         response = doBookingNotific_db(consumerMobileNumber, providerMobileNumber, bookingType, isBookingExpired, bookingStatus, bookingPrimaryFunction,
#                                        bookingSecondaryFunction, bookingTertiaryFunction, bookingTertiaryFunctionVarity, bookingFourthFunction, bookingFourthFunctionVarity,
#                                        bookingInUnit, bookingDate, bookingNote, village, tehsil, district, state, providerToken)
    
#         title = "New Booking"
#         body = f"You have a new booking from {consumerMobileNumber}. Type: {bookingType}, Status: {bookingStatus}"

#         logger.info("Before sending notification...")
#         notification_result = send_notification(providerToken, title, body, response)
#         logger.info("After sending notification...")

#         if isinstance(notification_result, str):
#             logger.info("Notification success. Returning success response.")
#             return JsonResponse({'result': 'success', 'message': 'Booking processed successfully'})
#         else:
#             logger.error("Notification failed. Returning failure response.")
#             return JsonResponse({'result': 'failure', 'message': 'Booking processed, but failed to send notification'})
#     else:
#         response = JsonResponse({
#             "result": "failure",
#             "message": "User Parameters should not be Null!"
#         })
#         return response
    
#----------------------------------------------------------------------
    


def getContactsNearby_fn(mobileNumber, primaryFunction, secondaryFunction, village, tehsil, nearbyRange,
                                                        latitude,longitude):
    result = getContactsNearby_db(
        mobileNumber, primaryFunction, secondaryFunction, village, tehsil, nearbyRange, latitude, longitude)

    data = []
    if result is not None:
        response = {
            "result": "success",
            "message": "success",
            "userList": []
        }

        for item in result:
            data = {
                "profileId": item[0],
                "firstName": item[1],
                "lastName": item[2],
                "mobileNumber": item[3],
                "village": item[4],
                "last_updated_at": item[5],
                "priority": item[6],
                "demandType": item[7],
                "distance":item[8]
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
# # ------------------------------------------------------------------------------------------
import concurrent.futures
from django.http import JsonResponse

def doBookingNotific_fn(consumerMobileNumber, providerMobileNumber, bookingType, isBookingExpired, bookingStatus,
                      bookingPrimaryFunction, bookingSecondaryFunction, bookingTertiaryFunction, bookingTertiaryFunctionVarity, bookingFourthFunction,
                      bookingFourthFunctionVarity, bookingInUnit, bookingDate, bookingNote, village, tehsil, district, state, providerToken):
    # Define a function to send notifications
    def send_notification(providerToken, title, body, data):
        message = messaging.Message(
            data=data,
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=providerToken
        )
        try:
            result = messaging.send(message)
            print("Result from send FCM:", result)
            return result
        except firebase_admin._messaging_utils.UnregisteredError as e:
            print(f"UnregisteredError: {e}")
            # Handle unregistered error, e.g., update the token in your database or remove it
            return {"error": "UnregisteredError", "message": str(e)}
        except Exception as e:
            print(f"Error sending FCM: {e}")
            return {"error": "UnknownError", "message": str(e)}


    # Define a function to perform database operations in parallel
    def perform_database_operations():
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit the functions for execution in parallel
            Booking = executor.submit(doBookingNotific_db, consumerMobileNumber, providerMobileNumber, bookingType, isBookingExpired, bookingStatus, bookingPrimaryFunction,
                                            bookingSecondaryFunction, bookingTertiaryFunction, bookingTertiaryFunctionVarity, bookingFourthFunction, bookingFourthFunctionVarity,
                                            bookingInUnit, bookingDate, bookingNote, village, tehsil, district, state, providerToken)

            # Use as_completed to wait for both functions to complete
            futures = [Booking]
            results = list(concurrent.futures.as_completed(futures))

            # Get the results in the order they were submitted
            database_result = results[0].result()

            return database_result

    # Perform database operations in parallel
    database_result = perform_database_operations()

    # Check if database operations were successful
    if database_result and database_result['result'] == 'success':
        # Prepare notification data
        notification_data = {
            "result": "success",
            "message": "success",
            "userList": [
                {"DatabaseResult": database_result},
            ]
        }

        # Send notification
        title = "New Booking"
        body = f"You have a new booking from {consumerMobileNumber}. Type: {bookingType}, Status: {bookingStatus}"
        notification_result = send_notification(providerToken, title, body, notification_data)

        # Check if notification was successful
        if isinstance(notification_result, str):
            return JsonResponse({'result': 'success', 'message': 'Booking processed successfully'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Booking processed, but failed to send notification'})
    else:
        return JsonResponse({'result': 'failure', 'message': 'Failed to process booking'})
