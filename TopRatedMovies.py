from mrjob.job import MRJob 
from mrjob.step import MRStep 
class CountMovieRatings(MRJob):
    def steps(self): 
        return [
        MRStep(mapper=self.mapper_1,
        reducer=self.reducer_1),
        MRStep(reducer=self.reducer_2)
        ]
    def mapper_1(self, _, line):
        user_id, movie_id, raƟng, Ɵmestamp = line.split('\t')
        yield movie_id, 1
    def reducer_1(self, key, values):
        yield 1, str(sum(values)).zfill(5)+key
    def reducer_2(self, count, movies):
        movies = sorted(movies, reverse=True)
        for movie in movies[0:10]:
            yield int(movie[0:5]), int(movie[5:])
if __name__ == '__main__':
CountMovieRatings.run()
