Forrst Growl Notifier
=====================
Written by: Alex Holt <alex@soyrex.com>

General:
--------
Will sit in the background and check forrst every 5 minutes for
how many notifications the user has. Just requires the user's 
name to function.

Installation: 
-------------
Drag the application into the applications folder.
Run it.

It should prompt you for your forrst user name.. this will then be
converted to a forrst id and stored in the file : ~/.forrst.user
If you delete this file, it should ask you to enter your user again
the next time you run it.

Requirements:
-------------
These should all be on your OSX system already.

- python
- unix commands: sed, tr

You need these:

- Growl

Known Bugs:
-----------
- You can't seem to quit it. use CMD-alt-ESC to Force Quit.
- Anything you report here: https://github.com/soyrex/AS-ForrstGrowl/issues
