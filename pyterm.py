                    ###############################################################################################################
                    ##  THIS PROGRAM IS FOR TESTING PURPOSES ONLY AND MAY NOT BE COPIED OR DISTRIBUTED IN ANY WAY SHAPE OR FORM  ##
                    ##  ALL RIGHTS ARE EXPLICITLY RESERVED TO THE ORIGINAL AUTHOR. THIS PROGRAM MAY BE USED FOR EDUCATIONAL      ##
                    ##  PURPOSES AND DEVELOPMENT PURPOSES ONLY. ANY COPY OF THIS PROGRAM THAT IS CLAIMED BY ANYONE OTHER THAN    ##
                    ##  THE AUTHOR IS A DIRECT VIOLATION OF LAW 187 IN THE INTERNATIONAL JUSTICE ACT.                            ##
                    ###############################################################################################################
        

#Imports->>---------#
from datetime import datetime as dt
from glob import glob
import os, sys, platform as pf, time as t, subprocess as sp, random, re
#-------->>--------#

#-------->>--------#
try:
    from colorama import Fore, Style, Back, init as colorinit
    colorinit()
except ImportError:
    print('Module not found: colorama\nIf you run pip do: python -m pip install colorama\nIf not then do python -m pip upgrade-pip')
    _303()
#-------->>--------#

# --> Local <-- # :) 
cmdhist = []    # ;)
# --> Local <-- # :)


#Commands
#-------->>--------#
def echo(text):
    print(text)
    
def crayon(text):
    print(Fore.YELLOW+text+Fore.WHITE)
    
def processor():
    print('Processor', pf.processor())
    
def version():
    print('Python', pf.python_version())
    
def roll():
    x = random.randint(1,6)+random.randint(1,6)
    print('You rolled a', str(x)+'!')
    
def listall():
    for file in glob('./*'):
        
        if os.path.isdir(file):
            print(Fore.BLUE+file+Fore.WHITE)
            
        if os.path.isfile(file):
            if file.endswith('.py') == True:
                print(Fore.YELLOW+file+Fore.WHITE)
                
            if file.endswith('.dll') == True:
                print(Fore.LIGHTWHITE_EX+file+Fore.WHITE)
                
            if file.endswith('.regtrans-ms') == True:
                print(Fore.CYAN+file+Fore.WHITE)
                
            if file.endswith('.NET') == True:
                print(Fore.LIGHTGREEN_EX+file+Fore.WHITE)
                
            if file.endswith('}') == True:
                print(Fore.LIGHTBLUE_EX+file+Fore.WHITE)
            if file.endswith('.txt') == True:
                print(Fore.LIGHTRED_EX+file+Fore.WHITE)
            if file.endswith('.txt') == True:
                print(Fore.LIGHTBLUE_EX+file+Fore.WHITE)
            else:
                print(Fore.YELLOW+file+Fore.WHITE)
    return;

def date():
    print(dt.now().strftime('%X'))
    
def cd(folder):
    try:
        os.chdir(folder)
    except FileNotFoundError:
        print('- Not Found | Suggested Command: ls')
        
def time():
    print(dt.now().strftime('%H:%M:%S.%f'))
    
def theme(style):
    if style == 'bright':
        #print(Style.BRIGHT+Back.BLACK+Fore.WHITE+f'Set theme to {style}')
        print('Command under maintenance!')
        return;
    
    if style == 'dim':
        print(Style.DIM+Back.BLACK+Fore.WHITE+f'Set theme to {style}')
        return;
    
    else:
        print('That is not a theme! Suggested Command: help 3')
        return;

    
def showthemes():
    print(Style.BRIGHT+'bright')
    print(Style.DIM+'dim'+Style.NORMAL)
    return;


def setcolor(color):
    
    color = color.lower()
    
    if color == 'red':
        print(Fore.RED+f'Changed color to {color}')
        
    if color == 'white':
        print(Fore.WHITE+f'Changed color to {color}')
        
    if color == 'black':
        print(Fore.BLACK+f'Changed color to {color}')
        
    if color == 'cyan':
        print(Fore.CYAN+f'Changed color to {color}')
        
    if color == 'magenta':
        print(Fore.MAGENTA+f'Changed color to {color}')
        
    if color == 'green':
        print(Fore.GREEN+f'Changed color to {color}')
        
    if color == 'blue':
        print(Fore.BLUE+f'Changed color to {color}')
        
    if color == 'yellow':
        print(Fore.YELLOW+f'Changed color to {color}')

        
def mkdir(fol):
    os.mkdir(fol)
    print(f'created: {Fore.YELLOW+fol+Fore.WHITE}')


def mkfile(file):
    with open(file, 'w') as file:
        file.write('Created file on {}!\n'.format(dt.now().strftime('%c')))
        file.close()
    print('Created {}'.format(file.name))


def _303():
    print(Fore.LIGHTRED_EX+'Exiting..')
    t.sleep(1)
    sys.exit(0)

    
def rmdir(fol):
    os.rmdir(fol)
    print(f'deleted: {Fore.YELLOW+fol+Fore.WHITE}')

    
def rmfile(name):
    name = str(name)
    try:
        os.remove(name)
        print(f'{Fore.YELLOW+"Successfully removed"} {file.name()+Fore.WHITE}')
        start()
    except FileNotFoundError:
        print(f'{name} not found! Please check your spelling and try again!')
        start()

    
def help_(page):
    if page == '1':
        print('echo <text>  ----> Returns output')
        print('help <page>  ----> Display help menu')
        print('help all     ----> Shows all commands')
        print('crayon <text> ---> Display colorized text')
        print('processor    ----> Displays processor information')
        print('version      ----> Gets the python version\n')
        print(Fore.YELLOW+'      - Page 1/4 -'+Fore.WHITE)
        return;

    
    if page == '2':
        print('roll ----> Rolls the dice')
        print('list ----> lists all items in folder')
        print('date ----> gets the date')
        print('time ----> gets the time')
        print('cd   ----> changes directory')
        print(Fore.YELLOW+'      - Page 2/4 -'+Fore.WHITE)
        return;

    
    if page == '3':
        print('setcolor ----> Changes the color of the terminal text')
        print('resetcolor --> Resets the color to default')
        print('theme <>  ---> Themes: Dim ')
        print('mkdir <folder> Creates a folder')
        print('mkfile <name>  Creates a file')
        print(Fore.YELLOW+'      - Page 3/4 -'+Fore.WHITE)
        return;

    
    if page == '4':
#       print('rdfile <file>  Reads the contents of a file')
#       print('rmfile <name>  Permanently deletes a specified file')
        print('rmdir <folder> ---> Deletes any given folder')
        print('sleep <time>   ---> pauses the terminal for x amount of seconds')
        print('history        ---> Relays command history')
        print('exit/logout--> Quits the program')
        print(Fore.YELLOW+'      - Page 4/4 -'+Fore.WHITE)
        return;

    
    if page == 'all':
        print('echo <text>  ----> Returns output')
        print('help <page>  ----> Display help menu')
        print('help all     ----> Shows all commands')
        print('crayon <text> ---> Display colorized text')
        print('processor    ----> Displays processor information')
        print('version      ----> Gets the python version')
        print('roll ----> Rolls the dice')
        print('list ----> lists all items in folder')
        print('date ----> gets the date')
        print('time ----> gets the time')
        print('cd   ----> changes directory')
        print('setcolor ----> Changes the color of the terminal text')
        print('resetcolor --> Resets the color to default')
        print('theme <>  ---> Themes: Dim ')
        print('mkfile <name>  Creates a file')
        print('mkdir <folder> Creates a folder')
#       print('rdfile <file>  Reads the contents of a file')
#       print('rmfile <name>  Permanently deletes a specified file')
        print('rmdir <folder> ---> Deletes any given folder')
        print('sleep <time>   ---> pauses the terminal for x amount of seconds')
        print('history        ---> Relays command history')
        print('exit/logout--> Quits the program')
    else:
        print(f'There is no page {page}!')
#-------->>--------#

        
os.chdir(r'C:\\')


# MAIN
#-------->>--------#
def start():
    
    while 1:
        
        Q = input(os.getcwd()+' >> ')
        cmdhist.append(Q)
        
        if Q.startswith('processor') == True:
            processor()

            
        if Q.startswith('sleep') == True:
            try:
                
                num = re.findall(r'[\w]+', Q)[1]
                time.sleep(int(num))
                
            except IndexError:
                print('Please specify an amount!')
                
            except ValueError:
                print('That is not a number!')

        if Q.startswith('quit') or Q.startswith('exit') == True:
            _303()

            
        if Q.startswith('echo') == True:
            try:
                echo(re.findall(r'[\w]+', Q)[1])
            except IndexError:
                print('Please specify some text to echo | suggested command: help 1')
                continue

            
        if Q.startswith('crayon') == True:
            try:
                crayon(re.findall(r'[\w]+', Q)[1])
            except IndexError:
                print('Please specify a color to color in!')
                continue
            
        if Q.lower() == 'history':
            trcker = 0
            for cmd in cmdhist:
                trcker += 1
                print(f"{Fore.LIGHTGREEN_EX+str(trcker)+'.'+Fore.WHITE} {cmd}")
                
        if Q.startswith('help') == True:
            
            try:
                
                arg = re.findall(r'[\w]+', Q)[1]
                arg = str(arg.lower())
                
                if arg == 'all':
                    help_('all')
                    start()
                
                if arg == '1':
                    help_(arg)
                    start()
                
                if arg == '2':
                    help_(arg)
                    start()
                
                if arg == '3':
                    help_(arg)
                    start()
                
                if arg == 'roll':
                    print('Rolls the dice! Usage: roll')
                    start()

                if arg == 'rmfile':
                    print('Deletes a file. | Usage: rmfile FILE_NAME\nNote: Must be a text file!')
                    start()
                    
                if arg == 'list':
                    print('Lists all items in current folder | Usage: list\nTip: You can also do ls')
                    start()
                
                if arg == 'ls':
                    print('Lists all items in current folder | Usage: ls\nTip: You can also do list')
                    start()
                
                if arg == 'date':
                    print('shows the date! | Usage: date')
                    start()
                
                if arg == 'theme':
                    print('Sets a color theme! Usage: theme <theme>\nTip: Do showthemes to view all color themes!')
                    start()
                
                if arg == 'version':
                    print('Displays the versio of python that you are running')
                    start()

                if arg == 'mkfile':
                    print('Creates a text file | Usage: mkfile FILE_NAME\nNote: This command can only create text files.')
                    start()
                    
                if arg == 'mkdir':
                    print('Creates a folder | Usage: Do mkdir FOLDER_NAME to create a folder')
                    start()
                
                if arg == 'rmdir':
                    print('Removes a folder | Usage: rmdir FOLDER_NAME <be careful with this command>')
                    start()
                
                if arg == 'setcolor':
                    print('Permanantly sets the text color | Usage: setcolor <color>')
                    start()
                
                if arg == 'resetcolor':
                    print('''Provided that your terminal is black with white text,
                          it resets the color of your terminal\nUsage: resetcolor''')
                    start()
                
                if arg == 'cd':
                    print('Changes the directory. | Usage: cd <folder>\nTip: Do ls to list all folders')
                    start()
                
                if arg == 'history':
                    print('Shows users command history. | Usage: history')
                    start()
                
                if arg == 'crayon':
                    print('Prints a demo of desired text. | Usage: crayon <text>')
                    start()
                
                if arg == 'echo':
                    print('Outputs desired text | Usage: echo <command>')
                    start()
                
                if arg == 'sleep':
                    print('Disables commands for a set amount of seconds | Usage: sleep <amount>')
                    start()
                
                if arg == 'processor':
                    print('Reviews and display processor details | Usage: processor')
                    start()
                
                if arg == 'exit':
                    print('Exits the terminal | Usage: exit')
                    start()
                
                if arg == 'quit':
                    print('An alias to the \'exit\' command. Do: help exit for more information')
                    start()

                if arg == 'rdfile':
                    print('The read file command allows the user to view the contents of a provided file\nUsage: rdfile <filename>')
                    start()

                else:
                    print(f'Hey there, \"{arg}\" is not in my inventory. Do help all for a list of commands')
                    start()
                          
            except IndexError:
                print('You haven\'t specified an argument. Did you mean help all?')
                start()

        if Q.startswith('roll') == True:
            roll()
            
        if Q.startswith('list') == True:
            listall()
            
        if Q.startswith('version') == True:
            version()
            
        if Q.startswith('mkdir') == True:
            try:
                mkdir(re.findall(r'[\w]+', Q)[1])
            except IndexError:
                print('Please specify a folder!')
                continue
            except FileNotFoundError:
                print(Fore.RED+f'That is not a folder! {Fore.WHITE+"Suggested Command: ls"}'+Fore.WHITE)
                
        if Q.startswith('rmdir') == True:
            try:
                rmdir(re.findall(r'[\w]+', Q)[1])
            except IndexError:
                print('Please specify a folder!')
                continue
            
            except FileNotFoundError:
                print(Fore.RED+f'That is not a folder! {Fore.WHITE+"Suggested Command: ls"}'+Fore.WHITE)
                
            except PermissionError:
                print(Fore.RED+'You don\'t have permission to delete that folder'+Fore.WHITE)
                
        if Q.startswith('rmfile') == True:
            try:
                rmfile(re.findall(r'[\w]+', Q)[1])
                
            except IndexError:
                print(Fore.RED+'Please specify a file to delete!'+Fore.WHITE)
                continue
            
            except PermissionError:
                print(Fore.RED+'You don\'t have permission to delete that file!'+Fore.WHITE)
                   
        if Q.startswith('ls') == True:
            listall()

            
        if Q.startswith('date') == True:
            date()

            
        if Q.startswith('time') == True:
            time()

            
        if Q.startswith('theme') == True:
            try:
                theme(re.findall(r'[\w]+', Q)[1])
            except IndexError:
                print('Please specify a theme!')
                continue

            
        if Q.startswith('cd') == True:
            try:
                if Q == r'cd\\':
                    cd('C:\\')
                    
                else:
                    cd(re.findall(r'[\w]+', Q)[1])
                    
            except IndexError:
                print('Please specify a folder')
                
            except PermissionError:
                print(Fore.RED+'You don\'t have access to that folder'+Fore.WHITE)
                
        if Q.startswith('setcolor') == True:
            try:
                setcolor(re.findall(r'[\w]+', Q)[1])
            except IndexError:
                print('Please specify a color')
                continue

            
        if Q.startswith('resetcolor') == True:
            print(Fore.WHITE+'--')
            continue
        
        
        if Q.startswith('mkfile') == True:
            try:
                mkfile(re.findall(r'[\w]+', Q)[1]+'.txt')
            except IndexError:
                print(Fore.RED+'Please specify a file to create!'+Fore.WHITE)
                continue
            
            except FileExistsError:
                print(Fore.RED+'That file already exists!'+Fore.WHITE)
                continue
            
            except Exception as Error:
                Error = str(Error)
                print(Error)
#-------->>--------#

# LAUNCH THE BABY :)
#-------->>--------#
if __name__ == '__main__':
    print(sys.argv[0])
    #start()
#-------->>--------#



    
