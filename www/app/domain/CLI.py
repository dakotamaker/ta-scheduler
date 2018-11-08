from .DataAccess import DataAccess
from .Account import Account
from .Course import Course
from .Lab import Lab
from .CommandHandler import CommandHandler


class CLI():
    
    def run(self):
        db = DataAccess()
        Account.LoadEntity(db)
        Course.LoadEntity(db)
        Lab.LoadEntity(db)
        ch = CommandHandler(db)
        print('********************************************************************************************************************')
        print('Welcome. If you are a user that has never logged in before, perform the login command with your desired new password.')
        print('********************************************************************************************************************')
        while True:
            try:
                while True:
                    cmd = input('> ')
                    ch.ProcessCommand(cmd)
            except KeyError:
                print('Invalid command')