import sys
import mechanicalsoup
import requests

import common_words
import discovery
from options import *
from custom_auth import *

(options, args) = parser.parse_args()

action = None
url = None
if len(sys.argv) == 3:
    action = "discover"
elif len(sys.argv) > 2:
    action = sys.argv[1]
    url = sys.argv[2]
elif len(sys.argv) <= 1:
    parser.error("No arguements Provided")

# handles the 2 major actions, as well as the test case for dvwa
if action == "discover" or action == "test" or url is None:
    if url is None:
        print("Action left blank; engaging in DVWA test...")
        url = "http://127.0.0.1:10000/dvwa"
    if options.common_words is None:
        parser.error("\'Common words\' file required for discovery.")
    if options.auth_type is not None:
        username = custom_auth[options.auth_type.lower()]["username"]
        password = custom_auth[options.auth_type.lower()]["password"]

        common_words.createFile()
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

        # part 1 output
        # print(browser.get_current_page(), "\n")

        urlList = discovery.discoverLinks(browser, url)
        for each in urlList:
            print(each)

    if action == "test":
        print("The code for testing the page will be implemented in part 3.")
else:
    print(sys.argv)
    parser.error("\nInvalid Action\nenter either discover or test as the first parameter.")

