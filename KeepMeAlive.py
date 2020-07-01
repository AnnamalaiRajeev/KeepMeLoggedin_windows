# Don't be Evil a choice but never a disability
# Author Annamalai Rajeev Chinnikannu
# Email - rach6572@colorado.edu
# ver 1.0
# Python 3.7
import pyautogui
import time
import random
from ctypes import Structure, windll, c_uint, sizeof, byref
pyautogui.FAILSAFE = False


class UserActivityInfo(Structure):
    _fields_ = [
        ('Size', c_uint),
        ('time', c_uint),
    ]


class AutoMouse(UserActivityInfo):

    def __init__(self):
        self._resolution = pyautogui.size()
        self._timer_default = 60 # seconds
        super().__init__()

    @property
    def _timer_default(self):
        return self.timer_default

    @_timer_default.setter
    def _timer_default(self, value):
        print("Setting default time out value...")
        self.timer_default = value

    def computeidletime1(self):
        lastInputInfo = UserActivityInfo()
        lastInputInfo.Size = sizeof(lastInputInfo)
        windll.user32.GetLastInputInfo(byref(lastInputInfo))
        millis = windll.kernel32.GetTickCount() - lastInputInfo.time
        return millis / 1000.0

    def automove(self):
        _time = random.randint(5, 30)
        time.sleep(_time)
        _x = random.randint(0, self._resolution[0])
        _y = random.randint(0, self._resolution[1])
        pyautogui.moveTo(_x, _y)
        pyautogui.moveTo(0, 0)
        pyautogui.click()


if __name__ == '__main__':
    _mouse = AutoMouse()
    while True:
        time.sleep(1)
        print(_mouse.computeidletime1())
        if _mouse.computeidletime1() >= _mouse._timer_default:
            _mouse.automove()