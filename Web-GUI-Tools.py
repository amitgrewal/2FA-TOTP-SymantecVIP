'''
For an easier method, visit these 2 websites:
Puvox: https://puvox.software/tools/symantec-vip-qr-code
Stefan Sundin: https://stefansundin.github.io/2fa-qr/

The Puvox tool will generate the Symantec VIP token and provide the Symantec credential ID as well as the related TOTP secret code, plus a scannable QR code

Stefan Sundin's tool is a more general-use tool that allows the user to make custom QR codes for TOTP apps like Google Authenticator.
With the TOTP secret code from Puvox, you can copy and paste it into Stefan's tool and then customize the label and issuer portions to your liking.
This is not necessary, but it does make the entry in TOTP/2FA apps look nicer and makes it easier to identify the correct TOTP/2FA entry.

Finally, don't forget to register the credential ID on the Symantec VIP website/through your 2FA/TOTP organization.
      To do this, create an entry in your 2FA/TOTP app or program.
      Then, go to the Symantec VIP/your 2FA/TOTP organization's website and enter the credential ID.
      Next, get the 6-digit TOTP code from your 2FA/TOTP app or program.
      Finally, enter the 6-digit code on the Symantec VIP website and save it. Make sure to test if it works or not with another 6-digit code!

'''
