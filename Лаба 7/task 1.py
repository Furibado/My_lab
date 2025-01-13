class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f'Имя сотрудника: {self.name}; айди сотрудника: {self.id}'

class Manager(Employee):

    def __init__(self, name, id, department, **kwargs):
        super().__init__(name, id, **kwargs)
        self.department = department

    def get_info(self):
        return f'Имя сотрудника: {self.name}; айди сотрудника: {self.id}; отдел: {self.department}'

    def manage_project(self):
        return f'{self.name} из отдела: {self.department} управляет проектами'

class Technician(Employee):

    def __init__(self, name, id, specialization, **kwargs):
        super().__init__(name, id, **kwargs)
        self.specialization = specialization

    def get_info(self):
        return f'Имя сотрудника: {self.name}; айди сотрудника: {self.id}; специальность: {self.specialization}'

    def perform_maintenance(self):
        return f'{self.name} со специальностью: {self.specialization} выполняет техническое обслуживание'

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization, spisok_workerov = []):
        super().__init__(name, id, department = department, specialization = specialization)
        self.spisok_workerov = spisok_workerov

    def get_info(self):
        return f'Имя сотрудника: {self.name}; айди сотрудника: {self.id}; отдел: {self.department}; специальность: {self.specialization}'
    def work(self):
        return f'{self.name} из отдела: {self.department} со специальностью: {self.specialization} выполняет работу'

    def add_employee(self, worker):
        self.spisok_workerov.append(worker)

    def get_team_info(self):
        for i in self.spisok_workerov:
            print(i.get_info())

employee = Employee("Leonardo", "1")
print(employee.get_info())
manager = Manager("Peter", "2", "Otdih")
print(manager.manage_project())
technician = Technician("John", "3", "testirovchik")
print(technician.perform_maintenance())
techmanager = TechManager("Robert", "4", "uborka", "podmetat", [])
print(techmanager.work())
techmanager.add_employee(manager)
techmanager.add_employee(employee)
techmanager.add_employee(technician)
techmanager.get_team_info()










