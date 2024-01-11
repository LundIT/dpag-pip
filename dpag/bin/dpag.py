"""Dpag Command Line Interface."""
import sys
import os
import subprocess

from pathlib import Path
import site
import django
def find_package_path(package_name):
    # Get site-packages directories
    site_packages_dirs = site.getsitepackages()

    # Search for the package in site-packages
    for dir in site_packages_dirs:
        package_path = os.path.join(dir, package_name)
        if os.path.exists(package_path):
            return package_path

    return None
def main():

    dpag = find_package_path("dpag")
    PROJECT_ROOT_DIR = Path(os.getcwd()).resolve()
    DJANGO_ROOT_DIR = PROJECT_ROOT_DIR / dpag
    sys.path.append(dpag)

    # The DJANGO_SETTINGS_MODULE has to be set to allow us to access django imports
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "DjangoProcessAdminGeneric.settings"
    )
    os.environ.setdefault(
        "PROJECT_ROOT", PROJECT_ROOT_DIR.as_posix()
    )
    print(PROJECT_ROOT_DIR.as_posix())
    # This is for setting up django
    print("sys.path: " + str(sys.path))
    django.setup()
    # subprocess.run(["python3", "manage.py", "createcachetable"], cwd=DJANGO_ROOT_DIR)
    # subprocess.run(["python3", "manage.py", "makemigrations"], cwd=DJANGO_ROOT_DIR)
    # subprocess.run(["python3", "manage.py", "migrate"], cwd=DJANGO_ROOT_DIR)

    command = ["uvicorn", "--reload", "--loop", "asyncio", f"--app-dir={DJANGO_ROOT_DIR}",
               "DjangoProcessAdminGeneric.asgi:application"]

    # Use subprocess.run to execute the command

    subprocess.run(command)


