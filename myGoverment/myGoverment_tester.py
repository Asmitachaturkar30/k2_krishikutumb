
import requests, json
import logging
from datetime import datetime

BASE_URL = 'http://65.0.225.117/'
ENDPOINT = 'k2kapi/myGoverment/'

api_data = [
    {
    "operation": "createGroup",
    "user": {
        "groupName": "gruopdata1",
        "groupOwnerFirstName": "John",
        "groupOwnerLastName": "Doe",
        "groupOwnerMobile": "9998887771",
        "groupType": "Type",
        "groupActivity": "Activity",
        "groupStatus": "Status",
        "activeInK2App": "Yes",
        "groupNote": "Group note goes here",
        "village": "Bhadungao",
        "tehsil": "Rehatgaon",
        "district": "Harda",
        "state": "Madhya Pradesh",
        "policyId":"2"
    }
},
    {
    "operation": "createMember",
    "user": {
        "memberProfileId": "12",
        "memberFirstName": "Mohan",
        "memberLastName": "Paliwal",
        "memberMobile": "9898989898",
        "groupName": "Mohan",
        "groupId": "5", 
        "memberStatus": "Active",
        "village": "Bhadugaon",
        "tehsil": "Rehatgaon",
        "district": "Harda",
        "state": "Madhya Pradesh"
    }
},
{
    "operation": "getGroup",
    "groupType": "All",
    "memberProfileId": "1",
    "state": "Madhya Pradesh",
    "district": "Harda"
},
{
    "operation": "getPolicy",
    "policyType": "All",
    "state": "Madhya Pradesh",
    "district": "Harda"
},
{
    "operation": "getMember",
    "groupId": "1"
},
{"operation": "getDocument",
 "policyId": "1"
},
{ 
   "operation":"deleteMember",
    "memberId":"12",
    "groupId":"5"
},
{ 
"operation":"deleteGroup",
    "groupId":"5"
},
{ 
   "operation":"getGroupByPolicy",
    "policyId":"6"
},
{
    "operation": "getGroupActivities",
    "groupId":"1"
},
{
    "operation": "getGroupDemandAvailability",
    "groupId": "1"
},
{
    "operation": "createUserPolicyDocument",
    "user": {
            "groupOwnerMobileNumber": "7896547854",
            "documentId": "1",
            "documentName": "docName",
            "documentType": "sampleDoc",
            "documentStatus": "Status",
            "documentCriteria": "documentCriteria",
            "documentDetails": "Details",
            "policyId": "1",
            "policyName": "policynamae1",
            "last_update_date": "2023-10-21T11:24:13",
            "DueDate": "2023-10-21T11:24:13"
        }
},
{
    "operation": "getUserPolicyDocument",
    "groupOwnerMobileNumber" : "7896547854",
    "policyId":"1"
},
{
    "operation": "UpdateUserPolicyDocument",
    "user": {
        "groupOwnerMobileNumber" : "7896547854",
        "documentId" : "1",
        "documentName" : "docName",
        "documentType" : "sampleDoc",
        "documentStatus" : "Status",
        "documentCriteria" : "documentCriteria",
        "documentDetails" : "Details",
        "policyId" : "1",
        "policyName" : "policyName1",
        "last_update_date": "2023-10-21T11:24:13",
        "DueDate": "2023-10-21T11:24:13"
    }
}

]

# # Set up logging for responses
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create loggers
logger_responses = logging.getLogger('govtPolicy_responses')
logger_results = logging.getLogger('govtPolicy_results')

# Create handlers for the loggers
handler_responses = logging.FileHandler('govtPolicy_responses.log')
handler_results = logging.FileHandler('govtPolicy_results.log')

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


# Process responses and log to api_result.log
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

