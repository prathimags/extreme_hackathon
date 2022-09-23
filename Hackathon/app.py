from flask import Flask, redirect, url_for, render_template, request
from libs.common_lib import *

groupRegFilePath="./Output_Files/hackathon_user_reg.csv"
qaMembersUsersList="./Output_Files/hackathon_members_list.csv"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/regform", methods=["GET", "POST"])
def regform():

    regArray = []
    
    if request.method == "POST":           
        
        group_name = request.form.get("group-name")
        group_members = request.form.getlist("group-members")        

        #print (group_name,group_members)

        regArray.append(group_name)
        
        for member in group_members:
            regArray.append(member)

        #print (regArray)

        writeArrayContentToCSVfile(groupRegFilePath,regArray,"a")

        updateMemberListFile(qaMembersUsersList, group_members)

        unreg_members = getUnregMemberListFromFile(qaMembersUsersList)
        return render_template("regMultiFormSuccess.html",members=unreg_members)

    unreg_members = getUnregMemberListFromFile(qaMembersUsersList)
    return render_template("regMultiForm.html",members=unreg_members)    


@app.route("/results")
def results():
    return render_template("redirect.html")

@app.route("/participantslist")
def participantlist():
    group_members = convertGroupMemContentToListOfDict(groupRegFilePath)
    return render_template("participantList.html", groups=group_members)

@app.route("/regformsuccess")
def regformsuccess():
    unreg_members = getUnregMemberListFromFile(qaMembersUsersList)
    return render_template("regMultiFormSuccess.html",members=unreg_members)

@app.route("/challenges")
def challenges():
    return render_template("challenges.html")

@app.route("/multiselect")
def multiselect():
    return render_template("multiselect.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
