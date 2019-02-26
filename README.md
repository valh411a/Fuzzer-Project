# Cameron DeVaul's Fuzzer Project
## currently in process of formatting for part 2
### Setup Instructions:
1. Download the files to a folder of choice:
    - input required includes an action, an url
    - custom authentication is recommended for testing purposes
### External Libraries:
- sys       *(for system argument requests)*
- requests  *(for handling http requests)*
- optparse  *(for creating and handling optional arguments)*
- json      *(for compartmentalized information handling)*
### Example Usage:
- (empty input)                         *returns an exception-caught error that inquires the necessity of using arguments*
- --custom-auth=dvwa                    *covers test case for crawling the dvwa*
- discover (url) --custom-auth=dvwa     *runs the discovery section of the fuzzer using dvwa authentication standards*
- test (url) --custom-auth=(auth_type)  *runs the discovery and test sections of the fuzzer using the authentication standard outlined by the user*
### Assignment notes:
- files are distributed so that I can add to them in future steps
- Output is coded as for how I interpreted it from the assignment
- Referenced from a similarly designed Fuzzer project code
    - https://github.com/tofferrosen/Fuzzer
    - migrated code to mechanicalsoup implementation
  
If you have any questions, feel free to email me.
 
 \- Cameron
