import configparser
import os
import qiskit

config = configparser.ConfigParser()


def get_ibm_token():
    this_folder = os.path.dirname(os.path.abspath(__file__))
    conf_file = os.path.join(this_folder, 'ibm.conf')
    config.read(conf_file)
    return config.get('ibm', 'token')


def register_token():
    qiskit.IBMQ.save_account(get_ibm_token())
