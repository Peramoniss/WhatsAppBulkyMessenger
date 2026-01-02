Must install selenium webdriver for the navigator you're using for scraping. Other requierements are available at `requirements.txt`

The idea is to have a csv in which you store informations about the people you want to snd the messages to.

The application originally had an SMTP system to send emails as well, but it was censored since there are private tokens involved with this.

To run the application, use `python bulk_messenger.py`. You start the application and log in with your whatsapp account. After that, confirm in the terminal with "Enter" that you have already logged in. Then, the hard-coded message will be passed to everyone in your csv. Bulky messaging!

WARNING:
The original code was much simpler, 6 months passed and whatsapp changed everything in the web app and none of it is working anymore. Now the only way to input images that are not considered stickers is using this pyautogui and a focus system, or with some strong reverse engineering that isn't the goal of this project. This rework will probably stop working again in 6 months anyways. Hopefully the base is helpful in any way later.