# Author : Pawan Trivedi

import os

def yumconfig():
    print('Configuring yum on your system')
    os.chdir('/etc/yum.repos.d')
    docker_conf = open('docker.repo', 'w')
    docker_conf.write("""
    [docker]
    baseurl = 'https://download.docker.com/linux/centos/7/x86_64/stable'
    gpgcheck = 0 """)
    docker_conf.close()

def install_docker():
    os.system('sudo yum install docker')
    os.system('sudo systemctl start docker')

def status_docker():
    re =os.system('sudo systemctl status docker')
    if re != 0:
        os.system('sudo systemctl start docker')

def info_docker():
    os.system('sudo docker info')

def os_image():
    print('''\n Select Which os image you want to download
        1 centos
        2 ubuntu
        ''')
    image_choice = input('Enter your choice ')
    if int(image_choice) == 1:
        os.system('sudo docker pull centos')
    elif int(image_choice) == 2:
        os.system('sudo docker pull ubuntu:20.04')

def launch_newos():
    print('Availble images are \n')
    available_image = os.system('sudo docker image ls')
    print('\n')
    os_name = input('Enter the os name ')
    image_name  = input('Enter the image ')
    os.system('sudo docker run -it --name {} {} '.format(os_name,image_name))

def list_allos():
    os.system('sudo docker ps -a')

def attach_os():
    print('All availble os...\n')
    os.system('sudo docker ps -a')
    os_start_name = input('\nEnter the OS name that you want to start and attach ') 
    os.system('sudo docker start {}'.format(os_start_name))
    os.system('sudo docker attach {}'.format(os_start_name))

def rm_os():
    print('All the availbel Os are...\n')
    os.system('sudo docker ps -a')
    os_stop_name = input('\n Which os you want to remove: ')
    os.system('sudo docker rm {}'.format(os_stop_name))
  
def rm_osimage():
     print('All the os images are...\n')
     os.system('sudo docker image ls')
     remove_image = input('Which image you want to remove ')
     os.system('sudo docker rmi {}'.format(remove_image))

  
while True:

    os.system('clear') 
    os.system('tput setaf 3')
    print(''' \t\t\t
    +--------------------------------+
    |  Welcome to the Docker Program |
    +--------------------------------+    
    ''')
    os.system('tput setaf 7')
    print('''
                    ##         .
                 ## ##        ==                      
           ## ## ## ## ##    ===                      
         /""""""""""""""""\___/  ===                  
    ~~~ { ~~  ~~~~  ~~~~  ~~~ ~/   ===--  ~~~        
        \______ 0           __/                       
         \     \         __/									
          \_____\_______/
    ''')
        
    print('''\n
         0. Need to configure yum for Docker : Login as root
         1. Install Docker
	 2. Check the Status of Docker, If it's stopped --> start the docker
	 3. check info of docker
	 4. Download os image for Docker
	 5. Launch a new OS 
	 6. List all the OS ( Running and Shutdown) 
         7. start a shutdown os and go inside
	 8. Remove or Delete OS permanentely
	 9. Remove the downloaded os image
	 10.To exit
    ''')

    choice  = input('Enter the choice ')
    print('\n')
    if int(choice) == 0:
        yumconfig()

    elif int(choice) == 1:
        install_docker()
        
    elif int(choice) == 2:
        status_docker()

    elif int(choice) == 3:
        info_docker()
	    
    elif int(choice) == 4:
        os_image()
	    
    elif int(choice) == 5:
       launch_newos()

    elif int(choice) == 6:
        list_allos()                    

    elif int(choice) == 7:
        attach_os()
        	
    elif int(choice) == 8:
        rm_os()

    elif int(choice) == 9:
       rm_osimage()
	    
    elif int(choice) == 10:
        exit()

    input("Enter to continue...")
	


