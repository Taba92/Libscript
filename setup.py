from setuptools import setup

setup(
    name = 'Libscript',
    version = '0.1',
    description = "Libreria per lo scripting di sistema general purpose",
    url = "https://github.com/Taba92/Libscript.git",
    author = 'Luca Tabanelli',
    author_email = "tabanelli@hotmail.it",
    license = "MIT",
    packages = [
        "Configuration",
        "Logging",
        "Backup"
    ],
    install_requires = [
    ],
    zip_safe = False
)