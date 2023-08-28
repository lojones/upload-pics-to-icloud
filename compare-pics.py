import os
import re




if __name__ == "__main__":
    first_folder = 'F:\\JanesPics\\all\\mypics\\uploaded'
    second_folder = 'F:\\JanesPics\\all\\iphotolib_originals'
    duplicates_folder = f"{second_folder}\\duplicates"
    ad_folder = f"{second_folder}\\appledouble"
    
    # get a list of filenames in second_folder that also exist in first_folder write it to stdout
    first_folder_files = os.listdir(first_folder)
    second_folder_files = os.listdir(second_folder)
    
    # for filename in second_folder_files:
    #     #check if filename starts with '._'
    #     if re.match(r'^\._', filename):
    #         # get filesize of filename
    #         filesize = os.path.getsize(f"{second_folder}\\{filename}")
    #         print(f"{filename} is {filesize} bytes")

    second_folder_files.sort()

    # create a copy of second_folder_files but each string array element has the first 5 characters cut off
    # this is to remove the date prefix from the filenames
    
    second_folder_files_withmetadata = []
    for filename in second_folder_files:
        # find filenames that start with a '._20[0-9][0-9]-' where n represents a digit
        if re.match(r'^\d{4}-\d{4}', filename):
            real_filename = filename
            matching_filename = f"{filename[5:]}"
            filename_info = { "real": real_filename, "matching": matching_filename }
            second_folder_files_withmetadata.append(filename_info)
        else:
            real_filename = filename
            matching_filename = filename
            filename_info = { "real": real_filename, "matching": matching_filename }
            second_folder_files_withmetadata.append(filename_info)
    
    same = []
    newpic = []

    # get filenames that are the same between the 2 lists first_folder_files and second_folder_files and write them to stdout
    for filename in second_folder_files_withmetadata:
        # filename = filename
        if filename["matching"] in first_folder_files:
            same.append(filename["real"])
            # print('\033[92m' + u'\u2588' + '\033[0m', end='')
            print(f"{filename['real']} | {filename['matching']}|")
            os.rename(f"{second_folder}\\{filename['real']}", f"{duplicates_folder}\\{filename['matching']}")
        else:
            newpic.append(filename["real"])
            # print('\033[91m' + u'\u2588' + '\033[0m', end='')
            # print(filename+"|",end='')
    
    print(f"count of same pics: {len(same)}")
    print(f"count of new pics: {len(newpic)}")
    print(f"count of iphotolib_originals files: {len(second_folder_files)}")


