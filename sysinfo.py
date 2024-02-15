import io
def checkos():
    try:
        with open("etc/kernelver") as file:
            return "NACO"
    except IOError:
        try:
          with open("etc/monacover") as monacofile:
            return "Monaco"
        except IOError:
          return "Other"

def sysinfo():
    os = checkos()
    osver = ""
    term = ""
    if (os == "NACO"):
        try:
            import lib.sysinfo as _sysinfo
            osver = _sysinfo.sysver()
            term = _sysinfo.term()
            print("""
          ((((((         ((((((         
          ((((((((       ((((((         
          (((((((((      ((((((         
          (((((((((((    ((((((         
          ((((((((((((   ((((((         
          (((((((((((((  ((((((         
          (((((((((((((((((((((         
          (((((((((((((((((((((         
          (((((((((((((((((((((         
          (((((((((((((((((((((         
          (((((((((((((((((((((         
          ((((((  (((((((((((((         
          ((((((   ((((((((((((         
          ((((((     ((((((((((         
          ((((((      (((((((((         
          ((((((       ((((((((                    
                  """)
            print("OS: " + os)
            print("Version: " + osver)
            print("Terminal: " + term)
        finally:
            pass
    elif (os == "Monaco"):
        print("""
                                                      
                                        
                                        
                  *****                  
                  @@@@@                 
*****            @@@@@@@            ****
  @@@          @@@@@@@@@@@          @@@ 
   @@@@      @@@@@@@@@@@@@@@      @@@@  
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
                                        
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
                                        
                                        
              """)
        print("OS: " + os)
    else:
      print("OS: " + os)
