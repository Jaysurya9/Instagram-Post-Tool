# InstagramPostman
Post a picture automatically on Instagram using Python

Prerequisites: Python Programming Language

Step 1: Install 'instabot' package using the below command in the terminal.

    pip install instabot
    
Step 2: Import class 'Bot' from 'instabot' package.

    from instabot import Bot 


Step 3: Create a varibale let’s say 'bot' and store the class 'Bot' in it.

    bot = Bot() 
    
Step 4: Login to your instagram account using the below command. Provide your Instagram 'username' and 'password'.

    bot.login(username = "******", password = "**********") 
    
Step 5: Upload your photo using the following command.

    bot.upload_photo("source_path/images/*.jpg", caption ="Post Info")


