# Movie-Database-Analysis
## Introduction
> This dataset is provided by the tMDb. There are 10866 rows, corresponding to unique movies, and 21 columns with variables including genre, runtime, title, and revenue. This covers information on movies released between 1960's to 2015.

### Identify Questions
Here are the questions I aim to address with this analysis.
1. Does a movie's budget effect its success?
    - This information would help production companies make informed decisions when funding projects.
2.	Does the season in which a movie was released effect a movie's success?
    - This would allow companies to plan production schedules efficiently.
3.	Have movie lengths decreased over time?
    - Based on personal experience, I hypothesize movies have gotten much longer in length over time. Many older movies I have seen are on average much shorter thn current releases.
4.	Which directors make the highest grossing films?
    - This is valuable to know when companies are looking to hire directors for their projects.
### Define Variables
**The variables used in this analysis are listed below**
- `budget`
- `revenue`
- `release_date`
- `runtime`
- `release_year`
- `voter_average`
- `vote_count`

For this analysis a movie's success is defined in two ways, the first is by a movie's revenue and the second, a movie's rating (`voter_average`). These will both be used to see if these variables are consistent with one another. For example, if a movie's budget effects a movie's revenue, does the budget effect a movie's rating in the same way?

---
## Data Cleaning
After importing this dataset, I printed the head of the dataframe and decided to remove some columns I knew I would not be using.

I then checked for any null values. Only 10 null values popped up originally, so I dropped those rows. To double check, I used .describe() to analyze the dataset. I noticed the budget, revenue, and runtime columns all had minimums of zero, meaning missing values. I used the .shape function to see how many rows had zero values for each column.

While the runtime column only has 31 missing values, both the budget and revenue column had a significant amount of missing data. Since over half the rows in these columns had missing data, filling these with the mean could drastically skew the data. Because of this, removed all rows with missing data. Even though this cut my dataset by over half, I decided having a smaller, more accurate dataset would be better than a heavily skewed one.

To do this, I replaced all 0 values with null values so I could drop them using .dropna(). I got this solution from a Stack Overflow thread (linked below). I then I checked for and dropped any duplicates.

---
## Adding a Seasons Column
The first step that needed to be done to answer my second research regarding the relationship between a movie's release season and its success was making the `release_date` column into a datetime dtype.

After doing a lot of research and reading many stackoverflow threads (linked below), I was able to create an if statement that extracted the season from the `release_date` column in the dataset. First, I transformed the month and day into strings so I could append them onto one another. I had to add a floating zero onto the day variable so dates like July 7th would read 707 rather than 77 (stackoverflow for this solution linked below). Then, I created a variable that consisted of the appended month and day and transformed it back into an integer so I could perform Boolean statements on it. From there I created an if statement that filtered each date in its respective season. I then assigned this to a new column called `release_season`.
