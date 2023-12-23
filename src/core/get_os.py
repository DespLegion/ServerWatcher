import platform
from src.core.logger import CustomLogger


custom_logger = CustomLogger(logger_name=__name__, log_level='info', logfile_name='core.log')
get_os_logger = custom_logger.create_logger()


def get_os_name():
    try:
        platform_name = platform.system()

        if platform_name == "Windows":
            return f"{platform_name} {platform.release()}"
        elif platform_name == "Linux":
            import distro
            print(f"Distro id - {distro.id()}")
            print(f"Distro version - {distro.version()}")
            print(f"Distro name standart - {distro.name()}")
            print(f"Distro name pretty - {distro.name(pretty=True)}")
            # os_name = os_human_name(distro.id())
            return os_human_name(distro.id()) if os_human_name(distro.id()) else distro.id().capitalize()
            # if os_human_name(distro.id()):
            #     return os_human_name(distro.id())
            # return distro.id().capitalize()
        else:
            return "Unsupported OS!"
    except Exception as err:
        get_os_logger.error(f'Error with OS identifier - {err}', exc_info=True)
        return "Error with OS identifier!"


def os_human_name(os_id):
    os_base = {
        "ubuntu": "Ubuntu",
        "debian": "Debian",
        "rhel": "RedHat",
        "centos": "CentOS",
        "fedora": "Fedora",
        "arch": "Arch Linux",
        "linuxmint": "Linux Mint",
        "altlinux": "ALT Linux",
        "openbsd": "OpenBSD",
        "netbsd": "NetBSD",
        "freebsd": "FreeBSD",
        "amzn": "Amazon Linux",
    }
    return os_base.get(os_id, None)

