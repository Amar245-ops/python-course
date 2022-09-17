


class Person:

    def __init__(self, name, gender="female"):
       self.name = name
       self.gender = gender

    def show(self):
        print("My Details")
        print(f'Name: {self.name}')
        print(f'Gender: {self.gender}')

class Student(Person):


    def __init__(self, name, gender, klass, college, stream):
        super().__init__(name, gender)
        self.klass = klass
        self.college = college
        self.stream = stream

    def show_more(self):
        print("More Details")
        print(f'College : {self.college}')
        print(f'Class : {self.klass}')
        print(f'Stream : {self.stream}')

class Coder(Student):

    def __init__(self, name, gender, klass, college, stream, prog_langs=[]):
        super().__init__(name, gender, klass, college, stream)
        self.prglangs = prog_langs

    def coding_experience(self):
        if len(self.prglangs) == 0:
            print(f"I, {self.name} dont know any programmig language")
        else:
            print(f"I, {self.name} know following programming language")
            for lang in self.prglangs:
                print(f"=> {lang}")
            print('---' * 20)

    def add_language(self, lang):
        self.prglangs.append(lang)

if __name__=="__main__":

    p = Person("John Cena", gender="male")
    p.show()

    std1 = Student('Ankit','male','Python class','digipodium','Data Science')
    std1.show()
    std1.show_more()

    coder = Coder('Tony stark', 'male', '9th', 'MIT','Computers')
    coder.show()
    coder.show_more()
    coder.coding_experience()
    print('Ek saal baad')
    coder.add_language('Python')
    coder.add_language('Java')
    coder.add_language('C++')
    coder.coding_experience()
