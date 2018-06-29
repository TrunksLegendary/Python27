import os
import subprocess


def ExecuteCMD(CMD, RES = False):
    import ctypes
    class disable_file_system_redirection:
        _disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
        _revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
        def __enter__(self):
            self.old_value = ctypes.c_long()
            self.success = self._disable(ctypes.byref(self.old_value))
        def __exit__(self, type, value, traceback):
            if self.success:
                self._revert(self.old_value)

    from subprocess import PIPE, Popen
    with disable_file_system_redirection():
        OBJ = Popen(CMD, shell = True, stdout = PIPE, stderr = PIPE)
    out, err = OBJ.communicate()
    print out
    print err
    RET = OBJ.returncode
    if RET == 0:
        if RES == True:
            if out:
                return out.strip()
            else:
                return True
        else:
            return True
    else:
        if RES == True:
            if err:
                return err.strip()
            else:
                return False
        else:
            return False

CMD=os.environ['Systemdrive']+r'\Program Files\Sophos\Sophos Endpoint Agent\uninstallcli.exe'
print CMD

if os.path.exists(CMD):
    print "Uninstallting Sophos"
    
    process = ExecuteCMD(CMD)
    if process :
        print "Uninstallation  Successfull"
    else:
        print "Sophos need to restart your  system and run the script Again"
else:
    print "Sophos Endpoint agent is not installed"
        
