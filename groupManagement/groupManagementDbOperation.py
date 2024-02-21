from django.db import connection
from datetime import datetime
from django.http import JsonResponse

def getUserGroups_db(groupId):
    try:
        cursor = connection.cursor()

        query = """SELECT DISTINCT
                    d1.id::text AS id,
                    d1.profileid,
                    d1.activitysequence,
                    d1.activityname,
                    d1.activitynamelocal,
                    d1.activityexpectedindays,
                    d1.needhelp,
                    d1.expenses,
                    d1.doneorskip,
                    TO_CHAR(d1.activityexpectedstartdate, 'DD-MM-YY HH24:MI:SS D') AS activityexpectedstartdate,
                    TO_CHAR(d1.activitycompleteddate, 'DD-MM-YY HH24:MI:SS D') AS activitycompleteddate,
                    TO_CHAR(d1.activityrescheduleddate, 'DD-MM-YY HH24:MI:SS D') AS activityrescheduleddate,
                    t1.memberFirstName,
                    t1.memberLastName,
                    t1.groupName,
                    t1.groupId,
                    d1.id
                FROM d_farmercropschedule d1
                JOIN d_member t1 ON t1.memberProfileId = d1.profileid
                WHERE
                    t1.groupId = %s
                    AND d1.activityexpectedstartdate BETWEEN (CURRENT_TIMESTAMP - interval '5 days') AND (CURRENT_TIMESTAMP + interval '25 days')
                ORDER BY d1.id ASC;
                """

        cursor.execute(query,(groupId,))

        response = cursor.fetchall()
        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})





