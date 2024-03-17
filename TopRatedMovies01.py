from mrjob.job import MRJob 
from mrjob.step import MRStep 
class GetTitle(MRJob): 
    def steps(self): 
        return [ 
        MRStep(mapper=self.mapper_movies, 
        reducer=self.reducer_Ɵtle_count),
        MRStep(mapper=self.mapper2, reducer=self.reducer2) 
        ] 
    def mapper_movies(self, _, line): 
        lst = line.split('|') 
        if len(lst) > 2: 
            movie_id, movie_Ɵtle, date = lst[0], lst[1], lst[2]
            yield movie_id, ("", movie_Ɵtle)
        else: 
            lst = line.split('\t') 
            count, movie_id = lst[0], lst[1] 
            yield movie_id, (count, "") 
    def reducer_Ɵtle_count(self, key, values):
        name = None 
        for count, movie_Ɵtle in sorted(values):
            if movie_Ɵtle:
                name = movie_Ɵtle
            else: 
                yield int(count), name 
    def mapper2(self, key, value): 
        yield 1, str(key).zfill(5) + value
    def reducer2(self, key, values):
        lst = sorted(values, reverse=True)
    for val in lst:
        yield val[0:5], val[5:]
if __name__ == '__main__':
GetTitle.run()
