import sys
import logging
def error_message_details(error,error_detail:sys):

    #_,_,exc_tb are the 3 things returned by sys when called. First two arent important but exc_tb are the 3 importatnt execution information provided by sys like which file, line the exception has occured
    _,_,exc_tb=error_detail.exc_info()
    
    #now we make a variable called file_name and get the filename using the below line of code 
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    #0, 1 and 2 are placeholders which we're going to replace using the .format function
    error_message="error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(str(error_message))
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
    
'''if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("divide by 0")
        raise CustomException(e,sys)'''
#this above block is written to test if the exception is caught or not
