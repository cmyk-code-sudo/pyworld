[app]
title = PyWorld
package.name = pyworld
package.domain = org.pyworld

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1.0

requirements = python3,kivy,numpy,jieba

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 21
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True

p4a.bootstrap = sdl2
p4a.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1