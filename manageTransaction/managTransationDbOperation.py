#!/usr/bin/python
from django.db import connection
from datetime import datetime
from django.http import JsonResponse
#------------------------------------------------------------------------------

def registerAvailabilityDemand_db(mobileNumber,demandType,demandPrimaryFunction,demandSecondaryFunction,demandTertiaryFunction,demandTertiaryFunctionVarity, demandFourthFunction,demandFourthFunctionVarity,demandInUnit,demandDate,demandNote,village,tehsil,district,state):
    try:

        cursor = connection.cursor()
        demandDate = datetime.strptime(demandDate, '%d-%m-%Y %H:%M:%S %A')      

        sql = """
        insert into d_demand (mobilenumber,demandtype,demandprimaryfunction,demandsecondaryfunction,demandtertiaryfunction,demandtertiaryfunctionvarity,
              demandfourthfunction,demandfourthfunctionvarity,demandinunit,demanddate,demandnote,village,tehsil,district,state)
              values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """
    
        cursor.execute(sql, (mobileNumber,demandType,demandPrimaryFunction,demandSecondaryFunction,demandTertiaryFunction,demandTertiaryFunctionVarity,
              demandFourthFunction,demandFourthFunctionVarity,demandInUnit,demandDate,demandNote,village,tehsil,district,state))
        connection.commit()
    
        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success','message': 'demand and availability is created successfully.'})
        else:
            return JsonResponse({'result': 'failure','message': 'demand and availability creation is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

#------------------------------------------------------------------------------

def doBooking_db(consumerMobileNumber, providerMobileNumber, bookingType, isBookingExpired, bookingStatus, bookingPrimaryFunction,
                 bookingSecondaryFunction, bookingTertiaryFunction, bookingTertiaryFunctionVarity, bookingFourthFunction,
                 bookingFourthFunctionVarity, bookingInUnit, bookingDate, bookingNote, village, tehsil, district, state):
    try:
        cursor = connection.cursor()

        # Parse the bookingDate string into a datetime object
        bookingDate = datetime.strptime(bookingDate, '%d-%m-%Y %H:%M:%S %A')

        sql = """
        INSERT INTO d_booking
        (consumermobilenumber, providermobilenumber, bookingtype, isbookingexpired, bookingstatus, bookingprimaryfunction,
         bookingsecondaryfunction, bookingtertiaryfunction, bookingtertiaryfunctionvarity, bookingfourthfunction,
         bookingfourthfunctionvarity, bookinginunit, bookingdate, bookingnote, village, tehsil, district, state)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (consumerMobileNumber, providerMobileNumber, bookingType, isBookingExpired, bookingStatus,
                            bookingPrimaryFunction, bookingSecondaryFunction, bookingTertiaryFunction,
                            bookingTertiaryFunctionVarity, bookingFourthFunction, bookingFourthFunctionVarity,
                            bookingInUnit, bookingDate, bookingNote, village, tehsil, district, state))
        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Booking is created successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Booking creation failed.'})

    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# --------------------------------------------------------------------------------------

def getBooking_db(providerMobileNumber, bookingPrimaryFunction, bookingSecondaryFunction, bookingTertiaryFunction):
    try:
        cursor = connection.cursor()


        # sql = """ select distinct cast(t1.mobilenumber as char) as mobilenumber, t1.firstname, t1.lastname, t1.village, t1.tehsil, 
        #         date_format(d1.bookingdate, '%%d-%%m-%%y %%h:%%i:%%s %%w') as last_updated_at, d1.bookingtype, d1.bookingstatus,
        #         date_format(d1.bookingdate, '%%d-%%m-%%y %%h:%%i:%%s %%w') as bookingdate, d1.bookingnote, d1.bookinginunit 
        #         from d_booking d1, d_userprofile t1
        #         where d1.providermobilenumber = %s and d1.bookingprimaryfunction = %s and d1.bookingsecondaryfunction = %s 
        #         and d1.bookingtertiaryfunction = %s and t1.mobilenumber = d1.consumermobilenumber; """
        sql=""" SELECT DISTINCT 
                CAST(t1.mobilenumber AS varchar) AS mobilenumber, 
                t1.firstname, 
                t1.lastname, 
                t1.village, 
                t1.tehsil, 
                TO_CHAR(d1.bookingdate, 'DD-MM-YY HH:MI:SS D') AS last_updated_at, 
                d1.bookingtype, 
                d1.bookingstatus, 
                TO_CHAR(d1.bookingdate, 'DD-MM-YY HH:MI:SS D') AS bookingdate, 
                d1.bookingnote, 
                d1.bookinginunit 
                FROM 
                    d_booking d1, 
                    d_userprofile t1
                WHERE 
                d1.providermobilenumber = %s 
                AND d1.bookingprimaryfunction = %s 
                AND d1.bookingsecondaryfunction = %s 
                AND d1.bookingtertiaryfunction = %s 
                AND t1.mobilenumber = d1.consumermobilenumber;
            """
        cursor.execute(sql, (providerMobileNumber, bookingPrimaryFunction, bookingSecondaryFunction, bookingTertiaryFunction))
        response = cursor.fetchall()

        cursor.close()
        connection.close()
        
        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -------------------------------------------------------------------------------------- 
# -----------------------------------------------------------------------------------

def getTertiaryContacts_db(primaryFunction, secondaryFunction, tertiaryFunction, tertiaryFunctionVariety, fourthFunction, fourthFunctionVariety, village, tehsil):
    # try:

        cursor = connection.cursor()

        sql="""SELECT DISTINCT CAST(t1.profileid AS varchar) AS profileId , t1.firstname, t1.lastname, t1.mobilenumber, t1.village, 
                        to_char(d1.demanddate, 'DD-MM-YY HH:MI:SS D') as last_updated_at,
                        '1' as priority, d1.demandtype as demandtype, d1.demandinunit as functionunit, 
                        d1.demandnote as description
                    FROM d_profiletertfourdata t1, d_demand d1 
                    WHERE d1.demandprimaryfunction = %s
                        AND d1.demandsecondaryfunction = %s 
                        AND d1.demandtertiaryfunction = %s 
                        AND d1.demandtertiaryfunctionvarity = %s
                        AND d1.demandfourthfunction = %s
                        AND d1.demandfourthfunctionvarity = %s
                        AND d1.mobilenumber = t1.mobilenumber 
                        AND d1.isdemandexpired IS NULL 
                        AND t1.village = %s 
                        AND t1.tehsil = %s
                    UNION ALL
                    SELECT DISTINCT CAST(t1.profileid AS varchar) AS profileId , t1.firstname, t1.lastname, t1.mobilenumber, t1.village, 
                        to_char(t1.last_updated_at, 'DD-MM-YY HH:MI:SS D') as last_updated_at,
                        '2' as priority, 'Available' as demandtype, t1.funtionunit as functionunit, 
                        t1.minimumrequirement as description
                    FROM d_profiletertfourdata t1 
                    JOIN r_primarysecondaryfunctions t2 ON t1.prisecid = t2.prisecid
                    WHERE t2.primaryfunction = %s
                        AND t2.secondaryfunction = %s
                        AND t1.tertiaryfunction = %s  
                        AND t1.tertiaryfunctionvariety = %s
                        AND t1.fourthfunction = %s
                        AND t1.fourthfunctionvariety = %s
                        AND t1.village = %s
                        AND t1.tehsil = %s
                        AND t1.mobilenumber NOT IN (
                            SELECT DISTINCT d2.mobilenumber
                            FROM d_demand d2
                            WHERE d2.demandprimaryfunction = %s
                                AND d2.demandsecondaryfunction = %s
                                AND d2.demandtertiaryfunction = %s
                                AND d2.demandtertiaryfunctionvarity = %s
                                AND d2.demandfourthfunction = %s
                                AND d2.demandfourthfunctionvarity = %s
                                AND d2.isdemandexpired IS NULL
                                AND d2.demandtype = 'Available'
                        ) 
                    ORDER BY priority, last_updated_at DESC;
                    """
        cursor.execute(sql, (
            primaryFunction, secondaryFunction, tertiaryFunction, tertiaryFunctionVariety, fourthFunction, fourthFunctionVariety,
            village, tehsil,
            primaryFunction, secondaryFunction, tertiaryFunction, tertiaryFunctionVariety, fourthFunction, fourthFunctionVariety,
            village, tehsil,
            primaryFunction, secondaryFunction, tertiaryFunction, tertiaryFunctionVariety, fourthFunction, fourthFunctionVariety
        ))

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        if response:
            return response  
        else:
            return None
    # except Exception as e:
    #     return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

def getContacts_db(mobileNumber, primaryFunction, secondaryFunction, village, tehsil):
    try:

        cursor = connection.cursor()

        sql = """SELECT DISTINCT CAST(t1.profileid AS varchar) AS profileId ,t1.firstname,t1.lastname,t1.mobilenumber,t1.village,
                TO_CHAR(d1.demanddate, 'DD-MM-YY HH:MI:SS D') AS last_updated_at,'1' AS priority,d1.demandtype AS demandtype
                FROM
                    d_profileprisecdata t1
                JOIN
                    d_demand d1
                ON
                    d1.demandprimaryfunction = %s
                    AND d1.demandsecondaryfunction = %s
                    AND d1.mobilenumber = t1.mobilenumber
                    AND d1.isdemandexpired IS NULL
                    AND t1.village = %s
                    AND t1.tehsil = %s
                UNION ALL
                SELECT DISTINCT CAST(t1.profileid AS varchar) AS profileId ,t1.firstname,t1.lastname,t1.mobilenumber,t1.village,
                TO_CHAR(t1.last_updated_at, 'DD-MM-YY HH:MI:SS D') AS last_updated_at,'2' AS priority,'Available' AS demandtype
                FROM
                    d_profileprisecdata t1
                WHERE t1.primaryfunction = %s
                AND t1.secondaryfunction = %s
                AND t1.mobilenumber NOT IN (
                    SELECT DISTINCT mobilenumber FROM d_demand
                    WHERE
                        demandprimaryfunction = %s
                        AND demandsecondaryfunction = %s
                        AND isdemandexpired IS NULL
                        AND demandtype = 'Available'
                )
                AND t1.village = %s
                AND t1.tehsil = %s
                ORDER BY priority,last_updated_at DESC;"""

        cursor.execute(sql, (primaryFunction,secondaryFunction,village,tehsil,primaryFunction,secondaryFunction,primaryFunction,secondaryFunction,village,tehsil))

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
    
# -----------------------------------------------------------------------------------

def createDevice_db(profileId, mobileNumber, Notes, Description):
    try:
        cursor = connection.cursor()

        sql = """
        insert into d_devicenotification (profileId, mobileNumber, Notes, Description)
        values (%s, %s, %s, %s)"""
        values = ( profileId, mobileNumber, Notes, Description)
    
        cursor.execute(sql, values)

        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Device is create successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Device create is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

# -----------------------------------------------------------------------------------

def getDeviceDetails_db(profileId, mobileNumber):
    try:
        cursor = connection.cursor()
        query = """SELECT DISTINCT CAST(deviceId AS varchar) AS deviceId, profileId, mobileNumber, Token, Notes, Description
                    FROM d_devicenotification
                    WHERE profileId = %s AND 
						  mobileNumber = %s;
						  
				"""

        cursor.execute(query,(profileId, mobileNumber))

        response = cursor.fetchall()
        cursor.close()
        connection.close()
        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

#---------------------------------------------------------------------------

def UpdateBooking_db(bookingId,bookingType,isBookingExpired,bookingStatus,
                                    bookingInUnit,bookingDate,bookingNote):
    # Inside UpdateBooking_db function
    try:
        cursor = connection.cursor()

        sql = """
            UPDATE d_booking
            SET bookingType = %s,
                isBookingExpired = %s,
                bookingStatus = %s,
                bookingInUnit = %s,
                bookingDate = TO_TIMESTAMP(%s, 'DD-MM-YYYY HH24:MI:SS Day'),
                bookingNote = %s
            WHERE booking_id = %s;
        """

        cursor.execute(sql, (
            bookingType, isBookingExpired, bookingStatus, bookingInUnit, bookingDate,
            bookingNote, bookingId
        ))

        connection.commit()

        if cursor.rowcount > 0:
            return {'result': 'success', 'message': 'Booking is updated successfully.'}
        else:
            return {'result': 'failure', 'message': 'Booking updation is failed.'}
    except Exception as e:
        return {'result': 'failure', 'message': f'An error occurred during database operations: {str(e)}'}
    finally:
        cursor.close()

#------------------------------------------------------------------------------

def doBookingNotific_db(consumerMobileNumber, providerMobileNumber, bookingType, isBookingExpired, bookingStatus, bookingPrimaryFunction,
                 bookingSecondaryFunction, bookingTertiaryFunction, bookingTertiaryFunctionVarity, bookingFourthFunction,
                 bookingFourthFunctionVarity, bookingInUnit, bookingDate, bookingNote, village, tehsil, district, state,providerToken):
    try:
        cursor = connection.cursor()

        # Parse the bookingDate string into a datetime object
        bookingDate = datetime.strptime(bookingDate, '%d-%m-%Y %H:%M:%S %A')

        sql = """
        INSERT INTO d_booking
        (consumermobilenumber, providermobilenumber, bookingtype, isbookingexpired, bookingstatus, bookingprimaryfunction,
         bookingsecondaryfunction, bookingtertiaryfunction, bookingtertiaryfunctionvarity, bookingfourthfunction,
         bookingfourthfunctionvarity, bookinginunit, bookingdate, bookingnote, village, tehsil, district, state)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (consumerMobileNumber, providerMobileNumber, bookingType, isBookingExpired, bookingStatus,
                            bookingPrimaryFunction, bookingSecondaryFunction, bookingTertiaryFunction,
                            bookingTertiaryFunctionVarity, bookingFourthFunction, bookingFourthFunctionVarity,
                            bookingInUnit, bookingDate, bookingNote, village, tehsil, district, state))
        connection.commit()

        if cursor.rowcount > 0:
            return ({'result': 'success', 'message': 'Booking is created successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Booking creation failed.'})

    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# --------------------------------------------------------------------------------------



# def getContactsNearby_db(mobileNumber, primaryFunction, secondaryFunction, village, tehsil, nearbyRange):
#     try:

#         cursor = connection.cursor()

        # sql = """SELECT DISTINCT CAST(t1.profileid AS varchar) AS profileId ,t1.firstname,t1.lastname,t1.mobilenumber,t1.village,
        #         TO_CHAR(t1.last_updated_at, 'DD-MM-YY HH:MI:SS D') AS last_updated_at,'2' AS priority,'available' AS demandtype
        #         FROM
        #             d_profileprisecdata t1
        #         WHERE t1.primaryfunction = %s
        #         AND t1.secondaryfunction = %s
        #         AND t1.mobilenumber NOT IN (
        #             SELECT DISTINCT mobilenumber FROM d_demand
        #             WHERE
        #                 demandprimaryfunction = %s
        #                 AND demandsecondaryfunction = %s
        #                 AND isdemandexpired IS NULL
        #                 AND demandtype = 'available'
        #         )
        #         AND t1.village = %s
        #         AND t1.tehsil = %s
        #         ORDER BY priority,last_updated_at DESC;


        #         WHERE 
        #             t1.primaryfunction = %s
        #             AND t1.secondaryfunction = %s
        #             AND t1.mobilenumber NOT IN (
        #             SELECT DISTINCT mobilenumber FROM d_demand
        #             WHERE
        #                 demandprimaryfunction = %s
        #                 AND demandsecondaryfunction = %s
        #                 AND isdemandexpired IS NULL
        #                 AND demandtype = 'available'
        #         )
		# 			AND ST_DWithin(
        #                         geom,
        #                         (SELECT geom FROM d_profileprisecdata WHERE village = %s LIMIT 1),
        #                         %s * 1000::integer
        #                     )
        #         ORDER BY 
        #             priority, 
        #             last_updated_at DESC;"""
        # cursor.execute(sql, (primaryFunction,secondaryFunction,village,tehsil,primaryFunction,
        #                      secondaryFunction,primaryFunction,secondaryFunction,village,nearbyRange))


    #     sql = """SELECT DISTINCT CAST(t1.profileid AS varchar) AS profileId ,t1.firstname,t1.lastname,t1.mobilenumber,t1.village,
    #             TO_CHAR(d1.demanddate, 'DD-MM-YY HH:MI:SS D') AS last_updated_at,'1' AS priority,d1.demandtype AS demandtype,distance
    #             FROM
    #                 d_profileprisecdata t1
    #             JOIN
    #                 d_demand d1
    #             ON
    #                 d1.demandprimaryfunction = %s
    #                 AND d1.demandsecondaryfunction = %s
    #                 AND d1.mobilenumber = t1.mobilenumber
    #                 AND d1.isdemandexpired IS NULL
    #                 AND t1.village = %s
    #                 AND t1.tehsil = %s
    #             UNION ALL
    #             SELECT DISTINCT CAST(t1.profileid AS varchar) AS profileId ,t1.firstname,t1.lastname,t1.mobilenumber,t1.village,
    #             TO_CHAR(t1.last_updated_at, 'DD-MM-YY HH:MI:SS D') AS last_updated_at,'2' AS priority,'Available' AS demandtype,

    #             FROM
    #                 d_profileprisecdata t1
    #             WHERE 
    #                 t1.primaryfunction = %s
    #                 AND t1.secondaryfunction = %s
    #                 AND t1.mobilenumber NOT IN (
    #                 SELECT DISTINCT mobilenumber FROM d_demand
    #                 WHERE
    #                     demandprimaryfunction = %s
    #                     AND demandsecondaryfunction = %s
    #                     AND isdemandexpired IS NULL
    #                     AND demandtype = 'available'
    #             )
	# 				AND ST_DWithin(
    #                             geom,
    #                             (SELECT geom FROM d_profileprisecdata WHERE village = %s LIMIT 1),
    #                             %s * 1000::integer
    #                         )
    #             ORDER BY 
    #                 priority, 
    #                 last_updated_at DESC;"""


    #     cursor.execute(sql, (primaryFunction,secondaryFunction,village,tehsil,primaryFunction,
    #                          secondaryFunction,primaryFunction,secondaryFunction,village,nearbyRange))

    #     response = cursor.fetchall()

    #     cursor.close()
    #     connection.close()

    #     if response:
    #         return response
    #     else:
    #         return None
    # except Exception as e:
    #     return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
    
# def getContactsNearby_db(mobileNumber, primaryFunction, secondaryFunction, village, tehsil, nearbyRange):
#     try:
#         cursor = connection.cursor()

        # sql = """SELECT DISTINCT
        #             CAST(t1.profileid AS varchar) AS profileId,
        #             t1.firstname,
        #             t1.lastname,
        #             t1.mobilenumber,
        #             t1.village,
        #             TO_CHAR(d1.demanddate, 'DD-MM-YY HH:MI:SS D') AS last_updated_at,
        #             '1' AS priority,
        #             d1.demandtype AS demandtype,
        #             ST_Distance(
        #                 ST_DWithin(
        #                     t1.geom,
        #                     (SELECT geom FROM d_profileprisecdata WHERE village = %s LIMIT 1),
        #                     %s * 1000::integer
        #                 )
        #             ) / 1000 AS distance
        #         FROM
        #             d_profileprisecdata t1
        #         JOIN
        #             d_demand d1
        #         ON
        #             d1.demandprimaryfunction = %s
        #             AND d1.demandsecondaryfunction = %s
        #             AND d1.mobilenumber = t1.mobilenumber
        #             AND d1.isdemandexpired IS NULL
        #             AND t1.village = %s
        #             AND t1.tehsil = %s
        #         UNION ALL
        #         SELECT DISTINCT
        #             CAST(t1.profileid AS varchar) AS profileId,
        #             t1.firstname,
        #             t1.lastname,
        #             t1.mobilenumber,
        #             t1.village,
        #             TO_CHAR(t1.last_updated_at, 'DD-MM-YY HH:MI:SS D') AS last_updated_at,
        #             '2' AS priority,
        #             'Available' AS demandtype,
        #             ST_Distance(
        #                 ST_DWithin(
        #                     t1.geom,
        #                     (SELECT geom FROM d_profileprisecdata WHERE village = %s LIMIT 1),
        #                     %s * 1000::integer
        #                 )
        #             ) / 1000 AS distance
        #         FROM
        #             d_profileprisecdata t1
        #         WHERE 
        #             t1.primaryfunction = %s
        #             AND t1.secondaryfunction = %s
        #             AND t1.mobilenumber NOT IN (
        #                 SELECT DISTINCT mobilenumber FROM d_demand
        #                 WHERE
        #                     demandprimaryfunction = %s
        #                     AND demandsecondaryfunction = %s
        #                     AND isdemandexpired IS NULL
        #                     AND demandtype = 'available'
        #             )
        #         AND ST_DWithin(
        #             t1.geom,
        #             (SELECT geom FROM d_profileprisecdata WHERE village = %s LIMIT 1),
        #             %s * 1000::integer
        #         )
        #         ORDER BY 
        #             priority, 
        #             last_updated_at DESC;"""

        # cursor.execute(sql, (
        #     village, nearbyRange,  # For the first ST_DWithin clause
        #     primaryFunction, secondaryFunction, village, tehsil,  # For the first part of the query
        #     village, nearbyRange,  # For the second ST_DWithin clause
        #     primaryFunction, secondaryFunction,  # For the second part of the query
        #     primaryFunction, secondaryFunction,  # For the subquery
        #     village, nearbyRange  # For the subquery
        # ))

#         response = cursor.fetchall()

#         cursor.close()
#         connection.close()

#         if response:
#             return response
#         else:
#             return None
#     except Exception as e:
#         return JsonResponse({'result': 'failure', 'message': f'An error occurred during database operations: {str(e)}'})


def getContactsNearby_db(mobileNumber, primaryFunction, secondaryFunction, village, tehsil, nearbyRange, 
                         latitude, longitude):
    # try:
        cursor = connection.cursor()
        villageGeom = f"POINT({longitude} {latitude})"
        print(villageGeom)
        sql = """ SELECT
                        CAST(t1.profileid AS varchar) AS profileId,t1.firstname,t1.lastname,t1.mobilenumber,t1.village,
                        TO_CHAR(d1.demanddate, 'DD-MM-YY HH:MI:SS D') AS last_updated_at,'1' AS priority,d1.demandtype AS demandtype,
                        ST_Distance(
                            t1.geom::geometry(Point, 4326),
                            %s::geometry(Point, 4326)
                        ) / 1000 AS distance

                    FROM
                        d_profileprisecdata t1
                        JOIN d_demand d1 ON d1.demandprimaryfunction = %s
                            AND d1.demandsecondaryfunction = %s
                            AND d1.mobilenumber = t1.mobilenumber
                            AND d1.isdemandexpired IS NULL
                            AND t1.village = %s
                            AND t1.tehsil = %s
                    UNION ALL
                    SELECT
                        CAST(t1.profileid AS varchar) AS profileId,t1.firstname,t1.lastname,t1.mobilenumber,t1.village,
                        TO_CHAR(t1.last_updated_at, 'DD-MM-YY HH:MI:SS D') AS last_updated_at,'2' AS priority,'Available' AS demandtype,
                        ST_Distance(
                            t1.geom::geometry(Point, 4326),
                            %s::geometry(Point, 4326)
                        ) / 1000 AS distance
                    FROM
                        d_profileprisecdata t1
                    WHERE
                        t1.primaryfunction = %s
                        AND t1.secondaryfunction = %s
                        AND t1.mobilenumber NOT IN (
                            SELECT DISTINCT mobilenumber
                            FROM d_demand
                            WHERE
                                demandprimaryfunction = %s
                                AND demandsecondaryfunction = %s
                                AND isdemandexpired IS NULL
                                AND demandtype = 'Available'
                        )
                        AND ST_DWithin(
                            t1.geom::geometry(Point, 4326),
                            %s::geometry(Point, 4326),
                            %s * 1000::integer
                        )
            ORDER BY distance, last_updated_at DESC NULLS LAST,priority;"""
        cursor.execute(sql, (villageGeom,primaryFunction, secondaryFunction, village, tehsil, villageGeom,primaryFunction, secondaryFunction, 
            primaryFunction, secondaryFunction,villageGeom, nearbyRange ))

        response = cursor.fetchall()
        print(response)
        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    # except Exception as e:
    #     return JsonResponse({'result': 'failure', 'message': f'An error occurred during database operations: {str(e)}'})
