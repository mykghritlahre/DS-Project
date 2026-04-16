### Commit 2: Logging and Exception Handling

### Summary
In this commit, we have implemented logging and exception handling mechanisms in our application. The logging will help us track the application's behavior and identify issues more easily, while the custom exception handling will provide more informative error messages.

### Changes Made
1. **Logging**: Integrated logging throughout the application to capture important events and errors.
2. **Custom Exception**: Created a custom exception class to handle errors more gracefully and provide detailed error messages.


### Logging
We have set up logging at various points in the application to capture key events and errors. The logs include timestamps, log levels, and contextual information (such as file names and line numbers) to aid in debugging and monitoring the application's behavior.

#### (1) `logger.py`
- Firstly, we have created a `logger.py` module to encapsulate all logging-related functionality. This module is responsible for configuring the logging settings and providing a logger instance that can be used throughout the application.
- Created a log directory to store log files and configured the logger to write logs to a file in this directory.
- Created a log file having its name based on the current date and time to ensure uniqueness and facilitate easier log management.
- set up the basic logging configuration, including log format and log level.

``` python
import logging
import os
from datetime import datetime

log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path,exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[ %(asctime)s ] [ %(levelname)s ] [ %(name)s ] [ line: %(lineno)d ][file: %(filename)s] - %(message)s",
    level=logging.INFO
)
```

#### (2) Testing
- Import logging from this `logger.py` file as (`from src.dsproject.logger import logging`)
- Use the logging instance in your tests to capture log output and verify logging behavior.

### Exception
we have implemented a custom exception class to handle errors more gracefully. This class extends the built-in `Exception` class and adds additional context to the error messages.

#### (1) `exceptions.py`
- Created a new module called `exceptions.py` to define custom exceptions.
- Implemented a `CustomException` class that takes an error message and an optional error code.

``` python
class CustomException(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code
```

#### (2) Usage
- In the application code, we can raise `CustomException` with a specific error message and code.
- This allows us to catch and handle these exceptions in a centralized manner, providing more informative error responses.

``` python
from src.dsproject.exceptions import CustomException

def some_function():
    try:
        # Some code that may raise an exception
    except Exception as e:
        raise CustomException("An error occurred", code=500) from e
```
