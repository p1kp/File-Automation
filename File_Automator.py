


# =============================================================================
# --PV$.1.0--#
# =============================================================================

import os, shutil, time

pwd = os.getenv('PWD')
try:
    print('\n//////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')
    str1 = "Welcome to File Automator" 
    str2 = str1.center(100)
    
    bold_start = '\033[1m'
    bold_end   = '\033[0m' 
    print ('    \033[1m \033[91m \033[4m'+str2+'\033[0m')
    
    #print(bold_start ,str2, bold_end)
    print('\n//////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')
    
    print('\033[1m\033[91m\033[4mPresent Working Directory\033[0m :',pwd)
    
    # 92=green, 91=red, 93=yellow
    #sipv --> search input variable #96 #100
    print()
    sipv = input("\033[1m\033[93m\033[4mEnter the file name that you want to move\033[0m : ")
    def find_files(filename, search_path):
       result = []
       path = '/Users'
    # Wlaking top-down from the root
       for root, dir, files in os.walk(path):
           if filename in files:
             result.append(os.path.join(root, filename))
       return result
    
    
    x = find_files(sipv,'/Users')
    print('\n'.join(map(str,x)))
    
    #cipv --> copy input variable
    print()
    cipv = input("\033[1m\033[93m\033[4mPaste File path shows above\033[0m : ")
    print()
    
    #Source path
    src = cipv
    
    #dipv --> Destination input variable
    dipv = input("\033[1m\033[93m\033[4mEnter your Destination\033[0m : ")
    print()
    
    #Destination path
    dst = dipv
    
    ld = os.path.dirname(dipv)
    print('\n--------------------------------------------------------------------------------------------------------------')
    print("\033[1m\033[93m\033[4mBefore moving file\033[0m : ") 
    print('--------------------------------------------------------------------------------------------------------------\n')
    
    ld1 = os.listdir(ld)
    file_count = len(ld1)
    
    print('\n'.join(map(str, ld1)))
    try:
        
        dest = shutil.move(src, dst)
        time.sleep(2)
        
    except Exception:
        print(" Destination path "+dest+" already exists")
    
    print('\n--------------------------------------------------------------------------------------------------------------')
    
    # List files and directories 
    # in "/Users / karanparmar / Downloads / Packages/  " 
    print('\n--------------------------------------------------------------------------------------------------------------')
    print("\033[1m\033[93m\033[4mAfter moving file\033[0m : ") 
    print('--------------------------------------------------------------------------------------------------------------\n')
    
    ld2 = os.path.dirname(dipv)
    ld3 = os.listdir(ld2)
    file_count1 = len(ld3)
    
    print('\n'.join(map(str, ld1)))
    print('--------------------------------------------------------------------------------------------------------------\n')
    
    
    print("Before moving file the total files of the {0} directory is {1} :".format(ld,file_count))
    print("After moving file the total files of the {0} directory is {1} :".format(ld,file_count1))
    print("\n\033[1m\033[92mYour file has been moved to your selected destination\033[0m\n")
    # Print path of newly 
    # created file 
    print("\033[1m\033[92m\033[4mDestination path\033[0m : ", '\033[1m\033[94m\033[4m',dest,'\033[0m') 

except:
    print("Something is Wrong. Please check.")


























