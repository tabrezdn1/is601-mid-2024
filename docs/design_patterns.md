# Design Patterns Implemented in the project

## Command Pattern: 
In a REPL (Read-Eval-Print Loop) application, the Command pattern is particularly useful for the following reasons:

- Modularity: Each command is encapsulated in its class, making the application's structure clean and organized.
- Extensibility: Adding new commands is straightforward and doesn't require altering existing code, facilitating easy updates and maintenance.
- Undo Operations: Supports implementing undo functionality by keeping a history of executed commands, allowing users to easily revert actions.
- Separation of Concerns: Decouples the input parsing and command execution, simplifying the main loop and enhancing code clarity.
- Easier Testing: Commands can be tested in isolation, improving the testability and reliability of the application.
The Command pattern essentially helps to keep REPL applications scalable, maintainable, and user-friendly.

Sample code from the project: 
```
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_instance: Command):
        self.commands[command_name] = command_instance

    def execute_command(self, command_name: str):
        # Easier to Ask for Forgiveness than Permission (EAFP)
        try:
            self.commands[command_name].execute()
        except KeyError: # Catch the exception if the operation fails
            print(f"No such command: {command_name}") # Exception caught and handled gracefully

    def list_commands(self):
        for index, command_name in enumerate(self.commands, start=1):
            print(f"{index}. {command_name}")

    def get_command_by_index(self, index: int):
        try:
            command_name = list(self.commands.keys())[index]
            return command_name
        except IndexError:
            return None
```

## Singleton Pattern:
Singleton Pattern
The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. This is particularly useful for:

- Controlled Access: Ensures controlled access to the sole instance, which is critical for coordinating actions across the system.
- Resource Management: Ideal for managing resources or configurations that are shared across the system.
- Consistency: Guarantees that stateful information is consistent since all code accesses a single instance.

Sample code from the project:
```
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class CommandHistoryManager(metaclass=Singleton):
    def __init__(self):
        self.history_file = 'data/command_history.csv'
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
            # Ensure that only the latest MAX_HISTORY_RECORDS are loaded
            self.history = self.history.tail(MAX_HISTORY_RECORDS)
        else:
            self.history = pd.DataFrame(columns=['Timestamp', 'Command'])

    def add_command(self, command_name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_entry = pd.DataFrame([[now, command_name]], columns=['Timestamp', 'Command'])
        self.history = pd.concat([self.history, new_entry], ignore_index=True).tail(MAX_HISTORY_RECORDS)
        self.save_history()

    def get_history(self):
        # Return a list of command names for backward compatibility
        return self.history['Command'].tolist()

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Timestamp', 'Command'])
        self.save_history()

    def save_history(self):
        """Saves the current command history to a CSV file."""
        self.history.to_csv(self.history_file, index=False)

    def load_history(self):
        """Loads the command history from a CSV file into a DataFrame."""
        if os.path.exists(self.history_file):
            return pd.read_csv(self.history_file)
        return pd.DataFrame(columns=['Timestamp', 'Command'])
```

## Factory Method:
The Factory Method pattern defines an interface for creating an object but lets subclasses alter the type of objects that will be created. It is beneficial for:

- Flexibility: Allows the class to defer instantiation to subclasses, providing flexibility in determining what objects are created.
- Extensibility: Supports adding new types of products without changing the existing factory's code, enhancing extensibility.
- Decoupling: Reduces the dependency between the application and concrete classes, promoting loose coupling.

Sample code from the project
```
self.command_handler.register_command("menu", MenuCommand(self.command_handler))

```

## Memento Pattern: 
The Memento pattern captures and externalizes an object's internal state so that the object can be returned to this state later. Its advantages include:

- Undo Functionality: Facilitates implementing undo mechanisms in applications by allowing the state of an object to be rolled back to a previous state.
- State Preservation: Enables saving and restoring state without exposing implementation details.
- Snapshot Handling: Useful for taking snapshots of application states, which can be restored later.

The functionality of CommandHistoryManager has a resemblance to the Memento pattern, which is used to capture and externalize an object's internal state so that the object can be restored to this state later.

Sample code from the project
```
class CommandHistoryManager(metaclass=Singleton):
    def __init__(self):
        self.history_file = 'data/command_history.csv'
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
            # Ensure that only the latest MAX_HISTORY_RECORDS are loaded
            self.history = self.history.tail(MAX_HISTORY_RECORDS)
        else:
            self.history = pd.DataFrame(columns=['Timestamp', 'Command'])

    def add_command(self, command_name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_entry = pd.DataFrame([[now, command_name]], columns=['Timestamp', 'Command'])
        self.history = pd.concat([self.history, new_entry], ignore_index=True).tail(MAX_HISTORY_RECORDS)
        self.save_history()

    def get_history(self):
        # Return a list of command names for backward compatibility
        return self.history['Command'].tolist()

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Timestamp', 'Command'])
        self.save_history()

    def save_history(self):
        """Saves the current command history to a CSV file."""
        self.history.to_csv(self.history_file, index=False)

    def load_history(self):
        """Loads the command history from a CSV file into a DataFrame."""
        if os.path.exists(self.history_file):
            return pd.read_csv(self.history_file)
        return pd.DataFrame(columns=['Timestamp', 'Command'])

```

## Strategy Pattern: 
The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This allows the algorithm to vary independently from clients that use it. Its benefits are:

- Flexibility: Clients can switch algorithms (strategies) at runtime, providing significant flexibility.
- Isolation: Isolates the implementation details of algorithms from the code that uses them.
- Extensibility: New strategies can be introduced without changing the context, making the application more extensible.

CSV command could also have been implemented with Strategy Pattern, but that would mean we have to manually register the command and add conditions check to plugin architecture. Manually registering CSV command with Strategy Pattern would look something like this:

```
sort_and_reduce_strategy = SortAndReduceStrategy(sort_by='Population', columns_to_keep=['State Abbreviation', 'State Name', 'Population'])
csv_command = CsvCommand(strategy=sort_and_reduce_strategy)
csv_command.execute()
```
