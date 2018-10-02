## bing.rpy
# A GNOME 3-like desktop environment
# Author(s): Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

init python:
    class BingDesktop(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "Desktop"
        long_name = "Bendy is not GNOME Desktop"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "BinG"
        author = "Project Alice"
        version = "1.0.0beta3"
        description = """\
Bendy is not GNOME is a GNOME 3-like desktop environment for AliceOS. It provides basic functionality of launching applets and file management.
        """

        # Define your icons here. They should be located in 
        # your Applet's Resources/icons/ folder
        icons = {
            16: "16.png",
            24: "24.png",
            32: "32.png",
            64: "64.png",
            128: "128.png",
            256: "256.png"
        }

        # Define what permissions your applet will need.
        # See the Applet Manifest wiki page for all possible
        # permissions
        permissions = {
            pm_notify, 
            pm_files, 
            pm_sysadmin, 
            pm_shell
        }

        launch = {
            "action": "[Hide('ActivitiesView'), Show('bing_desktop')]",
            "show_in_launcher": True
        }

        def __init__(self):
            pass    
    
    bendy = BingDesktop()

## Screen override
init 5:
    screen say(who, what):
        use bing_top_bar
        style_prefix "say"

        window:
            id "window"

            text what id "what"

            if who is not None:
                if who == s_name: #Sayori namebox
                    window:
                        style "nameboxblue"
                        text who id "who"
                if who == m_name: #Monika namebox
                    window:
                        style "nameboxgreen"
                        text who id "who"
                if who == y_name: #Yuri namebox
                    window:
                        style "nameboxpurple"
                        text who id "who"
                if who == n_name: #Natsuki namebox
                    window:
                        style "nameboxpink"
                        text who id "who"
                if who == mi_name: #Mio namebox
                    window:
                        style "nameboxred"
                        text who id "who"
                if who == sm_name: #Sayonika namebox
                    window:
                        style "nameboxteal"
                        text who id "who"
                if who == c_name: #Apple Store namebox
                    window:
                        style "namebox_apple"
                        text who id "who"
                if who == player: #MC namebox
                    window:
                        style "namebox_mc"
                        text who id "who"
                if who != s_name and who != m_name and who != y_name and who != n_name and who != player and who != sm_name and who != c_name: #Everyone else namebox
                    window:
                        style "namebox"
                        text who id "who"

        # If there's a side image, display it above the text. Do not display
        # on the phone variant - there's no room.
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0

        use quick_menu