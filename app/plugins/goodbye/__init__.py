import logging
from app.commands import Command

class GoodbyeCommand(Command):
    def execute(self):
        logging.info("Executing GoodbyeCommand.")  # Log the execution of the GoodbyeCommand
        print("Goodbye")  # Keep this for user interaction
        logging.info("GoodbyeCommand executed successfully.")  # Optionally log successful execution