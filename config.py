import os

from appium.options.android import UiAutomator2Options

from selene_in_action import utils

# context = os.getenv('context', 'bstack')
# run_on_bstack = os.getenv('run_on_bstack', 'false').lower() == 'true'
remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')
deviceName = os.getenv('deviceName')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
app = os.getenv('app', 'resources/app-alpha-universal-release.apk')
runs_on_bstack = app.startswith('bs://')
remote_url = 'http://hub.browserstack.com/wd/hub' if runs_on_bstack else remote_url
bstack_userName = os.getenv('bstack_userName', 'viktoriia_2MWTof')
bstack_accessKey = os.getenv('bstack_accessKey', 'ujoX88qbp3JnkYtck19m')


def driver_options():
    options = UiAutomator2Options()

    if deviceName:
        options.set_capability('deviceName', deviceName)

    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)

    options.set_capability('app',
                           app if (app.startswith('/') or runs_on_bstack or
                                          app.startswith('C:\\'))
                           else utils.path.abs_path_from_root(app))

    if runs_on_bstack:
        options.set_capability(
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',

                'userName': bstack_userName,
                'accessKey': bstack_accessKey,
            })

    return options