# defining a class STUDENT

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print(name,age,tracks,score)

#creating a function
    def change_name(self, name):
        return str(name)
    def change_age(self, age):
        return int(age)
    def add_track(self, tracks):
        return list(tracks)
    def get_score(self, score):
        return float(score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score(34.30))
