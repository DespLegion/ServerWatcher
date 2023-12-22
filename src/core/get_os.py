import platform


def get_os_name():
    platform_name = platform.system()

    if platform_name == "Windows":
        return f"{platform_name} {platform.release()}"
    elif platform_name == "Linux":
        import distro
        return distro.id()
    else:
        return "Unsupported OS!"
