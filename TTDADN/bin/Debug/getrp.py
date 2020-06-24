from mongodb_database import MyDatabase
import numpy as np
import matplotlib.pyplot as plt
import datetime
import argparse

def get_report_by_day(sensor, day, month, year):
    if sensor == "light":
        get_data_from_day = mydb.get_day_report(day,month,year,'light') ###Call from db
    else:
        get_data_from_day = mydb.get_day_report(day,month,year,'temp_humid')

    if sensor == "light":
        lights = []
        hours = []
        for item in get_data_from_day:
            t = item['time']
            temp = item['light']
            lights.append(temp)
            hours.append(t.hour + t.minute / 60 + t.second / 3600)
        lights = np.array(lights)
        hours = np.array(hours)
        hours = np.round(hours, 2)
        
        fig, ax = plt.subplots()
        ax.plot(hours, lights)
        
        title = "Statistic of light sensor at " + str(day) + "/" + str(month) + "/" + str(year)
        ax.set(xlabel='Hour', ylabel='Light', title=title)
        ax.set_xlim(0,24)
        fig.savefig("Light_Day_" + str(day) + "_" + str(month) + "_" + str(year) + ".png")
    elif sensor == "temp":
        lights = []
        hours = []
        for item in get_data_from_day:
            t = item['time']
            temp = item['temperature']
            lights.append(temp)
            hours.append(t.hour + t.minute / 60 + t.second / 3600)
        lights = np.array(lights)
        hours = np.array(hours)
        hours = np.round(hours, 2)
        
        fig, ax = plt.subplots()
        ax.plot(hours, lights)
        
        title = "Statistic of temperature sensor at " + str(day) + "/" + str(month) + "/" + str(year)
        ax.set(xlabel='Hour', ylabel='Temp', title=title)
        ax.set_xlim(0,24)
        fig.savefig("Temp_Day_" + str(day) + "_" + str(month) + "_" + str(year) + ".png")
    elif sensor == "humid":
        lights = []
        hours = []
        for item in get_data_from_day:
            t = item['time']
            temp = item['humid']
            lights.append(temp)
            hours.append(t.hour + t.minute / 60 + t.second / 3600)
        lights = np.array(lights)
        hours = np.array(hours)
        hours = np.round(hours, 2)
        
        fig, ax = plt.subplots()
        ax.plot(hours, lights)
        
        title = "Statistic of humid sensor at " + str(day) + "/" + str(month) + "/" + str(year)
        ax.set(xlabel='Hour', ylabel='Temp', title=title)
        ax.set_xlim(0,24)
        fig.savefig("Humid_Day_" + str(day) + "_" + str(month) + "_" + str(year) + ".png")

def get_report_by_week(sensor, week, year):
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    weekAvg = [0,0,0,0,0,0,0]

    first_day = datetime.datetime.strptime(str(year) + "-" + str(week-1) + "-1","%Y-%W-%w")
    last_day = datetime.datetime.strptime(str(year) + "-" + str(week-1) + "-0","%Y-%W-%w")

    first_str = str(first_day.day) + "/" + str(first_day.month) + "/" + str(first_day.year)
    last_str = str(last_day.day) + "/" + str(last_day.month) + "/" + str(last_day.year)

    x = np.arange(len(weekDays))  # the label locations
    width = 0.4  # the width of the bars

    if sensor == "light":
        get_data_from_week = mydb.get_week_report(week,year,'light') ###Call from db
    else:
        get_data_from_week = mydb.get_week_report(week,year,'temp_humid')

    if sensor == "light":
        for item in get_data_from_week:
            t_str = item['date']
            temp = item['day_light']
            date_class = datetime.datetime.strptime(t_str, "%Y-%m-%d")
            week_day = date_class.weekday()
            weekAvg[week_day] = temp
        fig, ax = plt.subplots()
        rects1 = ax.bar(x, weekAvg, width, label='light value')
        
        tilte = "Statistic of light sensor from " + first_str + " to " + last_str
        ax.set_ylabel('Light')
        ax.set_title(tilte)
        ax.set_xticks(x)
        ax.set_xticklabels(weekDays)
        ax.legend()

        for rect in rects1:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
        
        fig.tight_layout()
        fig.savefig("Light_Week_" + str(week) + "_" + str(year) + ".png")
    elif sensor == "temp":
        for item in get_data_from_week:
            t_str = item['date']
            temp = item['day_temp']
            date_class = datetime.datetime.strptime(t_str, "%Y-%m-%d")
            week_day = date_class.weekday()
            weekAvg[week_day] = temp
        fig, ax = plt.subplots()
        rects1 = ax.bar(x, weekAvg, width, label='temperature value')
        
        tilte = "Statistic of temperature sensor from " + first_str + " to " + last_str
        ax.set_ylabel('Temperature')
        ax.set_title(tilte)
        ax.set_xticks(x)
        ax.set_xticklabels(weekDays)
        ax.legend()

        for rect in rects1:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
        
        fig.tight_layout()
        fig.savefig("Temp_Week_" + str(week) + "_" + str(year) + ".png")
    elif sensor == "humid":
        for item in get_data_from_week:
            t_str = item['date']
            temp = item['day_humid']
            date_class = datetime.datetime.strptime(t_str, "%Y-%m-%d")
            week_day = date_class.weekday()
            weekAvg[week_day] = temp
        fig, ax = plt.subplots()
        rects1 = ax.bar(x, weekAvg, width, label='humid value')
        
        tilte = "Statistic of humid sensor from " + first_str + " to " + last_str
        ax.set_ylabel('Humid')
        ax.set_title(tilte)
        ax.set_xticks(x)
        ax.set_xticklabels(weekDays)
        ax.legend()

        for rect in rects1:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
        
        fig.tight_layout()
        fig.savefig("Humid_Week_" + str(week) + "_" + str(year) + ".png")

def get_report_by_month(sensor, month, year):
    width = 0.4
    ### Get day num:
    days_num = 0
    if month == 2:
        if year % 100 == 0:
            if year % 400 == 0:
                days_num = 29
            else:
                days_num = 28
        elif year % 4 == 0:
            days_num = 29
        else:
            days_num = 28
    elif month in [1,3,5,7,8,10,12]:
        days_num = 31
    else:
        days_num = 30

    daily_data = np.zeros(days_num)
    days_count = np.arange(days_num)+1

    get_data_from_month = []
    if sensor == "light":
        get_data_from_month = mydb.get_month_report(month,year,'light') ###Call from db
    else:
        get_data_from_month = mydb.get_month_report(month,year,'temp_humid')

    if sensor == "light":
        for item in get_data_from_month:
            t_str = item['date']
            temp = int(item['day_light'])
            date_class = datetime.datetime.strptime(t_str, "%Y-%m-%d")
            day = date_class.day
            daily_data[day-1] = temp
        fig, ax = plt.subplots()
        rects1 = ax.bar(days_count, daily_data, width, label='light value')
        
        tilte = "Statistic of light sensor in " + str(month) + "/" + str(year)
        ax.set_ylabel('Light')
        ax.set_title(tilte)
        ax.set_xticks(days_count)

        ax.legend()

        for rect in rects1:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
        
        fig.tight_layout()
        fig.savefig("Light_Month_" + str(month) + "_" + str(year) + ".png")
    elif sensor == "temp":
        for item in get_data_from_month:
            t_str = item['date']
            temp = int(item['day_temp'])
            date_class = datetime.datetime.strptime(t_str, "%Y-%m-%d")
            day = date_class.day
            daily_data[day-1] = temp
        fig, ax = plt.subplots()
        rects1 = ax.bar(days_count, daily_data, width, label='temp value')
        
        tilte = "Statistic of temperature sensor in " + str(month) + "/" + str(year)
        ax.set_ylabel('Temperature')
        ax.set_title(tilte)
        ax.set_xticks(days_count)

        ax.legend()

        for rect in rects1:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
        
        fig.tight_layout()
        fig.savefig("Temp_Month_" + str(month) + "_" + str(year) + ".png")
    elif sensor == "humid":
        for item in get_data_from_month:
            t_str = item['date']
            temp = int(item['day_humid'])
            date_class = datetime.datetime.strptime(t_str, "%Y-%m-%d")
            day = date_class.day
            daily_data[day-1] = temp
        fig, ax = plt.subplots()
        rects1 = ax.bar(days_count, daily_data, width, label='humid value')
        
        tilte = "Statistic of humid sensor in " + str(month) + "/" + str(year)
        ax.set_ylabel('Humid')
        ax.set_title(tilte)
        ax.set_xticks(days_count)

        ax.legend()

        for rect in rects1:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
        
        fig.tight_layout()
        fig.savefig("Humid_Month_" + str(month) + "_" + str(year) + ".png")


# Parser
parser = argparse.ArgumentParser(description='Get report')
parser.add_argument("--mode", help="Mode [day,week,month]")
parser.add_argument("--sensor", help="Sensor [light,temp,humid]")
parser.add_argument("--day", help="Day", default="0")
parser.add_argument("--week", help="Week", default="0")
parser.add_argument("--month", help="Month", default="0")
parser.add_argument("--year", help="Year", default="0")
args = vars(parser.parse_args())

mode = args['mode']
sensor = args['sensor']
day = int(args['day'])
week = int(args['week'])
month = int(args['month'])
year = int(args['year'])

mydb = MyDatabase()

if mode == "day":
	get_report_by_day(sensor, day, month, year)
elif mode == "week":
	get_report_by_week(sensor, week, year)
elif mode == "year":
	get_report_by_month(sensor, month, year)


