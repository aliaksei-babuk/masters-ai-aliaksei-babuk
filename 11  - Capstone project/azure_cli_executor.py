import logging
import subprocess
import streamlit as st


def azure_cli_login(client_id, tenant_id, client_secret):
    logging.info('Logging in to Azure CLI')
    login_command = f'az login --service-principal -u {client_id} -p {client_secret} --tenant {tenant_id}'
    result = subprocess.run(login_command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        st.error(f'Error logging in to Azure CLI: {result.stderr}')
        return False
    return True

def execute_azure_cli_command(command):
    logging.info(f'Executing Azure CLI command: {command}')
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        st.error(f'Error executing command: {result.stderr}')
    return result.stdout

def get_azure_data(client_id, tenant_id, client_secret, command):
    if azure_cli_login(client_id, tenant_id, client_secret):
        return execute_azure_cli_command(command)
    return None
