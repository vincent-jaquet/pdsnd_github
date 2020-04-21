import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Which city do you want investigate? ').lower()

    while(city not in ['chicago', 'new york city', 'washington']):
          city=input('Sorry we only have data for Chicago, New York City or Washington. Enter one of these city: ').lower()


    # Get user input for month (all, january, february, ... , june)
    month=input('Which month do you want investigate? from January to June or all: ').lower()

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Which day do you want investigate? all, Monday, Tuesday, ... Sunday: ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]
    num_to_month={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June"}
    print("The most common start month: ",num_to_month[popular_month])


    # Display the most common day of week
    popular_weekday = df['day_of_week'].mode()[0]
    print("The most common day of the week: ",popular_weekday)


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour: ",popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular start station: ",popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most popular end station: ",popular_end_station)

    # display most frequent combination of start station and end station trip
    df['combination']="from "+df['Start Station']+" to "+df['End Station']
    popular_combination = df['combination'].mode()[0]
    print("The most popular combination: ",popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['duration']=df['End Time']-df['Start Time']
    print("the total travel time: "+str(df['duration'].sum()))


    # display mean travel time
    print("the mean travel time: "+str(df['duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if city != 'washington':


        user_gender = df['Gender'].value_counts()
        print(user_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
        birth_stats=[df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0]]
        print("earliest birth year: ",birth_stats[0],", most recent birth year: ",birth_stats[1]," and most common birth year: ",birth_stats[2])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
