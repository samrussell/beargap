beargap
=======

You have an airgapped computer for a reason - you want to keep your data very, very safe. But sometimes, you need to let your airgapped computer communicate with the outside world. Maybe you're downloading a new app, or signing a transaction from your cold storage bitcoin wallet. How do you get a small amount of data to and from your airgapped computer, without letting anything else hitch a ride?

Enter beargap: the QR-code based communication channel for your airgapped computer.

How it works:

- Load up beargap.py on the source computer, and enter the data to be transmitted in the text box
- Generate QR codes
- Load up reader.py on the destination computer, and scan the QR codes
- Once all the codes are scanned, the data is reconstructed and displayed on the destination computer

Why would you do it this way?

- USB keys are too big (according to Bruce Schneier https://www.schneier.com/blog/archives/2013/10/air_gaps.html), and there's tons of room for something nasty to catch a ride
- The communications channel is wide open - you can video your transfers and audit them at a later date

Setup

You will need the following libraries:
- libzbar-dev
- zbar-tools
- python-qt4
- pyqt4-dev-tools
- python-qrcode
- PIL
- a few others? (will update soon)

Donations

If you find this useful, and want me to keep writing code like this, then feel free to donate to 1FTwGgGZhwnhoYM5d8ZwMLSihCpyejCaKi
