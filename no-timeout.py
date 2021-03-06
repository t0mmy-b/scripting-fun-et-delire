#!/usr/bin/python
#-*-coding: utf-8-*-
import time
import getpass
import random
from Quartz.CoreGraphics import CGEventCreateKeyboardEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGHIDEventTap
from subprocess import Popen, PIPE

"""

SCRIPT "No More Timeout"
Author: tbsx (tbsx (at) protonmail (dot) com)
Realease-Date: 160918

"""
class Keyboard:
    # KEYCODES
    shiftChars = {
        '~': '`',
        '!': '1',
        '@': '2',
        '#': '3',
        '$': '4',
        '%': '5',
        '^': '6',
        '&': '7',
        '*': '8',
        '(': '9',
        ')': '0',
        '_': '-',
        '+': '=',
        '{': '[',
        '}': ']',
        '|': '\\',
        ':': ';',
        '"': '\'',
        '<': ',',
        '>': '.',
        '?': '/'
    }
    keyCodeMap = {
        'a'                 : 0x00,
        's'                 : 0x01,
        'd'                 : 0x02,
        'f'                 : 0x03,
        'h'                 : 0x04,
        'g'                 : 0x05,
        'z'                 : 0x06,
        'x'                 : 0x07,
        'c'                 : 0x08,
        'v'                 : 0x09,
        'b'                 : 0x0B,
        'q'                 : 0x0C,
        'w'                 : 0x0D,
        'e'                 : 0x0E,
        'r'                 : 0x0F,
        'y'                 : 0x10,
        't'                 : 0x11,
        '1'                 : 0x12,
        '2'                 : 0x13,
        '3'                 : 0x14,
        '4'                 : 0x15,
        '6'                 : 0x16,
        '5'                 : 0x17,
        '='                 : 0x18,
        '9'                 : 0x19,
        '7'                 : 0x1A,
        '-'                 : 0x1B,
        '8'                 : 0x1C,
        '0'                 : 0x1D,
        ']'                 : 0x1E,
        'o'                 : 0x1F,
        'u'                 : 0x20,
        '['                 : 0x21,
        'i'                 : 0x22,
        'p'                 : 0x23,
        'l'                 : 0x25,
        'j'                 : 0x26,
        '\''                : 0x27,
        'k'                 : 0x28,
        ';'                 : 0x29,
        '\\'                : 0x2A,
        ','                 : 0x2B,
        '/'                 : 0x2C,
        'n'                 : 0x2D,
        'm'                 : 0x2E,
        '.'                 : 0x2F,
        '`'                 : 0x32,
        'k.'                : 0x41,
        'k*'                : 0x43,
        'k+'                : 0x45,
        'kclear'            : 0x47,
        'k/'                : 0x4B,
        'k\n'               : 0x4C,
        'k-'                : 0x4E,
        'k='                : 0x51,
        'k0'                : 0x52,
        'k1'                : 0x53,
        'k2'                : 0x54,
        'k3'                : 0x55,
        'k4'                : 0x56,
        'k5'                : 0x57,
        'k6'                : 0x58,
        'k7'                : 0x59,
        'k8'                : 0x5B,
        'k9'                : 0x5C,
        '\n'                : 0x24,
        '\t'                : 0x30,
        ' '                 : 0x31,
        'del'               : 0x33,
        'delete'            : 0x33,
        'esc'               : 0x35,
        'escape'            : 0x35,
        'cmd'               : 0x37,
        'command'           : 0x37,
        'shift'             : 0x38,
        'caps lock'         : 0x39,
        'option'            : 0x3A,
        'ctrl'              : 0x3B,
        'control'           : 0x3B,
        'right shift'       : 0x3C,
        'rshift'            : 0x3C,
        'right option'      : 0x3D,
        'roption'           : 0x3D,
        'right control'     : 0x3E,
        'rcontrol'          : 0x3E,
        'fun'               : 0x3F,
        'function'          : 0x3F,
        'f17'               : 0x40,
        'volume up'         : 0x48,
        'volume down'       : 0x49,
        'mute'              : 0x4A,
        'f18'               : 0x4F,
        'f19'               : 0x50,
        'f20'               : 0x5A,
        'f5'                : 0x60,
        'f6'                : 0x61,
        'f7'                : 0x62,
        'f3'                : 0x63,
        'f8'                : 0x64,
        'f9'                : 0x65,
        'f11'               : 0x67,
        'f13'               : 0x69,
        'f16'               : 0x6A,
        'f14'               : 0x6B,
        'f10'               : 0x6D,
        'f12'               : 0x6F,
        'f15'               : 0x71,
        'help'              : 0x72,
        'home'              : 0x73,
        'pgup'              : 0x74,
        'page up'           : 0x74,
        'forward delete'    : 0x75,
        'f4'                : 0x76,
        'end'               : 0x77,
        'f2'                : 0x78,
        'page down'         : 0x79,
        'pgdn'              : 0x79,
        'f1'                : 0x7A,
        'left'              : 0x7B,
        'right'             : 0x7C,
        'down'              : 0x7D,
        'up'                : 0x7E
    }

    def KeyDown(self, key):
        keyCode, shiftKey = self.toKeyCode(key)
        time.sleep(0.0001)
        if  shiftKey:
            CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, 0x38, True))
            time.sleep(0.0001)
        CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, keyCode, True))
        time.sleep(0.0001)
        if  shiftKey:
            CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, 0x38, False))
            time.sleep(0.0001)

    def KeyUp(self, key):
        keyCode, shiftKey = self.toKeyCode(key)
        time.sleep(0.0001)
        CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, keyCode, False))
        time.sleep(0.0001)

    def KeyPress(self, key):
        keyCode, shiftKey = self.toKeyCode(key)
        time.sleep(0.0001)
        if  shiftKey:
            CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, 0x38, True))
            time.sleep(0.0001)
        CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, keyCode, True))
        time.sleep(0.0001)
        CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, keyCode, False))
        time.sleep(0.0001)
        if  shiftKey:
            CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, 0x38, True))
            time.sleep(0.0001)

    def toKeyCode(self, c):
        shiftKey = False
        # Letter
        if c.isalpha():
            if not c.islower():
                shiftKey = True
                c = c.lower()
        if c in Keyboard.shiftChars:
            shiftKey = True
            c = Keyboard.shiftChars[c]
        if c in Keyboard.keyCodeMap:
            keyCode = Keyboard.keyCodeMap[c]
        else:
            keyCode = ord(c)
        return keyCode, shiftKey

    def Type(self, text):
        for key in text:
            self.KeyDown(key)
            self.KeyUp(key)
            time.sleep(0.1)


class Program:
    def __init__(self):
        global passwd
        global tmp

        passwd = "1111"
        tmp = "0000"
        while passwd != tmp:
            passwd = str(getpass.getpass("Mot de passe du compte: "))
            tmp = str(getpass.getpass("Confirmation du mot de passe: "))
            if passwd != tmp:
                print("Les mots de passe ne correspondent pas.")
            verif = str(raw_input("Voulez-vous vérifier votre mot de passe ? [y/N] "))
            if (verif == 'y' or verif == 'Y'):
                print("Le mot de passe entré est: "+"\033[1;33;m"+passwd+"\033[0;32;m")
                verif2 = str(raw_input("Ce mot de passe est-il correcte ? [Y/n] "))
                if (verif2 == 'y' or verif2 == 'Y' or verif2 == None):
                    pass
                else:
                    passwd = "1111"
                    tmp = "0000"
        self.loop()

    def loop(self):
        loopTime = 600
        while 1:
            self.screenLock()
            time.sleep(loopTime)
            self.screenUnlock(passwd)
            time.sleep(3)
                

    def screenUnlock(self,passwd):
        Keyboard().KeyPress('\n')
        time.sleep(0.2)
        Keyboard().Type(passwd)
        time.sleep(0.0001)
        Keyboard().KeyPress('\n')
        self.eraseLine()
    
    def eraseLine(self):
        Keyboard().KeyDown('cmd')
        Keyboard().KeyDown('a')
        Keyboard().KeyUp('cmd')
        Keyboard().KeyUp('a')
        Keyboard().KeyPress('delete')


    def screenLock(self):
        appleScript = '''
            on run {input, parameters}
                do shell script "open /System/Library/Frameworks/ScreenSaver.framework/Versions/A/Resources/ScreenSaverEngine.app"
            end run'''
        args = ['2', '2']
        p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate(appleScript)

print("\033[1;31;m"+"DISCLAIMER:\n" \
"Ce programme a uniquement été créé dans un but pédagogique.\n" \
"Son auteur ne pourra en aucun cas être tenu pour responsable de l'utilisation qui en sera faite.\n" \
"Vous devez donc acceptez d'assumer l'entière responsabilité de vos actes.")
check = str(raw_input("Acceptez-vous ces conditions ? [y/N] "))
print("\033[0;32;m")
if (check == 'y' or check == 'Y'):
    Program()
else:
    exit()
