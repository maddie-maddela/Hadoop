from mrjob.job import MRJob
from mrjob.step import MRStep
class CountMovieRatings(MRJob):
        def steps(self):
                return [
                MRStep(mapper=self.mapper_students_only
                ,reducer=self.reducer1)
                ,MRStep(reducer=self.reducer2)
                ,MRStep(reducer=self.reducer3)
                ]
        def mapper_students_only(self, _, line):
                lst = line.split('|')
                if len(lst) == 5: # u.user
                        user_id, age, gender, occupation = lst[0], lst[1], lst[2], lst[3]
                        yield int(user_id), ("-", "", gender)

                else: # u.data
                        lst = line.split('\t')
                        user_id_, movie_id, rating = lst[0], lst[1], lst[2]
                        yield int(user_id_), (movie_id, rating, "")

        def reducer1(self, key, values):
                for movie_id, rating, gender in values:
                        if gender == 'M': return
                        if gender == 'F': continue
                        yield  movie_id, int(rating)

        def reducer2(self, key, values):
                yield 1, str(max(values)).zfill(5)+key

        def reducer3(self,key,values):
                lst = sorted(values, reverse=True)
                for val in lst[0:10]:
                        yield int(val[5:]), int(val[0:5])
if __name__ == '__main__':
        CountMovieRatings.run()
