# Whatsapp-Blast by ELF

Whatsapp Bulk Messenger automates sending of messages via latest Whatsapp Web Version 2.2344.52

# Requirements

*  Python >= 3.10.0
*  Selenium 4.14.0
*  webdriver-manager 4.0.1

# Setup

1. Run `pip install -r requirements.txt`

# Steps

1. Enter the message you want to send inside `message.txt` file.
2. Enter the list of numbers line-separated in `listofnumbers.txt` file.
3. Change Title in line 51 'Blast WA For sales 12 Oct 2023'
4. Add attachment in line 53 and 55 or one of it if just one attachment
5. Run `python automator.py`.
6. Once the program starts, you'll see the message and count of numbers.
7. After a while, Chrome should pop-up and open web.whatsapp.com.
8. Scan the QR code to login into whatsapp.
9. Press `Enter` to start sending out messages.
10. Log failed data will be appear in failednumber.txt


