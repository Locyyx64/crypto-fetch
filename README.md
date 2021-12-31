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
Next, download the packages, that are listed in **_requirements.txt_**.
  ```
  pip install -r _/path/to/requirements.txt_
  ```
