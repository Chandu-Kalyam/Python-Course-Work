import os  # this will help to create the log file in the directory.
from datetime import datetime  # This helps to find current date and time.
import logging  # this will help to log the messages.
# Create a folder/ directory
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True) # create a logs folder if dont exist..

# Create a log file which will store the logs of the program.
# Give file name based upon date andd time.
log_file = os.path.join(log_dir, f"ML_pipeline_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

#  Writing logs inside the created log file.
logging.basicConfig(
    filename=log_file,  # The log file where the logs will be written.
    level=logging.ERROR, # The level of logging. It can be DEBUG, INFO, WARNING, ERROR, CRITICAL.
    format='%(asctime)s - %(levelname)s - %(message)s',
   
)

logging.debug("This is a debug log .... message")
logging.info("This is an info log .... message")
logging.warning("This is a warning log .... message")
logging.error("This is an error log .... message")
logging.critical("This is a critical log .... message")