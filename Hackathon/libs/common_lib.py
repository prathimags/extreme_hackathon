
import subprocess
import os, csv, sys

""" groupRegFilePath="./Output_Files/hackathon_user_reg.csv" """
""" qaMembersUsersList="./Output_Files/hackathon_members_list.csv" """

"""
    ---------------------------------------------------------------------------
    This function writes the file contents to the csv file path
    @param filePath - path of the file to write
    @param fileContents - contents to be written to the file
    @return - N/A
    ---------------------------------------------------------------------------
"""
def writeArrayContentToCSVfile(filePath,fileContent,writeMode):

    try:
        fp = open(filePath,writeMode,newline='')
    except OSError as err:
        print ("-----------------------------------------------------------------------------------------------------------")
        print ("Error: Invalid File Path!!\n\tError Message:",err)
        print ("\t Please check if the file Path is valid -",filePath,". If valid, check the file permissions")
        print ("-----------------------------------------------------------------------------------------------------------")
        sys.exit(-1)
    else:
        if (fp):
            writer = csv.writer(fp)
              
            writer.writerow(fileContent)
            fp.close()


"""
    ---------------------------------------------------------------------------
    This function writes the file contents to the csv file path - row by row
    @param filePath - path of the file to write
    @param fileContents - contents to be written to the file
    @return - N/A
    ---------------------------------------------------------------------------
"""
def writeListContentLbLToCSVfile(filePath,fileContents):

    try:
        fp = open(filePath,"w",newline='')
    except OSError as err:
        print ("-----------------------------------------------------------------------------------------------------------")
        print ("Error: Invalid File Path!!\n\tError Message:",err)
        print ("\t Please check if the file Path is valid -",filePath,". If valid, check the file permissions")
        print ("-----------------------------------------------------------------------------------------------------------")
        sys.exit(-1)
    else:
        if (fp):
            writer = csv.writer(fp)

            #Write the fileContents into .csv file
            for row in fileContents:                
                writer.writerow(row)
            fp.close()

"""
    ---------------------------------------------------------------------------
    This function reads the file contents from the csv file path - row by row
    @param filePath - path of the file to read
    @return - array with file contents
    ---------------------------------------------------------------------------
"""
def readFileContentFromCSVfile(filePath):
    fileContents = []

    try:
        fp = open(filePath,"r",newline='')
    except OSError as err:
        print ("-----------------------------------------------------------------------------------------------------------")
        print ("Error: Invalid File Path!!\n\tError Message:",err)
        print ("\t Please check if the file Path is valid -",filePath,". If valid, check the file permissions")
        print ("-----------------------------------------------------------------------------------------------------------")
        sys.exit(-1)
    else:
        if (fp):
            reader = csv.reader(fp)

            #Read the fileContents from .csv file
            for row in reader:
                fileContents.append(row)
                #print (fileContents)
            fp.close()

    return fileContents

"""
    ---------------------------------------------------------------------------
    This function generates a dictionary from the file contents 
    @param groupRegFilePath - path to the file
    @return - dictionary with file contents
    ---------------------------------------------------------------------------
"""
def convertGroupMemContentToListOfDict(groupRegFilePath):
    fileContents = readFileContentFromCSVfile(groupRegFilePath)

    group_members_list = []

    for group in fileContents:
        group_members_dict = {}
        group_members_dict['name'] = group[0]

        group_members = ""
        no_of_members = len(group)

        for i in range(1,no_of_members):
            if (i == (no_of_members-1)):
                group_members += str(group[i])
                break
                
            group_members += str(group[i]) + ", "

        group_members_dict['member'] = group_members
        group_members_dict['badge'] = "N/A"

        group_members_list.append(group_members_dict)

    return group_members_list



"""
    -----------------------------------------------------------------------------
    This function generates a list of unregistered members from the file contents 
    @param groupRegFilePath - path to the file
    @return - list of unregistered members
    -----------------------------------------------------------------------------
"""
def getUnregMemberListFromFile(qaMembersUsersList):
    fileContents = readFileContentFromCSVfile(qaMembersUsersList)

    reg_members = []
    unreg_members = []

    for member in fileContents:

        members_name = member[0]
        registration_flag = str(member[1])

        if (registration_flag == 'No'):
            unreg_members.append(members_name)
        else:
            reg_members.append(members_name)

    return unreg_members


"""
    ---------------------------------------------------------------------------
    This function updates the member list in file  
    @param groupRegFilePath - path to the file
    @return - None
    ---------------------------------------------------------------------------
"""
def updateMemberListFile(qaMembersUsersList, registered_members):
    fileContents = readFileContentFromCSVfile(qaMembersUsersList)

    updated_members = []

    for member in fileContents:

        member_data = []

        members_name = str(member[0])
        if (members_name in registered_members):
            registration_flag = 'Yes'
        else:
            registration_flag = member[1]

        member_data.append(members_name)
        member_data.append(registration_flag)

        updated_members.append(member_data)

    writeListContentLbLToCSVfile(qaMembersUsersList,updated_members)