
import requests, json
import logging
from datetime import datetime
import urllib3

BASE_URL = 'http://65.0.225.117/'
ENDPOINT = 'k2kapi/myFarm/'

api_data = [
    {
        "operation": "createFarmDetails",
        "user": {
            "profileId": "52",
            "farmName": "Pali",
            "farmType": "Active",
            "soilType": "NA",
            "farmStatus": "Owner",
            "farmSizeInAcre": "2 acre",
            "farmElectricity": "Yes",
            "waterPHValue": "NA",
            "farmWaterSource": "Yes",
            "scheduledcropsname": "Na"
        }
    }
#     {
#   "operation": "createFarmerCropScheduleMulitRow",
#   "user": [{
#     "profileId": "60",
#     "farmId": "5",
#     "cropStatus": "Active",
#     "cropName": "Wheat",
#     "activitySequence": "2",
#     "activityName": "Irrigation",
#     "activityNameLocal": "Irrigation",
#     "activityExpectedInDays": "2",
#     "needHelp": "No",
#     "expenses": "1000",
#     "doneOrSkip": "Done",
#     "activityExpectedStartDate": "23-08-2023 19:30:00 Wednesday",
#     "activityCompletedDate": "23-08-2023 19:30:00 Wednesday",
#     "activityRescheduledDate": "23-08-2023 19:30:00 Wednesday"
#   },
#   {
#     "profileId": "61",
#     "farmId": "5",
#     "cropStatus": "Active",
#     "cropName": "Wheat",
#     "activitySequence": "3",
#     "activityName": "Irrigation2",
#     "activityNameLocal": "Irrigation2",
#     "activityExpectedInDays": "2",
#     "needHelp": "No",
#     "expenses": "1000",
#     "doneOrSkip": "Done",
#     "activityExpectedStartDate": "23-08-2023 19:30:00 Wednesday",
#     "activityCompletedDate": "23-08-2023 19:30:00 Wednesday",
#     "activityRescheduledDate": "23-08-2023 19:30:00 Wednesday"
#   }
#   ]
# },
# {	
# 	"operation" : "getCropSchedule",
# 	"cropName":"Wheat",
# 	"state":"Madhya Pradesh",
# 	"district":"Harda"
# },
# {	
# 	"operation" : "getFarmDetails",
# 	"profileId":"52"
# },
# {	
# 	"operation" : "getFarmerCropSchedule", 
# 	"cropName":"Wheat",
# 	"farmId":"4",
# 	"profileId":"62"
# },
# {
#   "operation": "updateFarmerCropSchedule",
#   "user": [
#   {
#     "needHelp": "yes",
#     "expenses": "4000",
#     "doneOrSkip": "No",
#     "activityExpectedStartDate": "23-08-2023 20:30:00 Wednesday",
#     "activityCompletedDate": "16-08-2023 20:30:00 Wednesday",
#     "activityRescheduledDate": "16-08-2023 20:30:00 Wednesday",
#     "profileId": "62",
#     "farmId": "4",
#     "id": "17"
#   },
#     {
#     "needHelp": "yes",
#     "expenses": "3000",
#     "doneOrSkip": "No",
#     "activityExpectedStartDate": "16-08-2023 20:30:00 Wednesday",
#     "activityCompletedDate": "16-08-2023 20:30:00 Wednesday",
#     "activityRescheduledDate": "16-08-2023 20:30:00 Wednesday",
#     "profileId": "62",
#     "farmId": "4",
#     "id": "16"
#   }
#   ]
# },
# {
#    "operation":"deleteFarm",
#    "user":{
#       "profileId":"52",
#       "farmId":"5"  }
# }
]

# # Set up logging for responses
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create loggers
logger_responses = logging.getLogger('myFarm_responses')
logger_results = logging.getLogger('myFarm_results')

# Create handlers for the loggers
handler_responses = logging.FileHandler('myFarm_responses.log')
handler_results = logging.FileHandler('myFarm_results.log')

# Define log formats (if needed)
formatter = logging.Formatter('%(message)s')

# Set the formatter for the handlers
handler_responses.setFormatter(formatter)
handler_results.setFormatter(formatter)

# Add the handlers to the loggers
logger_responses.addHandler(handler_responses)
logger_results.addHandler(handler_results)

# Set the logging levels (if needed)
logger_responses.setLevel(logging.INFO)
logger_results.setLevel(logging.INFO)

# Process responses and log to api_responses.log
try:
    for data in api_data:
        response = requests.post(f'{BASE_URL}{ENDPOINT}', json=data)
        
        if response.status_code == 200:
            result = response.json().get('result', 'unknown')
            # log_message = f"{current_datetime}\n{BASE_URL}{ENDPOINT}\n\t{data['operation']} = {result}\n\t{json.dumps(data)}\n\t{json.dumps(response.json())}\n{'- -'*60}"
            log_message = f"{current_datetime}\n{BASE_URL}{ENDPOINT}\n{data['operation']} = {result}\nRequest Data:\n{json.dumps(data, indent=4)}\nResponse Data:\n{json.dumps(response.json(), indent=4)}\n{'- -'*60}"

            print(log_message)
            # logging.info(log_message)
            logger_responses.info(log_message)
        else:
            print(f"API for operation '{data['operation']}' returned an error. Status code: {response.status_code}")
            print("Response content:")
            print(response.text)
            logging.error(f"{current_datetime}\n\tAPI for operation '{data['operation']}' returned an error. Status code: {response.status_code}, Response: {response.text}")
except (urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError) as e:
    print(f"Failed to establish a connection: {str(e)}")
    logging.error(f"{current_datetime}\nFailed to establish a connection: {str(e)}")

# Process responses and log to api_result.log
try:
 for data in api_data:
     response = requests.post(f'{BASE_URL}{ENDPOINT}', json=data)
    
     if response.status_code == 200:
         result = response.json().get('result', 'unknown')
         log_message = f"{current_datetime}\n{BASE_URL}{ENDPOINT}\n{data['operation']} = {result}\n{'-*'*40}"
         print(log_message)
         logger_results.info(log_message)
     else:
         print(f"API for operation '{data['operation']}' returned an error. Status code: {response.status_code}")
         print("Response content:")
         print(response.text)
         logging.error(f"{current_datetime}\n\tAPI for operation '{data['operation']}' returned an error. Status code: {response.status_code}, Response: {response.text}")

except (urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError) as e:
    print(f"Failed to establish a connection: {str(e)}")
    logging.error(f"{current_datetime}\nFailed to establish a connection: {str(e)}")