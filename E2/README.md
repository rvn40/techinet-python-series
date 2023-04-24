# Python Labs (Ngoprek): How to Install Python 3 on Ubuntu 22.04

Today Python is become a popular and universal programming language, meaning you can create almost any programs with python. It’s versatile enough for use in web development and app design. 

## Prerequisite
- A system running Ubuntu 22.04
- An ubuntu user with sudo privileges
- Access to a terminal/cli
- Internet connection

## Instructions

For instruction in video format:

[<img src="https://cdn.activestate.com/wp-content/uploads/2021/12/python-coding-mistakes.jpg" width="560" height="315">](https://www.youtube.com/embed/7cng0PQeBzE)

## How to install

#### Checking current version

Most source versions of Ubuntu come with Python pre-installed nowadays. Therefore, before we start we need to check our version of Python by entering the following:

```
python --version
```
or 

```
python3 --version
```

if there is no python available on the machine we can proceed with next steps.

#### Update Local Repositories

```
sudo apt update -y
```

#### Install Supporting Software

```
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget curl -y
```

#### Download the Latest Version of Python Source Code

Now you can go to official python website and find the latest version for ubuntu. When this docs created the latest version is python 3.11.

```
curl https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tgz -O python3-11-3.tgz
```

#### Extract Compressed Files

```
tar -xf Python3-11-3.tgz
```

#### Configure System

The ./configure command evaluates and prepares Python to install on your system. Using the --optimization option speeds code execution by 10-20%.

```
cd python-3-11-3
```

```
./configure --enable-optimizations
```

#### Install Python Without re-Write Current Installation

```
sudo make altinstall
```

#### Install Python (Overwrite Current Default Python Installation)

```
sudo make install
```

#### Verify Python Version

```
python3 --version
```