class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름:",areum.name,"나이:",areum.age,"성별:",areum.sex)

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름",25,"여자")
areum.who()
areum.setInfo("지승",30,"남자")
areum.who()