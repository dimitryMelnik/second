import logging

URL = "https://accounts.google.com/"
REAL_TEST_EMAIL = "checking.point.test@gmail.com"
REAL_PHONE = "+972537291566"
REAL_PW = "wordpassS2!"
WRONG_PW = ["passWord1!", "WORDPASSs2!", "wordpasss2!", "wordpasS2!", "wordpaSSS2!"]
REAL_EMAIL_MAX_SYMBOLS = "testinglongestusernamepossible@gmail.com"
REAL_EMAIL_MIN_SYMBOLS = "sixsix@gmail.com"
NEGATIVE_EMAILS = [('dmitrymelnik19888888888@gmail.com', r"Couldn’t find your Google "
                                                         r"Account"),
                   ('dmitrymelnik1988gmail.com', r"Couldn’t find your Google Account"),
                   ('dmitrymelnik1988@.com', r"Enter a valid email or phone number"),
                   ('@gmail.com', r"Enter a valid email or phone number"),
                   ('dmitrymelnik 1988@gmail.com', r"Enter a valid email or phone number"),
                   ('"dmitrymelnik1988"@gmail.com', r"Enter a valid email or phone number"),
                   ('dmitrymelnik1988[@gmail.com', r"Enter a valid email or phone number"),
                   ('dmitrymelnik1988)@gmail.com', r"Enter a valid email or phone number"),
                   ('dmitrymelnik1988:@gmail.com', r"Enter a valid email or phone number"),
                   ('dmitrymelnik1988;@gmail.com', r"Enter a valid email or phone number"),
                   ('user.name+tag+sorting!#$%&\'*+/=?^_{|}~@example.com', r"Couldn’t find your Google Account"),
                   ('+972537291567', r"Couldn't find your Google Account. Try using your email address instead."),
                   ('sixsi@gmail.com', r"Couldn’t find your Google Account"),
                   ('+97253729156', r"Enter a valid email or phone number"),
                   ('+9725372915667', r"Enter a valid email or phone number")]


