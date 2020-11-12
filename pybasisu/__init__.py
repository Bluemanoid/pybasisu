import os, platform, pkg_resources
import subprocess
import pathlib
import logging
import copy


def _get_basisu_binary_path():
    is_msys = platform.system().startswith("MING") or platform.system().startswith("MSYS_NT")
    is_cygwin = platform.system().startswith("CYGWIN_NT")
    is_windows = platform.system() == "Windows" or is_msys or is_cygwin
    is_linux = platform.system()
    is_macos = platform.system() == "Darwin"

    if is_windows:
        if platform.architecture()[0] == '64bit':
            exename = os.path.join("binaries", "Win64", "basisu.exe")
        elif platform.architecture()[0] == '64bit':
            exename = os.path.join("binaries", "Win32", "basisu.exe")
        else:
            raise NotImplementedError('This tool is only available for Windows 32 & 64 bits.')
    elif is_macos:
        exename = os.path.join("binaries", "macOS", "basisu")
    elif is_linux:
        if platform.architecture()[0] == '64bit':
            exename = os.path.join("binaries", "Linux64", "basisu")
        elif platform.architecture()[0] == '32bit':
            exename = os.path.join("binaries", "Linux32", "basisu")
        else:
            raise NotImplementedError('This tool is only available for Linux 32 & 64 bits.')
    else:
        raise NotImplementedError('This tool is only available for Windows, Linux and macOS.')

    basisu_path = pkg_resources.resource_filename('pybasisu', exename)
    return basisu_path


def basisu(args=[], silent=False):
    basisu_args = [_get_basisu_binary_path()]
    basisu_args.extend(args)
    subprocess.run(basisu_args, stdout=(subprocess.DEVNULL if silent else None))
