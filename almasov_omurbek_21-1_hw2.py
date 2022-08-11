class Company():
    def __init__(self):
        self.company_bank = company_bank
        self.company_name = company_name

class Person(Company):

    def __init__(self,company_bank, company_name, first_name, last_name, salary):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


    def get_salary(self):
        if self.company_bank <= self.salary:
            print("У компание не достаточно средств!")
        else:
           print(f'Вы приняты \nваша зарплата { self.company_bank - self.salary}')

     def person_info(self):
        print(f"Fullname:{self.first_name} {self.last_name} {self.salary}")

person1 = Person("500", "Табуретка Баяна","Залупкин","Петя", "700")
person1.get_salary()
person1.person_info()




