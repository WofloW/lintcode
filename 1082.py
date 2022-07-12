# 1082 · 员工的重要度
# https://www.lintcode.com/problem/1082/description?utm_source=sc-libao-zyq
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    """
    @param imput:
    @param id:
    @return: the total importance value
    """
    def getImportance(self, employees, id):
        # Write your code here.
        hashmap = {employee.id: employee for employee in employees}
        result = 0
        queue = [id]
        while queue:
            e = hashmap[queue.pop()]
            result += e.importance
            for sub in e.subordinates:
                queue.append(sub)
        return result