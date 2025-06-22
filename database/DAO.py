from database.DB_connect import DBConnect
from model.pilota import Pilota


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_years():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT(year) as anno FROM seasons"""
            cursor.execute(query)

            for row in cursor:
                result.append(row['anno'])

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_nodes(year:int):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct r.driverId, surname
                        from results r , drivers d
                        where r.driverId=d.driverId
                        and r.raceId in (select raceId 
                                        from races 
                                        where  year= %s)
                        and r.position is not null"""
            cursor.execute(query, (year, ))
            for row in cursor:
                result.append(Pilota(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getVittorie(year: int, d1 :int , d2: int):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select count(distinct r1.raceId) as vittorie
                    from results r1, results r2
                    where r1.driverId= %s and r2.driverId = %s
                    and r1.position is not null and r2.`position` is not null 
                    and r1.position < r2.`position` and
                    r1.raceId in (select raceId 
                                    from races 
                                    where  year=%s)
                    and r2.raceId =r1.raceId"""
            cursor.execute(query, (d1, d2, year))
            for row in cursor:
                result.append(row['vittorie'])

            cursor.close()
            cnx.close()
        return result[0]
