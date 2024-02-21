
import requests, json
import logging
from datetime import datetime

BASE_URL = 'http://65.0.225.117/'
ENDPOINT = 'k2kapi/myFinance/'

api_data = [
    {
   "operation":"createBudget",
   "user":{
      "profileId":"1",
      "note":"this is note",
      "date":"03-10-2023 01:02:30 Wednesday",
      "primaryFunction":"NA",
      "secondaryFunction":"Owner",
      "amountType":"Expenses",
      "amountTypeFunction":"General",
      "amount":"11200"
   }
},
{ 
 "operation" : "getBudgetDetials",
 "profileId":"1"
},
{
   "operation":"updateBudget",
   "user":{ 
       "transactionId":"4",
      "profileId":"2",
      "note":"NA",
      "date":"16-10-2023 12:02:30 monday",
      "primaryFunction":"NA",
      "secondaryFunction":"Owner",
      "amountType":"Expenses",
      "amountTypeFunction":"General",
      "amount":"1000"
   }
},
{ 
   "operation":"deleteBudget",
   "user":{ "transactionId":"1" }
}
]

# # Set up logging for responses
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create loggers
logger_responses = logging.getLogger('budget_responses')
logger_results = logging.getLogger('budget_results')

# Create handlers for the loggers
handler_responses = logging.FileHandler('budget_responses.log')
handler_results = logging.FileHandler('budget_results.log')

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

