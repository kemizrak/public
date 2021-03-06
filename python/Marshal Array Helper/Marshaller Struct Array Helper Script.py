"""

Objective:
    We are currently having difficulties with marshalling data types with nested structure array from C to C#.

    e.g

        MyStruct
        {
        int myInt;
        NestedStruct struct[10];
        }

        NestedStruct
        {
        char x[35];
        int value;
        }

    When we marshal the struct we are currently getting errors. Lots of suggestions from
    google and stackoverflow was tried but we failed.

        [MarshalAs(UnmanagedType.ByValArray,SizeConst = 10)]
        public NestedStruct[] NestedStructArray; // this doesn't work and we get Exception error.


    The workaround found as of the moment is to create a separate variable instead of declaring them as array.

	
	If you run the script, it will output a file. From there, you can check the file and you will see:
	
	// Generated by Python Script
	// This part will be placed inside the structure
	public NestedStruct nestedstructelems0;
	public NestedStruct nestedstructelems1;
	public NestedStruct nestedstructelems2;

	// Generated by Python Script
	// This part can be used to declare an array for easier access
	{nestedstructelems0,nestedstructelems1,nestedstructelems2}

	This will take lots of manual work especially if the array is very big. Just copy and paste and test.

License:

    This program is free software. It comes without any warranty, to
    the extent permitted by applicable law. You can redistribute it
    and/or modify it under the terms of the Do What You Want To Public
    License, Version 3, as published by Devin Weaver. See
    http://tritarget.org/wywtpl/COPYING for more details.


Revision:
    Version 00.08.00
        - Initial release


Notes:
	Fully tested with Python 2.7.6
	
    Please feel free to play with this tool.
"""


# USERS CAN MODIFY THIS #

STR_MODIFIER="public"

STR_VARIABLE_TYPE="NestedStruct"

STR_VARIABLENAME="nestedstructelems"

STR_VARIABLE_OWNER="owner." # you can leave this as "" if you dont want it to have an owner
STR_VARIABLE_OWNER="" # you can leave this as "" if you dont want it to have an owner

STARTING_IDX=0
NUM_ELEMENTS=3

OUTFILENAME="c:\\temp\\out.txt"

########################################
### DO NOT MODIFY ANYTHING BELOW #######
########################################

def GenStructString():
    str='// Generated by Python Script\n// This part will be placed inside the structure\n'
    for x in range (0,NUM_ELEMENTS):
        str+="%s %s %s%d;\n" % (STR_MODIFIER.strip(),STR_VARIABLE_TYPE.strip(),STR_VARIABLENAME.strip(),STARTING_IDX+x)
    return str



def GenArrayString():
    str='\n// Generated by Python Script\n// This part can be used to declare an array for easier access\n'
    str+='{'
    for x in range (0,NUM_ELEMENTS):
        str+="%s%s%d," % (STR_VARIABLE_OWNER.strip(),STR_VARIABLENAME.strip(),STARTING_IDX+x)


    return str[:-1] + '}'


print "=== Marshal Helper Tool for Arrayed Structures ==="
print "Processing..."

with open(OUTFILENAME,'w') as f:
    f.write(GenStructString())
    f.write(GenArrayString())

print "Done! Please open the file: " + OUTFILENAME
