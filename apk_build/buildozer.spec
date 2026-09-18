[app]
# (str) Title of your application
title = HackerLocker

# (str) Package name
package.name = hackerlocker

# (str) Package domain (needed for android/ios packaging)
package.domain = org.hackerlocker

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of directory to exclude into the source.dir
source.exclude_dirs = tests, bin, .git, .github, __pycache__

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Presplash of the application
presplash.filename = %(source.dir)s/logo.png
android.presplash_color = #0A0D14

# (str) Icon of the application
icon.filename = %(source.dir)s/logo.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
android.orientation = portrait

# (bool) Indicate if the application should be fullscreen to not
android.fullscreen = 1

# (list) Permissions
# android.permissions = INTERNET,VIBRATE

# (bool) Automatically accept the Android SDK licenses (needed for CI builds)
android.accept_sdk_license = True

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android entrypoint
android.entrypoint = main.py

# (list) The Android archs to build for (arm64-v8a covers all modern phones)
android.archs = arm64-v8a

# (bool) Android UI setup
android.window_borderless = 1

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1