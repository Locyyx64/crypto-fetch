# crypto-fetch
A simple cryptocurrency tracker, made with Python. It uses Selenium as it's web scraper, and firefox as the webdriver itself. (Geckodriver)
Note: It's development is still in progress, so do not be surprised, if you come across any bugs.

**Only usable on a Linux machine. If you are on Windows, change the directory to the webdriver in the code.**

Unfortunately, it can only search 100 cryptocurrencies at max, because I haven't figured out what to do with the CAPTCHA yet.
***Enjoy! ;)***

## _Installing_ <br />
First of all, make sure that you have python3 and python3-pip installed.
  ### If you are using a Ubuntu/Debian based Linux distribution:
  ```
  sudo apt update
  sudo apt install python3 python3-pip
  ```
  ### If you are using an Arch based distribution:
  ```
  sudo pacman -Syu
  sudo pacman -S python python-pip
  ```
Next, clone the repo:
  ```
  git clone https://github.com/Locyyx64/crypto-fetch.git
  ```
After that, download the packages, that are listed in **_requirements.txt_**.
  ```
  pip install -r path/to/requirements.txt
  ```
Now, download the **Mozilla webdriver** (geckodriver), and add it to your **/usr/local/bin** directory. (If you can't put it here, put it in one of the other $PATH directories, and make sure to change the directory to it in the code itself.)

### _Configurations_ <br />
If you want to run the command from the terminal, you can do:
  ```
  chmod +x path/to/crypto.py
  ```
And after that, you can run it from the terminal like this:
  ```
  ./path/to/crypto.py
  ```
If you want to make it a Bash command, you can add an alias to the script in your **.bashrc** file.
