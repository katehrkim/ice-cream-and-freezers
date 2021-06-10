# Will you need other classes? What attributes will those classes have?
# How will classes talk to each other?

# - As a ice cream maker, I want to make different types of ice cream (peanut butter, chocolate chip, etc.).
# - As a ice cream maker, I want to place batches of ice cream in an freezer.
# - As a ice cream maker, I want to know when a batch of ice cream is ready to be removed from the freezer.

# 1. Make one freezer (it will store lists of ice creams)
# 2. Initialize ice creams (flavor, time required in minutes, status, time passed in minutes)
from enum import Enum

class Status(Enum):
    WATERY = 1
    ALMOST_READY = 2
    READY = 3
    FREEZER_BURNED = 4

class IceCream:
    def __init__(self, flavor):
        self.flavor = flavor
        if flavor == 'peanut butter':
            self.time_required = 30
        elif flavor == 'chocolate chip':
            self.time_required = 45
        elif flavor == 'strawberry cheesecake':
            self.time_required = 65
        else:
            print("Sorry! We don't sell that flavor. Please come back another time!")
            quit()
        self.time_passed = 0
        self.status = Status.WATERY
        self.update_status()
    
    def update_status(self):
        if self.time_passed >= self.time_required * 2:
            self.status = Status.FREEZER_BURNED
        elif self.time_passed >= self.time_required:
            self.status = Status.READY
        elif self.time_passed >= self.time_required / 2:
            self.status = Status.ALMOST_READY
        else:
            self.status = Status.WATERY
        
class Freezer:
    def __init__(self):
        self.freezer = []
    
    def pass_time(self, amount):
        for each in self.freezer:
            each.time_passed += amount
            each.update_status()

    def print_status(self):
        for each in self.freezer:
            print(f'{each.flavor}: {each.time_passed} passed out of {each.time_required} - {each.status}')

    def add_ice_cream(self, flavor):
        ice_cream = IceCream(flavor)
        self.freezer.append(ice_cream)
        print(f'Added {flavor} flavored ice cream to the freezer!')

    def take_out_ice_cream(self, flavor):
        harvested = None
        for i, each in enumerate(self.freezer):
            if each.flavor == flavor:
                if each.status == Status.FREEZER_BURNED:
                    self.freezer.pop(i)
                    print('Freezer burned:( Throwing ice cream away...')
                if each.status == Status.READY:
                    harvested = self.freezer.pop(i)
        if harvested == None:
            print('Sorry! Your ice cream is not ready.')
        else:
            print(f'Your {flavor} flavored ice cream is ready to eat!')

ice_cream_machine = Freezer()
while True:
    user_input = input('Please choose an option:\n1. Add ice cream\n2. Take out ice cream\n3. Print status\n4. Pass time\n5. Quit\n> ')
    if user_input == '1':
        answer = input('Which flavor? Options are:\n- peanut butter\n- chocolate chip\n- strawberry cheesecake\n> ')
        ice_cream_machine.add_ice_cream(answer)
    elif user_input == '2':
        answer = input('Which flavor? Options are:\n- peanut butter\n- chocolate chip\n- strawberry cheesecake\n> ')
        ice_cream_machine.take_out_ice_cream(answer)
    elif user_input == '3':
        ice_cream_machine.print_status()
    elif user_input == '4':
        answer = input('How much time (in minutes)?: ')

        ice_cream_machine.pass_time(int(answer))
    else:
        break

