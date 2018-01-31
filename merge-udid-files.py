import glob
import sys
import os

# get path to udid files
path_to_files = input('Absolute Path to Device UDID Files (ex: /Users/johndoe/Desktop): ')

# add trailing slash if DNE
path_to_files = os.path.join(path_to_files, '')

if os.path.exists(path_to_files) and os.path.isdir(path_to_files):
    # assumes all files have the format `device-udid-export*.txt`
    filenames = glob.glob(path_to_files + 'device-udid-export*.txt')

    # create output file with header line
    out_file = open(path_to_files + 'device-udid-all.txt', 'w')
    out_file.write('Device ID\tDevice Name\n')

    for filename in filenames:
        uuid_file = open(filename, 'r')
        uuid_file.readline() # skip header line
        uuid_and_name = uuid_file.readline() # get device uuid and name
        out_file.write(uuid_and_name + "\n") # write device uuid and name
        uuid_file.close()

    out_file.close()

    print('Merged UDID File Created At: ' + path_to_files + 'device-udid-all.txt')
else:
    print('Path does not exist at ' + path_to_files)
