from database.DB_connect import DBConnect
from model.locazioni import Locazione

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getProvider():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct Provider 
                    from nyc_wifi_hotspot_locations"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['Provider'])
        cursor.close()
        conn.close()
        return sorted(result)

    @staticmethod
    def getLocation(provider):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select Location , Latitude , Longitude
                    from nyc_wifi_hotspot_locations nwhl 
                    where nwhl.Provider =%s 
                    group by Location """
        cursor.execute(query,(provider,))
        for row in cursor:
            result.append(Locazione(row['Location'],row['Latitude'],row['Longitude']))
        cursor.close()
        conn.close()
        return list(result)

