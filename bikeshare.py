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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
          city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n").lower()
          if city not in ('new york city', 'chicago', 'washington'):
            print("Sorry, I didn't find that. please try again.")
            continue
          else:
            break

    while True:
        t = input("\nWould you like to filter the date by month, day, both, or not at all? Type 'none' for no time filter.\n").lower()
        if t not in ['month','day','both','none']:
            print("Sorry, I didn't find that. please try again.")
            continue
        else:    
            #get user input for month (all, january, february, ... , june)
            while t=='both':    
                month = input("\nWhich month would you like to filter by? January, February, March, April, May, June\n").lower()
                if month not in ('january', 'february', 'march', 'april', 'may', 'june'):
                    print("Sorry, I didn't catch that. Try again.")
                    continue
                else:
                    #get user input for day of week (all, monday, tuesday, ... sunday)
                    while True:
                        day = int(input("\nWhich day? please type your response as an integer (e.g., 1=sunday\n"))
                        if day not in [1,2,3,4,5,6,7]:
                            print("Sorry, I didn't catch that. Try again.")
                            continue
                        else:
                            break
                        break
                break     
            while t=='month':  
                month = input("\nWhich month would you like to filter by? January, February, March, April, May, June\n").lower()
                day=-1
                if month not in ('january', 'february', 'march', 'april', 'may', 'june'):
                    print("Sorry, I didn't catch that. Try again.")
                    
                    continue
                else:
                    break
            while t=='day': 
             while True:
                day = int(input("\nWhich day? please type your response as an integer (e.g., 1=sunday\n"))
                month=-1
                if day not in [1,2,3,4,5,6,7]:
                 
                 print("Sorry, I didn't catch that. Try again.")
                 
                 continue
                break
            if t=='none':
                month=-1
                day=-1
            break
        break
    print('-'*40)
    
    return city, month, day

 #ipython bikeshare.py
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
    df=pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    
    
    
    if month!=-1 and day !=-1:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        df = df[df['day_of_week'] == day]
        
    elif month in ['january', 'february', 'march', 'april', 'may', 'june']:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    elif day in [1,2,3,4,5,6,7]:
        df = df[df['day_of_week'] == day]
    else:
        df=df
 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    #  display the most common day of week
    most_common_day_of_week=df['day_of_week'].mode()[0]
    print('Most common day of week:',most_common_day_of_week)
    #  display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station=df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)
    # display most commonly used end station
    End_station=df['End Station'].value_counts().idxmax()
    print('Most Commonly used end station:', End_station)

    #  display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/36000, " Days")

    #  display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/36000, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    #Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    Req = ['yes', 'no']
    RowData = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while RowData not in Req:
       RowData =input(("\nDo you want to show the raw data? Yes or No ")).lower()
         
        #the raw data from the df is displayed if user opts for it
       if RowData == "yes":
        print(df.head())
       elif RowData not in Req:
            print("Input does not seem to match yes , No.")
            print("\nRestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while RowData == 'yes':
        RowData = input(print("Do you want to view more raw data?")).lower()
        counter += 5
        #If user opts for it, this displays next 5 rows of data
        if RowData == "yes":
             print(df[counter:counter+5])
        elif RowData != "yes":
             break

    print('-'*80)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
