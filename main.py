import re

counter = 0

regex = re.compile(r'(\d+)-(\d+)\s(.):\s(.+)')

with open('day2_input.txt', 'r') as f:

    for line in f.readlines():

        line = line.rstrip('\n')

        regex_match = regex.match(line)
        min_number = int(regex_match.group(1))
        max_number = int(regex_match.group(2))
        char_in_pass = regex_match.group(3)
        full_pass = regex_match.group(4)

        char_counter = 0

        for i in full_pass:
            if i == char_in_pass:
                char_counter += 1

        if min_number <= char_counter <= max_number:
            counter += 1
    print('Valid:', counter)
