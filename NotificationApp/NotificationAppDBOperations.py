import json
from django.db import connection
from datetime import datetime
from django.http import JsonResponse

def createDevice_db(profileId, mobileNumber, deviceToken, Notes, Description):
    try:
        cursor = connection.cursor()

        # Check if the device with the given profileId already exists
        cursor.execute("SELECT * FROM d_devicenotification WHERE profileId = %s", (profileId,))
        existing_device = cursor.fetchone()

        if existing_device:
            # Update the existing device token
            sql = """
            UPDATE d_devicenotification 
            SET token = %s 
            WHERE profileId = %s
            """
            cursor.execute(sql, (deviceToken, profileId))
            connection.commit()
            return {'result': 'success', 'message': 'Device updated successfully'}
        else:
            # Create a new device
            sql = """
            INSERT INTO d_devicenotification (profileId, mobileNumber, token, Notes, Description)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (profileId, mobileNumber, deviceToken, Notes, Description))
            connection.commit()

            return {'result': 'success', 'message': 'Device created successfully'}

    except Exception as e:
        # Handle specific exceptions, log the error, and consider rolling back the transaction
        return {'result': 'failure', 'message': f'An error occurred: {str(e)}'}

    finally:
        cursor.close()



#---------------------------------------------------------------------------------------------


def getUserNotification_db(profileId):
    try:
        cursor = connection.cursor()
        query = """SELECT
    CAST(notification_id AS VARCHAR) AS notification_id,
    profileId,
    userId,
    notification_text,
    notification_type,
    is_read
FROM d_notifications
WHERE profileId = %s;
"""

        cursor.execute(query, (profileId,))
        response = cursor.fetchall()

        cursor.close()  # Close the cursor here, not the connection

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database operations: {str(e)}'})