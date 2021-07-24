'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''

import heapq

class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        # {ID: list of top five scores}
        student_scores = {}
        for result in results:
            ID = result.id
            score = result.score
            student_scores[ID] = student_scores.get(ID, [])
            heapq.heappush(student_scores[ID], score)
            if len(student_scores[ID]) > 5:
                heapq.heappop(student_scores[ID])
        ans = {}
        for ID, scores in student_scores.items():
            ans[ID] = round(sum(scores) / 5, 2)
        return ans

'''
Algorithm:
Min-Heap

Note:
Record class
round(avg, 2)
'''