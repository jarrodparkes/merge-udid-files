import glob

# assumes all files have the format `device-udid-export*.txt`
filenames = glob.glob('device-udid-export*.txt')

# create output file with header line
out_file = open("device-udid-all.txt","w")
out_file.write("Device ID\tDevice Name\n")

for filename in filenames:
    uuid_file = open(filename, "r")
    uuid_file.readline() # skip header line
    uuid_and_name = uuid_file.readline() # get device uuid and name
    out_file.write(uuid_and_name + "\n") # write device uuid and name
    uuid_file.close()

out_file.close()
