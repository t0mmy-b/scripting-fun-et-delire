import androidhelper
import time

service = "bluetooth"
droid = androidhelper.Android()
droid.dialogCreateAlert("You need to turn on {0}".format(service))
droid.dialogSetPositiveButtonText("Turn on")
droid.dialogSetNegativeButtonText("Exit")

ans = droid.dialogGetResponse()

print(ans)