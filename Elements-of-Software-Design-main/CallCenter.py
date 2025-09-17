from collections import deque
class Call:
    def __init__(self,caller_id):
        self.caller_id = caller_id
        self.level = 0 # 0: Respondent, 1: Manager, 2: Director

    def escalate(self):
        if self.level<2:
            self.level += 1

class Employee:
    def __init__(self, name):
        self.name = name
        self.free = True
        self.current_call = None

    def take_call(self, call: Call):
        self.free = False
        self.current_call = call
        print(f"{self.name} is handling call from {call.caller_id}")

    def finish_call(self):
        finished = self.current_call
        self.free = True
        self.current_call = None
        print(f"{self.name} has ended their handling of the call")
        return finished

    def __str__(self):
        return f"{self.name}"

class Respondent(Employee):
    pass

class Manager(Employee):
    pass
class Director(Employee):
    pass

class CallCenter:
    def __init__(self):
        self.employee = {0:[],1:[], 2:[]}
        self.waiting_calls = deque()

    def add_employee(self,employee: Employee, level):
        print("adding:", employee.name,level)
        self.employee[level].append(employee)

    def employee_list(self):
        return self.employee

    def dispatch_call(self, call: Call):
        for lvl in range(call.level, 3):
            for emp in self.employee[lvl]:
                if emp.free:
                    emp.take_call(call)
                    return
        print(f"No available employees. Call from {call.caller_id} added to the queue")
        self.waiting_calls.append(call)

    def escalate_call(self, call:Call):
        call.escalate()
        self.dispatch_call(call)

    def employee_finished(self,employee:Employee, handled = True):
        call = employee.finish_call()

        if not handled:
            print(f"{employee.name} could not resolve call {call.caller_id}; escalating")
            self.escalate_call(call)
        else:
            if self.waiting_calls:
                next_call = self.waiting_calls.popleft()
                self.dispatch_call(next_call)

    def __str__(self):
        return f"{self.employee}"

if __name__ == "__main__":
        cc = CallCenter()

        cc.add_employee(Respondent("Ali"),0)
        cc.add_employee(Respondent("Bop"),0)
        cc.add_employee(Manager("Che"), 1)
        cc.add_employee(Director("Dye"), 2)


        c1 = Call("caller1")
        c2 = Call("caller2")
        c3 = Call("caller3")

        cc.dispatch_call(c1)
        cc.dispatch_call(c2)
        cc.dispatch_call(c3)

        #escalation part
        cc.employee_finished(cc.employee[0][0], handled = False)
        #went smoothly
        cc.employee_finished(cc.employee[0][1], handled = True)




