"""Explore bikeshare data for Chicago, New York City, and Washington.

This script is part of the Udacity Bikeshare project. It asks the user for a
city, month, and day, then prints descriptive statistics about the selected data.
"""

import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """Ask user to specify a city, month, and day to analyze.

    Returns:
        tuple: city, month, day
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input('Choose a city: chicago, new york city, or washington\n').strip().lower()
        if city in CITY_DATA:
            break
        print('Invalid city. Please enter chicago, new york city, or washington.')

    while True:
        month = input('Choose a month: january, february, march, april, may, june, or all\n').strip().lower()
        if month == 'all' or month in MONTHS:
            break
        print('Invalid month. Please enter a month from January to June, or all.')

    while True:
        day = input('Choose a day of week: monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all\n').strip().lower()
        if day == 'all' or day in DAYS:
            break
        print('Invalid day. Please enter a valid day of the week, or all.')

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """Load data for the selected city and filter by month and day.

    Args:
        city (str): name of the city to analyze
        month (str): month name or 'all'
        day (str): day name or 'all'

    Returns:
        DataFrame: filtered city data
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month_number = MONTHS.index(month) + 1
        df = df[df['month'] == month_number]

    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df


def time_stats(df):
    """Display statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('Most common month:', df['month'].mode()[0])
    print('Most common day of week:', df['day_of_week'].mode()[0])
    print('Most common start hour:', df['hour'].mode()[0])

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Display statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('Most common start station:', df['Start Station'].mode()[0])
    print('Most common end station:', df['End Station'].mode()[0])

    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    print('Most common trip:', df['Trip'].mode()[0])

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Display statistics on total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('Total travel time:', df['Trip Duration'].sum())
    print('Mean travel time:', df['Trip Duration'].mean())

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Display statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('\nUser types:')
    print(df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print('\nGender counts:')
        print(df['Gender'].value_counts())
    else:
        print('\nGender data is not available for this city.')

    if 'Birth Year' in df.columns:
        print('\nEarliest birth year:', int(df['Birth Year'].min()))
        print('Most recent birth year:', int(df['Birth Year'].max()))
        print('Most common birth year:', int(df['Birth Year'].mode()[0]))
    else:
        print('\nBirth year data is not available for this city.')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    """Display five rows of raw data at a time if the user requests it."""
    index = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of raw data? Enter yes or no.\n').strip().lower()
        if view_data != 'yes':
            break
        print(df.iloc[index:index + 5])
        index += 5


def main():
    """Run the bikeshare data analysis program."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').strip().lower()
        if restart != 'yes':
            break


if __name__ == '__main__':
    main()
