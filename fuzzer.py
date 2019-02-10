import argparse

parser = argparse.ArgumentParser()

commandGroup = parser.add_mutually_exclusive_group()

commandGroup.add_argument('--custom-auth=string', help='Signal that the fuzzer should use hard-coded authentication for'
                                                       ' a specific application (e.g. dvwa). Optional.')

parser.parse_args()

# python fuzzer.py [discover | test] url OPTIONS
#
# COMMANDS: discover            Output a comprehensive, human-readable list of all discovered inputs to the system
#                               (e.g., form fields, search boxes). Techniques include both crawling and guessing.
#
#           test                Discover all inputs, then attempt a list of exploit vectors on those inputs.
#                               Report potential vulnerabilities.
#
# OPTIONS:
#   --custom-auth=string        Signal that the fuzzer should use hard-coded authentication for a specific
#                               application (e.g. dvwa). Optional.
#
#   Discover options:
#     --common-words=file       Newline-delimited file of common words to be used in page guessing. Required.
#
#   Test options:
#     --vectors=file            Newline-delimited file of common exploits (e.g., XSS script, path-traversal script) to
#                               vulnerabilities. Required.
#
#     --sensitive=file          Newline-delimited file data that should never be leaked. It's assumed that this data is
#                               in the application's database (e.g. test data),
#                               but is not reported in any response. Required.
#
#     --random=[true|false]     When false, try each input to each page systematically.  When true, choose a random
#                               page, then a random input field and test all vectors. Default: false.
#
#     --slow=millis             Number of milliseconds considered when a response is considered "slow". Optional,
#                               defaults to 500 milliseconds
#
# Examples:
#   # Discover inputs
#   fuzz discover http://localhost:8080 --common-words=mywords.txt
#
#   # Discover inputs to DVWA using our hard-coded authentication
#   fuzz discover http://localhost:8080 --custom-auth=dvwa
#
#   # Discover and Test DVWA without randomness
#   fuzz test http://localhost:8080 --custom-auth=dvwa --common-words=words.txt --vectors=vectors.txt
#   --sensitive=creditcards.txt --random=false
