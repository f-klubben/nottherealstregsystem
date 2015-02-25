[![Build Status](https://travis-ci.org/f-klubben/stregsystem.svg?branch=master)](https://travis-ci.org/f-klubben/stregsystem) [![Coverage Status](https://coveralls.io/repos/f-klubben/stregsystem/badge.svg)](https://coveralls.io/r/f-klubben/stregsystem)

The Stregsystem is used at F-Klubben to pay for goods bought at Strandvejen and for signup to various events held by F-klubben. The main development and maintenance of the Stregsystem is maintained by FIT and daily use is handled by TREO.

The Stregsystem is written as a Python 3 (https://www.python.org/) web application powered by the web framework Django (https://www.djangoproject.com/). Starting with version 4.0, FIT has chosen to make development of the system open source, licensed under THE LIMFJORDS-PORTER-WARE LICENSE. Everyone is encouraged to contribute in various ways - see the contribution guideline below.

# Contributing to Stregsystem
Everyone can contibute in some way or another to the Stregsystem. Below are some of the ways you can help out, including a guide to getting started writing your own code and submitting it as a Pull Request!

## Submitting Feature Requests and Reporting Bugs
One of the easiest ways of getting starting contributing, is to submit feature requests and reporting bugs. It all starts with your GitHub account, so if you do not already have one, now is the time.

At the Stregsystem repository at GitHub, go to the issues section. From here, you can submit issues, which can be either bugs of feature requests.

Whatever you submit, be as clear and precise as possible, and please keep it in English for everyone to understand. When submitting bugs, describe what you did to provoke the bug and whether or not it can be reproduced. If the bug happened while you tried to use the production Stregsystem, please also specify in which room, the approximate time and your Stregsystem username.

When submitting feature requests, please be aware that FIT reserve the right to turn down any feature request for whatever reason. Priority number 1 is to keep the system stable, not to bloat the system with features!

## Writing Yor Own Code
If you have an urge to contrubute with code, you might be wise to have a chat with FIT members in advance. In the end, pull requests toward the repository will be handled by FIT, and we alone decide which features that are being merged into the repository. It is not that we do not want your code, but we might as well just be in agreement in advance!

### Setting up Ubuntu for Python 3 Development
This assumes Ubuntu 14.04 or newer. On older systems, it might be more beneficial to compile Python 3.4 yourself from source (it's not hard, we promise).

#### Ubuntu 14.04
The virtual environment that ships with Ubuntu 14.04 is a bit broken (https://bugs.launchpad.net/ubuntu/+source/python3.4/+bug/1290847). There are several ways around this. One is to accept it is broken, and install pip manually for each virtual environment you create, or simply compile Python 3.4 yourself. We will go with the first option.

The following command will install Git and the PostgreSQL dependency.

```bash
$ sudo apt-get install libpq-dev git
```

Now, when you later setup your virtual environment, the steps are a bit different. Where you would normally use `pyvenv-3.4 env` you will instead use `pyvenv-3.4 env --without-pip`. After that you run the command `curl https://bootstrap.pypa.io/get-pip.py | env/bin/python` which will install the latest pip. After this you can follow the tutorial.

#### Ubuntu 14.10 and later
Ubuntu 14.10 fixes the problem of 14.04, but you will need to install virtual environment yourself. The following command will install the normal virtual environment, as well as a dependency needed for PostgreSQL. For good measure, we will also install Git.

```bash
$ sudo apt-get install libpq-dev python3.4-venv git
```

If you run `python3` now, you should be greeted with an interactive Python shell that states version 3.4.x.

### Setting up Mac OS X for Python 3 Development
The easiest thing is to administer your Python installations using Homebrew - whatever Apple ships with OS X by default is most likely outdated and cannot easily be updated. You will be prompted to install XCode Command Line Tools if you do not have it already.

```bash
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew doctor
```

To your `~/.bash_profile` add the following to ensure that Homebrew packages take precedence over everything else, and be sure to run `source ~/.bash_profile` afterwards for it to take effect.

```bash
export PATH=/usr/local/bin:$PATH
```

Time to install Python 3 and one dependency for PostgreSQL drivers to run (we likely will not need them since locally we can run SQLite3, but just to be safe!). While we are at it, we will also install an up to date version of Python 2.

```bash
$ brew install postgresql
$ brew install python --with-brewed-openssl
$ brew install python3 --with-brewed-openssl
$ pip install virtualenv
```

Note that we choose to not use Apple's OpenSSL, since it sucks (trust us on this, Apple do not know how to SSL).

Also note that we manually install virtualenv for Python 2 on the last line. Virtualenv comes bundled with Python 3, so no need to install anything there.

### Virtual Environments in Python
When programming Python, virtual environments are used in order to keep a bundle of packages together for a particular project inside a virtual environment, such that they do not interfere with other projects, or the installed system packages. As a use case, consider you were upgrading to a new version of Django, and want to test if everything is working as intended. Instead of potentially ruining your whole environment, and all other Django projects you have, you create a new virtual environment and simply upgrade Django inside this environment, leaving everything else intact.

With Python 3 installations, you should have `pyvenv-3.4` available somewhere on your PATH. This will set up a Python 3.4 virtual environment. Inside your cloned Git repository of the Stregsystem, type the following:

```bash
$ pyvenv-3.4 env
$ source env/bin/activate
```

The first line creates a new environment simply called `env` (this name is ignored by our `.gitignore`, so it is safe to use). The second line activates the environment; your shell should change, and from this point on, the activate Python will be that of your virtual environment. Confirm this by doing:

```bash
(env) $ which python
```

Which should yield the path to Python inside your virtual environment.

From here, you can install Python packages using `pip` inside your virtual environment. See https://pip.pypa.io/en/latest/ for more on what pip is and how it works.

To deactivate your virtual environment, simply run `deactivate`.

### Getting the Code
If you simply want to get hold of the code and run it, the following few commands will get you started. It assumes you have Git and Python 3.4 installed, as well as the PostgreSQL dependencies.

```bash
$ git clone https://github.com/f-klubben/stregsystem.git
$ cd stregsystem
$ pyvenv-3.4 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ cd stregsystem
$ python manage.py runserver
```

If you point your browser to `http://localhost:8000/` you should now see the Stregsystem. Happy hacking!

### Writing Your First Pull Request
Instead of re-writing something that already exists, we refer to the Django contributing guidelines, specifically: https://docs.djangoproject.com/en/1.7/internals/contributing/writing-code/working-with-git/. You will of course need to replace the Django repository URL with your own, but otherwise, the process is exactly the same. If you have any questions, feel free to poke anyone from FIT - wel are happy to help!

## Coding Style
We roughly adhere to the Django coding style, see https://docs.djangoproject.com/en/1.7/internals/contributing/writing-code/coding-style/.

Two linting tools are being run by the build server:

* **flake8** is being run instead of a PEP8 check. In addition to PEP8, flake8 checks for a number of things including usage of unused variables, use of variables before declaration etc. We have also turned on a complexity check to prevent overly large and cross functions and methods.
* **isort** makes sure our Python imports are somewhat organized. Refer to the documentation for the convention being used - we run with pretty much default settings.

## Running the Test Suite
Since you are reading this, we assume you already have everything set up and running. Sweet!

Running the test suite is as simple as running the following command from the Django project folder while your virtual environment is active:

```bash
$ python manage.py test --settings=stregsystem.settings.unittest
```
