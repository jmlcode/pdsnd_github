### 2018.10.14
* This project and _README_ file were created on 2018.10.14.
* On a side note, *bikeshare_2.py* file was first finalized on 2018.10.09.

### Post Python Project on GitHub
**Programming for Data Science Nanodegree Program**

### User-interactive Python Script for Exploring US Bikeshare Data
The script is built on the following components. Functions used in the _.py_ script either directly reflect these components or complement these components.
1. Filter
  * Requests user to specify each of the following.
    1. which City's (Chicago, NYC, or Washington) bikeshare data to review
    2. what filter (by month, day of week, both, or all) to apply when reviewing the data
    3. specific month and/or day of week if applicable
  * Specific options for months and days of week were determined after a preliminary review of the bikeshare data in all three cities
  * Returns the user's inputs in a format that can be used in the next component
2. Load
  * Use the three inputs from "Filter" to return the appropriate subset of the bikeshare data
  * Loading the data includes cleaning the data to facilitate the computations in the next component
3. Analyze
  * Use the subset of the data from "Load" to compute the statistics and answer the following.
    1. most frequent times of travel
    2. most popular stations of trip
    3. total and average duration of trip
    4. details of bike-user samples
4. Follow-up
  * Adds user-interactive features to the script
  * Request user to specify
    1. whether first *n* records of data needs to be displayed
    2. whether the script should run for another round

### Additional Files
* Bikeshare data from Chicago, NYC, and Washington are used for running the _.py_ script.
* The three _.csv_ files are not added to and tracked in GitHub due to the large file size.

### Credits
* **Additional Files** mentioned above were provided by _Motivate_, a bike share system provider in the U.S.
* Knowledge for using GitHub to post this work in Python was obtained from Udacity's sample remote repository in GitHub (https://github.com/udacity/course-collaboration-travel-plans)
