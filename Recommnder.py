import pandas as pd

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('dataset.csv')
df.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)
df.groupby('title')['rating'].count().sort_values(ascending=False).head(10)
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()
print("\t\t\tMovies ratings with high number of ratings\n")
print (ratings.sort_values('num of ratings',ascending=False).head(10))
moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
#we are taking two movies from the higly rated movies and checking other movies similar to those genres
starwars_user_ratings = moviemat['Star Wars (1977)'] # star wars=sci-fi
fargo_user_ratings = moviemat['Fargo (1996)'] #fargo=drama
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_fargo = moviemat.corrwith(fargo_user_ratings)
corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.sort_values('Correlation',ascending=False).head(10)
corr_starwars = corr_starwars.join(ratings['num of ratings'])
corr_starwars.head()
print("\t\t\tMovies similar to starwars\n")
print (corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head())
corr_fargo = pd.DataFrame(similar_to_fargo,columns=['Correlation'])
corr_fargo.dropna(inplace=True)
corr_fargo = corr_fargo.join(ratings['num of ratings'])
print("\t\t\tMovies similar to Fargo\n")
print(corr_fargo[corr_fargo['num of ratings']>100].sort_values('Correlation',ascending=False).head())