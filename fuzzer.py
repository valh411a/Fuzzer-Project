import sys
import mechanicalsoup
import requests

from options import *
from custom_auth import *

(options, args) = parser.parse_args()

action = sys.argv[1]
url = sys.argv[2]

# handles the 2 major actions, as well as the test case for dvwa
if action == "discover" or action == "test" or action == 'http://127.0.0.1:10000/dvwa/login.php':
    if options.auth_type is not None:
        username = custom_auth[options.auth_type.lower()]["username"]
        password = custom_auth[options.auth_type.lower()]["password"]

        # Details to be posted to the login form
        payload = {
            "username": username,
            "password": password,
            "Login": "Login"
        }

        session = requests.Session()
        browser = mechanicalsoup.StatefulBrowser(session)

        browser.open(custom_auth[options.auth_type.lower()]["login_url"])
        browser.select_form()
        browser["username"] = username
        browser["password"] = password
        browser.submit_selected()

        # output
        print(browser.get_current_page())

        # if the --custom-auth option is not invoked, crawl the page (part 2)
    if action == "test":
        print("The code for testing the page will be implemented in part 3.")
else:
    parser.error("\nInvalid Action\nenter either discover or test as the first parameter.")
