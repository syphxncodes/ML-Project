import logging
import os
from datetime import datetime


#gives us date and time
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # This specifies that every single log will be with the current working directory
os.makedirs(logs_path,exist_ok=True) #Update the file
LOG_FILE_PATH= os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


        
        