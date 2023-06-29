class Person():
    def __init__(self, name, age, occupation,oranization):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.oranization = oranization

    def introduce(self):
        print(f"Hi! it's me {self.name} and I am {self.age} years old.I am {self.occupation} of {self.oranization}")    






person = Person('Danyal',20,'Student', 'NUML')

person.introduce()

