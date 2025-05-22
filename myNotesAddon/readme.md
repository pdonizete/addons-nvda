# MyNotes Add-on for NVDA

*   **Author:** Jules
*   **Version:** 1.0

## Description

MyNotes is an NVDA add-on that allows you to quickly save snippets of selected text to a personal notes file and easily view your collected notes whenever you need them. It's designed to be a simple and efficient way to keep track of important information you come across while using your computer.

## Features

*   **Copy Selected Text:** Instantly copy any selected text from your current application and append it to your notes file.
*   **View Saved Notes:** Open a browseable window to view all the notes you have saved.

## Installation

1.  **Download:** Download the `MyNotes-X.Y.nvda-addon` file (where X.Y is the version number).
2.  **Install:**
    *   Open NVDA.
    *   Go to the NVDA menu (NVDA+N).
    *   Navigate to "Tools" and then select "Manage add-ons."
    *   Click the "Install..." button.
    *   In the file dialog, browse to and select the downloaded `.nvda-addon` file.
    *   Confirm the installation when prompted. NVDA may need to restart.

## How to Use

### Copying Text to Notes

1.  Select the text you want to save in any application (e.g., a sentence in your web browser, a paragraph in a document).
2.  Press the shortcut: `Control+Insert+Q`.
3.  NVDA will announce "Text copied to notes" if successful, or an error message if something went wrong.

### Viewing Your Notes

1.  Press the shortcut: `Control+Insert+A`.
2.  A window titled "My Saved Notes" will appear, displaying all the text you have previously saved. You can navigate this window like any other text document in NVDA (e.g., using arrow keys).

## Notes File Location

Your notes are saved in a plain text file named `.my_nvda_notes.txt`. This file is located in your user's home directory.

*   On Windows, this is typically `C:\Users\YourUserName\.my_nvda_notes.txt` (replace `YourUserName` with your actual Windows username).
*   On Linux or macOS (if you were to use parts of this code there), `~` refers to your home directory (e.g., `/home/yourusername/`).

The `.` at the beginning of the filename might make it a hidden file on some systems, but it's just a regular text file that you can also open with any text editor if needed.

## Troubleshooting and Feedback

If you encounter any issues or have feedback or suggestions for improving MyNotes, please report them via the GitHub repository: [https://github.com/yourusername/MyNotesAddon](https://github.com/yourusername/MyNotesAddon) (Note: This is a placeholder URL from the add-on manifest).

## License

This add-on is released under the MIT License. (Optional - if you choose to include a license)
