import os
import platform
import _winreg


def gid(x):
    find=x
    winreg = _winreg
    REG_PATH1 = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    REG_PATH2 = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    registry_key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, REG_PATH1, 0, winreg.KEY_READ)
    winreg.CloseKey(registry_key)
    name = []
    string=[]

    registry_key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, REG_PATH1, 0, winreg.KEY_READ)
    i=0

    while True:
        try:
            sub_registry_key = winreg.EnumKey(registry_key, i)
            newpath1 = REG_PATH1 + '\\' + sub_registry_key
            new_registry_key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, newpath1, 0, winreg.KEY_READ)
            try:
                DisplayName, getname = winreg.QueryValueEx(new_registry_key, 'DisplayName')
                UninstallString, getname = winreg.QueryValueEx(new_registry_key, 'UninstallString')
                winreg.CloseKey(new_registry_key)
                name.append(DisplayName)
                string.append( UninstallString )
            except:
                pass
            i += 1
        except:
            break

    registry_key1 = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, REG_PATH2, 0, winreg.KEY_READ)
    ii=0
    while True:
        try:
            sub_registry_key1 = winreg.EnumKey(registry_key1, ii)
            newpath2 = REG_PATH2 + '\\' + sub_registry_key1
            new_registry_key1 = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, newpath2, 0, winreg.KEY_READ)
            try:
                DisplayName1, getname = winreg.QueryValueEx(new_registry_key1, 'DisplayName')
                DisplayVersion1, getname = winreg.QueryValueEx(new_registry_key1, 'DisplayVersion')
                UninstallString1, getname = winreg.QueryValueEx(new_registry_key1, 'UninstallString')
                winreg.CloseKey(new_registry_key1)
                name.append(DisplayName1)
                string.append(UninstallString1 )
            except:
                pass
            ii += 1
        except:
            break
    try:
        registry_key2 = winreg.OpenKey( winreg.HKEY_CURRENT_USER, REG_PATH1, 0, winreg.KEY_READ)
        iii=0
        while True:
            try:
                sub_registry_key2 = winreg.EnumKey(registry_key2, iii)
                newpath3 = REG_PATH1 + '\\' + sub_registry_key2
                new_registry_key2 = winreg.OpenKey( winreg.HKEY_CURRENT_USER, newpath3, 0, winreg.KEY_READ)
                try:
                    DisplayName2, getname = winreg.QueryValueEx(new_registry_key2, 'DisplayName')
                    UninstallString2, getname = winreg.QueryValueEx(new_registry_key2, 'UninstallString')
                    winreg.CloseKey(new_registry_key2)
                    name.append( DisplayName2)
                    string.append(UninstallString2 )
                except:
                    pass
                iii += 1
            except:
                break
    except:
        pass
    try:
        registry_key3 = winreg.OpenKey( winreg.HKEY_CURRENT_USER, REG_PATH2, 0, winreg.KEY_READ)
        iiii=0
        while True:
            try:
                sub_registry_key3 = winreg.EnumKey(registry_key3, iiii)
                newpath4 = REG_PATH2 + '\\' + sub_registry_key3
                new_registry_key3 = winreg.OpenKey( winreg.HKEY_CURRENT_USER, newpath4, 0, winreg.KEY_READ)
                try:
                    DisplayName3, getname = winreg.QueryValueEx(new_registry_key3, 'DisplayName')
                    UninstallString3, getname = winreg.QueryValueEx(new_registry_key3, 'UninstallString')
                    winreg.CloseKey(new_registry_key3)
                    name.append( DisplayName3 )
                    string.append(UninstallString3 )
                except:
                    pass
                iiii += 1
            except:
                break
    except:
        pass
    out={}
    for i in name:
        if find.lower() in i.lower():
            x=i
    for k,v in zip(name,string):
        out[k] = v
    x1=out[x]
    
    if x1:
        cmd=x1+' /quiet REBOOT=ReallySuppress REMOVE=ALL'
        os.popen(cmd).read()

def uni():
    arch=platform.machine()
    if 'AMD64' in arch:
        if os.path.exists(os.environ['PROGRAMFILES(X86)']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos Patch Agent")):
                os.chdir(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos Patch Agent"))
                print "\n\t*)Sophos Anti-Virus  Uninstallation started......"                
                out=os.popen("C:\Program Files\Sophos\Sophos Patch Agent\Sophos Patch Agent.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos Patch Agent")):
                os.chdir(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos Patch Agent"))
                print "\n\t*)Sophos Anti-Virus  Uninstallation started......"                
                out=os.popen("C:\Program Files\Sophos\Sophos Patch Agent\Sophos Patch Agent.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)
                
    else:
        if os.path.exists(os.environ['PROGRAMFILES']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES'],"Sophos Patch Agent")):
                print "\n\t*)Malwarebytes  Anti-Malware  Uninstallation started......"                
                os.chdir(os.path.join(os.environ['PROGRAMFILES'],"Sophos Patch Agent"))
                out=os.popen("C:\Program Files\Sophos\Sophos Patch Agent\Sophos Patch Agent.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)
                
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES'],"Sophos Anti-Virus")):
                os.chdir(os.path.join(os.environ['PROGRAMFILES'],"Sophos Anti-Virus"))
                print "\n\t*)Sophos Anti-Virus  Uninstallation started......"                
                out=os.popen("C:\Program Files\Sophos\Sophos Patch Agent\Sophos Patch Agent.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)
     
def uni2():
    arch=platform.machine()
    if 'AMD64' in arch:
        if os.path.exists(os.environ['PROGRAMFILES(X86)']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos Network Threat Protection")):
                print "\n\t*)Sophos Network Threat Protection  Uninstallation started......"                
                os.chdir(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos Network Threat Protection"))
                out=os.popen("C:\ProgramData\Sophos\AutoUpdate\cache\ntp64\Sophos Network Threat Protection.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)
                
    else:
        if os.path.exists(os.environ['PROGRAMFILES']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES'],"Sophos Network Threat Protection")):
                os.chdir(os.path.join(os.environ['PROGRAMFILES'],"Sophos Network Threat Protection"))
                print "\n\t*)Sophos Network Threat Protection  Uninstallation started......"
                out=os.popen("C:\ProgramData\Sophos\AutoUpdate\cache\ntp64\Sophos Network Threat Protection.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)

def uni3():
    if 'AMD64' in arch:
        if os.path.exists(os.environ['PROGRAMFILES(X86)']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos System Protection")):
                print "\n\t*)Sophos System Protection  Uninstallation started......"                
                os.chdir(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos System Protection"))
                out=os.popen("C:\ProgramData\Sophos\AutoUpdate\cache\ssp\SophosSystemProtection.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)
                
    else:
        if os.path.exists(os.environ['PROGRAMFILES']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES'],"Sophos System Protection")):
                os.chdir(os.path.join(os.environ['PROGRAMFILES'],"Sophos System Protection"))
                print "\n\t*)Sophos System Protection  Uninstallation started......"
                out=os.popen("C:\ProgramData\Sophos\AutoUpdate\cache\ssp\SophosSystemProtection.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)

def uni4():
    if 'AMD64' in arch:
        if os.path.exists(os.environ['PROGRAMFILES(X86)']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos Anti-Virus")):
                print "\n\t*Sophos Anti-Virus  Uninstallation started......"                
                os.chdir(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos Anti-Virus"))
                out=os.popen("C:\ProgramData\Sophos\AutoUpdate\cache\savxp\Sophos Anti-Virus.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)
                
                
    else:
        if os.path.exists(os.environ['PROGRAMFILES']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES'],Sophos Anti-Virus")):
                os.chdir(os.path.join(os.environ['PROGRAMFILES'],"Sophos Anti-Virus"))
                print "\n\t*)Sophos Anti-Virus  Uninstallation started......"
                out=os.popen(" C:\ProgramData\Sophos\AutoUpdate\cache\savxp\Sophos Anti-Virus.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)

def uni5():
    if 'AMD64' in arch:
        if os.path.exists(os.environ['PROGRAMFILES(X86)']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos Remote Management System")):
                print "\n\t*Sophos Remote Management System  Uninstallation started......"                
                os.chdir(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos Remote Management System"))
                out=os.popen("MsiExec.exe /X{FED1005D-CBC8-45D5-A288-FFC7BB304121} /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)
                   
    else:
        if os.path.exists(os.environ['PROGRAMFILES']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES'],Sophos Remote Management System")):
                os.chdir(os.path.join(os.environ['PROGRAMFILES'],"Sophos Remote Management System"))
                print "\n\t*)Sophos Remote Management System  Uninstallation started......"
                out=os.popen("MsiExec.exe /X{FED1005D-CBC8-45D5-A288-FFC7BB304121} /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)

def uni6():
    if 'AMD64' in arch:
        if os.path.exists(os.environ['PROGRAMFILES(X86)']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos AutoUpdate")):
                print "\n\t*Sophos AutoUpdate  Uninstallation started......"                
                os.chdir(os.path.join(os.environ['PROGRAMFILES(X86)'],"Sophos AutoUpdate"))
                out=os.popen("C:\ProgramData\Sophos\AutoUpdate\cache\sau\Sophos AutoUpdate.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)
                   
    else:
        if os.path.exists(os.environ['PROGRAMFILES']):
            if os.path.exists(os.path.join(os.environ['PROGRAMFILES'],Sophos AutoUpdate")):
                os.chdir(os.path.join(os.environ['PROGRAMFILES'],"Sophos AutoUpdate"))
                print "\n\t*)Sophos AutoUpdate  Uninstallation started......"
                out=os.popen("C:\ProgramData\Sophos\AutoUpdate\cache\sau\Sophos AutoUpdate.msi /VERYSILENT /SUPPRESSMSGBOXES /NORESTART").read()
                print(out)
"""
def uni4():
    import os
    import _winreg
    import re
    def check():
        inst=os.popen("wmic product get name,identifyingnumber").read()      
        return inst
    def reg():
        blacklist=r"Malwarebytes' Managed Client"
        def collectprograms(rtkey,pK,kA):
            try:
                list=[]
                oK=_winreg.OpenKey(rtkey,pK,0,kA)
                i=0
                while True:
                    try:
                        bkey=_winreg.EnumKey(oK,i)
                        vkey=os.path.join(pK,bkey)
                        oK1=_winreg.OpenKey(rtkey,vkey,0,kA)
                        try:
                            DN,bla=_winreg.QueryValueEx(oK1,'DisplayName')
                            inlist=[DN.strip(), vkey, pK]
                            list.append(inlist)
                            
                        except:
                            pass
                        i+=1
                    except:
                        break
            except:
                pass
            return list            
        uninstallkey_32='SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall'
        if 'PROGRAMFILES(X86)' in os.environ.keys():
            
            rklist=[(_winreg.HKEY_LOCAL_MACHINE,uninstallkey_32,_winreg.KEY_WOW64_32KEY | _winreg.KEY_READ),
                    (_winreg.HKEY_LOCAL_MACHINE,uninstallkey_32,_winreg.KEY_WOW64_64KEY | _winreg.KEY_READ),
                    (_winreg.HKEY_CURRENT_USER,uninstallkey_32,_winreg.KEY_WOW64_32KEY | _winreg.KEY_READ),
                    (_winreg.HKEY_CURRENT_USER,uninstallkey_32,_winreg.KEY_WOW64_64KEY | _winreg.KEY_READ)]
        else:
            
            rklist=[(_winreg.HKEY_LOCAL_MACHINE,uninstallkey_32,_winreg.KEY_READ),
                    (_winreg.HKEY_CURRENT_USER,uninstallkey_32,_winreg.KEY_READ)]

        bet=[]
        for i in rklist:
            col=collectprograms(i[0], i[1], i[2])
            for c in col:
                print c
                if blacklist in c:
                    bet.append(c[1])
        if not bet:
            print "Please Mention the valid blacklist Installed Software"
        else:
            for i in bet:
                print i
                j=i.replace(" ", '" "')
                v='\\'
                path="HKEY_LOCAL_MACHINE"+v+i
                path1="HKEY_LOCAL_MACHINE"+v+j
                got=path1
        return got
    inst=check()
    if len(inst)>0:
        find=re.findall("{.*}\s\sMalwarebytes'\sManaged\\sClient",inst)
        if len(find)>0:
            final=re.findall('{.*}',find[0])[0]            
            if len(final) == 38:
                print "\n\t*)Malwarebytes' Managed Client Uninstallation started......"  
                cmd='msiexec.exe /x %s /quiet REBOOT=ReallySuppress REMOVE=ALL'%final
                os.popen(cmd).read()
            else:
                fin=reg()
                fina=fin.split('\\')[-1]
                final1=re.findall('{.*}',fina)[0]
                print "\n\t*)Malwarebytes' Managed Client Uninstallation started......"  
                cmd='msiexec.exe /x %s /quiet REBOOT=ReallySuppress REMOVE=ALL'%final1
                os.popen(cmd).read()
                        
"""            
def checkapp(AppName):
    import _winreg
    import os
    AppName = AppName.lower()
    def DNDS(rtkey, pK, kA):
        ln = []
        lv = []
        try:
            oK = _winreg.OpenKey(rtkey, pK, 0, kA)
            i = 0
            while True:
                try:
                    bkey = _winreg.EnumKey(oK, i)
                    vkey = os.path.join(pK, bkey)
                    oK1 = _winreg.OpenKey(rtkey, vkey, 0, kA)
                    try:
                        tls = []
                        DN, bla = _winreg.QueryValueEx(oK1, 'DisplayName')
                        DV, bla = _winreg.QueryValueEx(oK1, 'DisplayVersion')
                        _winreg.CloseKey(oK1)
                        ln.append(DN)
                        lv.append(DV)
                    except:
                        pass
                    i += 1
                except:
                    break
            _winreg.CloseKey(oK)
            return zip(ln, lv)
        except:
            return zip(ln, lv)

    rK = _winreg.HKEY_LOCAL_MACHINE
    sK = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    openedKey = _winreg.OpenKey(rK, sK, 0, _winreg.KEY_READ)
    arch, bla = _winreg.QueryValueEx(openedKey, 'PROCESSOR_ARCHITECTURE')
    arch = str(arch)
    _winreg.CloseKey(openedKey)

    if arch == 'AMD64':
        fList = DNDS(_winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', _winreg.KEY_WOW64_32KEY | _winreg.KEY_READ)
        fList.extend(DNDS(_winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', _winreg.KEY_WOW64_64KEY | _winreg.KEY_READ))
        fList.extend(DNDS(_winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', _winreg.KEY_WOW64_32KEY | _winreg.KEY_READ))
        fList.extend(DNDS(_winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', _winreg.KEY_WOW64_64KEY | _winreg.KEY_READ))
    else:
        fList = DNDS(_winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', _winreg.KEY_READ)
        fList.extend(DNDS(_winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', _winreg.KEY_READ))
    fList = set(fList)

    lr = []
    rs = 0
    for i in fList:
        a, b = i
        if AppName in a.lower():
            lr.append('success: {} is installed'.format(a))
            lr.append('{:<25}{:5}'.format(a, b))
            rs += 1
        else:
            rs += 0
    if rs:
        return True
    return False

def recheck():
    app3=checkapp('Sophos Patch Agent')
    app8=checkapp('Sophos Patch Agent')
    if app3:
        print '\n\t\t*)Try again with Uninstall String'
        gid('Sophos Patch Agent')
        if app8:
            print "\n\t\t*)Sophos Patch Agent  Uninstalled Failed...."
            return '0'
        else:
            print "\n\t\t*)Sophos Patch Agent  Uninstalled Successfully...."
            return '1'
    else:
        print "\n\t*)Sophos Patch Agent  Uninstalled Successfully...."
        return '1'
def recheck1():
    app4=checkapp('Sophos Network Threat Protection')
    app9=checkapp('Sophos Patch Agent')
    if app4:
        print '\n\t\t*)Try again with Uninstall String'
        gid('Sophos Network Threat Protection')
        if app9:
            print "\n\t\t*)Sophos Network Threat Protection  Uninstalled Failed...."
            return '0'
        else:
            print "\n\t\t*)Sophos Network Threat Protection  Uninstalled Successfully...."
            return '1'

    else:
        print "\n\t*)Sophos Network Threat Protection  Uninstalled Successfully...."
        return '1'
def recheck2():
    app6=checkapp('Sophos System Protection')
    app10=checkapp('Sophos Anti-Virus')
    if app6:
        print '\n\t\t*)Try again with Uninstall String'
        gid('Sophos System Protection')
        if app10:
            print "\n\t\t*)Sophos Anti-Virus Uninstalled Failed...."
            return '0'
        else:
            print "\n\t\t*)Sophos Anti-Virus Uninstalled Successfully...."
            return '1'
            
    else:
        print "\n\t*)Sophos System Protection Uninstalled Successfully...."
        return '1'

def recheck3():
    app7=checkapp("Sophos Remote Management System")
    app11=checkapp('Sophos AutoUpdate')
    if app7:
        print "\n\t*)Sophos Remote Management System Uninstalled Failed...."        
    else:
        print "\n\t*)Sophos Remote Management System Uninstalled Successfully...."
        return '1'
    

app1=checkapp('Sophos Anti-Virus')
app2=checkapp('Sophos Patch Agent')
app5=checkapp('Sophos Network Threat Protection')
app7=checkapp("Sophos System Protection")

if app1:
    print "Sophos Anti-Virus is Found in the system"
    uni()
    r=recheck()
else:
    print "\nSophos Anti-Virus is not found in the system"
    r=1
if app2:
    print "\nSophos Patch Agent is Found in the System"
    uni2()
    r1=recheck1()
else:
    print "\nSophos Patch Agent is not found in the system"
    r1=1
if app5:
    print "\nSophos Network Threat Protection  is Found in the system"
    uni3()
    r2=recheck2()
else:
    print "\nSophos Network Threat Protection is not found in the system"
    r2=1

if app7:
    print "\nSophos System Protection is Found in the system"
    uni4()
    r3=recheck3()
else:
    print "\nSophos System Protection is not found in the system"
    r3=1

    


