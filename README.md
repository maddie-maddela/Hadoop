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

This info can be obtained by working on the u.user dataset. The code is shown below.

https://github.com/maddies-codespace/Hadoop/blob/6d3763ba02680d751f1ad638597591c14faedf04/CommonOccupation.py#L1-L15

To run the code, use this command: python3 CommonOccupation.py u.user 

The results can be seen here:

![CommonOccupation](https://github.com/maddies-codespace/Hadoop/assets/141537679/443672a7-5ed2-4945-b7ae-207ddce2e1c1)

In order to reduce it to only one result, we can change ‘for val in lst[0:10]:’ inside reducer_2() to ‘for val in lst[0:1]:’


## Find the top 10 most rated movies

This info cannot be obtained by working on a single dataset. First, let us filter out the relevant movie IDs from the u.data dataset. The code is shown below.

https://github.com/maddies-codespace/Hadoop/blob/6d3763ba02680d751f1ad638597591c14faedf04/TopRatedMovies.py#L1-L20

To run the code, use this command: python3 TopRatedMovies.py u.data > out1 

This will save the top 10 movie IDs as out1.

The results can be seen here:

![TopRatedMovies](https://github.com/maddies-codespace/Hadoop/assets/141537679/8eee24cb-0bfc-40b6-87e8-1cff71c25d9a)

We now have to map these movie IDs to movie names using the u.item dataset. The code is shown below.

https://github.com/maddies-codespace/Hadoop/blob/6d3763ba02680d751f1ad638597591c14faedf04/TopRatedMovies01.py#L1-L33

To run the code, use this command: python3 TopRatedMovies01.py u.item out1 > out2

![TopRatedMovies01](https://github.com/maddies-codespace/Hadoop/assets/141537679/3bd4757e-80e7-4e29-8798-52e406c414da)


## Find the top 10 highest-rated movies by female users

This info can be obtained by working with the u.user, u.data, and u.item datasets.

First, we generate a list of movies with a 5 star rating. The code is shown below.

https://github.com/maddies-codespace/Hadoop/blob/9d41caff9fee39944d58d06c04060ccd09818f28/TopRatedMoviesF.py#L1-L36

To run the code, use this command: python3 TopRatedMoviesF.py u.user u.data 

The output is shown below. 

![TopRatedMoviesF](https://github.com/maddies-codespace/Hadoop/assets/141537679/8cf0f42f-314a-4ffe-9858-8dafb70343eb)

The highlighted table above shows movie_id in column1 and no. of times it was reviewed in column2. What we want is the highest-rated movies list. The code needs to be modified to address that. Here is the new code.

https://github.com/maddies-codespace/Hadoop/blob/9d41caff9fee39944d58d06c04060ccd09818f28/TopRatedMoviesF_modified.py#L1-L36

To run the code, use this command: python3 TopRatedMoviesF_modified.py u.data out1

The output is shown below. 

![TopRatedMoviesF1](https://github.com/maddies-codespace/Hadoop/assets/141537679/f0f32b7c-ddb8-4cd7-bd53-c17840a8ba78)

There are tons of movies with a 5 star rating. So, this sorted it based on 9’s in the movie ID. Now, we can map movie IDs with movie names using the TopRatedMovies01.py code from the previous section.

https://github.com/maddies-codespace/Hadoop/blob/6d3763ba02680d751f1ad638597591c14faedf04/TopRatedMovies01.py#L1-L33

To run the code, use this command: python3 TopRatedMovies01.py u.item out1 

The output is shown below. 

![TopRatedMoviesF2](https://github.com/maddies-codespace/Hadoop/assets/141537679/8d748cd2-655a-4328-a17d-52cabc61ed6b)
