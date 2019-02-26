from optparse import OptionParser

usage = "Usage: %prog [discover | test] url [OPTIONS]"
parser = OptionParser(usage=usage)

parser.add_option('--custom-auth=strings', dest='auth_type', metavar='String',  help='Signal that the fuzzer should '
                                                                                     'use hard-coded authentication '
                                                                                     'for a specific application ('
                                                                                     'e.g. dvwa). Optional.')
parser.add_option('--common-words=file', dest='common_words', metavar='File', help='File that contains common words '
                                                                                   'to be used for input and page '
                                                                                   'guessing. Required for discovery')
