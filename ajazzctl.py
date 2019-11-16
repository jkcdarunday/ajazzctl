from mapping import *

START_BYTE = 4
STATE_SIZE = 16 + 3
PAYLOAD_SIZE = 64
COMMAND_PAYLOAD_SIZE = 8


# Notes:
# [4, checksum, ?, ?, ?, ?, ?, send/receive]
# - Packet always starts with 4
# - Second index is the sum of everything after
# - First 8 bytes looks like command data
# - Remaining bytes look like params
# - After sending start, keyboard returns with 19 bytes starting with 5 which I assume is its state or version

def main():
    device = open('/dev/hidraw3', 'rb+')

    begin_command(device)
    write_command(device, commands['set_mode'], modes['drop'] )
    write_command(device, commands['set_random_color'], [0])
    write_command(device, commands['set_key_color'] + keys['fn'], [255, 255, 255])
    end_command(device)


def begin_command(device):
    write(device, commands['start'])
    read_state(device)
    read(device)

def write_command(device, command, data=[]):
    write(device, command, data)
    return read(device)

def end_command(device):
    write(device, commands['end'])
    read(device)



def write(device, command: [], data=[]):
    command_payload = pad_command([4] + int_to_2byte(sum(command + data)) + command)
    payload = pad_payload(command_payload + data)

    print("SENT: ", payload)

    device.write(bytearray(payload))

def int_to_2byte(value):
    return [value % 256, value // 256]


def read(device):
    response = list(device.read(PAYLOAD_SIZE))
    print("RECV:", response)
    return response


def read_state(device):
    response = list(device.read(STATE_SIZE))
    print("RECV:", response)
    return response


def pad_payload(payload):
    return payload + [0] * (PAYLOAD_SIZE - len(payload))


def pad_command(command_payload):
    return command_payload + [0] * (COMMAND_PAYLOAD_SIZE - len(command_payload))


if __name__ == "__main__":
    main()
