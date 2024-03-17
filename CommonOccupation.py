from mrjob.job import MRJob 
from mrjob.step import MRStep 
class CountOccupation(MRJob): 
    def steps(self): 
        return [ 
        MRStep(mapper=self.mapper_1, 
        reducer=self.reducer_1) 
        ] 
    def mapper_1(self, _, line): 
        user_id, age, gender, occupaƟon, zip = line.split('\t') 
        yield occupaƟon, 1 
    def reducer_1(self, key, values): 
        yield 1, str(sum(values)).zfill(5), key 
if __name__ == '__main__': 
CountOccupation.run() 