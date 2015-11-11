import jenkins
import argparse

JOB = 'geo2tag-test'

# for search branch number
ACTIONS = u'actions'
LAST_BUILD_REVISION = u'lastBuiltRevision'
NAME = u'name'
BRANCH = u'branch'
NUMBER = 2

RESULT = u'result'
SUCCESS = u'SUCCESS'
FIXED = u'FIXED'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--branch',
        required=True)
    args = parser.parse_args()
    server = jenkins.Jenkins(
        'http://jenkins.osll.ru',
        username='tatyana.berlenko',
        password='qwerty')
    last_build_number = server.get_job_info(
        JOB)['lastCompletedBuild']['number']
    print last_build_number
    for i in range(last_build_number, 0, -1):
        inf = server.get_build_info(JOB, i)
        print inf[ACTIONS]
        print inf[ACTIONS][NUMBER]
        print inf[ACTIONS][NUMBER][LAST_BUILD_REVISION]
        print inf[ACTIONS][NUMBER][LAST_BUILD_REVISION][BRANCH]
        if args.branch == inf[ACTIONS][NUMBER][LAST_BUILD_REVISION][BRANCH][NAME]:
            if inf[RESULT] == SUCCESS or inf[RESULT] == FIXED:
                print 'This task', args.branch, 'is successfully completed'
            else:
                print 'This task', args.branch, 'is unsuccessfully completed'
            break
        else:
            print 'This task', args.branch, 'not found'


if __name__ == '__main__':
    main()
