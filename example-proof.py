#install libraries
pip3 install python-vipaccess
pip3 install qrencode

#generate a Symantec VIP token with all details, including credential ID and TOTP secret code
vipaccess provision -p -t SYMC

#example output
'''
....
Generating request...
Fetching provisioning response...
Getting token from response...
Decrypting token...
Checking token...
Credential created successfully:
        otpauth://totp/VIP%20Access:SYMC54313423?period=30&digits=6&issuer=Symantec&secret=5YKAUZA4I4RAIJIZBU4KME34XLODWEUX&algorithm=SHA1
This credential expires on this date: 2022-03-14T14:57:31.615Z

You will need the ID to register this credential: SYMC54313423

You can use oathtool to generate the same OTP codes
as would be produced by the official VIP Access apps:

    oathtool -d6 -b --totp    5YKAUZA4I4RAIJIZBU4KME34XLODWEUX  # 6-digit code
    oathtool -d6 -b --totp -v 5YKAUZA4I4RAIJIZBU4KME34XLODWEUX  # ... with extra information
'''

#generate QR code for authentication apps like Google Authenticator
'''
qrencode -t ANSI256 'otpauth://totp/VIP%20Access:SYMC54313423?period=30&digits=6&issuer=Symantec&secret=5YKAUZA4I4RAIJIZBU4KME34XLODWEUX&algorithm=SHA1'
'''

