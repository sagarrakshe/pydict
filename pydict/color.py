class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def print_meaning(meaning):
    print bcolors.WARNING + meaning + bcolors.ENDC

def print_heading(heading):
    print bcolors.OKGREEN + heading + bcolors.ENDC

def print_line(line):
    print bcolors.HEADER + line + bcolors.ENDC

def print_word(word):
    print bcolors.OKBLUE + word + bcolors.ENDC

def print_error(err):
    print bcolors.FAIL + err + bcolors.ENDC
