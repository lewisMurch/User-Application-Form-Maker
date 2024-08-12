# Define lists of values for each placeholder
crsid_list = ["xqj29", "ub473", "pmd18", "cvu47", "ieo54", "jrf28", "pwi93", "gkj65", "blm20", "shw92", "dwq41", "qrv77", "lpe58", "wmo93", "dne16", "kyl80", "zdr94", "uhr56", "mvo42", "npl37", "fkj31", "rzu88", "hye72", "csg39", "yji19", "fow46", "vru83", "gmr22", "evo19", "tkh64", "bsc20", "gpe56", "mzw17"]

first_name_list = ["Alex", "Eva", "Chris", "Mia", "Nathan", "Sofia", "Ella", "Kai", "Jasper", "Nina", "Ryan", "Aria", "Luke", "Liam", "Zoe", "Ivy", "Ethan", "Amelia", "Riley", "Luca", "Nora", "Aiden", "Lila", "Max", "Anna", "Toby", "Luna", "Owen", "Leah", "Evan", "Maya", "Ava", "Jack", "Emily"]

last_name_list = ["Kim", "Jung", "Park", "Lee", "Choi", "Kang", "Yoon", "Seo", "Hwang", "Ryu", "Jeong", "Hong", "Yang", "Bae", "Chung", "Kwon", "Nam", "Roh", "Ko", "Ahn", "Kim", "Cho", "Lee", "Shin", "Hwang", "Lim", "Ahn", "Jang", "Kang", "Im", "Jin", "Kwon", "Yoo", "Na"]

course_list = ["MSc", "MSc", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "MSc", "MSc", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD", "PhD"]



# Sample command template
template = "idmuseradd -a {} -f {} -s {} -e 2024-10-09; "
template2 = "IoA user account for {} student {} {} ({})\n"
template3 = "{} {} - RT#\n{}\n\n"
template4 = "ipa user-mod --password {}; "
template5 = "ssh {}@muon1.ast.cam.ac.uk\n"

# Number of commands to generate
num_commands = len(crsid_list)

command2 = ""

# Generate and print the commands
for i in range(num_commands):
    crsid = crsid_list[i]
    first_name = first_name_list[i]
    last_name = last_name_list[i]
    course = course_list[i]
    
    command = template5.format(crsid)
    command2 = command2 + command
print(command2)
    

