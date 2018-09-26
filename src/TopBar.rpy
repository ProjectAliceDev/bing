screen bing_top_bar():
    add "Applets/BinG/Resources/elements/topbar.png"
    style_prefix "top_bar"
    hbox:
        xfill True
        ysize 32
        
        textbutton _("Activities") action Show("ActivitiesView"):
            style "top_bar_activities_button"
            xalign 0.015

        python:
            from time import gmtime, strftime
            get_current_date = strftime("%a %B %d  %H:%M")
        label _(get_current_date):
            style "top_bar_activities_button"
            xalign 0.980

init 2:
    style top_bar_activities_button is gui_medium_button
    style top_bar_activities_button_text is gui_medium_button_text

    style top_bar_activities_button_text is aliceos_bold:
        color "#ffffff"
        size 18
        hover_color banana[300]