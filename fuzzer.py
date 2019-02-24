import sys
import mechanicalsoup
import requests

from options import *
from custom_auth import *

(options, args) = parser.parse_args()

# action = sys.argv[1]
url = sys.argv[1]

# if action == "discover" or action == "test":
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
    # print(browser.get_current_page(), "\n")
    # print(browser.get_current_page().find_all("input", class_='loginInput'), "\n")
    browser.select_form()
    browser.get_current_form().print_summary()
    browser["username"] = username
    browser["password"] = password
    browser.submit_selected()
    browser.launch_browser()

    # if the --custom-auth option is not invoked, crawl the page (part 2)
else:
    print("code will be added in part 2")
