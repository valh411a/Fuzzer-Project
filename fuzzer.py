import sys

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
    session.post(custom_auth[options.auth_type.lower()]["login_url"], data=payload)
    page = session.get(url + "/" + options.auth_type)

    # set the security cookie to low!
    cookies = session.cookies
    session_id = cookies["PHPSESSID"]
    session.cookies.clear()  # clear the cookies in the cookie

    session.cookies["PHPSESSID"] = session_id
    session.cookies["security"] = "low"

    # I'm hoping this is what you meant by "print the contents of the HTML of the DVWA home page to the console",
    # if not, let me know and I can modify it if needed.
    print(page.content)

    # if the --custom-auth option is not invoked, crawl the page (part 2)
else:
    print("code will be added in part 2")
