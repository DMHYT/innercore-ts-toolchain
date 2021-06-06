from urllib.request import urlretrieve
from zipfile import ZipFile
from subprocess import call
from os import getcwd, rename, remove
from json import dumps
name = input("Enter your mod's name: ")
author = input("Enter your mod's author's name: ")
version = input("Enter your mod's version (any text): ")
description = input("Enter your mod's short description: ")
isClientOnly = "true" if input("Will your mod be only client? (+ / -): ") else "false"
print("Downloading template mod archive from GitHub...")
urlretrieve("https://raw.githubusercontent.com/DMHYT/innercore-ts-toolchain/main/mod-archive.zip", getcwd() + "\\mod-archive.zip")
print("Extracting archive...")
with ZipFile(getcwd() + "\\mod-archive.zip") as mod_archive:
    mod_archive.extractall(getcwd())
print("Archive has been successfully extracted!")
remove(getcwd() + "\\mod-archive.zip")
print("Archive has been successfully removed!")
def change_tsconfig():
    tsconfig_text = ""
    with(open(getcwd() + "\\tsconfig.json", 'r')) as tsconfig:
        tsconfig_text = tsconfig.read()
    tsconfig_text = tsconfig_text.replace("mod_template", name)
    with(open(getcwd() + "\\tsconfig.json", 'w')) as tsconfig:
        tsconfig.write(tsconfig_text)
change_tsconfig()
rename(getcwd() + "\\out\\mod_template\\", getcwd() + "\\out\\" + name + "\\")
with(open(getcwd() + "\\out\\" + name + "\\mod.info", 'w')) as mod_info:
    mod_info.write(dumps({
        'name': name,
        'author': author,
        'version': version,
        'description': description
    }))
with(open(getcwd() + "\\out\\" + name + "\\launcher.js", 'w')) as launcher:
    launcher.write(
        "ConfigureMultiplayer({\n    name: \"" + name + \
        "\",\n    version: \"" + version + \
        "\",\n    description: \"" + description + \
        "\",\n    isClientOnly: " + isClientOnly + \
        "\n});\nLaunch();")
print("Project was set up successfully!")
print("Downloading InnerCore TS declarations...")
print("------------------------------")
call([r'{}'.format(getcwd() + "\\tools\\docs.bat")])
print("------------------------------")
print("InnerCore TS declarations have been successfully downloaded!")
print("TOOLCHAIN SETUP PROCESS FINISHED WITH NO ERRORS!")
print("Thanks for using this mini-toolchain!")
input()