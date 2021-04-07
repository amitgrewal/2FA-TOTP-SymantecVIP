#This code was ran in Anaconda Command Prompt Terminal with the base(root) environment
#Make sure pip is installed

# Install latest release from PyPI or dlenski's GitHub Repo
pip3 install python-vipaccess
pip3 install https://github.com/dlenski/python-vipaccess/archive/HEAD.zip
#dependencies should be installed automatically

#instructions for usage
'''
usage: vipaccess provision [-h] [-p | -o DOTFILE] [-t TOKEN_MODEL]

optional arguments:
  -h, --help            show this help message and exit
  -p, --print           Print the new credential, but don't save it to a file
  -o DOTFILE, --dotfile DOTFILE
                        File in which to store the new credential (default
                        ~/.vipaccess)
  -i ISSUER, --issuer ISSUER
                        Specify the issuer name to use (default: Symantec)
  -t TOKEN_MODEL, --token-model TOKEN_MODEL
                        VIP Access token model. Often SYMC/VSMT ("mobile"
                        token, default) or SYDC/VSST ("desktop" token). Some
                        clients only accept one or the other. Other more
                        obscure token types also exist:
                        https://support.symantec.com/en_US/article.TECH239895.html
'''

#example output
'''
Generating request...
Fetching provisioning response from Symantec server...
Getting token from response...
Decrypting token...
Checking token against Symantec server...
Credential created successfully:
	otpauth://totp/VIP%20Access:SYMC12345678?secret=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&issuer=Symantec&algorithm=SHA1&digits=6
This credential expires on this date: 2019-01-15T12:00:00.000Z

You will need the ID to register this credential: SYMC12345678

You can use oathtool to generate the same OTP codes
as would be produced by the official VIP Access apps:

    oathtool    -b --totp AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  # output one code
    oathtool -v -b --totp AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  # ... with extra information
'''

#must install qrencode for the following code
pip3 install qrencode
#example of code to generate scannable QR code from secret for apps like Google Authenticator
'''
qrencode -t UTF8 'otpauth://totp/VIP%20Access:SYMCXXXX?secret=YYYY&issuer=Symantec&algorithm=SHA1&digits=6'
'''

#example of code to generate TOTP 6-digit codes
'''
usage: vipaccess show [-h] [-s SECRET | -f DOTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -s SECRET, --secret SECRET
                        Specify the token secret on the command line (base32
                        encoded)
  -f DOTFILE, --dotfile DOTFILE
                        File in which the credential is stored (default
                        ~/.vipaccess
'''


