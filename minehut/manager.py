#
#       Credits to @jp-krow on github for some awesome code :)
#

import asyncio

import pyppeteer as tr
import requests

from .plugin import Plugin

BASE_API_URL = "https://api.minehut.com"


class Credentials:
    def __init__(self, minehut_session_id: str, minehut_auth_token: str):
        self.minehut_session_id = minehut_session_id
        self.minehut_auth_token = minehut_auth_token


class ServerManager:
    def __init__(self, id: str, credentials: Credentials):
        self.id = id
        self.headers = {
            "x-session-id": credentials.minehut_session_id,
            "authorization": credentials.minehut_auth_token
        }

    def allData(self):
        data = requests.get('{}/server/{}/all_data'.format(BASE_API_URL, self.id), headers=self.headers).json()
        return data

    def startFromHibernation(self):
        return requests.post('{}/server/{}/start_service'.format(BASE_API_URL, self.id), headers=self.headers).json()

    def stopFromHibernation(self):
        return requests.post('{}/server/{}/destroy_service'.format(BASE_API_URL, self.id), headers=self.headers).json()

    def start(self):
        return requests.post('{}/server/{}/start'.format(BASE_API_URL, self.id), headers=self.headers).json()

    def stop(self):
        return requests.post('{}/server/{}/shutdown'.format(BASE_API_URL, self.id), headers=self.headers).json()

    def restart(self):
        return requests.post('{}/server/{}/shutdown'.format(BASE_API_URL, self.id), headers=self.headers).json()

    def visibility(self, visibility: bool):
        data = {"visibility", visibility}
        return requests.post('{}/server/{}/shutdown'.format(BASE_API_URL, self.id), data=data,
                             headers=self.headers).json()

    def sendCommand(self, command: str):
        data = {"command": command}
        return requests.post('{}/server/{}/send_command'.format(BASE_API_URL, self.id), data=data,
                             headers=self.headers).json()

    def changeServerIcon(self, icon: str):
        data = {"icon_id": icon}
        return requests.post('{}/server/{}/icon/equip'.format(BASE_API_URL, self.id), data=data,
                             headers=self.headers).json()

    def rename(self, name: str):
        data = {"name": name}
        return requests.post('{}/server/{}/change_name'.format(BASE_API_URL, self.id), data=data,
                             headers=self.headers).json()

    def editServerProperties(self, field: str, value: str):
        data = {"field": field, "value": value}
        return requests.post('{}/server/{}/edit_server_properties'.format(BASE_API_URL, self.id), data=data,
                             headers=self.headers).json()

    def installPlugin(self, plugin: Plugin):
        data = {"plugin": plugin.getId()}
        return requests.post('{}/server/{}/install_plugin'.format(BASE_API_URL, self.id), data=data,
                             headers=self.headers).json()

    def uninstallPlugin(self, plugin: Plugin):
        data = {"plugin": plugin.getId()}
        return requests.post('{}/server/{}/remove_plugin'.format(BASE_API_URL, self.id), data=data,
                             headers=self.headers).json()

    def resetPluginConfig(self, plugin: Plugin):
        data = {"plugin": plugin.getId()}
        return requests.post('{}/server/{}/remove_plugin_data'.format(BASE_API_URL, self.id), data=data,
                             headers=self.headers).json()

    def saveWorld(self):
        return requests.post('{}/server/{}/save'.format(BASE_API_URL, self.id), headers=self.headers).json()

    def resetWorld(self):
        return requests.post('{}/server/{}/reset_world'.format(BASE_API_URL, self.id), headers=self.headers).json()

    def getBackups(self):
        return requests.get('{}/v1/server/{}/backups'.format(BASE_API_URL, self.id), headers=self.headers).json().json()

    def restoreBackup(self, backup):
        data = {"backup_id": backup}
        return requests.post('{}/v1/server/{}/backup/apply'.format(BASE_API_URL, self.id), data=data,
                             headers=self.headers).json()

    def createBackup(self, backup):
        data = {"backup_id": backup}
        return requests.post('{}/v1/server/{}/backup/create'.format(BASE_API_URL, self.id), data=data,
                             headers=self.headers).json()

    def deleteBackup(self, backup):
        data = {"backup_id": backup}
        return requests.delete('{}/v1/server/{}/backup'.format(BASE_API_URL, self.id), data=data,
                               headers=self.headers).json()

    def reset(self):
        return requests.post('{}/server/{}/reset_all'.format(BASE_API_URL, self.id), headers=self.headers).json()

    def repair(self):
        return requests.post('{}/server/{}/repair_files'.format(BASE_API_URL, self.id), headers=self.headers).json()


# Scape minehut dashboard for auth token and session id
async def scrapeCredentials(email: str, password: str):
    browser = await tr.launch(headless=True, args=['--no-sandbox'])

    page = await browser.newPage()

    await page.goto("https://minehut.com/login")

    await page.waitForSelector("input[name='email']", visible=True)

    await page.type("[name=email]", email)
    await page.type("[name=password]", password)

    await page.click("[name=submit]")

    await page.waitForSelector("h3[class='d-flex align-center justify-center justify-sm-start']", visible=True)

    localStorage = await page.evaluate('''() =>
        Object.assign({}, localStorage)''')

    await browser.close()

    return Credentials(localStorage.get("minehut_session_id"), localStorage.get("minehut_auth_token"))


def getCredentials(email: str, password: str):
    return asyncio.get_event_loop().run_until_complete(scrapeCredentials(email, password))
