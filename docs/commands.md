# All available commands and their functionalities with screenshots
Below is the screenshot when you run the app with `python main.py` command.

![alt text](../images/commands/all.png)

## 1. calculator:
Basic calculator option with menu-driven navigation, here's an example of sum.

![alt text](../images/commands/calc.png)

## 2. csv:
CSV command uses pandas library and reads a CSV file, and generates a new CSV file with sorting the states by population. Below is a sample usage:

![alt text](../images/commands/csv.png)

## 3. exit:
Basic exit command to exit out application.

![alt text](../images/commands/exit.png)

## 4. goodbye:
Prints out goodbye.

![alt text](../images/commands/goodbye.png)

## 5. greet:
Print with a greeting message.

![alt text](../images/commands/greet.png)

## 6. history:
All the commands that are entered are tracked into a history state, which can be accessed by this command. Same as the calculator command even this is nested and 0 is used to navigate back. Here is an example of the load and delete command from the history command.

![alt text](../images/commands/history.png)
## 7. openai:
This is an extension command for integrating the OPEN AI chatbot, with customized Agent. Professor has showcased Movie Agent, which will be integrated with LangChain. This is not part of the requirement and is completely independent, please exclude this from grading. However, this is documented as part of project documentation. Hope this will not cause any confusion.

![alt text](../images/commands/openai.png)
## 8. menu:
This is a menu command, which basically prints out all the registered commands, to extend this further - this menu command also runs in itself, as in every option selected from the menu command output works. Here is a sample of the exit implemented from the menu command.

![alt text](../images/commands/menu.png)
