from hid import get_device_name, get_device_id

import mappings

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
    compatible_devices = find_compatible_devices()
    for compatible_device in compatible_devices:
        (device, mapping, filename) = compatible_device
        device_name = get_device_name(device)

        try:
            modes, commands, keys = mapping.modes, mapping.commands, mapping.keys

            print(f"Found compatible device {device_name} in {filename}")

            begin_command(device, commands)
            write_command(device, commands['set_mode'], modes['drop'])
            write_command(device, commands['set_random_color'], [0])
            write_command(device, commands['set_key_color'] + keys['fn'], [255, 255, 255])
            end_command(device, commands)
        except:
            print(f'Failed to send to {filename}')


def find_compatible_devices():
    compatible_devices = []
    for i in range(1, 100):
        try:
            filename = f'/dev/hidraw{i}'
            device = open(filename, 'rb+')
            device_id = get_device_id(device)

            mapping = mappings.get_device_mapping(device_id)
            if mapping:
                compatible_devices.append((device, mapping, filename))
            else:
                device.close()
        except FileNotFoundError:
            break

    if not compatible_devices:
        raise FileNotFoundError("No supported device found")

    return compatible_devices


def begin_command(device, commands):
    write(device, commands['start'])
    read_state(device)
    read(device)


def write_command(device, command, data=[]):
    write(device, command, data)
    return read(device)


def end_command(device, commands):
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
