![Sandesh](https://user-images.githubusercontent.com/77227201/171690740-452e3b46-307f-4994-9966-2a74d8f5bfa7.jpg)

# Sandesh

> Send Personalized HTML Rich Emails using data from CSV file. 

![Forks](https://img.shields.io/github/forks/wasimreja/sandesh.svg)
![Stars](https://img.shields.io/github/stars/wasimreja/sandesh.svg)
![Issues](https://img.shields.io/github/issues/wasimreja/sandesh.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

## Getting Started

- Make sure you have Python installed in your system.

- Download or Clone the repo and then move into the project directory.
  ```shell
  git clone https://github.com/wasimreja/sandesh.git
  cd sandesh
  ```

- Install all dependencies:
  ```shell
  pip install -r requirements.txt
  ```

- Write your email inside `mail.html`.

- To include data from the spreadsheet in your email, use placeholders that correspond to column names surrounded by curly braces, such as `{{name}}`.

- Put your data inside `data.csv` file.

- **Do not put original email password.** 
  Create Gmail Account then turn on 2 step Verification, and then set up an [App Password](https://support.google.com/accounts/answer/185833?hl=en).

- All set up you are now ready to go. Run the `send.py` file:
  ```shell
  python3 send.py
  ```
