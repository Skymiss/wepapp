class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]


def sanitize(time_string):
    if '_' in time_string:
        splitter = '_'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temple = data.strip().split(',')
        return AthleteList(temple.pop(0), temple.pop(0), temple)
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None

sarah = get_coach_data('sarah.txt')
print(sarah.name + "fastest times are: " + str(sarah.top3()))

vera = AthleteList('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', "1-21", '2.22'])
print(vera.top3())
