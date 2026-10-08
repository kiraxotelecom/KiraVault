# Buildozer spec for KiraVault — Google Colab (Linux) build
# Pure Python + Kivy app, single-arch (arm64-v8a) APK.

[app]

# (str) Title of your application
title = KiraVault

# (str) Package name
package.name = kiravault

# (str) Package domain (needed for android/ios packaging)
package.domain = com.kiravault

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude
source.exclude_exts = spec,log,md,txt

# (list) List of directories to exclude
source.exclude_dirs = tests, bin, venv, .venv, .buildozer, __pycache__, backups

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,*.pyc,*.bak,*.log

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0,pyjnius,plyer,android

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/my_icon.png

# (list) Supported orientations
orientation = portrait

# (list) List of services to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

# Kivy version to use
osx.kivy_version = 2.2.0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
#
#   POST_NOTIFICATIONS     - needed on Android 13+ for reminder notifications
#   WRITE_EXTERNAL_STORAGE - needed on Android 9 and below for the backup copy
#   READ_EXTERNAL_STORAGE  - companion, so a restore can read its own backups
android.permissions = POST_NOTIFICATIONS, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 24

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. Usually matches android.minapi.
#android.ndk_api = 24

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android SDK
# android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
#
# NOTE (KiraVault): Not needed for the current build. autobackup.py uses Android's
# MediaStore Downloads API (API >= 29) which works without extra manifest XML.
# Only add the file below if a future version needs to talk to other apps.
#android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra xml to write directly inside the <manifest><application> tag
#android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (str) Full name including package path of the Java class that implements Python Service
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (bool) If True, your application will be listed as a home app (launcher app)
# android.home_app = False

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory.
#android.add_assets =

# (list) Put these files or directories in the apk res directory.
#android.add_resources =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support.
#android.enable_androidx = True

# (list) add java compile options
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add
#android.add_gradle_repositories =

# (list) packaging options to add
#android.add_packaging_options =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (list) Copy these files to src/main/res/xml/
#android.res_xml = PATH_TO_FILE,

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (str) screenOrientation to set for the main activity.
#android.manifest.orientation = fullSensor

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add
#android.library_references =

# (list) Android shared libraries to add to AndroidManifest.xml
#android.uses_library =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
#android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for.
#
# NOTE (KiraVault): Building ONLY arm64-v8a — covers every modern Android phone
# (2017 onward) and makes the first build roughly twice as fast.
# To also support very old 32-bit phones, use:
#     android.archs = arm64-v8a, armeabi-v7a
android.archs = arm64-v8a

# (int) overrides automatic versionCode computation
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
#
# NOTE (KiraVault): Android's own Auto Backup, separate from autobackup.py.
# Leave True — a second safety net for the SQLite database.
android.allow_backup = True

# (str) XML file for custom backup rules
# android.backup_rules =

# (str) manifest placeholders
# android.manifest_placeholders = [:]

# (bool) Skip byte compile for .py files
# android.no-byte-compile-python = False

# (str) The format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
# android.debug_artifact = apk

# (str) Display cutout mode for Android API >= 28
#android.display_cutout = never

#
# Python for android (p4a) specific
#

# NOTE (KiraVault): On Colab, p4a installs its prerequisites cleanly with apt.
# We use the default branch — no pins, no Mac workarounds.
#p4a.branch = master
#p4a.commit = HEAD

# (str) python-for-android URL to use for checkout
#p4a.url =

# (str) python-for-android fork
#p4a.fork = kivy

# (str) python-for-android git clone directory
#p4a.source_dir =

# (str) The directory with your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to pass to p4a
#p4a.port =

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
#p4a.setup_py = false

# (str) extra command line arguments to pass to p4a
#p4a.extra_args =

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
#ios.ios_deploy_dir = ../ios_deploy
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2

# (bool) Whether or not to sign the code
ios.codesign.allowed = false

# iOS signing settings (not used for Android builds)
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"
#ios.codesign.development_team.debug = <hexstring>
#ios.codesign.release = %(ios.codesign.debug)s
#ios.codesign.development_team.release = <hexstring>

# iOS usage descriptions
#ios.media_usage_description = "<APP> needs to access your media in order to <Do X and Y and Z> "
#ios.local_network_usage_description = "<App> needs permissions to <Do X and Y and Z> in your Local Area Network"
#ios.camera_usage_description = "<App> uses Camera to do <X and Y and Z>"

# (bool) Allow StatusBar to be controlled by API
# ios.viewcontroller_based_statusbar_appearance = False

# iOS .ipa manifest URLs (not used for Android builds)
#ios.manifest.app_url =
#ios.manifest.display_image_url =
#ios.manifest.full_size_image_url =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin