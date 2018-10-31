@echo off

XCOPY "%userprofile%\Desktop\Chat\Python Chat room" "C:\PyJaric\Chat" /D /E /C /R /I /K /Y 

XCOPY /v "C:\PyJaric\Chat\Client\client files\bullhorn_2CD_icon.ico" "%userprofile%\AppData"

xcopy /v "C:\PyJaric\Chat\Client\client files\Bullhorn_1.1.lnk" "%userprofile%\Desktop"  /Y

xcopy /v "C:\PyJaric\Chat\Client\client files\Bullhorn_1.1.lnk" "%userprofile%\Desktop" /Y

msg * Bullhorn has successfully installed.

rd /s /q "%userprofile%\Desktop\Chat"



