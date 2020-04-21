import ctypes, fcntl
from ioctl_opt import IOR, IOC, IOC_READ, IOC_WRITE


class hidraw_devinfo(ctypes.Structure):
    _fields_ = [
        ('bustype', ctypes.c_uint),
        ('vendor', ctypes.c_short),
        ('product', ctypes.c_short),
    ]


HIDIOCGRAWINFO = IOR(ord('H'), 0x03, hidraw_devinfo)
HIDIOCGRAWNAME = lambda length: IOC(IOC_READ, ord('H'), 0x04, length)


def get_device_name(fd, length=1024):
    name = (ctypes.c_char * length)()
    actual_length = fcntl.ioctl(fd, HIDIOCGRAWNAME(length), name, True)
    if actual_length < 0:
        raise OSError(-actual_length)
    if name[actual_length - 1] == b'\x00':
        actual_length -= 1
    return name[:actual_length]


def get_device_id(fd, length=1024):
    device_id = hidraw_devinfo()
    actual_length = fcntl.ioctl(fd, HIDIOCGRAWINFO, device_id, True)
    if actual_length < 0:
        raise OSError(-actual_length)
    return device_id
