from mrjob.job import MRJob
from mrjob.step import MRStep
class GetCount(MRJob):
        def steps(self):
                return [
                MRStep(mapper=self.mapper_1,
                reducer=self.reducer_1),
                MRStep(reducer=self.reducer2)
                ]
        def mapper_1(self, _, line):
                lst = line.split('\t')
                user_id, rest1, rest2, rest3 = lst[0], lst[1], lst[2], lst[3]
                yield user_id,1

        def reducer_1(self, key, values):
                yield 1,str(sum(values)).zfill(5)+key

        def reducer2(self, key, values):
                lst = sorted(values, reverse=True)
                for val in lst[0:10]:
                        yield int(val[0:5]), int(val[5:])

if __name__ == '__main__':
        GetCount.run()
