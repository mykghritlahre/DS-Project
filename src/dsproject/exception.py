import sys
from src.dsproject.logger import logging



#(2)
# copied from documentation
def error_message_detail(error_message, error_details: sys) -> str:
    ''' This function extracts error details and logs them '''
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    logging.error(f"Error occurred in file: [{file_name}] at line: [{line_number}] - [{error_message}]")
    return f"Error occurred in file: [{file_name}] at line: [{line_number}] - [{error_message}]"


#(1)
class CustomException(Exception):
    def __init__(self,error_message, error_details : sys ):
        super().__init__(error_message)
        # self.error_message = (need a function for acessing error message details fn(error_message,error_details))
        self.error_message = error_message_detail(error_message, error_details)
    
    def __str__(self):
        return self.error_message
