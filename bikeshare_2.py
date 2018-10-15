# Jong Min (Jay) Lee_Udacity Programming for Data Science_Project 2: Python

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january','february','march','april','may','june']
dow = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    print('\nEnter Inputs for Exploring US Bikeshare Data')
    while True:
        print('\n1. Would you like to see data for Chicago, New York City, or Washington?')
        city = input('   See data for the city: ').lower()
        if city in CITY_DATA:
            break
        else:
            print('\n   [Invalid Entry] Please enter one of the three cities.')

    # get user input for month and day of week
    while True:
        print('\n2. Would you like to filter the data by month, day, both or not at all (enter "None")?')
        filter_by = input('   Filter the data by: ').lower()
        if filter_by == 'none':
            month = 'all'
            day = 'all'
            break
        elif filter_by == 'month':
            day = 'all'
            month = get_filters_month()
            break
        elif filter_by == 'day':
            month = 'all'
            day = get_filters_day()
            break
        elif filter_by == 'both':
            day = get_filters_day()
            month = get_filters_month()
            break
        else:
            print('\n   [Invalid Entry] Please enter month, day, both or None.')

    print('\n [Request] Explore Bikeshare Data for {} with filters month: {}, day: {}\n'.format(city.title(), month.title(), day.title()))
    print('-'*40)

    return city, month, day

def get_filters_month():
    while True:
        filter_by_month = input('\n   Filter the data by the month: ').lower()
        if filter_by_month in months:
            break
        else:
            print('\n   [Invalid Entry] Please enter a month from January to June.')

    return filter_by_month

def get_filters_day():
    while True:
        filter_by_day = input('\n   Filter the data by the day of the week: ').lower()
        if filter_by_day in dow:
            break
        else:
            print('\n   [Invalid Entry] Please enter a day from Monday to Sunday.')

    return filter_by_day


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
    print('\nLoading .csv data ...')
    df = pd.read_csv(CITY_DATA[city])

    # Apply datetime properties to Start Time column values
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create new columns for month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # both or by month only
    if month != 'all':
        month_num = months.index(month) + 1
        df = df[df['month'] == month_num]
        print('[Loading] applied filter for month: {}...'.format(month.title()))

    # both or by day only
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        print('[Loading] applied filter for day: {}...'.format(day.title()))

    print('\n Completed loading .csv data for {} with filters month: {}, day: {}\n'.format(city.title(), month.title(), day.title()))
    print('-'*40)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n[Analysis 1/4] Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month (if filter applied for month)
    if len(df['month'].unique()) != 1:
        popular_month_num = df['month'].mode()[0]
        popular_month = months[popular_month_num - 1]
        print(' - Most popular month: {}'.format(popular_month.title()))

    # display the most common day of week (if filter applied for day)
    if len(df['day_of_week'].unique()) != 1:
        popular_dow = df['day_of_week'].mode()[0]
        print(' - Most popular day: {}'.format(popular_dow))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(' - Most popular hour: {}'.format(popular_hour))

    print("\n Completed calculating most frequent times of travel (%s seconds).\n" % (format(time.time() - start_time,'.4f')))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n[Analysis 2/4] Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print(' - Most commonly used Stations')
    popular_start_st = df['Start Station'].mode()[0]
    popular_start_st_count = df['Start Station'].value_counts()[0]
    print('   Start: {} ({} times)'.format(popular_start_st,popular_start_st_count))

    popular_end_st = df['End Station'].mode()[0]
    popular_end_st_count = df['End Station'].value_counts()[0]
    print('     End: {} ({} times)'.format(popular_end_st,popular_end_st_count))

    # display most frequent combination of start station and end station trip
    popular_combin_st = (df['Start Station'] +','+ df['End Station']).mode()[0]
    popular_combin_st_count = (df['Start Station'] +','+ df['End Station']).value_counts()[0]
    print(' - Most frequent combination of Stations: ({} times)'.format(popular_combin_st_count))
    for i, station in enumerate(popular_combin_st.split(',')):
        if i == 0:
            print('   Start: {}'.format(station))
        else:
            print('     End: {}'.format(station))

    print("\n Completed calculating most popular stations and trip (%s seconds).\n" % (format(time.time() - start_time,'.4f')))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n[Analysis 3/4] Calculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(' - Total Travel Time: {} seconds'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print(' - Mean Travel Time : {} seconds'.format(df['Trip Duration'].mean()))

    print("\n Completed calculating trip duration (%s seconds).\n" % (format(time.time() - start_time,'.4f')))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\n[Analysis 4/4] Calculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(' - User Type:')
    for usertype in df['User Type'].unique():
        print('   {}: {}'.format(usertype,df[df['User Type']==usertype]['User Type'].count()))

    if city in ['chicago','new york city']:
        # Display counts of gender
        print(' - Gender:')
        for gender in df['Gender'].unique():
            print('   {}: {}'.format(gender,df[df['Gender']==gender]['Gender'].count()))

        # Display earliest, most recent, and most common year of birth
        print(' - Birth Year:')
        print('   Earliest        : {}'.format(int(df['Birth Year'].min())))
        print('   Most Recent     : {}'.format(int(df['Birth Year'].max())))
        common_yob = df['Birth Year'].mode()[0]
        common_yob_count = df[df['Birth Year']==common_yob]['Birth Year'].count()
        print('   Most Common Year: {} ({} times)'.format(int(common_yob),common_yob_count))

    else:
        print(' - Gender and Birth Year data not available for {}'.format(city))

    print("\n Completed calculating user stats (%s seconds).\n" % (format(time.time() - start_time,'.4f')))
    print('-'*40)


def top_n(df):
    """See top # records of the data frame."""

    while True:
        top_n = input('\nWould you like to see top # records? [Yes or No] ').lower()

        if top_n == 'yes':
            while True:
                try:
                    n = int(input('\nHow many records would you like to see?\nEnter a number from 1 to 10: '))
                except:
                    print('\n [Invalid Entry] Please try again.')
                else:
                    if n >= 1 and n <= 10:
                        i = 1
                        for row in df.head(n).index:
                            print('\n{}th Record'.format(i))
                            for column in df.columns[1:-3]:
                                print('  - {}: {}'.format(column,df[column][row]))
                            i += 1
                        break
                    else:
                        print('\n [Invalid Entry] Please try again.')
            break
        elif top_n == 'no':
            print('\n Top # records will not be displayed.')
            break
        else:
            print('\n [Invalid Entry] Please enter Yes or No.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        top_n(df)

        restart = input('\nEnter yes to perform another analysis. Otherwise, enter any characters.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
