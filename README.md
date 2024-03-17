# Hadoop Project
Some coding work exploring the functionality of Hadoop

The code below uses the MapReduce operations to query the MovieLens dataset and extract relevant information based on specific criteria. The dataset consists of several files, including u.data, u.item, ratings, u.users, and more. The dataset can be downloaded from [MovieLens](https://grouplens.org/datasets/movielens/100k/)

This data set consists of:
  * 100,000 ratings (1-5) from 943 users on 1682 movies

  * Each user has rated at least 20 movies
 
  * Simple demographic info for the users (age, gender, occupation, zip)

The data was collected through the MovieLens web site (movielens.umn.edu) during the seven-month period from September 19th, 1997 through April 22nd, 1998. This data has been cleaned up - users who had less than 20 ratings or did not have complete demographic information were removed from this data set. The important datasets are listed below.

u.data     -- The full u data set, 100000 ratings by 943 users on 1682 items.
              Each user has rated at least 20 movies.  Users and items are
              numbered consecutively from 1.  The data is randomly
              ordered. This is a tab separated list of 
	         user id | item id | rating | timestamp. 
              The time stamps are unix seconds since 1/1/1970 UTC   

u.info     -- The number of users, items, and ratings in the u data set.

u.item     -- Information about the items (movies); this is a tab separated
              list of
              movie id | movie title | release date | video release date |
              IMDb URL | unknown | Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |
              The last 19 fields are the genres, a 1 indicates the movie
              is of that genre, a 0 indicates it is not; movies can be in
              several genres at once.
              The movie ids are the ones used in the u.data data set.

u.genre    -- A list of the genres.

u.user     -- Demographic information about the users; this is a tab
              separated list of
              user id | age | gender | occupation | zip code
              The user ids are the ones used in the u.data data set.

u.occupation -- A list of the occupations.

## Find the most active year for movie releases

This info can be obtained by working on the u.item dataset. The code is shown below.

https://github.com/maddies-codespace/Hadoop/blob/e048d9bf33508021b7b65a421bf41a72c87b44fb/ReleaseDate.py#L1-L21

To run the code, use this command: python3 ReleaseYear.py u.item

The results can be seen here:

![ReleaseDate](https://github.com/maddies-codespace/Hadoop/assets/141537679/6e4a59df-feac-4355-ac9c-331dec3eae10)



## Find the most common occupation among users



## Find the top 10 highest-rated movies with an average rating greater than 4.5
