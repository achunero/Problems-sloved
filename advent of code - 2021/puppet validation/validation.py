import concurrent.futures.process
import getpass
import time
import multiprocessing
from pprint import pprint

import paramiko
import warnings
#from cryptography.utils import DeprecatedIn25
#warnings.simplefilter('ignore', DeprecatedIn25)

def get_username_password():

    username = getpass.getuser()
    password = getpass.getpass()
    return(username,password)

def branch_switch(host):

    # cmd = "hostname;sudo puppet agent -t --environment cloud_better_build --tags log4j_config"
    cmd = "hostname;sudo puppet agent --enable:sudo puppet agent -t --environment production"
    # cmd = "sudo systemctl status storm-supervisor.service"
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.readlines()
    response = "Working on host {}".format(output[0])
    response += "Completed switching branch on host {}".format(output[0])

    return response

def validation(host):

    # cmd = "sudo systemctl status storm-supervisor.service | grep Active"
    # cmd = "cat /etc/puppetlabs/puppet/puppet.conf| grep env;sudo systemctl status storm-supervisor.service | grep Active"
    cmd = "hostname; cat /etc/puppetlabs/puppet/puppet.conf| grep env; sudo /opt/ds_agent/dsa_control -m"

    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.readlines()
    response = ''.join(output)
    # print(response)
    return response

def puppet_validation(host):

    # cmd = "sudo systemctl status storm-supervisor.service | grep Active"
    # cmd = "grep '{nolookups}' /wayfair/pkg/storm/storm-1.1.2/log4j2/worker.xml;grep '{nolookups}' /wayfair/pkg/storm/storm-1.1.2/log4j2/cluster.xml"
    cmd = "sudo /opt/ds_agent/dsa_control -m"
    # cmd = "hostname;grep '{nolookups}' /wayfair/pkg/storm/storm-1.1.2/log4j2/worker.xml"

    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.readlines()
    response = ''.join(output)
    if "HTTP Status: 200 - OK" not in response :
        no_response = {response : host}
        return no_response
    else:
        good_response = ""
        return good_response
        pass

def service_restart(host,username,password):

    # cmd = "sudo systemctl restart storm-supervisor.service;sudo systemctl restart storm-logviewer.service;sudo systemctl restart storm-ui.service"
    cmd = "hostname"
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.readlines()
    response = ''.join(output)
    print(response)
    # return response


if __name__ == '__main__':
    with concurrent.futures.process.ProcessPoolExecutor() as executor:
        host_list = [
            "stormsc1-iad1-1.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-10.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-11.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-12.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-13.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-14.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-15.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-16.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-17.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-18.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-19.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-2.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-20.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-21.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-22.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-23.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-24.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-3.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-4.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-5.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-6.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-7.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-8.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-iad1-9.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-1.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-11.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-12.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-13.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-14.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-16.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-17.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-18.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-19.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-2.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-20.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-21.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-22.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-23.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-24.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-25.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-26.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-27.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-28.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-3.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-30.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-32.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-33.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-34.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-35.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-36.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-37.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-38.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-39.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-4.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-40.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-42.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-43.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-44.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-45.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-46.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-47.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-48.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-49.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-5.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-50.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-53.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-55.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-56.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-58.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-59.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-6.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-60.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-61.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-62.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-63.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-64.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-65.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-66.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-67.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-68.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-7.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-8.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-dsm1-9.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-1.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-10.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-11.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-12.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-13.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-14.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-15.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-16.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-17.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-18.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-19.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-2.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-20.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-21.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-22.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-23.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-24.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-3.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-4.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-5.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-6.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-7.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-8.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-pdx1-9.c.wf-gcp-us-bigdata-prod.internal",
            "stormsc1-fra1-1.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-10.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-11.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-12.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-13.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-14.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-15.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-16.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-17.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-18.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-19.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-2.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-20.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-21.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-22.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-23.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-24.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-3.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-4.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-5.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-6.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-7.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-8.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-fra1-9.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-1.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-10.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-11.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-12.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-13.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-14.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-15.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-16.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-17.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-18.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-19.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-2.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-20.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-21.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-22.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-23.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-24.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-3.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-4.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-5.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-6.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-7.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-8.c.wf-gcp-eu-bigdata-prod.internal",
            "stormsc1-grq1-9.c.wf-gcp-eu-bigdata-prod.internal",
        ]
        # pprint(host_list)
        (username, password) = get_username_password()

        #To Switch branch
        # results = executor.map(branch_switch, host_list)
        # for result in results:
        #     print("--------")
        #     print(result)

        # To do validation
        # results = executor.map(validation, host_list)
        # for result in results:
        #     print("--------")
        #     print(result)

        # To do Puppet Validation
        results_dict = executor.map(puppet_validation, host_list)
        for result in results_dict:
            print(result)

        # To service restart Service
        # for host in host_list:
        #     print("working on host {}".format(host))
        #     service_restart(host, username, password)
        #     time.sleep(1)
        #     print("Sleeping for 6 seconds")