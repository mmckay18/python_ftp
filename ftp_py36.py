from ftplib import FTP
import glob
import argparse
import os


def grabFile(file):
    filename = file
    print(filename)
    localfile = open(filename, 'wb')
    #print(localfile.write)
    ftp.retrbinary('RETR ' + filename, localfile.write, 217252800)
    #print(ftp.retrbinary('RETR ' + filename, localfile.write, 1024))
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
    ftp = FTP(args.host)
    # ftp = FTP('archive.stsci.edu')
    ftp.login(user=args.username, passwd=args.password)
    # ftp.login(user='anonymous', passwd='mckaymyles18@gmail.com')

    # ftp.cwd('/stage/anonymous/anonymous12084')
    ftp.cwd(args.data_dir)
    ftp.retrlines('LIST')
    list_of_files = ftp.nlst()
    #print(list_of_files)
    for file in list_of_files:
        print('Copying {} to {}'.format(file, args.path))
        grabFile(file)

    ftp.quit()
    # placeFile()



#run ftp_py36.py --path='/Users/mmckay/Desktop/' --host='archive.stsci.edu' --username='anonymous' --userpw='mckaymyles18@gmail.com' --data_dir='/stage/anonymous/anonymous12084'
