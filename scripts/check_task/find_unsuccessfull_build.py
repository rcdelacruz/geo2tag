import time
import jenkins
import argparse
from jira import JIRA
from check_test_scenario_field import check_test_scenario_field
import time

JOB = 'geo2tag-test'
JENKINS_URL = 'http://jenkins.osll.ru'
JENKINS_USERNAME = 'test.user'
JIRA_USERNAME = 'jira.test.user.geomongo'
PASSWORD = 'iJwF4aLg5FLQXP3a'
JIRA_PROJECT = 'https://geo2tag.atlassian.net'
options = {
    'server': JIRA_PROJECT
}

# for search branch number
ACTIONS = u'actions'
LAST_BUILD_REVISION = u'lastBuiltRevision'
NAME = u'name'
BRANCH = u'branch'
RESULT = u'result'
SUCCESS = u'SUCCESS'
FIXED = u'FIXED'
ARG_BRANCH = '--branch'
NUMBER = 'number'
LAST_COMPLETED_BUILD = 'lastCompletedBuild'


def check_issue(branch):
    jira = JIRA(options, basic_auth=(JIRA_USERNAME, PASSWORD))
    sess_get = jira._session.get
    DEV_STATUS = 'https://geo2tag.atlassian.net/rest/dev-status/1.0'
    _issue = 'issue/detail?issueID=23309'
    _args = 'applicationType=bitbucket&dataType=pullrequest&_=%s' % int(time.time())

    req_url = '%s/%s&%s' % (DEV_STATUS, _issue, _args)
    response = sess_get(req_url)
    raw_data = json.loads(response.content)
 
    for req in raw_data['detail'][0]['pullRequests']:
        print('%s\n%s\n\n' % (req['name'], req['url']))

    issue = get_jira_issue(jira, branch)
    test_scenario_field = check_test_scenario_field(issue)
    if test_scenario_field:
        find_unsuccessfull_build_for_branch(jira, issue, branch)


def find_unsuccessfull_build_for_branch(jira, issue, branch):
    server = get_jenkins_server()
    last_build_number = server.get_job_info(
        JOB)[LAST_COMPLETED_BUILD][NUMBER]
    print "Last Build Number: ", last_build_number
    for i in range(last_build_number, 0, -1):
        inf = server.get_build_info(JOB, i)
        if LAST_BUILD_REVISION in inf[ACTIONS][2]:
            number = 2
        elif LAST_BUILD_REVISION in inf[ACTIONS][3]:
            number = 3
        else:
            print 'branch number for', i, 'build not found'
            continue
        index_branch = inf[ACTIONS][number][LAST_BUILD_REVISION][
            BRANCH][0][NAME].find('/') + 1
        found_branch = inf[ACTIONS][number][LAST_BUILD_REVISION][
            BRANCH][0][NAME][index_branch:index_branch + 7]
        if found_branch == branch:
            if inf[RESULT] == SUCCESS or inf[RESULT] == FIXED:
                print 'This task', branch, 'is successfully completed'
            else:
                print 'This task', branch, 'is unsuccessfully completed'
                reopened_task(jira, issue, branch)
            break


def get_jira_issue(jira, branch):
    branch = branch[0:7]
    issue = jira.issue(branch)
    return issue


def reopened_task(jira, issue, branch):
    jira.transition_issue(issue, u'Reopened')
    jira.add_comment(branch, 'Autotest fail')


def get_branch_number():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        ARG_BRANCH,
        required=True)
    args = parser.parse_args()
    return args.branch


def get_jenkins_server():
    server = jenkins.Jenkins(
        JENKINS_URL,
        username=JENKINS_USERNAME,
        password=PASSWORD)
    return server


if __name__ == '__main__':
    check_issue(get_branch_number())
