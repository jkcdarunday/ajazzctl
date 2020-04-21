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

## How does it work
It writes the same commands used by the Windows and writes these to the Ajazz HID Raw device (`/dev/hidraw*`)

## Usage
```sh
sudo python ajazzctl.py
```
