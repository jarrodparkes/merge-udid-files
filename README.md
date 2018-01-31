# Merge UDID Files

![](https://img.shields.io/badge/python-3.4.3-yellow.svg)

If you've used Crashlytics Beta or other services for distributing and testing iOS apps, then you know the headaches involved with manually adding new device IDs to the Apple Developer Portal. Every time someone registers to test with Crashlytics Beta, you receive an email with their UDID in an attachment. This script is used to combine many such attachments into a single file for upload on the Apple Developer Portal.

## How to Use

1. Select all Crashlytics emails in your email client and export their attachments. This is very easy using the macOS Mail app. After you've selected all emails, you can go to **File-->Save Attachments...** and then select a location on your machine where you want to save them.

![](/get-emails.png)

2. Move all the attachments into this directory with the Python file (at some point I'll allow you to specify a path in the Python script...)

3. Run `python merge-udid-files.py`

4. The file `device-udid-all.txt` is generated. Use it for upload in the Apple Developer Portal!

## Example

Some example attachment files have been provided with the names and UDID's obscured. If you'd like to test the script first just run `python merge-udid-files.py` and see the resulting `device-udid-all.txt` files.
