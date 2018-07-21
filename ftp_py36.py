from ftplib import FTP
import glob
import argparse
import os


def grabFile(file):
    filename = file
    print(filename)
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()


# def placeFile():
#    filename = 'ibc301qrq_drc.fits'
#    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
#    ftp.quit()

def parse_args():
    """Parses command line arguments.

    Parameters:
        nothing

    Returns:
        args : argparse.Namespace object
            An argparse object containing all of the added arguments.

    Outputs:
        nothing
    """

    # Create help string:
    path_help = 'Path to working directory.'
    host_help = 'Connect to host, default port (ex. archive.stsci.edu)'
    username_help = 'Login username'
    password_help = 'Login password'
    data_dir_help = 'Server directory with data'

    # Add arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-path', dest='path', action='store',
                        type=str, required=True, help=path_help)

    parser.add_argument('--host', '-host', dest='host', action='store',
                        type=str, required=True, help=host_help)

    parser.add_argument('--username', '-username', dest='username', action='store',
                        type=str, required=True, help=username_help)

    parser.add_argument('--password', '-password', dest='password', action='store',
                        type=str, required=True, help=password_help)

    parser.add_argument('--data_dir', '-data_dir', dest='data_dir', action='store',
                        type=str, required=True, help=data_dir_help)

    # Parse args:
    args = parser.parse_args()

    return args


# -------------------------------------------------------------------
if __name__ == '__main__':
    args = parse_args()

    os.chdir(args.path)  # cd into working directory
    # ftp = FTP('archive.stsci.edu')
    # ftp.login(user='anonymous', passwd='mckaymyles18@gmail.com')
    # ftp.cwd('/stage/anonymous/anonymous12084')
    ftp = FTP(args.host) # connect to host
    ftp.login(user=args.username, passwd=args.password) #Login username and password
    ftp.cwd(args.data_dir) # cd into data directory on the host server
    ftp.retrlines('LIST')# list all files in host server directory
    list_of_files = ftp.nlst() #makes a list of all the files in server directory

    for file in list_of_files: #iterates through file list
        print('Copying {} to {}'.format(file, args.path)) # print statement
        grabFile(file)# download file from server

    ftp.quit() # quit out of ftp
    # placeFile()

    # ====================================================
    
    #Example command line run
    #staged hst data from MAST
    #run ftp_py36.py --path='/Users/mmckay/Desktop/' --host='archive.stsci.edu' --username='anonymous' --userpw='mckaymyles18@gmail.com' --data_dir='/stage/anonymous/anonymous12084'

    # ====================================================


