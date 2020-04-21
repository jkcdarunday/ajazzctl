# ajazzctl
Tool for controlling RGB lighting for the Ajazz AK66 keyboard

## Status
This current supports only Ajazz AK66. To support other Ajazz keyboards, this will need an update to the mappings/* files.

## Requirements
* Python 3

## Setup
```sh
pip install -r requirements.txt
```

## Usage
CLI parsing has not been implemented yet.

Change the commands in ajazzctl.py based on mappings in the mappings folder then execute:
```sh
sudo python ajazzctl.py
```

## How does it work
It writes the same commands used by the Windows and writes these to the Ajazz HID Raw device (`/dev/hidraw*`)

## How was it done
I ran the original Ajazz configuration tool on a Windows virtual machine and attached my Ajazz keyboard to it. Then, I used wireshark with usbmon to monitor the data it sends to and receives from the keyboard while doing changes in the configuration tool.

Adding support to other keyboard would probably require the same process.
