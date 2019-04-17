#!/usr/bin/env python3

import time
from notify_run import Notify

notifier = Notify()


def check_time() -> int:
    current_time = time.strftime('%-H:%-M').split(':')
    hours = [8, 10, 13, 15, 18, 20]
    if int(current_time[0]) in hours:
        return hours.index(current_time[0])
    elif int(current_time[0]) in hours and int(current_time[1]) == 30:
        return hours.index(current_time[0])
    else:
        return 0


class Content:
    def __init__(self):
        self.food = ["2xFromages Blancs 0%", "2xBlancs D'oeufs",
                     "Riz OU Légume ET Viande [BLANCHE OU ROUGE<=5%MG] OU Poisson[BLANC]",
                     "2xTranche de Jambon de poulet", "2xBlancs D'oeufs", "Légume ET Viande OU Poisson[BLANC]"]

    def alert(self):
        if check_time():
            print("[+] Notification sent@[" + time.strftime('%-H:%-M%-S')+"]")
            notifier.send(check_time(), action=None)
        else:
            print("[*] Time isn't reached...")


def main():
    print("Program started on "+ time.strftime('%B, %A %-d @%-H:%-M:%-S'))
    pusher = Content()
    while True:
        if int(time.strftime('%-H')) in [21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7]:
            print("[!] It's night time, checking every 10 minutes...")
            time.sleep(600)
        else:
            print("[*] Checking...")
            pusher.alert()
            print("[*] Rechecking in 30 seconds")
            time.sleep(30)


if __name__ == '__main__':
    main()
