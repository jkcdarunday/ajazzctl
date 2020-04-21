from mappings import ak66

device_mappings = {
    (0x04b4, 0x1009): ak66
}


def get_device_mapping(device_id):
    return device_mappings.get((device_id.vendor, device_id.product)) or None
