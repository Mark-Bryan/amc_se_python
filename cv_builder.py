'''
 - Name
 - Occupation
 - Synopsis
 - Qualifications
 '''

cv_builder = {
'Name':{
    'first_name' : "Suhmayah", 
    'last_name' : "Banda",
    },

'occupation' : "Priest",
'Synopsis' : 'Hi there ! My name is Suhmayah Banda, I am a software developer',
'qualifications':[
    {
    'name' : 'Ordinary Level',
    'description' : 'I had my Olevels in PSS Bali'
    },

    {
        'name' : 'Advanced Level',
    'description' : 'I had my Alevels in PSS Mankon'
    }
    
    
    ]


}

print(cv_builder)

"""
CV for first_name last_name
occupation

About Me
Synopsis

Qualifications
----
qualification_name
qualification_description
---
"""

CV ={
    'Name':{
        'firstName' : 'Banyeh',
        'lastName' : 'Akika',
    },
'occupation' : 'Cook',

'About Me' : {
    'description' : 'I am a male who lives in the UK',
    },
'Synopsis' : 'I am a junior chef at McDonalds',

'Qualifications' : [
    {
        'qualification_name' : ' Assistant Chef',
        'qualification_description' : 'I am an assistant chef to the main chef at McDonalds restaurant. I represent the head chef when he is not arounf'
    }
]
    

}

print("CV For", CV['Name'][''])