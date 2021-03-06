""" ====================================================================
NoLicense Public License   http://www.hanynet.com/nlpl.html

Version 1, 31 August 2011 (EN)



PREAMBLE

The fundamental principle of the license NoLicense Public License is the complete freedom of use and circulation of knowledge and therefore the absolute absence of specific obligations or requirements for its access.

PRINCIPLES

The works of intellect are usually regulated and governed by licenses that require an owner who owns full rights and who may grant a license to use, modify, copy, distribute and sell them.
The license NoLicense Public License (NLPL) is a non-license because it provides no distinction between the author, the owner and the user of the work. The use or the mere possession of a work, even involuntary or unconscious, determines the full and rightful ownership. As a result there is less chance that it may be claimed sole ownership on the work as it is impossible to attribute its origin and its intellectual property. This license certifies irrevocably the right of everyone to consider and treat the work as their own and dispose of it according to their possibilities and according to their will without any obligation, constraint or limitation. The license NoLicense Public License ensures that the works remain unchanged property of any owner, therefore collective ownerships. The real author of the work renounces in a definitive and irrevocable way to claim exclusive rights of any kind on the work. The actual author also renounces to be formally recognized as such. The spread of anonymous works is allowed and encouraged. The spread of works whose origin is clearly indicated is allowed and protected by the habits. To recognize the artistic, intellectual and technical merits of the actual author, to give practical support for the care, development and maintenance of the work, to encourage its use, dissemination, analysis and criticism are part of these habits.
As a non-license, the license NoLicense Public License certifies the state of fact and as such does not require that you accept its terms to be valid.

RULES

- No license is required to obtain, use, modify, copy or distribute this code.

- The possession of this code determines its properties. Anyone who comes into possession of this code becomes its owner.

- The owner has the code according to its will without any obligation, restriction or limit.

- The use of this code is under the sole responsibility of the user.

- The origin of this code is not formally determined or determinable.

- The origin of this code coincides with its ultimate goal, whatever it is. Any person receiving, using, modifying, distributing or copying this code assumes the responsibility of being the author and the owner.

- It is not necessary to accept the terms of this license to obtain, use, modify, copy or distribute this code.

- The principles and the effects of this license remain valid even if the terms of this license are not accepted.

- This license is not editable.

- The use of this license is free. Who uses this license is free.
==================================================================== """




""" ====================================================================
This program is for decoding Wiegand 26-bit data.
==================================================================== """



# This part can be modified
WIEGAND_26BIT_DATA='11111010010011111101000100'









""" ====================================================================
                 ### DONT TOUCH ANYTHING BELOW ###
==================================================================== """






class WiegandData:
    OddParity=None
    FacilityCode=None
    UserCode=None
    EvenParity=None
    Bit1Count=None





def DecodeWiegand26Bit(strData):
    wiegData=WiegandData()

    myData=strData

    dataaOnly=myData[1:-1]

    bit1Count=dataaOnly.count('1')

    intMyData=int(myData,2)

    oddParity=intMyData&0x01
    intMyData=intMyData>>1

    facilityCode=intMyData&0xFFFF
    intMyData=intMyData>>16

    userCode=intMyData&0xFF
    intMyData=intMyData>>8

    evenParity=intMyData&0x01

    wiegData.OddParity=oddParity
    wiegData.FacilityCode=facilityCode
    wiegData.UserCode=userCode
    wiegData.EvenParity=evenParity
    wiegData.Bit1Count=bit1Count

    return wiegData





if(__name__=='__main__'):

    wiegData=DecodeWiegand26Bit(WIEGAND_26BIT_DATA)

    print "ODDPARITY",wiegData.OddParity
    print "FACILITYCODE",wiegData.FacilityCode
    print "USERCODE",wiegData.UserCode
    print "EVENPARITY",wiegData.EvenParity

    print "Checking..." ,

    if 1:
        if((wiegData.Bit1Count%2)==0):
            print "EVEN PARITY is 1!"
        else:
            print "ODD PARITY is 1!"



# Eof