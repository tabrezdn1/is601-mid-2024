import logging
from app.commands import Command

class Chat(Command):
    def execute(self):
        logging.info("Chat command executed: Engaging with AI.")
        print(f"Hi this is AI")  # Maintain user interaction