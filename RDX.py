#<\>!python3.11
import os,platform,time
fuck=platform.architecture()[0]
if fuck=="64bit":
    os.system('clear');print('[!] Your Device is 64 bit');time.sleep(1);print('\n\n[!] Your Python Version :');time.sleep(1);os.system('python --version')
    time.sleep(2)
    from rdx64 import register_device
    register_device()
else:
    print('\nYOUR DEVICE 32 BIT NOT SUPPORT')

#---------------------------------------------------------#
#                    THIS TOOL OWNED BY
#                  • MAHADI HASAN AFRIDI •
#---------------------------------------------------------#
