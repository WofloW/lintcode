# Use two stacks to implement one queue
# Stack: first in last out
# Queue: first in first out

# Simulate actions like
# push(1)
# pop()
# push(2)
# push(3)
# top()
# pop()

# In queue
# [1]
# []
# [2]
# [2, 3]
# [2, 3]        (return 2)
# [3]


# In two stacks
# stack1 [1] stack2 []
# stack1 [] stack2 [1] => stack1 [] stack2[]
# stack1 [2] stack2 []
# stack1 [2, 3] stack2 []
# stack1 [] stack2 [3, 2] (return 2)
# stack1 [] stack2 [3]
class MyQueue:
    def __init__(self, ):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        self.stack1.append(element)

    """
    @return: An integer
    """

    def pop(self, ):
        # write your code here
        self.top()
        return self.stack2.pop()

    """
    @return: An integer
    """

    def top(self, ):
        # write your code here
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]