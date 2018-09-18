import androidhelper
import time
import sys

service = "bluetooth"
droid = androidhelper.Android()
droid.dialogCreateAlert("You need to turn on {0}".format(service))
droid.dialogSetPositiveButtonText("Turn on")
droid.dialogSetNegativeButtonText("Exit")

ans = droid.dialogGetResponse()

if ans[1]['which'] == 'positive':
    print("oui")
else:
    sys.exit(0)