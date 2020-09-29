import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv('/Users/jordanmazza/Desktop/Udacity Files/Project 2/movies.csv')
# Dropping the columns I won't be using
df.drop(columns=['id', 'popularity', 'cast', 'homepage', 'tagline', 'keywords', 'overview', 'genres', 'production_companies', 'budget_adj', 'revenue_adj'], inplace=True)

# Checking for any missing or irregular data
## print(df.isna().any())
## print(df.describe())
## print(df[df['revenue'] == 0].shape)
## print(df[df['budget'] == 0].shape)
## print(df[df['runtime'] == 0].shape)
df.replace(0, np.nan, inplace=True)
df.dropna(axis=0, how='any', inplace=True)
## print(df.isna().any())
## print(df.describe())
## print(df.shape)

# checking for and dropping duplicates
## print(df[df.duplicated()])
df.drop_duplicates(keep='first', inplace=True)
## print(df[df.duplicated()])

df['release_date'] =  pd.to_datetime(df['release_date'])
## print(df.info())

# Creating a column that shows which season a movie was released during
def season_release(date):
    month = str(date.month)
    day = str(date.day).zfill(2)
    month_day = int(month + day)
    if (month_day >= 321 and month_day <=620):
         return 'Spring'
    elif (month_day >= 621 and month_day <= 922):
        return 'Summer'
    elif (month_day >= 923 and month_day < 1220):
        return 'Fall'
    else:
        return 'Winter'
df['release_season'] = df['release_date'].map(season_release)

# Creating variables for my analysis
director_rev = df.groupby('director', as_index=False)['revenue'].mean().sort_values('revenue', ascending=False)
director_rev = director_rev.head(10)
runtime_mean = df.groupby('release_year')['runtime'].mean()

# Plotting my anlaysis
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)

# Budget and moive success
ax1.scatter(y=df['budget'], x=df['vote_average'])
ax1.set_ylabel('Bugdet (in 100 millions)')
ax1.set_xlabel('Rating (out of 10)')
ax1.set_title('Movie Budget Compared to Rating')

ax2.scatter(y=df['budget'], x=df['revenue'])
ax2.set_ylabel('Bugdet (in 100 millions)')
ax2.set_xlabel('Movie Revenue (in Billions)')
ax2.set_title('Movie Budget Compared to Revenue')

# Release season and movie success
ax3.bar(x=df['release_season'], height=df['revenue'])
ax3.set_xlabel('Season of Release')
ax3.set_ylabel('Movie Revenue (in Billions)')
ax3.set_title('Release Season Compared to Revenue')

ax4.bar(x=df['release_season'], height=df['vote_average'])
ax4.set_xlabel('Season of Release')
ax4.set_ylabel('Rating (out of 10)')
ax4.set_title('Release Season Compared to Rating')

# Runtime trends over time
ax5.plot(runtime_mean)
ax5.set_xlabel('Year')
ax5.set_ylabel('Movie Length (in minutes)')
ax5.set_title('Movie Lengths Over Time')

# Directors with highest grossing films
ax6.bar(x=director_rev['director'], height=director_rev['revenue'])
ax6.set_xlabel('Director')
ax6.set_ylabel('Average Movie Revenue')
ax6.set_title('Top Ten Highest Grossing Directors')

plt.show()