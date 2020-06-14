## @package EngineeringTool
# 13Aug12 last change MPL

import os,sys,subprocess
from AzCamCommands import FindFile,GetObject
import Globals

def EngineeringTool():
    """
    Starts the EngineeringTool GUI.
    EngineeringTool is a interface for debugging AzCam controllers, written in LabVIEW.
    """

    status,f,p=FindFile('EngineeringTool.py')
    if status!=Globals.OK:
        return [Globals.ERROR,'EngineeringTool not found']
    GUIProgram=os.path.join(p,'builds/'+Globals.OSType,'EngineeringTool')

    # add proper extension for this OS
    if os.sys.platform.startswith('win'):
        GUIProgram=GUIProgram+'.exe'
    elif os.sys.platform.startswith('linux'):
        GUIProgram=GUIProgram+'.e'

    # make arguments
    args=['-s',str(Globals.LocalHost),'-p',str(GetObject('cmdserver').Port)]
    arg=' '.join(args)

    if os.name=='posix':
        s='xterm -e \'.\\'+GUIProgram+' '+arg+'\''
        subprocess.Popen(s,shell=True)
    else:
        s=GUIProgram+' '+arg
        subprocess.Popen(s)

    return [Globals.OK]

# execute
if __name__=='__main__':
    args=sys.argv[1:]
    EngineeringTool(*args)
