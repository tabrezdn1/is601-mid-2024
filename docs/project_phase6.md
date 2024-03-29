# Sample screenshot of project phase 6 working setup
![alt text](../images/phase6.png)

This phase focuses on adding data-related operations and also implementing any further design pattern concepts.

## Added features to the project as part of this phase:
1. New command - history
- Every command is stored in a history state, and as this will only have one instance, therefore using the Singleton Design Pattern is the right choice. This history is again a sub-menu command with operations like LOAD, CLEAR, SAVE, and DELETE a particular command, that gets recorded in history. All this history also gets added to a CSV file using pandas when the operations(menu options) are executed.
2. New command - csv
- Applying the concept of data structures and using pandas and numpy, the CSV command reads a CSV file, sorts the data and creates a new file, and saves it. (Here in this case we have data from a few US states and we sort this data based on population and generate a new file, the sorting is in ascending order).

## Run the app
- `python main.py`

## Testing Commands

- Run all tests with `pytest`.
- To test a specific file, use `pytest tests/test_main.py`.
- For linting and coverage, `pytest --pylint --cov` commands can be used separately.