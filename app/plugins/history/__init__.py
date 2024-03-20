from app.commands import Command, CommandHistoryManager


class HistoryCommand(Command):
    def execute(self):
        command_history = CommandHistoryManager()
        history = command_history.get_history()
        print("Command History:")
        for command in history:
            print(command)
