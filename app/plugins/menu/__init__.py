from app.commands import Command

class MenuCommand(Command):
    def execute(self, *args):
        print(f'You entered the \'menu\' command.')
