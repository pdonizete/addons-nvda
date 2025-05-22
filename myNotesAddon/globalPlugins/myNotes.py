# This is the main plugin file for MyNotes
# It will contain the core logic for copying selected text and saving it to a notes file.

# Import necessary NVDA modules
import globalPluginHandler
import scriptHandler
import addonHandler

# Initialize translations
addonHandler.initTranslation()
_ = addonHandler.translation.gettext

import api
import ui
import os
# wx can be used for file dialogs, not used in this version
# import wx 
# shutil is for file operations, not strictly needed for simple text append
# import shutil 
# focusHandler might be an alternative to api.getNavigatorObject() in some cases
# import focusHandler 
import textInfos

# Define the plugin class
class MyNotesPlugin(globalPluginHandler.GlobalPlugin):
    
    @scriptHandler.script(gesture="kb:control+insert+q")
    def script_copySelectedText(self, gesture):
        """
        Copies the selected text and appends it to a notes file.
        """
        try:
            nav = api.getNavigatorObject()
            text_info = textInfos.TextInfo(nav)
            text_info.expand(textInfos.UNIT_SELECTION)
            selected_text = text_info.text

            if selected_text:
                notes_file_path = os.path.expanduser("~/.my_nvda_notes.txt")
                try:
                    with open(notes_file_path, "a", encoding="utf-8") as f:
                        f.write(selected_text + "\n")
                    ui.message(_("Text copied to notes."))
                except IOError as e:
                    ui.message(_("Error writing to notes file: {error}").format(error=e))
                    # Optionally, log the error for debugging
                    # import logging
                    # logging.error(f"MyNotesPlugin: Error writing to file: {e}")
            else:
                ui.message(_("No text selected."))
        except Exception as e:
            # Catch any other unexpected errors during script execution
            ui.message(_("An unexpected error occurred: {error}").format(error=e))
            # Optionally, log the error
            # import logging
            # logging.error(f"MyNotesPlugin: Unexpected error in script_copySelectedText: {e}")

    @scriptHandler.script(gesture="kb:control+insert+a")
    def script_showNotes(self, gesture):
        """
        Reads the notes file and displays its content in a browseable message.
        """
        notes_file_path = os.path.expanduser("~/.my_nvda_notes.txt")
        try:
            if os.path.exists(notes_file_path) and os.path.getsize(notes_file_path) > 0:
                with open(notes_file_path, "r", encoding="utf-8") as f:
                    notes_content = f.read()
                ui.browseableMessage(notes_content, title=_("My Saved Notes"))
            else:
                ui.message(_("No notes found."))
        except IOError as e:
            ui.message(_("Error reading notes file: {error}").format(error=e))
            # Optionally, log the error
            # import logging
            # logging.error(f"MyNotesPlugin: Error reading file: {e}")
        except Exception as e:
            # Catch any other unexpected errors during script execution
            ui.message(_("An unexpected error occurred while showing notes: {error}").format(error=e))
            # Optionally, log the error
            # import logging
            # logging.error(f"MyNotesPlugin: Unexpected error in script_showNotes: {e}")

    # If you want to keep the old gesture or add new ones, you can define them here.
    # For this task, we are only using the decorator method for the new gesture.
    # __gestures = {
    # "kb:control+shift+c": "someOtherFunction", # Example if you had other functions
    # }

# NVDA automatically discovers and loads GlobalPlugin classes.
# No explicit instantiation is needed here.
