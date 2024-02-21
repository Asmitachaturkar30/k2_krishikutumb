
import requests, json
import logging
from datetime import datetime

BASE_URL = 'http://65.0.225.117/'
ENDPOINT = 'k2kapi/manageProfile/'

api_data = [
  {
    "operation": "createProfile",
    "user": {
      "firstName": "मोहन-परीक्षा1",
      "lastName": "मोहन-उपयोगकर्ता1",
      "mobileNumber": "7005800290",
      "village": "Bhadugaon",
      "tehsil": "Rehatgaon",
      "district": "Harda",
      "state": "Madhya Pradesh"
    }
  },
  {
    "operation": "getProfile",
    "mobileNumber": "7005800290"
  },
  {
    "operation": "createMultipleProfile",
    "user": [
      {
        "profileId": "10",
        "priSecId": "3",
        "firstName": "मोहन-परीक्षा1",
        "lastName": "मोहन-उपयोगकर्ता1",
        "mobileNumber": "7897894567",
        "primaryFunction": "Machine13",
        "secondaryFunction": "Machine13",
        "functionUnit": "NA-Flut",
        "volume": "100",
        "minimumRequirement": "10",
        "village": "Bhadugaon",
        "tehsil": "Rehatgaon",
        "district": "Harda",
        "state": "Madhya Pradesh"
      },
      {
        "profileId": "11",
        "priSecId": "2",
        "firstName": "मोहन-परीक्षा1",
        "lastName": "मोहन-उपयोगकर्ता1",
        "mobileNumber": "998866557",
        "primaryFunction": "Farmer24",
        "secondaryFunction": "Farme24r",
        "functionUnit": "NA-Flut",
        "volume": "100",
        "minimumRequirement": "10",
        "village": "Bhadugaon",
        "tehsil": "Rehatgaon",
        "district": "Harda",
        "state": "Madhya Pradesh"
      }
    ]
  },
  {
    "operation": "getUserData",
    "mobileNumber": "9981733901"
  },
  {
    "operation": "createTertiaryProfile",
    "user": {
      "priSecId": "1",
      "profileId": "1",
      "firstName": "John",
      "lastName": "Doe",
      "mobileNumber": "9955667710",
      "tertiaryFunction": "Tertiary Function40",
      "fourthFunction": "Fourth Function",
      "tertiaryFunctionVariety": "Variety 21",
      "fourthFunctionVariety": "Variety 22",
      "functionUnit": "Function Unit",
      "volume": 100,
      "minimumRequirement": 50,
      "village": "Bhadugaon",
      "tehsil": "Rehatgaon",
      "district": "Harda",
      "state": "Madhya Pradesh"
    }
  },
  {
    "operation": "getContacts",
    "mobileNumber": "9981733901",
    "primaryFunction": "Machine",
    "secondaryFunction": "Cultivator",
    "village": "Bhadugaon",
    "tehsil": "Rehatgaon"
  },
  {
    "operation": "deleteProfile",
    "user": {
      "mobileNumber": "7897894567",
      "primaryFunction": "Machine13",
      "secondaryFunction": "Machine13"
    }
  },
  {
    "operation": "updateProfile",
    "user": {
      "firstName": "मोहन-परीक्षा1",
      "lastName": "मोहन-उपयोगकर्ता1",
      "mobileNumber": "7005800290",
      "village": "Bhadugaon",
      "tehsil": "Rehatgaon",
      "district": "Harda",
      "state": "Madhya Pradesh"
    }
  }
]


# # Set up logging for responses
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create loggers
logger_responses = logging.getLogger('ManageProfile_responses')
logger_results = logging.getLogger('ManageProfile_results')

# Create handlers for the loggers
handler_responses = logging.FileHandler('ManageProfile_responses.log')
handler_results = logging.FileHandler('ManageProfile_results.log')

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

