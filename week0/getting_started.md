# Preparing Your Dev Environment
## Objective
After following along with this document, your computer will be ready for the accelerator, and you won’t have to worry about installing or configuring too much software.

This document will provide take you through the installation of Python, SQLite Browser, and installing Python’s Flask package.

## Getting started
Installing Python
The first thing you’re going to want to do is to install Python. **Python** is the programming language we’re going to be using for the duration of this program.

You can find an installer for your operating system at [python.org](http://python.org):
- [Windows](https://www.python.org/downloads/)
- [macOS](https://www.python.org/downloads/macos/)
- [Linux](https://www.python.org/downloads/source/)

Make sure you install the latest Python 3 release! As of 9/12/2022,  the latest version of Python 3 is Python **3.10.7**.

If you are struggling with the installation, here is an excellent resource to help you.

## Installing Pip
Next, you’ll want to install [pip](https://pypi.org/project/pip/); it’s the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes. During the accelerator, we’ll use this to install any packages we need.

Packages are online resources that we can install. They allow us to do many different things without actually having to program and debug the functionality ourselves.

To install pip, we’re going to open the command terminal and type the following and then press enter. <sub>([source](https://pip.pypa.io/en/stable/installation/))</sub>

```bash
python -m ensurepip --upgrade
```

## Installing Python packages
Now that we've installed Python and its package manager, we are going to install the required packages for the upcoming project.

The packages we are going to be using are:
- [Flask](https://pypi.org/project/Flask/)
- [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/)

In the command prompt, you can do this by running the following commands.
```pip
pip install -U Flask
pip install -U Flask-SQLAlchemy
```

## Installing VS Code
If you have a code editor preference, I encourage you to use whatever you're most comfortable with and disregard this section.

However, if you have no experience, I strongly recommend using VS Code for the accelerator as it's very user friendly and easy to learn.

VS Code is a free code editor, which runs on the macOS, Linux, and Windows operating systems.

Follow the platform-specific guides below:
- [macOS](https://code.visualstudio.com/docs/setup/mac)
- [Linux](https://code.visualstudio.com/docs/setup/linux)
- [Windows](https://code.visualstudio.com/docs/setup/windows)

VS Code is lightweight and should run on most available hardware and platform versions. You can review the System Requirements to check if your computer configuration is supported. <sub>([source](https://code.visualstudio.com/docs/setup/setup-overview))</sub>

## Downloading the DB Browser for SQLite
All of the programming language related installation is complete - now the only thing left to install is the [DB Browser for SQLite](https://sqlitebrowser.org/).

Installing this isn't explicitly necessary, however if you don't have any prior experience with SQL before it'll help a lot.

This tool will provide a GUI (graphical user interface) for viewing and editing a SQLite database.

You can find a version for your operating system [here](https://sqlitebrowser.org/dl/).

Although we will not be working with databases for a couple of weeks, I recommend you play around with this application and try to get an understanding of SQLite.

## Wrap-up
Now that you've installed all of the previously listed software, you're ready to go! I appreciate you taking your time to be prepared before the first meeting.