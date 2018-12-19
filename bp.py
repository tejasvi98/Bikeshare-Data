import datetime
import pandas as pd
import calendar

def city_name():
	'''prompts user to input city and return file name for that city bikeshare data'''
	city = input("Hello! Let\'s explore some US bikeshare data!\nwould you like to see data for chicago, New York, or Washington?\n").lower()
	if city == "chicago" or city == "Chicago":
		return 'chicago.csv'
	elif city == "new york" or city == "New York":
		return 'new_york_city.csv'
	elif city == "Washington" or city == "washington":
		return 'washington.csv'
	else:
		print("Sorry, not sure which city you are referring to, Please try again.")
		return city_name()

def time_filter():
	'''prompts user to input time period and returns output output according to selected time filter'''
	time_filter = input("which time filter would you like to apply:- \n1. month\n2. day\n3. type none for no filter\n")
	if time_filter == "month":
		return ["month",month_filter()]
	elif time_filter == "day":
		return['day',day_filter()]
	elif time_filter == "none":
		return['none', 'no time filter']
	else:
		print("no such filter available, Please Try again")
		return time_filter()

def month_filter():
	'''prompts user to input month and returns month being input by user'''
	m = input("from January to June which month you want to see\n").lower()
	if m == "January" or m == "january":
		return '01'
	elif m == "February" or m == "february":
		return '02'
	elif m == "March" or m == "march":
		return '03'
	elif m == "April" or m == "april":
		return '04'
	elif m == "May" or m == "may":
		return '05'
	elif m == "June" or m == "june":
		return '06'
	else:
		print("input month is not in calendar! enter again\n")
		return month_filter()

def day_filter():
	''' prompts user to input day and returns day input by user'''
	day = input("from Monday to Sunday, Which day you want to choose?\n").lower()
	if day == "Monday" or day == "monday":
		return 0
	elif day == "Tuesday" or day == "tuesday":
		return 1
	elif day == "Wednesday" or day == "wednesday":
		return 2
	elif day == "Thursday" or day == "thursday":
		return 3
	elif day == "Friday" or day == "friday":
		return 4
	elif day == "Saturday" or day == "saturday":
		return 5
	elif day == "Sunday" or day == "sunday":
		return 6
	else:
		print("day input is not present in week please try againn\n")
		return day_filter()

def popular_month(df):
	#returns the most popular month 
	popular = df.groupby('Month')['Start Time'].count()
	return "Most Popular Month: " + calendar.month_name[int(popular.sort_values(ascending = False).index[0])]

def popular_day(df):
	#returns the most popular day
	popular = df.groupby('Day of Week')['Start Time'].count()
	return "Most popular Day: " + calendar.day_name[int(popular.sort_values(ascending = False).index[0])]

def popular_hour(df):
#returns the most popular hour of day
	hour = df.groupby('Hour of Day')['Start Time'].count()
	popular_hour = hour.sort_values(ascending = False).index[0]
	h = datetime.datetime.strptime(popular_hour, "%H")
	return "Most popular hour of day: " + h.strftime("%I %p")

def trip_time(df):
	#returns total and average trip duration according to filters applied
	total_trip = df['Trip Duration'].sum()
	avg_trip = df['Trip Duration'].mean()
	m,s = divmod(total_trip,60)
	h,m = divmod(m,60)
	d,h = divmod(h,24)
	y,d = divmod(d,365)
	total_trip = "\n total trip duration: %d years %02d days %02d hrs %02d min %02d sec" % (y,d,h,m,s)
	m,s = divmod(avg_trip,60)
	h,m = divmod(m,60)
	avg_trip = "\n average trip duratin : %d hrs %02d min %02d sec" % (h,m,s)
	return [total_trip,avg_trip]

def popular_station(df):
	#returns most popular start and end stations
	start_station = df.groupby('Start Station')['Start Station'].count()
	end_station = df.groupby('End Station')['End Station'].count()
	sort_start_station = start_station.sort_values(ascending = False)
	sort_end_station = end_station.sort_values(ascending = False)
	total = df['Start Station'].count()
	popular_start_station = "\nMost popular start station: " + sort_start_station.index[0] + " (" + str(sort_start_station[0]) + " trips, " + '{0:.2f}%'.format(((sort_start_station[0]/total) * 100)) + " of trips)"
	popular_end_station = "\nMost popular end station: " + sort_end_station.index[0] + " (" + str(sort_end_station[0]) + " trips, " + '{0:.2f}%'.format(((sort_end_station[0]/total) * 100)) + " of trips)"
	return [popular_start_station,popular_end_station]

def popular_trip(df):
	#return most popular trip from start to end station
	trip = df.groupby(['Start Station','End Station'])['Start Station'].count()
	sorted_trip = trip.sort_values(ascending=False)
	total_trip = df['Start Station'].count()
	return "Most popular trip: " + "\n  Start station: " + str(sorted_trip.index[0][0]) + "\n  End station: " + str(sorted_trip.index[0][1]) + "\n  (" + str(sorted_trip[0]) +  " trips, " + '{0:.2f}%'.format(((sorted_trip[0]/total_trip) * 100)) + " of trips)"

def user(df):
    #returns number of users
    user_type_count = df.groupby('User Type')['User Type'].count()
    return user_type_count


def gender(df):
    #returns gender of riders
    gender = df.groupby('Gender')['Gender'].count()
    return gender


def birth_years(df):
    #returns birth year
    early_birth = "Earliest birth year: " + str(int(df['Birth Year'].min()))
    most_recent_birth = "Most recent birth year: " + str(int(df['Birth Year'].max()))
    birth_year = df.groupby('Birth Year')['Birth Year'].count()
    sort_birth_year = birth_year.sort_values(ascending=False)
    total_trip = df['Birth Year'].count()
    most_common_birth = "Most common birth year: " + str(int(sort_birth_year.index[0])) + " (" + str(sort_birth_year.iloc[0]) + " trips, " + '{0:.2f}%'.format(((sort_birth_year.iloc[0]/total_trip) * 100)) + " of trips)"
    return [early_birth, most_recent_birth, most_common_birth]    

def individual_trips(df, current_line):
    #returns individual trips
    display_trips = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    display_trips = display_trips.lower()
    if display_trips == 'yes' or display_trips == 'y':
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return individual_trips(df, current_line)
    if display_trips == 'no' or display_trips == 'n':
        return
    else:
        print("\nwant to see more data. Please try again.")
        return individual_data(df, current_line)

def stats():
	#calculate statistics according to input by user
	city = city_name()
	city_df = pd.read_csv(city)

	def none_filter(str_date):
	    #for none filter
	    date = datetime.date(int(str_date[0:4]), int(str_date[5:7]), int(str_date[8:10]))
	    return date.weekday()

	city_df['Day of Week'] = city_df['Start Time'].apply(none_filter)
	city_df['Month'] = city_df['Start Time'].str[5:7]
	city_df['Hour of Day'] = city_df['Start Time'].str[11:13]
	time_period = time_filter()
	filter_period = time_period[0]
	filter_period_value = time_period[1]
	filter_period_label = 'No filter'

	if filter_period == 'none':
		filtered_df = city_df
	elif filter_period == 'month':
		filtered_df = city_df.loc[city_df['Month'] == filter_period_value]
		filter_period_label = calendar.month_name[int(filter_period_value)]
	elif filter_period == 'day':
		filtered_df = city_df.loc[city_df['Day of Week'] == filter_period_value]
		filter_period_label = calendar.day_name[int(filter_period_value)]
	print('\n')
	print(city[:-4].upper().replace("_", " ") + ' -- ' + filter_period_label.upper())
	print('-------------------------------------')

	print('Total trips: ' + "{:,}".format(filtered_df['Start Time'].count()))
	if filter_period == 'none' or filter_period == 'day':
		print(popular_month(filtered_df))
	if filter_period == 'none' or filter_period == 'month':
		print(popular_day(filtered_df))
	print(popular_hour(filtered_df))
	trip_duration_statistics = trip_time(filtered_df)
	print(trip_duration_statistics[0])
	print(trip_duration_statistics[1])
	most_popular_station = popular_station(filtered_df)
	print(most_popular_station[0])
	print(most_popular_station[1])
	print(popular_trip(filtered_df))
	print('')
	print(user(filtered_df))

	if city == 'chicago.csv' or city == 'new_york_city.csv':
		print('')
		print(gender(filtered_df))
		birth_years_data = birth_years(filtered_df)
		print('')
		print(birth_years_data[0])
		print(birth_years_data[1])
		print(birth_years_data[2])
	individual_trips(filtered_df, 0)

	def restart():
		#to restart
		restart = input('\nWould you like to restart the program(yes/no)\n')
		if restart.lower() == 'yes' or restart.lower() == 'y':
			stats()
		elif restart.lower() == 'no' or restart.lower() == 'n':
			return
		else:
			print("\nInvalid Input , Please Try Again\n")
			return restart()

	restart()

if __name__ == "__main__":
	stats()