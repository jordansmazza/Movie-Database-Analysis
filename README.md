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