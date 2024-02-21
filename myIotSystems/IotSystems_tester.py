import requests, json
import logging
from datetime import datetime

BASE_URL = 'http://65.0.225.117/'
ENDPOINT = 'k2kapi/myIotSystems/'

api_data = [
    {
   "operation":"createIOTWorkingData",
   "user":{
      "deviceId":"3",
      "profileId":"8",
      "deviceConfig1ParaName":"NA1",
      "deviceConfig1ParaValue":"NA1",
      "deviceConfig2ParaName":"NA1",
      "deviceConfig2ParaValue":"NA1",
      "deviceConfig3ParaName":"NA1",
      "deviceConfig3ParaValue":"NA1",
      "deviceConfig4ParaName":"NA1",
      "deviceConfig4ParaValue":"NA1",
      "deviceConfig5ParaName":"NA1",
      "deviceConfig5ParaValue":"NA1"
   }
},
{
   "operation":"createIOTDevice",
   "user":{
      "profileId":"63",
      "deviceRegisteredNumber":"8989754789",
      "deviceName":"mob1",
      "deviceType":"mob1",
      "deviceVendor":"NA1",
      "deviceTypeAgriculture":"starter",
      "deviceStatus":"on",
      "deviceConfig1ParaName":"NA",
      "deviceConfig1ParaValue1":"NA",
      "deviceConfig1ParaValue2":"NA",
      "deviceConfig1ParaValue3":"NA",
      "deviceConfig2ParaName":"NA",
      "deviceConfig2ParaValue1":"NA",
      "deviceConfig2ParaValue2":"NA",
      "deviceConfig2ParaValue3":"NA",
      "deviceConfig3ParaName":"NA",
      "deviceConfig3ParaValue1":"NA",
      "deviceConfig3ParaValue2":"NA",
      "deviceConfig3ParaValue3":"NA",
      "deviceConfig4ParaName":"NA",
      "deviceConfig4ParaValue1":"NA",
      "deviceConfig4ParaValue2":"NA",
      "deviceConfig4ParaValue3":"NA",
      "deviceConfig5ParaName":"NA",
      "deviceConfig5ParaValue1":"NA",
      "deviceConfig5ParaValue2":"NA",
      "deviceConfig5ParaValue3":"NA"
   }
},
{	
	"operation" : "getMobileIOTDetails",
	"profileId":"63"
},
{	
	"operation" : "getMobileIOTWorkingHistory",
	"profileId":"8",
	"deviceId":"3"
}

]

# # Set up logging for responses
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create loggers
logger_responses = logging.getLogger('IotSystem_response')
logger_results = logging.getLogger('IotSystem_results')

# Create handlers for the loggers
handler_responses = logging.FileHandler('IotSystem_response.log')
handler_results = logging.FileHandler('IotSystem_results.log')

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

