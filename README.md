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

---
## Analysis
For my first analysis, I made two scatterplots to see the relationship between a movie's budget and its success. In the first scatterplot, a movie’s success is measured with the movie’s rating while the second scatterplot, success is measured with the movie’s revenue. I wanted to explore both measures of success to see if they showed similar results.

For my second analysis, I used bar graphs to show a movie’s success per season. Again, I created two bar graphs, the first using success as the movie’s rating and the second as the movie’s revenue. Since seasons are a categorical variable, a bar chart better suits this analysis in comparison to a line chart or scatter plot.

My third analysis is a line plot showing how movie runtimes have changed over time. I used a line plot because this plot type is best suited for showing changes over time. Since each year in the dataframe has multiple runtime entries, the first time I tried to plot this it was unreadable. So, I grouped the dataset by year and then took the average runtime to create a more coherent visualization.

Finally, for my last analysis, I performed a similar grouping method. From this method, I was able to group by directors and find the average movie revenue for the movies they directed. Since there were thousands of directors, I also sorted by the revenue column in descending order and used only the first 10 inputs. This gave me the top ten directors/director teams with the highest grossing films. I used a bar chart for this visualization because the director column is categorical.

---
## Conclusions
In my first plot, it doesn’t seem like there is any correlation between movie budget and success as even high budget movies were rated similarly to low budget movies. Looking at the second scatterplot, however, there does seem to be a loose correlation between movie budget and revenue, where the higher the budget, the higher the revenue. Neither of these scatter plots show a significant correlation between the variables, so more analysis would be required before coming to any conclusions.

In regard to my second question using the release season and movie success variable, I got surprising results. I went into this analysis expecting summer releases to be the most successful category; however, as seen below, this is not the case. When using revenue as the success variable, it is clear that movies released in the Fall seem to be much more successful than any other season. Again, when you compare these results to the bar chart where success is defined as movie ratings, the release season seems to have no effect.

My hypothesis about movie runtimes increasing overtime was proven wrong. It seems movie times have actually significantly decreased from the 1960's onward. This shows the importance of research and visualization. If I had not performed this analysis, I would have made a blatantly incorrect assumption about runtime trends over time.

My final plot shows the visualization for my fourth question – a chart of directors with - on average - the highest grossing movies. Interestingly enough, many of the directors in this top ten list directed animated movies like Pixar and DreamWorks movies. This could be valuable for production companies to know because it shows there is a lot of money and return on investment in animated movies.


