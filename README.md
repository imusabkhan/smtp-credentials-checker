# SMTP Credentials Checker
This repository contains a Python script to verify the validity of SMTP credentials. During penetration testing activities, I often encounter SMTP credentials and struggle to find a reliable tool to confirm their validity. To simplify this task, I developed this straightforward script to send emails using your local setup.

If you find my work helpful and would like to show your support, you can buy me a coffee! ☕

<a href="https://www.buymeacoffee.com/imusabkhan" target="_blank">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;">
</a>


## Features
- **Simple and Easy to Use:** Just provide the SMTP server, port, username, and password to check the credentials.
- **Quick Validation:** Efficiently checks if the provided SMTP credentials are valid.
- **Minimal Dependencies:** Lightweight with minimal external dependencies, making it easy to set up and run.

## Prerequisites
- Python 3.x

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/imusabkhan/smtp-credentials-checker.git
   cd smtp-credentials-checker
   python3 check_smtp_credentials.py
   ```
2. Update the script with your email configuration and credentials:
   ```
   FROM_EMAIL = 'your_email@example.com'
   PASSWORD = 'your_password'
   SERVER = 'your_smtp_server'
   PORT = 587 #'smtp_port'
   TO_EMAIL = 'recipient_email@example.com'
   ```

## DigitalOcean Referral

If you're interested in trying out DigitalOcean for hosting your projects, you can sign up using [this referral link](https://m.do.co/c/6b4b1bf0f63e). By using this link, you'll get some free credits to start with.

[Sign up on DigitalOcean](https://m.do.co/c/6b4b1bf0f63e)

## Social Profiles

[Medium](https://medium.com/@imusabkhan) |
[YouTube](https://www.youtube.com/musabkhan) |
[LinkedIn](https://www.linkedin.com/in/musab1995/) |
[Twitter](https://twitter.com/Musab1995) |
[HackerOne](https://hackerone.com/musabkhan) |
[Facebook](https://facebook.com/imusabkhan) |
[Instagram](https://instagram.com/imusabkhan)

## Disclaimer

Usage of these tools for unauthorized access or any malicious activity is strictly prohibited. Use them responsibly and with proper authorization.
