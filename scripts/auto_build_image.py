import os
import argparse
import subprocess
from datetime import datetime


def getDateImage(name_img):
    str_dockerimg = 'docker images --format "{{.CreatedAt}}" ' + name_img
    date = subprocess.Popen(str_dockerimg,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    res = date.communicate()
    resdate = datetime.strptime(res[0][0:19], "%Y-%m-%d %H:%M:%S")
    return resdate


def getDateEditFile(path_file):
    sec = os.path.getatime(path_file)
    return datetime.fromtimestamp(sec)


def compDate(date1, date2):
    if date1 > date2:
        return True
    else:
        return False


def buildImage(date_img):
    date1 = getDateEditFile('dockerfile')
    date2 = getDateEditFile('scripts/setup_pip_dependencies.sh')
    date3 = getDateEditFile('scripts/requirements.txt')
    if compDate(date1, date_img) or compDate(date2, date_img) or \
       compDate(date3, date_img):
        print 'Start build'
        os.system('./scripts/build_docker.sh')
        print 'Date image: ' + str(date_img)
        print 'Date dockefile: ' + str(date1)
        print 'Date setup_pip_dependencies.sh: ' + str(date2)
        print 'Date requirements.txt ' + str(date3)
    else:
        print 'It does not require rebuilding'
        print 'Date image: ' + str(date_img)
        print 'Date dockefile: ' + str(date1)
        print 'Date setup_pip_dependencies.sh: ' + str(date2)
        print 'Date requirements.txt: ' + str(date3)


def run():
    parser = argparse.ArgumentParser(description='Auto build image docker')
    parser.add_argument('--name', help='Name image')
    args = parser.parse_args()
    date0 = getDateImage(args.name)
    buildImage(date0)

if __name__ == '__main__':
    run()
