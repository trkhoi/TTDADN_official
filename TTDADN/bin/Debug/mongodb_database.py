import pymongo
from datetime import datetime
from collections import OrderedDict



class MyDatabase():
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://admin:Gociuss823434@dadn-mg0ho.mongodb.net/<dbname>?retryWrites=true&w=majority")
        self.db = self.client.mydb

    def insert_temp_humid(self, temperature, humid):
        self.db.temp_humid.insert_one(
            {
                'temperature': temperature,
                'humid': humid,
                'time': datetime.now()
            }
        )

    def insert_light(self, light):
        self.db.light.insert_one(
            {
                'light': light,
                'time': datetime.now()
            }
        )

    def get_day_report(self, day,month,year,device):
        date = datetime(year,month,day).date().isoformat()
        if(device == 'temp_humid'):
            coll = self.db.temp_humid
        elif (device == 'light'):
            coll = self.db.light
        else:
            assert False
        if(device == 'temp_humid'):
            pipeline = [
                {'$addFields': {'timePart': {'$dateToString': {"format": "%Y-%m-%d", "date": "$time" }}}},
                {"$match": {"timePart": date}},
                {'$project': {'time' : 1, 'temperature' : 1, 'humid' : 1, '_id' : 0}},
                {"$sort": OrderedDict([("time", 1)])}
            ]
        else:
            pipeline = [
                {'$addFields': {'timePart': {'$dateToString': {"format": "%Y-%m-%d", "date": "$time"}}}},
                {"$match": {"timePart": date}},
                {'$project': {'time': 1, 'light': 1, '_id' : 0}},
                {"$sort": OrderedDict([("time", 1)])}
            ]
        return list(coll.aggregate(pipeline))

    def get_month_report(self, month,year,device):
        date = datetime(year, month, 1).date().isoformat()
        month = date[:7]
        if (device == 'temp_humid'):
            coll = self.db.temp_humid
        elif (device == 'light'):
            coll = self.db.light
        else:
            assert False
        if (device == 'temp_humid'):
            pipeline = [
                {'$addFields': {'month': {'$dateToString': {"format": "%Y-%m", "date": "$time"}}}},
                {'$addFields': {'day': {'$dateToString': {"format": "%Y-%m-%d", "date": "$time"}}}},
                {"$match": {"month": month}},
                {"$group": {"_id": "$day", "day_temp": {"$avg": "$temperature"}, "day_humid": {"$avg": "$humid"}}},
                {'$addFields': {'date': '$_id'}},
                {'$project': {'_id' : 0, 'date': 1, 'day_temp': 1, 'day_humid': 1}},
                {"$sort": OrderedDict([("date", 1)])}
            ]
        else:
            pipeline = [
                {'$addFields': {'month': {'$dateToString': {"format": "%Y-%m", "date": "$time"}}}},
                {'$addFields': {'day': {'$dateToString': {"format": "%Y-%m-%d", "date": "$time"}}}},
                {"$match": {"month": month}},
                {"$group": {"_id": "$day", "day_light": {"$avg": "$light"}}},
                {'$addFields': {'date': '$_id'}},
                {'$project': {'_id': 0, 'date': 1, 'day_light': 1}},
                {"$sort": OrderedDict([("date", 1)])}
            ]
        return list(coll.aggregate(pipeline))

    def get_week_report(self, week,year,device):
        weekiso = str(year) + '-' + str(week)
        if (device == 'temp_humid'):
            coll = self.db.temp_humid
        elif (device == 'light'):
            coll = self.db.light
        else:
            assert False
        if (device == 'temp_humid'):
            pipeline = [
                {'$addFields': {'week': {'$dateToString': {"format": "%Y-%V", "date": "$time"}}}},
                {'$addFields': {'day': {'$dateToString': {"format": "%Y-%m-%d", "date": "$time"}}}},
                {"$match": {"week": weekiso}},
                {"$group": {"_id": "$day", "day_temp": {"$avg": "$temperature"}, "day_humid": {"$avg": "$humid"}}},
                {'$addFields': {'date': '$_id'}},
                {'$project': {'_id' : 0, 'date': 1, 'day_temp': 1, 'day_humid': 1}},
                {"$sort": OrderedDict([("date", 1)])}
            ]
        else:
            pipeline = [
                {'$addFields': {'week': {'$dateToString': {"format": "%Y-%V", "date": "$time"}}}},
                {'$addFields': {'day': {'$dateToString': {"format": "%Y-%m-%d", "date": "$time"}}}},
                {"$match": {"week": weekiso}},
                {"$group": {"_id": "$day", "day_light": {"$avg": "$light"}}},
                {'$addFields': {'date': '$_id'}},
                {'$project': {'_id': 0, 'date': 1, 'day_light': 1}},
                {"$sort": OrderedDict([("date", 1)])}
            ]
        return list(coll.aggregate(pipeline))

if __name__ == "__main__":
	a = MyDatabase()
	print(a.get_day_report(14,6,2020,'light'))
	print(a.get_week_report(24,2020,'light'))
	print(a.get_month_report(6,2020,'light'))