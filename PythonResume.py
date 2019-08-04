#!/usr/bin/python

import webbrowser

#education
education = ("1999 - 2003 | \033[1mBilkent University\033[0m | B.A. in International Relations\n CGPA:\033[0m 3.30 / 4.00 - Outstanding Academic Achievement Scholarship\n2004 - 2006 | \033[1mBilkent University\033[0m | Masters Degree Business Administration\n CGPA: 3.69 / 4.00 - Tuition Waiver Scholarship\n2005 - 2006 | \033[1mJonkoping International Business School\033[0m | ERASMUS Exchange Student\nJul 2019 - Sep 2019 | \033[1mBrainstation - Toronto\033[0m | Certificate in Digital Marketing")

#work experience
workExperience = ("2006 - 2008 | \033[1mArcelik\033[0m | Territory Sales Representative\n2009 - 2011 | \033[1mHonda Motor Company\033[0m | District Sales Manager\n2011 - 2016 | \033[1mFord Motor Company\033[0m | District Sales Manager\n2016 - 2017 | \033[1mHonda Motor Company\033[0m | District Sales Manager\n2017 - 2019 | \033[1mHonda Plaza Terakki\033[0m | Fleet Leasing Manager\n2019 - now  | \033[1mBell Canada\033[0m | Territory Sales Consultant")

#skills
skills = ("Business Analysis, Business Development, Business Planning, Competitive Analysis, Continuous Improvement, \nCustomer Relationship Management (CRM), Customer Retention, Customer Satisfaction, Customer Service,\nForecasting, Key Account Management, Leadership, Management,\nMarketing, Market Analysis, Marketing Strategy, Mentorship, Negotiation, \nPricing, Project Management, Strategic Planning, Sales, Sales Operations, Sales Process, \nTeam Management, Team Leadership, Teamwork, \n\033[1mLanguages:\033[0m English, Turkish, Italian\n\033[1mSoftware:\033[0m HTML, CSS, Python, Microsoft Office, Microsoft Excel, Microsoft Word, Microsoft PowerPoint")

#volunteer experience
volunteer = ("2017 - 2018 | \033[1mGaranti Partners\033[0m | Business Mentor\n2019 - now  | \033[1mCanadian Cancer Society\033[0m | Fundraiser")

#select section
section = [1, 2, 3, 4, 5, 6]
view1 = int(input("Which section of the Resume would you like to see? \n1 for Education ; 2 for Work Experience ; 3 for Skills ; 4 for Volunteer Experience\n->"))

#print section
if view1 == section[0] :
    print(education)
if view1 == section[1] :
    print(workExperience)
if view1 == section[2] :
    print(skills)
if view1 == section[3] :
    print(volunteer)

#select next section or go to LinkedIn profile

view2 = int(input("Would you like to see another section of the Resume? \n1 for Education ; 2 for Work Experience ; 3 for Skills ; 4 for Volunteer Experience\nAlternatively, you can hit 5 to visit my LinkedIn Profile or hit 6 to terminate this program\n->"))

#print section
if view2 == section[0] :
    print(education)
if view2 == section[1] :
    print(workExperience)
if view2 == section[2] :
    print(skills)
if view2 == section[3] :
    print(volunteer)
if view2 == section[4] :
    webbrowser.open_new("https://www.linkedin.com/in/aydingoz/")
    import sys
    print("My LinkedIn Profile will open in a new browser window. Let's keep in touch")
    sys.exit(0)
if view2 == section[5]:
    import sys
    print("Thanks for stopping by. Have a nice day!")
    sys.exit(0)


#select next section or go to LinkedIn profile

view3 = int(input("Would you like to see another section of the Resume? \n1 for Education ; 2 for Work Experience ; 3 for Skills ; 4 for Volunteer Experience\nAlternatively, you can hit 5 to visit my LinkedIn Profile or hit 6 to terminate this program\n->"))

#print section
if view3 == section[0] :
    print(education)
if view3 == section[1] :
    print(workExperience)
if view3 == section[2] :
    print(skills)
if view3 == section[3] :
    print(volunteer)
if view3 == section[4] :
    webbrowser.open_new("https://www.linkedin.com/in/aydingoz/")
    import sys
    print("My LinkedIn Profile will open in a new browser window. Let's keep in touch")
    sys.exit(0)
if view3 == section[5]:
    import sys
    print("Thanks for stopping by. Have a nice day!")
    sys.exit(0)

#select next section or go to LinkedIn profile

view4 = int(input("Would you like to see another section of the Resume? \n1 for Education ; 2 for Work Experience ; 3 for Skills ; 4 for Volunteer Experience\nAlternatively, you can hit 5 to visit my LinkedIn Profile or hit 6 to terminate this program\n->"))

#print section
if view4 == section[0] :
    print(education)
if view4 == section[1] :
    print(workExperience)
if view4 == section[2] :
    print(skills)
if view4 == section[3] :
    print(volunteer)
if view4 == section[4] :
    webbrowser.open_new("https://www.linkedin.com/in/aydingoz/")
    import sys
    print("My LinkedIn Profile will open in a new browser window. Let's keep in touch")
    sys.exit(0)
if view4 == section[5]:
    import sys
    print("Thanks for stopping by. Have a nice day!")
    sys.exit(0)

#select next section or go to LinkedIn profile

view5 = int(input("Would you like to see another section of the Resume? \n1 for Education ; 2 for Work Experience ; 3 for Skills ; 4 for Volunteer Experience\nAlternatively, you can hit 5 to visit my LinkedIn Profile or hit 6 to terminate this program\n->"))

#print section
if view5 == section[0] :
    print(education)
if view5 == section[1] :
    print(workExperience)
if view5 == section[2] :
    print(skills)
if view5 == section[3] :
    print(volunteer)
if view5 == section[4] :
    webbrowser.open_new("https://www.linkedin.com/in/aydingoz/")
    import sys
    print("My LinkedIn Profile will open in a new browser window. Let's keep in touch")
    sys.exit(0)
if view5 == section[5]:
    import sys
    print("Thanks for stopping by. Have a nice day!")
    sys.exit(0)
