from interfaces import master_interface
import platform
import os

# default application data location
WINDOWS_DEFAULT_LOCATION = os.environ.get("APPDATA")
LINUX_DEFAULT_LOCATION = ""

# checking if directory already exists for
if platform.system() == "Windows":
    if os.path.isdir(os.path.join(WINDOWS_DEFAULT_LOCATION, "WebTrackerX")):
        pass
    else:
        os.mkdir(os.path.join(WINDOWS_DEFAULT_LOCATION, "WebTrackerX"))
else:
    # most probably linux systems
    pass


def main():
    if __name__ == "__main__":
        master_interface.main()


main()
