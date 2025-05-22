# Test Plan for "MyNotes" NVDA Add-on

This document outlines the manual test plan for the "MyNotes" NVDA add-on.

## Test Environment

*   **NVDA Version:** Test with the `minNVDAVersion` (2019.3) and `lastTestedNVDAVersion` (2023.1) as specified in `addon.json`, and ideally the latest stable NVDA release.
*   **Operating System:** Windows (as NVDA is primarily a Windows screen reader).
*   **Applications for Testing Text Copying:**
    *   Web Browsers: Firefox (latest), Chrome (latest)
    *   Text Editors: Notepad, Notepad++
    *   Productivity Software: Microsoft Word (if available), LibreOffice Writer

## 1. Core Functionality - Copying Notes

*   **Test Case 1.1:** Select text in a web browser (e.g., Firefox, Chrome) and press `Control+Insert+Q`.
    *   **Steps:**
        1.  Open a web browser.
        2.  Navigate to any webpage with selectable text.
        3.  Select a short piece of text (e.g., a sentence).
        4.  Press `Control+Insert+Q`.
    *   **Expected:**
        *   NVDA announces: "Text copied to notes." (or its translated equivalent).
        *   The selected text is appended to `~/.my_nvda_notes.txt`.
        *   Verify the file content manually.

*   **Test Case 1.2:** Press `Control+Insert+Q` without any text selected.
    *   **Steps:**
        1.  Ensure no text is selected in the current application focus.
        2.  Press `Control+Insert+Q`.
    *   **Expected:**
        *   NVDA announces: "No text selected." (or its translated equivalent).
        *   The `~/.my_nvda_notes.txt` file remains unchanged (if it exists) or is not created.

*   **Test Case 1.3:** Copy multiple pieces of text sequentially from different applications.
    *   **Steps:**
        1.  Select and copy text from a web browser using `Control+Insert+Q`.
        2.  Select and copy text from Notepad using `Control+Insert+Q`.
        3.  Select and copy another piece of text from the web browser.
    *   **Expected:**
        *   Each piece of text is appended to the `~/.my_nvda_notes.txt` file in the correct order.
        *   Verify the file content manually.

*   **Test Case 1.4:** Try copying very long text.
    *   **Steps:**
        1.  Select a large block of text (e.g., several paragraphs or a whole article page).
        2.  Press `Control+Insert+Q`.
    *   **Expected:**
        *   Text is copied successfully.
        *   NVDA announces: "Text copied to notes."
        *   Verify the content in `~/.my_nvda_notes.txt` (it might be truncated if there are system limits, but the add-on should handle it gracefully).

*   **Test Case 1.5 (Manual Check):** Verify the content of `~/.my_nvda_notes.txt` after several copy operations.
    *   **Steps:**
        1.  Perform several copy operations as described in previous test cases.
        2.  Open `~/.my_nvda_notes.txt` using a text editor.
    *   **Expected:**
        *   Content matches all the text snippets that were copied.
        *   Each copied snippet appears on a new line.
        *   Text encoding (UTF-8) is preserved for special characters.

## 2. Core Functionality - Viewing Notes

*   **Test Case 2.1:** Press `Control+Insert+A` when the notes file contains text.
    *   **Steps:**
        1.  Ensure `~/.my_nvda_notes.txt` contains some text (perform copy operations if needed).
        2.  Press `Control+Insert+A`.
    *   **Expected:**
        *   A browseable message dialog appears.
        *   The title of the dialog is "My Saved Notes" (or its translated equivalent).
        *   The content of the dialog matches the content of `~/.my_nvda_notes.txt`.
        *   Standard NVDA navigation commands (arrow keys, page up/down, etc.) work within the dialog.
        *   The dialog can be closed (e.g., with Escape key).

*   **Test Case 2.2:** Press `Control+Insert+A` when the notes file is empty.
    *   **Steps:**
        1.  Ensure `~/.my_nvda_notes.txt` exists but is empty (0 bytes).
        2.  Press `Control+Insert+A`.
    *   **Expected:**
        *   NVDA announces: "No notes found." (or its translated equivalent).
        *   No dialog appears.

*   **Test Case 2.3:** Press `Control+Insert+A` when the notes file does not exist.
    *   **Steps:**
        1.  Ensure `~/.my_nvda_notes.txt` does not exist (e.g., delete it if it was created).
        2.  Press `Control+Insert+A`.
    *   **Expected:**
        *   NVDA announces: "No notes found." (or its translated equivalent).
        *   No dialog appears.

*   **Test Case 2.4:** View notes after adding multiple entries of varying lengths.
    *   **Steps:**
        1.  Copy a short sentence.
        2.  Copy a long paragraph.
        3.  Copy another short phrase.
        4.  Press `Control+Insert+A`.
    *   **Expected:**
        *   All entries are displayed correctly in the browseable dialog in the order they were added.
        *   Formatting (newlines between entries) is correct.

## 3. Error Handling (Simulated if necessary)

*   **Test Case 3.1 (Conceptual - Manual Simulation):** Notes file becomes unwritable.
    *   **Steps:**
        1.  Create `~/.my_nvda_notes.txt` and copy some text to it.
        2.  Change the permissions of `~/.my_nvda_notes.txt` to read-only (e.g., via file properties in Windows Explorer).
        3.  Try to copy new selected text using `Control+Insert+Q`.
    *   **Expected:**
        *   NVDA announces an error message similar to: "Error writing to notes file: [specific error like PermissionError]" (or its translated equivalent).
    *   **Cleanup:** Restore write permissions to the file.

*   **Test Case 3.2 (Conceptual - Manual Simulation):** Notes file is corrupted (e.g., invalid UTF-8 sequence if manual edit).
    *   **Steps:**
        1.  Create `~/.my_nvda_notes.txt` and copy some text.
        2.  Manually open the file with an editor that allows saving with a different encoding, and save it with an encoding that introduces characters invalid for UTF-8, or manually insert invalid byte sequences.
        3.  Try to view notes using `Control+Insert+A`.
    *   **Expected:**
        *   NVDA announces an error message similar to: "Error reading notes file: [specific error like UnicodeDecodeError]" (or its translated equivalent).
        *   Alternatively, the browseable message might display replacement characters for the corrupted parts, but the add-on should not crash.
    *   **Cleanup:** Delete or fix the corrupted notes file.

## 4. Add-on Installation and Structure

*   **Test Case 4.1:** Build the add-on.
    *   **Steps:**
        1.  Run `scons` in the `myNotesAddon` directory (or download the artifact from GitHub Actions if set up).
    *   **Expected:**
        *   A file named `myNotesAddon-1.0.nvda-addon` (or reflecting the current version in `addon.json`) is created in the `myNotesAddon` directory.
        *   No build errors are reported.

*   **Test Case 4.2:** Install the generated `.nvda-addon` file in NVDA.
    *   **Steps:**
        1.  Open NVDA.
        2.  Navigate to NVDA Menu -> Tools -> Manage add-ons.
        3.  Click "Install..." and select the generated `myNotesAddon-X.Y.nvda-addon` file.
        4.  Follow the on-screen prompts to install and restart NVDA if prompted.
    *   **Expected:**
        *   The add-on installs without errors.
        *   After NVDA restarts (if it did), the MyNotes add-on is listed in the "Manage add-ons" dialog with status "Running" or "Enabled".

*   **Test Case 4.3:** Check add-on information in "Manage add-ons".
    *   **Steps:**
        1.  Go to NVDA Menu -> Tools -> Manage add-ons.
        2.  Select "MyNotes" from the list.
        3.  Review the information displayed (or click "About add-on" if available).
    *   **Expected:**
        *   The displayed Name, Version, Author, and Description match the details provided in the `myNotesAddon/addon.json` file.

## 5. Documentation

*   **Test Case 5.1:** Review `readme.md`.
    *   **Steps:**
        1.  Open and read the `myNotesAddon/readme.md` file.
    *   **Expected:**
        *   Instructions for installation and usage are clear, accurate, and easy to follow.
        *   All functionalities (copying, viewing) are covered.
        *   Keyboard shortcuts (`Control+Insert+Q`, `Control+Insert+A`) are correctly listed.
        *   Information about the notes file location is correct.
        *   Placeholder URLs are noted if not yet updated.

## 6. Internationalization (Conceptual - Requires Populated Translation Files)

*   **Test Case 6.1:** Test with a translated language (e.g., Spanish).
    *   **Prerequisites:**
        1.  A `.po` file for the target language (e.g., `myNotesAddon/locale/es/LC_MESSAGES/myNotesAddon.po`) must be created and populated with translations.
        2.  The `.po` file must be compiled into a `.mo` file by the `scons` build process.
    *   **Steps:**
        1.  Install the add-on built with the translations.
        2.  Change NVDA's language (NVDA Menu -> Preferences -> Settings -> General -> Language).
        3.  Restart NVDA.
        4.  Perform actions that trigger UI messages:
            *   Copy text (`Control+Insert+Q`).
            *   Attempt to copy with no text selected.
            *   View notes (`Control+Insert+A`).
            *   Attempt to view non-existent notes.
    *   **Expected:**
        *   All user-facing messages ("Text copied to notes.", "No text selected.", "No notes found.", "My Saved Notes" title, error messages) appear in the selected language (e.g., Spanish).

## 7. Shortcut Key Conflicts (Exploratory)

*   **Test Case 7.1:** Check for shortcut conflicts in common applications.
    *   **Steps:**
        1.  With the MyNotes add-on active, use common applications (web browser, text editor, email client, office suite).
        2.  Perform common tasks in these applications.
        3.  Note if `Control+Insert+Q` or `Control+Insert+A` are commonly used shortcuts in these applications for different critical functions.
        4.  Specifically test if these shortcuts interfere with text selection or navigation tasks.
    *   **Expected:**
        *   Ideally, no conflicts with critical, frequently used functions in major applications.
        *   If conflicts are found, they should be documented. The severity of the conflict will determine if the add-on's shortcuts need to be changed. (This is subjective and for information gathering).

## Post-Testing

*   Document all test results, noting any deviations from expected outcomes.
*   Report bugs or issues found, providing clear steps to reproduce.
*   Consider if any test cases need refinement or if new test cases are needed.
