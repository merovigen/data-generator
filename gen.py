#!/usr/bin/env python3
import numpy as np

def main():
    repeat_count = 5000
    batch_size = 10000

    # numbers only dict
    number_dict = {
        'age': dict(len=120, data=None),
        'building': dict(len=312, data=None),
        'tax_id': dict(len = 999999999, data=None),
        'zip': dict(len = 999999, data=None),
        'telephone': dict(len = 9999999, data=None),
    }

    # files-related dict with reading
    files = ['first_names', 'middle_names', 'surnames', 'sex', 'countries', 'industries', 'languages', 'races', 'streets', 'towns',]
    list_dict = {f: {} for f in files}
    for fl in list_dict:
        with open(f'{fl}.list') as f:
            list_dict[fl]['data'] = [s.strip() for s in f.readlines()]
        list_dict[fl]['len'] = len(list_dict[fl]['data'])

    # Merge!
    full_dict = {**list_dict, **number_dict}
    size_list = np.array([l['len'] for l in full_dict.values()])

    with open('outfile', 'a') as f:
        f.write('First Name,Second Name,Surname,Sex,Country,Work Industry,Language,Race,Street,City,Age,Building,Tax ID,ZIP,Phone Number\n')

    for _ in range(0,repeat_count):
        # random generation
        random_array = np.random.randint(1000000000, size=(batch_size ,15))

        # do mod
        modded_random_array = np.mod(random_array, size_list)

        # get values
        # `batch_size` lines in array, size of 15 fields
        string_to_write=''
        with open('outfile', 'a') as f:
            for line in modded_random_array:
                for index, field in enumerate(full_dict.values()):
                    string_to_write += f"{field['data'][line[index]]}," if field['data'] else f'{line[index]},'
                string_to_write = string_to_write[:-1] + '\n'
            f.write(string_to_write)

if __name__ == '__main__':
    main()

# first_name
# second_name
# surname
# race
# sex = ["male", "female"]
# country
# street
# language
# marital_ statuses = ["married", "single", "divorced", "widowed"]
# work industry
#
# age
# building
# zip
# telephone
# tax_id
