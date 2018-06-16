
class SplitSumsNaive:
    def do_task(self, task):
        def f(x):
            return (int(x) + self.last_sum) % 1000000001
        if task[0] == 's':
            op, left, right = task.split()
            left, right = f(left), f(right)
            s = self.sumof(left, right)
            self.last_sum = s
            return s
        op, val = task.split()
        val = f(val)
        if op == '?':
            ret = self.find(val)
            return ['Not found','Found'][ret]
        if op == '+':
            self.add(val)
        elif op == '-':
            self.remove(val)
    
    def run_tasks(self, tasks):
        results = []
        if isinstance(tasks, str):
            tasks = tasks.split(';')
        self.last_sum = 0
        for task in tasks:
            ret = self.do_task(task)
            if ret is not None:
                results.append(ret)
        return results

    def test(self, tasks, exam):
        if isinstance(exam, str):
            exam = exam.split(';')
        exam = [str(x) for x in exam]
        self.__init__()
        results = [str(x) for x in self.run_tasks(tasks)]
        assert results == exam, "\nneed {}\ngot  {}".format(results, exam)

    def __init__(self):
        self.vals = set()
        self.last_sum = 0

    def add(self, val):
        self.vals.add(val)
        return self
        
    def remove(self, val):
        if val in self.vals:
            self.vals.remove(val)
        return self

    def find(self, val):
        return val in self.vals
    
    def sumof(self, left, right):
        s = 0
        for val in self.vals:
            if left <= val <= right:
                s += val
        return s        


def main():
    ssn = SplitSumsNaive()
    num_tasks = int(input())
    for _ in range(num_tasks):
        ret = ssn.do_task(input())
        if ret is not None:
            print(ret)

main()