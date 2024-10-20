import board
import digitalio
import storage
from kmk.bootcfg import bootcfg

bootValue = bootcfg(
    sense=digitalio.DigitalInOut(board.GP0),
    source=digitalio.DigitalInOut(board.GP14),
    usb_id=('peachKB', 'peach_keyboard'),
)

if(bootValue):
    storage.disable_usb_drive()
