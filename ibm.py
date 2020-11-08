import configparser
import qiskit

config = configparser.ConfigParser()


def get_ibm_token():
    config.read('ibm.conf')
    return config['IBM']['token']


def register_token():
    qiskit.IBMQ.save_account(get_ibm_token())
