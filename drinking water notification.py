import time
#Install plyer using PIP INSTALL PLYER then this code will run
from plyer import notification

if __name__ == '__main__':

    while True:
        notification.notify(
        title = "Please drink a glass of water",
        message = " Abhishek, this is your reminder to drink Water, your skin will thank you later.....",
        timeout = 10
        )
        time.sleep(60*60)
    
    
    