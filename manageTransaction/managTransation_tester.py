
import requests, json
import logging
from datetime import datetime

BASE_URL = 'http://65.0.225.117/'
ENDPOINT = 'k2kapi/manageTransaction/'

api_data = [
  {
 "operation" : "getContacts",
 "mobileNumber":"9981733901",
 "primaryFunction":"Machine",
 "secondaryFunction":"Cultivator",
 "village":"Bhadugaon",
 "tehsil":"Rehatgaon"
},
{
   "operation":"doBooking",
   "user":{
      "consumerMobileNumber":"8547854741",
      "providerMobileNumber":"8547854741",
      "bookingType":"New",
      "isBookingExpired":"No",
      "bookingStatus":"New",
      "bookingPrimaryFunction":"Machines",
      "bookingSecondaryFunction":"Tractor",
      "bookingTertiaryFunction":"NA",
      "bookingTertiaryFunctionVarity":"Tractor",
      "bookingFourthFunction":"NA",
      "bookingFourthFunctionVarity":"Tractor",
      "bookingInUnit":"NA",
      "bookingDate":"23-08-2023 19:30:00 Wednesday",
      "bookingNote":"TestOnly",
      "village":"Bhadugaon",
      "tehsil":"Rehatgaon",
      "district":"Harda",
      "state":"Madhya Pradesh"
   }
},
{	"operation" : "getBooking",
	"providerMobileNumber" : "8547854741",
	"bookingPrimaryFunction" : "Machines",
	"bookingSecondaryFunction" : "Tractor",
	"bookingTertiaryFunction" : "NA"
},
{
   "operation":"registerAvailabilityDemand",
   "user":{
      "mobileNumber":"9981733903",
      "demandType":"Demand",
      "demandPrimaryFunction":"Machine",
      "demandSecondaryFunction":"Tractor",
      "demandTertiaryFunction":"Demand",
      "demandTertiaryFunctionVarity":"Machine",
      "demandFourthFunction":"Tractor",
      "demandFourthFunctionVarity":"Demand",
      "demandInUnit":"Tons",
      "demandDate":"23-08-2023 19:30:00 Wednesday",
      "demandNote":"10 tons",
      "village":"Bhadugaon",
      "tehsil":"Rehatgaon",
      "district":"Harda",
      "state":"Madhya Pradesh"
   }
},
{
 "operation" : "getTertiaryContacts",
  "primaryFunction": "Machines",
  "secondaryFunction": "Tractor",
  "tertiaryFunction": "NA",
  "tertiaryFunctionVariety": "Tractor",
  "fourthFunction": "NA",
  "fourthFunctionVariety": "Tractor",
  "village":"Bhadugaon",
  "tehsil":"Rehatgaon"
}


]


# # Set up logging for responses
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create loggers
logger_responses = logging.getLogger('transation_responses')
logger_results = logging.getLogger('transation_results')

# Create handlers for the loggers
handler_responses = logging.FileHandler('transation_responses.log')
handler_results = logging.FileHandler('transation_results.log')

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

