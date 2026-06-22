# Bikeshare Project

## Project Overview
This project analyzes bikeshare data from three major U.S. cities: Chicago, New York City, and Washington. The Python program allows the user to choose a city, month, and day, then displays statistics about travel times, stations, trip duration, and users.

## Date Created
June 2026

## Files Used
The project uses the following files:

- `bikeshare.py`: Python script used to run the bikeshare analysis.
- `chicago.csv`: Bikeshare data for Chicago.
- `new_york_city.csv`: Bikeshare data for New York City.
- `washington.csv`: Bikeshare data for Washington.
- `.gitignore`: Prevents CSV data files from being pushed to GitHub.
- `README.md`: Provides information about the project.

## How to Run the Project
To run the project, open a terminal in the project folder and type:

```bash
python bikeshare.py
```

The program will ask the user to enter:

1. A city: `chicago`, `new york city`, or `washington`
2. A month: `january`, `february`, `march`, `april`, `may`, `june`, or `all`
3. A day: any day of the week or `all`

After the filters are selected, the program prints bikeshare statistics and gives the user the option to view raw data.

## Statistics Calculated
The program calculates:

- Most common month
- Most common day of week
- Most common start hour
- Most common start station
- Most common end station
- Most common trip
- Total travel time
- Average travel time
- User type counts
- Gender counts, when available
- Earliest, most recent, and most common birth year, when available

## Git Branches Used
This project uses three branches:

- `main`: Contains the original project files.
- `documentation`: Contains README documentation updates.
- `refactoring`: Contains improved and cleaner Python code.

## Gitignore Explanation
The `.gitignore` file is used to make sure that `.csv` files are not pushed to GitHub because the dataset files are large and should not be included in the repository.

## Credits
This project was completed as part of the Udacity programming project. The dataset and project instructions were provided by Udacity.
