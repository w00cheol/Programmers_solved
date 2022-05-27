class soo4ja:
    def __init__(self, person, lenA, trueAnswers):
        self.submit = []
        self.count = 0
        self.lenA = lenA
        self.trueAnswers = trueAnswers[::]
        if person == 1:
            marking = [1, 2, 3, 4, 5]
            for i in range(lenA):
                self.submit.append(marking[i%5])
        if person == 2:
            marking = [2, 1, 2, 3, 2, 4, 2, 5]
            for i in range(lenA):
                self.submit.append(marking[i%8])
        if person == 3:
            marking = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
            for i in range(lenA):
                self.submit.append(marking[i%10])
    def check(self):
        for i in range(0, self.lenA):
            if self.submit[0] == self.trueAnswers[0]:
                self.count += 1
            del self.submit[0]
            del self.trueAnswers[0]
        return self.count
def solution(answers):
    lenA = len(answers)
    people = [[1, soo4ja(1, lenA, answers).check()], [2, soo4ja(2, lenA, answers).check()], [3, soo4ja(3, lenA, answers).check()]]
    best = max(people, key = lambda x: x[1])[1]
    return list(map(lambda y: y[0], list(filter(lambda x: x[1] == best, people))))