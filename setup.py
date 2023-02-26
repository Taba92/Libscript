from setuptools import setup

setup(
    name = 'Libscript',
    version = '0.1',
    description = "Libreria per lo scripting di sistema general purpose",
    author = 'Luca Tabanelli',
    author_email = "tabanelli@hotmail.it",
    license = "MIT",
    packages = [
        "Configuration",
        "Logging",
        "Backup"
    ],
    install_requires = [
       "onedrivesdk"
    ],
    zip_safe = False
)