class Employee:
    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.id = employee_id
    
    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}"
    
class Manager(Employee):
    def __init__(self, name: str, employee_id: int, department: str):
        Employee.__init__(self, name, employee_id)
        self.department = department
    
    def get_info(self):
        base_info = Employee.get_info(self)
        return f"{base_info}, Должность: Менеджер, Отдел: {self.department}"

    def manage_project(self, project_name: str):
        return f"{self.name} наставник проекта '{project_name}'"
    
class Technician(Employee):
    def __init__(self, name: str, employee_id: int, specialization: str):
        Employee.__init__(self, name, employee_id)
        self.specialization = specialization
    
    def get_info(self):
        base_info = Employee.get_info(self)
        return f"{base_info}, Должность: Техник, Специализация: {self.specialization}"

    def perform_maintenance(self, equipment: str):
        return f"{self.name} ({self.specialization}) выполняет обслуживание {equipment}"
    
class TechManager(Manager, Technician):
    def __init__(self, name: str, employee_id: int, department: str, specialization: str):
        Manager.__init__(self, name, employee_id, department)
        Technician.__init__(self, name, employee_id, specialization)
        self.subordinates = []
       
    def get_info(self):
        base_info = Employee.get_info(self)
        return f"Имя: {self.name}, ID: {self.id}, Должность: Технический менеджер, Отдел: {self.department}, Специализация: {self.specialization}"

    def add_employee(self, employee: Employee) -> str: #5
        self.subordinates.append(employee)
        return f"Сотрудник {employee.name} добавлен в подчинение {self.name}"
    
    def get_team_info(self) -> str:
        if not self.subordinates:
            return f"У {self.name} нет подчинённых"
        
        team_info = [f"Команда {self.name}:"]
        for i, employee in enumerate(self.subordinates, 1):
            team_info.append(f"{i}. {employee.get_info()}")
        
        return "\n".join(team_info)
    
    def manage_project(self, project_name: str):
        return Manager.manage_project(self, project_name)
    
    def perform_maintenance(self, equipment: str):
        return Technician.perform_maintenance(self, equipment)
    
if __name__ == "__main__":
    employee = Employee("Артём", 1)
    manager = Manager("Вагиф", 2, "Маркетинг")
    technician = Technician("Макс", 3, "Электрик")
    tech_manager = TechManager("Артём", 4, "ИТ", "Системный администратор")

    tech_manager.add_employee(manager)
    tech_manager.add_employee(technician)

    print(tech_manager.get_info())
    print(tech_manager.manage_project('ОПГ'))
    print(tech_manager.perform_maintenance('оборудования'))
    print(tech_manager.get_team_info())
    
    print(manager.get_info(), manager.manage_project('ООО Ромашка'), sep="\n")
    
    print(technician.get_info(), technician.perform_maintenance('сети'), sep="\n")
