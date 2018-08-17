# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from gtts import gTTS
from bs4 import BeautifulSoup
import time,random,sys,re,goslate,requests,urllib,os,json,subprocess,codecs,threading,glob,wikipedia

cl = LINETCR.LINE()
#cl.login(qr=True)
cl.login(token="ErYNH0HmsXFvxATfHIj8.+hT72C/sNWhx0CFc83gtAa.0/oaNMEcKajrqjbYvn9nwNF27Pp+nIYSz865GQBEWM0=")

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""         ⚠彡 T⃟E⃟A⃟M⃟ L⃟O⃟N⃟G⃟O⃟R⃟ 彡⚠

  ✈✈✈✈✈✈✈✈✈✈✈✈✈✈
🔹 Key
🔹 Me
🔹 Mid
🔹 Mid
🔹 Cek @
🔹 Ping
🔹 Speed
🔹 Gift-Gift3
🔹 Kalender
🔹 Config
🔹 Update
🔹 Mcheck
🔹 Myname
🔹 Mybio
🔹 Respon
🔹 Mybot
🔹 Creator
🔹 Backup
🔹 mybackup
🔹 Restart 
🔹 Remove chat
🔹 Vn /kode Text
🔹 Kode
🔹 Say /text
🔹 Invite: \Mid
🔹 Jam Say: \Nama
🔹 Gn \Nama Grup
🔹 Allbio: \Text
🔹 Album: \Mid
🔹 TL: \Text
🔹 Mybio: \Text
🔹 Cn: \Text
  
♻ C̶O̶M̶M̶A̶N̶D̶ I̶N̶ G̶R̶O̶U̶P̶ ♻
🔹 In
🔹 Out
🔹 Url
🔹 Tag
🔹 Cancel
🔹 Ourl
🔹 Mcheck
🔹 Curl
🔹 Ginfo
🔹 All out
🔹 Ulti @
🔹 Invitgc 1-2
🔹 Gc
🔹 Info @
🔹 Spam on 
🔹 Spamunicode
🔹 Spam1
🔹 Glist
🔹 Ava @
🔹 Ava group
🔹 Cover @
🔹 Spam @
🔹 Gcancel
🔹 Set member:
🔹 Mimic on
🔹 Target
🔹 Del target
🔹 Target list
🔹 Translate-id
🔹 Translate-en
🔹 Translate-ru
🔹 Translate-ko
🔹 Translate-ja
🔹 Translate-ro
🔹 Translate-ar
🔹 Staff add @
🔹 Staff del @
🔹 Stafflist
🔹 .Lyric
🔹 .instagram
🔹 Youtube /Text
🔹 Bc: /Text
🔹 Music /Judul Lagu
🔹 Kedapkedip /Text
🔹 Wikipedia /Text

🔞 C̶O̶M̶M̶A̶N̶D̶ I̶N̶ K̶I̶C̶K̶E̶R̶ 🔞
🔹 Nk @
🔹 Ban
🔹 Unban
🔹 Ban:
🔹 Unban:
🔹 Clear ban
🔹 Gbye
🔹 Mayhem
🔹 Cleanse
🔹 Fuck 1-2
🔹 Vkick

⛔ S̶E̶T̶U̶P̶ G̶R̶O̶U̶P̶ ⛔ 
🔹 Contact
|  -(Contact ON/OFF)
|
🔹 Auto Join
|  -(Auto join ON/OFF)
|  
🔹 Add
|  -(Add ON/OFF)
|
🔹 Share
|  -(Share ON/OFF)
|
🔹 Jam
|  -(Jam ON/OFF)
|
🔹 Leave
|  -(Leave ON/OFF)
|
🔹 Cancel Protect 
|  -(Cancel ON/OFF)
|
🔹 Invite Protect
|  -(Invite ON/OFF)
|
🔹 Protect
|  -Protect ON/OFF
|
🔹 Qr Protect
|  -(Qr ON/OFF)
|
🔹 All Protect                       
|  -(Allprotect ON/OFF) 
|  
  ✈✈✈✈✈✈✈✈✈✈✈✈✈✈ 
  
        ⚠彡 T⃟E⃟A⃟M⃟ L⃟O⃟N⃟G⃟O⃟R⃟ 彡⚠
"""
KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]
admin= ["ufc7b7bd9cf929f01d7d1c7c2f3719368"]
admsa= ["ufc7b7bd9cf929f01d7d1c7c2f3719368"]
staff=[]
whitelist=[]

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":3},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"           THANKS FOR ADD\n\nCreator: line.me/R/ti/p/~addtapigakpc\n\n           ~-™T⃟E⃟A⃟M⃟ L⃟O⃟N⃟G⃟O⃟R⃟ ™-~",
    "lang":"JP",
    "comment":"  ",
    "commentOn":False,
    "commentBlack":{},
    "teman":{},
    "wblack":False,
    "dblack":False,
    "AutoKick":False, 
    "clock":True,
    "tag":True,
    "qr":True,
    "Contact":True,
    "cName":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "members":1,
}
wait3 = {
    "copy":False,
    "copy2":False,
    "target":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for tex in tex:
        for command in commands:
            if string ==command:
                return True


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
                    

#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
		if wait["AutoKick"] == True:
                    if op.param2 in admin:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
			cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
			    cl.kickoutFromGroup(op.param1,[op.param2])
			    cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in admin:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in admin:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------              
      
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ufc7b7bd9cf929f01d7d1c7c2f3719368":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)                    
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return

                
#---------------------------------------------------------------------------                        
            elif msg.text in ["Mimic on","mimic on"]:
                    if wait3["copy"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic On")
                    else:
                    	wait3["copy"] = True
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic On")
                        else:
    	                	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Mimic off","mimic:off"]:
                    if wait3["copy"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic Off")
                    else:
                    	wait3["copy"] = False
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic Off")
                        else:
	                    	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Target list"]:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in wait3["target"]:
                                mc += "✅ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            elif "Target @" in msg.text:
                        target = msg.text.replace("Target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"Target added")
            elif "Del target @" in msg.text:
                        target = msg.text.replace("Del target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"Target deleted")                            

#--------------------------------- TRANSLATE --------------------------------
            if "@"+cl.getProfile().displayName in msg.text:
                if wait["tag"] == True:
                    tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                    jawab = (cl.getProfile().displayName+" sedang sibuk/Off\nJika penting silakan Pesonal chat\n#Automatically Answered by Bots")
                    jawaban = (jawab)
                    cl.sendText(msg.to,jawaban)

            elif "Translate-en " in msg.text:
                txt = msg.text.replace("Translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "Translate-id " in msg.text:
                txt = msg.text.replace("Translate-id ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')                
                    
            elif "Translate-ko " in msg.text:
                txt = msg.text.replace("Translate-ko ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'ko')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate KO'
                except:
                    cl.sendText(msg.to,'Error.')       
                    
            elif "Translate-ru " in msg.text:
                txt = msg.text.replace("Translate-ru ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'ru')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate RU'
                except:
                    cl.sendText(msg.to,'Error.')        
                    
            elif "Translate-ja " in msg.text:
                txt = msg.text.replace("Translate-ja ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'ja')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate JA'
                except:
                    cl.sendText(msg.to,'Error.')       
                    
            elif "Translate-ar " in msg.text:
                txt = msg.text.replace("Translate-ar ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'ar')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate AR'
                except:
                    cl.sendText(msg.to,'Error.')             
                    
            elif "Translate-ro " in msg.text:
                txt = msg.text.replace("Translate-ro ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'ro')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate RO'
                except:
                    cl.sendText(msg.to,'Error.')                                                                                                                                                 
#----------------------------------------------------------------------------
#---------------Cek Sider---------------
            elif "Lurk" in msg.text:
                if msg.toType == 2:
                    cl.sendText(msg.to, "Set reading point:" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif "View" in msg.text:
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
    
                        cl.sendText(msg.to, "╔═══════════════%s\n╠═══════════════\n%s╠═══════════════\n║Reading point creation:\n║ [%s]\n╚═══════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "Auto set reading point in:" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "Reading point has not been set.")
#---------------------------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 1000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")


            elif '.lyric ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('.lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))     
                                                
#---------------------------------------------------------------------------
            elif msg.text in ["Salam1"]:
                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
#---------------------------------------------------------------------------
            elif "Vkick " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass                      
#---------------------------------------------------------------------------
            elif msg.text.lower() == 'key':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
#---------------------------------------------------------------------------
            elif "Mc: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
#---------------------------------------------------------------------------
            elif "Ma: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
#---------------------------------------------------------------------------                    
            elif 'gn ' in msg.text.lower():
                if msg.toType == 2:
                    aditya = cl.getGroup(msg.to)
                    aditya.name = msg.text.replace("Gn ","")
                    cl.updateGroup(aditya)
#-----------------------------------------------------------------------                  
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#---------------------------------------------------------------------------                
            elif msg.text.lower() == 'mybot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
#---------------------------------------------------------------------------                
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)                
            elif msg.text.lower() == 'me1':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif msg.text.lower() == 'me2':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif msg.text.lower() == 'me3':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
#---------------------------------------------------------------------------                
            elif msg.text.lower() == 'hore':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846756",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'ok':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846755",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'siap bos':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846757",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'thx':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846759",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'lol':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846776",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'tidak':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'no':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'suntuk':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875040",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'apa?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == '?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'pose dulu':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875030",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift2':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'f44b6a1a-bdfa-47f7-a839-e7938eb71aac',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift3':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                cl.sendMessage(msg)
#---------------------------------------------------------------------------                
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites")
                        else:
                            cl.sendText(msg.to,"No invites")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"No invites")
                    else:
                        cl.sendText(msg.to,"No invites")
#---------------------------------------------------------------------------
            elif msg.text.lower() == 'ourl':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
#---------------------------------------------------------------------------
            elif msg.text.lower() == 'curl':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
#---------------------------------------------------------------------------
            elif msg.text in ["Glist"]:
                if msg.from_:
                   gid = cl.getGroupIdsJoined()
                   h = ""
                   for i in gid:
                    h += "• %s\n\n" % (cl.getGroup(i).name +"   >> "+str(len(cl.getGroup(i).members))+"")
                   cl.sendText(msg.to,"           🔱List Group🔱\n\n\n"+ h +"> Total Group : " +str(len(gid))+"")
#---------------------------------------------------------------------------
            elif msg.text.lower() == 'mid':
                cl.sendText(msg.to,mid)
            elif msg.text.lower() == 'mid1':
                ki.sendText(msg.to,kimid)
            elif msg.text.lower() == 'mid2':
                ki2.sendText(msg.to,ki2mid)
            elif msg.text.lower() == 'mid3':
                ki3.sendText(msg.to,ki3mid)
#---------------------------------------------------------------------------
            elif "Allmid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
#---------------------------------------------------------------------------                
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#---------------------------------------------------------------------------                
            elif "Allcn:" in msg.text:
                string = msg.text.replace("Allcn:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    cl.sendText(msg.to,"Name Changed To " + string + "")
#---------------------------------------------------------------------------                
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                    cl.sendText(msg.to,"🔄 Bio Turns Into " + string + "")
#---------------------------------------------------------------------------                
            elif "Cn:" in msg.text:
                string = msg.text.replace("Cn:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"🔄 Name Changed To : " + string + "")           
#---------------------------------------------------------------------------     

            if msg.text.lower() in ["tag"]:
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    mention(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    mention(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)

#---------------------------------------------------------------------------
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e)) 

            elif "@Namalu " in msg.text:
                tanya = msg.text.replace("@Namalu ","")
                jawab = ("Jgn Tag Si Namalu!!","Berisik jgn tag si Namalu dia masih tidur")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                cl.sendText(msg.to,"Done")

            elif msg.text == "Spam1":
                    cl.sendText(msg.to,"3")
                    cl.sendText(msg.to,"2")
                    cl.sendText(msg.to,"1")
                    cl.sendText(msg.to,"Fuck Off")
                    cl.sendText(msg.to,"Ku mengejar bus yang mulai berjalan")
                    cl.sendText(msg.to,"Ku ingin ungkapkan kepada dirimu")
                    cl.sendText(msg.to,"Kabut dalam hatiku telah menghilang")
                    cl.sendText(msg.to,"Dan hal yang penting bagiku pun terlihat")
                    cl.sendText(msg.to,"Walaupun jawaban itu sebenarnya begitu mudah")
                    cl.sendText(msg.to,"Tetapi entah mengapa diriku melewatkannya")
                    cl.sendText(msg.to,"Untukku menjadi diri sendiri")
                    cl.sendText(msg.to,"Ku harus jujur, pada perasaanku")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Ku berlari sekuat tenaga")
                    cl.sendText(msg.to,"Ku suka selalu ku suka")
                    cl.sendText(msg.to,"Ku teriak sebisa suaraku")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Walau susah untukku bernapas")
                    cl.sendText(msg.to,"Tak akan ku sembunyikan")
                    cl.sendText(msg.to,"Oogoe daiyamondo~")
                    cl.sendText(msg.to,"Saat ku sadari sesuatu menghilang")
                    cl.sendText(msg.to,"Hati ini pun resah tidak tertahankan")
                    cl.sendText(msg.to,"Sekarang juga yang bisa ku lakukan")
                    cl.sendText(msg.to,"Merubah perasaan ke dalam kata kata")
                    cl.sendText(msg.to,"Mengapa sedari tadi")
                    cl.sendText(msg.to,"Aku hanya menatap langit")
                    cl.sendText(msg.to,"Mataku berkaca kaca")
                    cl.sendText(msg.to,"Berlinang tak bisa berhenti")
                    cl.sendText(msg.to,"Di tempat kita tinggal, didunia ini")
                    cl.sendText(msg.to,"Dipenuhi cinta, kepada seseorang")
                    cl.sendText(msg.to,"Ku yakin ooo ku yakin")
                    cl.sendText(msg.to,"Janji tak lepas dirimu lagi")
                    cl.sendText(msg.to,"Ku yakin ooo ku yakin")
                    cl.sendText(msg.to,"Akhirnya kita bisa bertemu")
                    cl.sendText(msg.to,"Ku yakin ooo ku yakin")
                    cl.sendText(msg.to,"Ku akan bahagiakan dirimu")
                    cl.sendText(msg.to,"Ku ingin kau mendengarkan")
                    cl.sendText(msg.to,"Oogoe daiyamondo~")
                    cl.sendText(msg.to,"Jika jika kamu ragu")
                    cl.sendText(msg.to,"Takkan bisa memulai apapun")
                    cl.sendText(msg.to,"Ungkapkan perasaanmu")
                    cl.sendText(msg.to,"Jujurlah dari sekarang juga")
                    cl.sendText(msg.to,"Jika kau bersuar")
                    cl.sendText(msg.to,"Cahaya kan bersinar")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Ku berlari sekuat tenaga")
                    cl.sendText(msg.to,"Ku suka selalu ku suka")
                    cl.sendText(msg.to,"Ku teriak sebisa suaraku")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Sampaikan rasa sayangku ini")
                    cl.sendText(msg.to,"Ku suka selalu ku suka")
                    cl.sendText(msg.to,"Ku teriakkan ditengah angin")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Walau susah untuk ku bernapas")
                    cl.sendText(msg.to,"Tak akan ku sembunyikan")
                    cl.sendText(msg.to,"Oogoe daiyamondo~")
                    cl.sendText(msg.to,"Katakan dengan berani")
                    cl.sendText(msg.to,"Jika kau diam kan tetap sama")
                    cl.sendText(msg.to,"Janganlah kau merasa malu")
                    cl.sendText(msg.to,"“Suka” itu kata paling hebat!")
                    cl.sendText(msg.to,"“Suka” itu kata paling hebat!")
                    cl.sendText(msg.to,"“Suka” itu kata paling hebat!")
                    cl.sendText(msg.to,"Ungkapkan perasaanmu")
                    cl.sendText(msg.to,"Jujurlah dari sekarang juga..")
                    cl.sendText(msg.to,"Anugerah terindah adalah ketika kita masih diberikan waktu untuk berkumpul bersama orang-orang yang kita sayangi.")
                    cl.sendText(msg.to,"Cuma dirimu seorang yang bisa meluluhkan hati ini. Kamulah yang terindah dalam hidupku.")
                    cl.sendText(msg.to,"Aku ingin meraih kembali cintamu menjadi kenyataan. Saat diriku dalam siksaan cinta, dirimu melenggang pergi tanpa pernah memikirkan aku.")
                    cl.sendText(msg.to,"Tak ada yang salah dengan CINTA. Karena ia hanyalah sebuah kata dan kita sendirilah yang memaknainya.")
                    cl.sendText(msg.to,"Mencintaimu adalah inginku. memilikimu adalah dambaku. meski jarak jadi pemisah, hati tak akan bisa terpisah.")
                    cl.sendText(msg.to,"Dalam cinta ada bahagia, canda, tawa, sedih, kecewa, terluka, semua itu tidak akan terlupakan dalam hal cinta, itu yang artinya cinta.")
                    cl.sendText(msg.to,"Seseorang yang berarti, tak akan dengan mudah kamu miliki. Jika kamu sungguh mencintai, jangan pernah berhenti berusaha untuk hati.")
                    cl.sendText(msg.to,"Jika esok pagi menjelang, akan aku tantang matahari yang terbangun dari tidur lelap nya.")
                    cl.sendText(msg.to,"Ketulusan cinta hanya dapat dirasakan mereka yang benar-benar mempunyai hati tulus dalam cinta.")
                    cl.sendText(msg.to,"Kamu tak perlu menjadikan dirimu cantik/ganteng untuk bisa memilikiku, kamu hanya perlu menunjukkan bahwa aku membutuhkanmu.")
                    cl.sendText(msg.to,"Ada seribu hal yang bisa membuatku berpikir ununtuk meninggalkanmu, namun ada satu kata yang membuatku tetap disini. Aku Cinta Kamu.")
                    cl.sendText(msg.to,"Aku pernah jatuhkan setetes air mata di selat Sunda. Di hari aku bisa menemukannya lagi, itulah waktunya aku berhenti mencintaimu.")
                    cl.sendText(msg.to,"Cinta adalah caraku bercerita tentang dirimu, caraku menatap kepergian mu dan caraku tersenyum, saat menatap indah wajahmu.")
                    cl.sendText(msg.to,"Datang dan pergi seperti angin tidak beraturan dan arah merasakan cinta dalam kehidupan kadang ku bahagia kadang ku bersedih.")
                    cl.sendText(msg.to,"Cinta adalah caraku bercerita tentang dirimu, caraku menatap kepergian mu dan caraku tersenyum, saat menatap indah wajahmu.")
                    cl.sendText(msg.to,"Saat jarak memisahkan, satu yang harus kamu ketahui. Akan aku jaga cinta ini ununtukmu.")
                    cl.sendText(msg.to,"Bersandarlah di pundaku sampai kau merasakan kenyamanan, karena sudah keharusan bagiku ununtuk memberikanmu rasa nyaman.")
                    cl.sendText(msg.to,"Air mata merupakan satu-satunya cara bagimana mata berbicara ketika bibir tidak mampu menjelaskan apa yang membuatmu terluka.")
                    cl.sendText(msg.to,"Hidup tidak bisa lebih baik tanpa ada cinta, tapi cinta dengan cara yang salah akan membuat hidupmu lebih buruk.")
                    cl.sendText(msg.to,"Mencintaimu hanya butuh waktu beberapa detik, namun untuk melupakanmu butuh waktu seumur hidupku.")
                    cl.sendText(msg.to,"Hidup tidak bisa lebih baik tanpa ada cinta, tapi cinta dengan cara yang salah akan membuat hidupmu lebih buruk.")
                    cl.sendText(msg.to,"Mencintaimu hanya butuh waktu beberapa detik, namun ununtuk melupakanmu butuh waktu seumur hidupku.")
                    cl.sendText(msg.to,"Cinta merupakan keteguhan hati yang ditambatkan pada kemanusiaan yang menghubungkan masa lalu, masa kini dan masa depan.")
                    cl.sendText(msg.to,"Ketika mencintai seseorang, cintailah apa adanya. Jangan berharap dia yang sempurna, karena kesempurnaan adalah ketika mencinta tanpa syarat.")
                    cl.sendText(msg.to,"Cinta bukanlah tentang berapa lama kamu mengenal seseorang, tapi tentang seseorang yang membuatmu tersenyum sejak kamu mengenalnya.")
                    cl.sendText(msg.to,"Ketika mereka bertanya tentang kelemahanku, aku ingin mengatidakan bahwa kelemahanku itul adalah kamu. Aku merindukanmu di mana-mana dan aku sanagat mencintaimu.")
                    cl.sendText(msg.to,"Kehadiranmu dalam hidupku, aku tahu bahwa aku bisa menghadapi setiap tantangan yang ada di hadapanku, terima kasih telah menjadi kekuatanku.")
                    cl.sendText(msg.to,"Meneriakkan namamu di deras hujan, memandangmu dari kejauhan, dan berdo’a di hening malam. Cinta dalam diam ini lah yang mampu kupertahankan.")
                    cl.sendText(msg.to,"Perempuan selalu menjaga hati orang yang dia sayangsehingga hati dia sendiri tersiksa. inilah pengorbanan perempuan ununtuk lelaki yang tidak pernah sadar.")
                    cl.sendText(msg.to,"Ketika kau belum bisa mengambil keputusan ununtuk tetap bertahan dengan perasaan itu, sabarlah, cinta yang akan menguatkanmu.")
                    cl.sendText(msg.to,"Aku tidak akan pernah menjajikan ununtuk sebuah perasaan, tapi aku bisa menjanjikan ununtuk sebuah kesetiaan.")
                    cl.sendText(msg.to,"Cinta yang sebenarnya tidak buta, cinta yaitu adalah hal yang murni, luhur serta diharapkan. Yang buta itu jika cinta itu menguasai dirimu tanpa adanya suatu pertimbangan.")
                    cl.sendText(msg.to,"Aku tercipta dalam waktu, ununtuk mengisi waktu, selalu memperbaiki diri di setiap waktu, dan semua waktu ku adalah ununtuk mencintai kamu.")
                    cl.sendText(msg.to,"Cinta akan indah jika berpondasikan dengan kasih sang pencipta. Karena sesungguhnya Cinta berasal dari-Nya Dan cinta yang paling utama adalah cinta kepada Yang Kuasa.")
                    cl.sendText(msg.to,"Bagi aku, dalam hidup ini, hidup hanya sekali, cinta sekali dan matipun juga sekali. Maka tidak ada yang namanya mendua.")
                    cl.sendText(msg.to,"Tuhan..jagalah ia yang jauh disana, lindungi tiap detik hidup yang ia lewati,sayangi dia melebihi engkau menyayangiku.")
                    cl.sendText(msg.to,"Kapan kau akan berhenti menyakitiku, lelah ku hadapi semua ini tapi aku tidak bisa memungkiri aku sangat mencintaimu.")
                    cl.sendText(msg.to,"Ketidakutan terbesar dalam hidupku bukan kehilanganmu, tapi melihat dirimu kehilangan kebahagiaanmu.")
                    cl.sendText(msg.to,"Cinta yang sesungguhnya akan mengatidakan aku butuh kamu karna aku siap ununtuk mencintaimu dan menjalani suka duka bersamamu")
                    cl.sendText(msg.to,"Seseorang pacar yang baik adalah dia yang JUJUR dan tidak pernah membuat kamu selalu bertanya-tanya atau selalu mencurigai dia")
                    cl.sendText(msg.to,"Cinta bukanlah sebuah kata cinta, yang sebenarnya adalah cinta yang menyentuh hati dan perasaan")
                    cl.sendText(msg.to,"Kau datang di saat ke egoisan akan cinta tengah mendera. Membawa cahaya dan kedamaian, membuatku tidak mudah menyerah ununtuk merengkuh kisah cinta bersamamu")
                    cl.sendText(msg.to,"Aku sangat menyukai kebersamaan karena kebersamaan mengajarkan kita tentang suka dan duka di lalui bersama")
                    cl.sendText(msg.to,"Mungkin Tuhan sengaja memberi kita berjumpa dengan orang yang salah sebelum menemui insan yang betul supaya apabila kita akhirnya menemui insan yang betul, kita akan tahu bagaimana ununtuk bersyukur dengan pemberian dan hikmah di balik pemberian tersebut.")
                    cl.sendText(msg.to,"Getaran di hatiku yang lama haus akan belaianmu seperti saat dulu dan kau bisikan kata ‘aku cinta padamu’ aku merindukannya")
                    cl.sendText(msg.to,"Terkadang air mata adalah tanda kebahagiaan yang tidak terucapkan. Dan senyuman adalah tanda sakit yang mencoba ununtuk kuat")
                    cl.sendText(msg.to,"Dicintai dan disayangi kamu adalah anugerah terindah yang tuhan berikan padaku.")
                    cl.sendText(msg.to,"Mencintai kamu butuh waktu beberapa detik, Namun melupakanmu butuh waktu ku seumur hidup.")
                    cl.sendText(msg.to,"Datang dan pergi seperti angin tidak beraturan dan arah merasakan cinta dalam kehidupan kadang aku bahagia dan juga kadang aku bersedih.")
                    cl.sendText(msg.to,"Air mata merupakan satu-satunya cara bagimana mata berbicara ketika bibir tidak mampu lagi menjelaskan apa yang membuatmu terluka.")
                    cl.sendText(msg.to,"Jauh sebelum bertemu denganmu, aku telah mengenalmu dalam doaku.")
                    cl.sendText(msg.to,"Mungkin dia tidak sadar bahwa aku itu cemburu dan mungkin juga dia tidak merasa bahwa aku sangat terluka, tidak mendengar bahwa hatiku sedang menangis.")
                    cl.sendText(msg.to,"Kehadirmu membawa cinta, memberi bahagia, dan juga rasa rindu yang tiada pernah ada akhirnya.")
                    cl.sendText(msg.to,"Aku nngak mau jadi wakil rakyat, aku maunya jadi wali murid yang ngambil raport anak kita besok.")
                    cl.sendText(msg.to,"Seperti hujan yang turun di tanah yang tandus, seperti itulah arti hadirmu dengan cinta dan kasih sayang untukku.")
                    cl.sendText(msg.to,"Tanda-tanda cinta adalah ketika anda merasa bahwa kebahagiaan orang tersebut lebih penting daripada kebahagiaanmu sendiri.")
                    cl.sendText(msg.to,"Cinta tidak hanya apa yang anda rasakan, tetapi apa yang harus anda lakukan.")
                    cl.sendText(msg.to,"Cinta adalah sebuah kekuatan untuk melihat kesamaan dan tidak kesamaan.")
                    cl.sendText(msg.to,"Cinta adalah pengalaman penuh emosi yang dirasakan banyak orang tetapi hanya beberapa orang saja yang bisa menikmatinya.")
                    cl.sendText(msg.to,"Cinta adalah berbagi. Karena walau ada di dua raga yang berbeda, setiap pasangan hanya memiliki satu hati.")
                    cl.sendText(msg.to,"Saat kita berjauhan, sebenarnya hanya raga kitalah yang jauh. Namun hati kita selalu dekat, karena hatiku ada di hatimu.")
                    cl.sendText(msg.to,"Cinta datang dengan pengorbanan yang akan memberikan petunjuk siapa diri kita yang sebenarnya.")
                    cl.sendText(msg.to,"Cinta begitu lembut dan merdu, namun jangan kau gunankan untuk merayu. Karena rayuan hanyalah akan mengosongkan makna kecintaan yang sesungguhnya.")
                    cl.sendText(msg.to,"Cinta bukanlah penuntutan, penguasaan, pemaksaan, dan pengintimidasian. Tak lain itu hanyalah cara manusia mendefinisikannya. Karena cinta adalah perjuangan, pengorbanan, tanggungjawab, kejujuran, dan keikhlasan.")
                    cl.sendText(msg.to,"Derajat cinta hanya bisa diukur dengan seberapa besar “Pemberian” yang kita korbankan.")                    
#---------------------------------------------------------------------------                
            elif msg.text == "Okeb":
                    cl.sendText(msg.to,"nekopoi.host")
                    cl.sendText(msg.to,"sexvideobokep.com")
                    cl.sendText(msg.to,"memek.com")
                    cl.sendText(msg.to,"pornktube.com")
                    cl.sendText(msg.to,"faketaxi.com")
                    cl.sendText(msg.to,"videojorok.com")
                    cl.sendText(msg.to,"watchmygf.mobi")
                    cl.sendText(msg.to,"xnxx.com")
                    cl.sendText(msg.to,"pornhd.com")
                    cl.sendText(msg.to,"xvideos.com")
                    cl.sendText(msg.to,"vidz7.com")
                    cl.sendText(msg.to,"m.xhamster.com")
                    cl.sendText(msg.to,"xxmovies.pro")
                    cl.sendText(msg.to,"youporn.com")
                    cl.sendText(msg.to,"pornhub.com")
                    cl.sendText(msg.to,"anyporn.com")
                    cl.sendText(msg.to,"hdsexdino.com")
                    cl.sendText(msg.to,"rubyourdick.com")
                    cl.sendText(msg.to,"anybunny.mobi")
                    cl.sendText(msg.to,"cliphunter.com")
                    cl.sendText(msg.to,"sexloving.net")
                    cl.sendText(msg.to,"free.goshow.tv")
                    cl.sendText(msg.to,"eporner.com")
                    cl.sendText(msg.to,"Pornhd.josex.net")
                    cl.sendText(msg.to,"m.hqporner.com")
                    cl.sendText(msg.to,"m.spankbang.com")
                    cl.sendText(msg.to,"m.4tube.com")
                    cl.sendText(msg.to,"brazzers.com")
#-----------------------------------------------
            elif "Vnid " in msg.text:
                 psn = msg.text.replace("Vnid ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
                 
            elif "Vnen " in msg.text:
                 psn = msg.text.replace("Vnen ","")
                 tts = gTTS(psn, lang='en', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
                 
            elif "Vnru " in msg.text:
                 psn = msg.text.replace("Vnru ","")
                 tts = gTTS(psn, lang='ru', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
                 
            elif "Vnvi " in msg.text:
                 psn = msg.text.replace("Vnvi ","")
                 tts = gTTS(psn, lang='vi', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
                 
            elif "Vnmy " in msg.text:
                 psn = msg.text.replace("Vnmy ","")
                 tts = gTTS(psn, lang='my', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
                 
            elif "Vnms " in msg.text:
                 psn = msg.text.replace("Vnms ","")
                 tts = gTTS(psn, lang='ms', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
                 
            elif "Vnja " in msg.text:
                 psn = msg.text.replace("Vnja ","")
                 tts = gTTS(psn, lang='ja', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')         
                 
            elif "Vnko " in msg.text:
                 psn = msg.text.replace("Vnko ","")
                 tts = gTTS(psn, lang='ko', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')                                                                                                              
                 
 #---------------------------------------------------------------------------               
            elif "Copy " in msg.text:
                copy0 = msg.text.replace("Copy ","")
                copy1 = copy0.lstrip()
                copy2 = copy1.replace("@","")
                copy3 = copy2.rstrip()
                _name = copy3
		group = cl.getGroup(msg.to)
		for contact in group.members:
		    cname = cl.getContact(contact.mid).displayName
		    if cname == _name:
			cl.CloneContactProfile(contact.mid)
			cl.sendText(msg.to, "Done ✅")
		    else:
			pass
#--------------------------------------------------------
	    elif "Set member: " in msg.text:
		if msg.from_ in admin:
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
		else:
		    cl.sendText(msg.to, "Khusus Admin")			
#--------------------------------------------------------
	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")		    		    		
#---------------------------------------------------------------------------
            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"                
#---------------------------------------------------------------------------                
            elif "Staff add @" in msg.text:
                if msg.from_ in admsa or admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found.")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Staff added.")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Staff remove @" in msg.text:
                if msg.from_ in admsa or admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found.")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Staff deleted.")
                            except:
                                passp
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if msg.from_ in admin == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    mc = ""
                    for mi_d in admin:
                      if mi_d not in admsa:
                        mc += "\n⏰ " + cl.getContact(mi_d).displayName
                    cl.sendText(msg.to, "Staff :\n" + mc)
                    print "[Command]Stafflist executed"               
#---------------------------------------------------------------------------                
            elif '.instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))                 
#---------------------------------------------------------------------------                
            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")     
                                                           
            elif msg.text in ["Restart"]:
                cl.sendText(msg.to, "Bot has been restarted")
                restart_program()
                print "@Restart"                                
#-----------------------------------------------------------------                        
            elif "Youtube " in msg.text:
                query = msg.text.replace("Youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'                 
                                    
#-------------------------------------------------                                        
            elif "Ava @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Ava @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#-----------------------------------------------                                
	    elif "Ava group" in msg.text:
                   group = cl.getGroup(msg.to)
                   path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                   cl.sendImageWithURL(msg.to, path)                            
#-----------------------------------------------
            elif msg.text in ["Sp1","Speed","speedbot"]:
                start = time.time()
                ki.sendText(msg.to, "「 Debug 」\nType: speed\nTesting..")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "「 Debug 」\nType: speed\nTime taken: %s  " % (elapsed_time))

            elif msg.text in ["Sp2","Speed","speedbot"]:
                start = time.time()
                ki2.sendText(msg.to, "「 Debug 」\nType: speed\nTesting..")
                elapsed_time = time.time() - start
                ki2.sendText(msg.to, "「 Debug 」\nType: speed\nTime taken: %s  " % (elapsed_time))

            elif msg.text in ["Sp3","Speed","speedbot"]:
                start = time.time()
                ki3.sendText(msg.to, "「 Debug 」\nType: speed\nTesting..")
                elapsed_time = time.time() - start
                ki3.sendText(msg.to, "「 Debug 」\nType: speed\nTime taken: %s  " % (elapsed_time))                
            
            elif msg.text in ["Sp","Speed","speedbot"]:
                start = time.time()
                cl.sendText(msg.to, "「 Debug 」\nType: speed\nTesting..")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "「 Debug 」\nType: speed\nTime taken: %s  " % (elapsed_time))
                elapsed_time = time.time() - start
                #ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                #kk.sendText(msg.to, "%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                #kc.sendText(msg.to, "%sseconds" % (elapsed_time))
#---------------------------------------------------------------------------
            elif msg.text in ["Lirik akad"]:
                cl.sendText(msg.to,"[Verse 1]\n\nBetapa bahagianya hatiku saat\nKu duduk berdua denganmu\nBerjalan bersamamu\nMenarilah denganku\n\n[Verse 2]\n\nNamun bila hari ini adalah yang terakhir\nNamun ku tetap bahagia\nSelalu kusyukuri\nBegitulah adanya\n\n[Pre-Chorus]\n\nNamun bila kau ingin sendiri\nCepat cepatlah sampaikan kepadaku\nAgar ku tak berharap\nDan buat kau bersedih\n\n[Chorus]\n\nBila nanti saatnya telah tiba\nKuingin kau menjadi istriku\nBerjalan bersamamu dalam terik dan hujan\nBerlarian kesana-kemari dan tertawa\nNamun bila saat berpisah telah tiba\nIzinkanku menjaga dirimu\nBerdua menikmati pelukan di ujung waktu\nSudilah kau temani diriku\n\n[Solo]\n\n[Pre-Chorus]\n\nNamun bila kau ingin sendiri\nCepat cepatlah sampaikan kepadaku\nAgar ku tak berharap\nDan buat kau bersedih\n\n[Chorus]\n\nBila nanti saatnya telah tiba\nKuingin kau menjadi istriku\nBerjalan bersamamu dalam terik dan hujan\nBerlarian kesana-kemari dan tertawa\nNamun bila saat berpisah telah tiba\nIzinkanku menjaga dirimu\nBerdua menikmati pelukan di ujung waktu\nSudilah kau temani diriku\n\n[Outro]\n\nSudilah kau menjadi temanku\nSudilah kau menjadi istriku\n")

            elif msg.text in ["Lirik dia"]:
                cl.sendText(msg.to,"Di suatu hari tanpa sengaja kita bertemu\nAku yang pernah terluka, kembali mengenal cinta\nHati ini kembali temukan senyum yang hilang\nSemua itu karena dia\n\nOh tuhan kucinta dia\nKu sayang dia, rindu dia\nInginkan dia\nUtuhkanlah rasa cinta di hatiku\nHanya padanya, untuk dia\n\nJauh waktu berjalan kita lalui bersama\nBetapa di setiap hari\nKu jatuh cinta padanya\nDicintai oleh dia kumerasa sempurna\nSemua itu karena dia\n\nOh tuhan kucinta dia\nKu sayang dia, rindu dia\nInginkan dia\nUtuhkanlah rasa cinta di hatiku\nHanya padanya, untuk dia\n\nOh tuhan ku cinta dia\nKu sayang dia, rindu dia\nInginkan dia\nUtuhkanlah rasa cinta di hatiku\nHanya padanya, untuk dia\nHanya padanya, untuk dia\n")
#---------------------------------------------------------------------------                
            elif msg.text in ["PING","Ping","ping"]:
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")                
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")                
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")                
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#---------------------------------------------------------
            elif "1cn:" in msg.text:
                string = msg.text.replace("1cn:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"🔄 Name Changed To :" + string + "")
#--------------------------------------------------------
            elif "2cn:" in msg.text:
                string = msg.text.replace("2cn:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"🔄 Name Changed To :" + string + "")
#--------------------------------------------------------
            elif "3cn:" in msg.text:
                string = msg.text.replace("3cn:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"🔄 Name Changed To :" + string + "")
#-----------------------------------------
            elif msg.text in ["Myname"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[DisplayName]===\n\n" + h.displayName)
#-----------------------------------------
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n\n" + h.statusMessage)                                       
#--------------------------------------------------------
	    elif msg.text in ["Self Like"]:
		try:
		    print "activity"
		    url = cl.activity(limit=10000)
		    print url
		    cl.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    cl.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Bro Jadi Ngopi Gak Nanti??")
		    ki.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    ki.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Bro Jadi Ngopi Gak Nanti??")
		    ki2.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    ki2.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Bro Jadi Ngopi Gak Nanti??")
		    ki3.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    ki3.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Bro Jadi Ngopi Gak Nanti??")
		    cl.sendText(msg.to, "Done ✅")
		except Exception as E:
		    try:
			cl.sendText(msg.to,str(E))
		    except:
			pass
#--------------------------------------------------------
	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = cl.getGroupIdsJoined()
		for i in gid:
		    cl.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~addtapigakpc")
		cl.sendText(msg.to,"Success BC! ✅")
#--------------------------------------------------------
	    elif msg.text in ["Remove chat"]:
		cl.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Removed all chat")
#--------------------------------------------------------
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"🔄 Bio Changed To" + string + "")
#------------------------------------------------------              
            elif msg.text.lower() == 'Runtime':
                eltime = time.time()
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)      
#---------------------------------------------------------------------------
            elif "Kepo " in msg.text:
                tanggal = msg.text.replace(" ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)               
#---------------------------------------------------------------------------
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                
#---------------------------------------------------------------------------                
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to on")
                    else:
                        cl.sendText(msg.to,"contact already on")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to on")
                    else:
                        cl.sendText(msg.to,"contact already on")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to off")
                    else:
                        cl.sendText(msg.to,"contact already off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to off")
                    else:
                        cl.sendText(msg.to,"contact already off")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to on")
                    else:
                        cl.sendText(msg.to,"Protection already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to on")
                    else:
                        cl.sendText(msg.to,"Protection already on")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'qr on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to on")
                    else:
                        cl.sendText(msg.to,"Protection Qr already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to on")
                    else:
                        cl.sendText(msg.to,"Protection Qr already on")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'invit on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to on")
                    else:
                        cl.sendText(msg.to,"Protection Invite already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to on")
                    else:
                        cl.sendText(msg.to,"Protection Invite already on")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'cancel on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already on")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to on")
                    else:
                        cl.sendText(msg.to,"Autojoin already on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to on")
                    else:
                        cl.sendText(msg.to,"Autojoin already on")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
#-----------------------------------------------------------------                
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to off")
                    else:
                        cl.sendText(msg.to,"Autojoin already off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to off")
                    else:
                        cl.sendText(msg.to,"Autojoin already off")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'protect off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to off")
                    else:
                        cl.sendText(msg.to,"Protection already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to off")
                    else:
                        cl.sendText(msg.to,"Protection already off")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'qr off':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to off")
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to off")
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'invit off':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Protection Invite already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Protection Invite already off")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'cancel off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already off")
#-----------------------------------------------------------------                        
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
#-----------------------------------------------------------------              
            elif msg.text in ["Tag on"]:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Tag On")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag On")
                    else:
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Tag off"]:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Tag Off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag Off")
                    else:
                        cl.sendText(msg.to,"Already off")                            
          
            elif msg.text.lower() == 'leave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'leave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
 #-----------------------------------------------------------------                       
            elif msg.text.lower() == 'share on':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to on")
                    else:
                        cl.sendText(msg.to,"Share already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to on")
                    else:
                        cl.sendText(msg.to,"Share already on")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'share off':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to off")
                    else:
                        cl.sendText(msg.to,"Share already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to off")
                    else:
                        cl.sendText(msg.to,"Share already off")
#--------------------------------------------------------
	    elif "Autokick:on" in msg.text:
		wait["AutoKick"] = True
		cl.sendText(msg.to,"AutoKick Active")

	    elif "Autokick:off" in msg.text:
		wait["AutoKick"] = False
		cl.sendText(msg.to,"AutoKick off")                                       
#-----------------------------------------------------------------
            elif msg.text in ["Allprotect on","Mode on"]:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invit n")
                    else:
                        cl.sendText(msg.to,"Invit on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invit On")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"Cancel on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect On")
                    else:
                        cl.sendText(msg.to,"Done")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Link On")
                    else:
                        cl.sendText(msg.to,"Link On")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Link On")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Allprotect off","Mode Off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                    else:
                        cl.sendText(msg.to,"Invite OFF")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
 #-----------------------------------------------------------------                       
            elif msg.text.lower() == 'setup':
                md = ""
                if wait["contact"] == True: md+="         ⚠ SET ⚠\n\n✏ Contact : ❌\n\n"
                else: md+="         ⚠ SET ⚠\n\n✏ Contact : ✔\n\n"
                #--------------------------------------------------------
                if wait["autoJoin"] == True: md+="✏ Auto Join : ✔\n\n"
                else: md +="✏ Auto Join : ❌\n\n"
                #--------------------------------------------------------
                if wait["autoCancel"] == True:md+="✏ Auto cancel : ✔\n\n"
                else: md+= "✏ Group cancel : ❌\n\n"
                #--------------------------------------------------------
                if wait["leaveRoom"] == True: md+="✏ Auto leave : ✔\n\n"
                else: md+="✏ Auto leave : ❌\n\n"
                #--------------------------------------------------------
                if wait["timeline"] == True: md+="✏ Share : ✔\n\n"
                else:md+="✏ Share : ❌\n\n"
                #--------------------------------------------------------
                if wait["autoAdd"] == True: md+="✏ Auto add : ✔\n\n"
                else:md+="✏ Auto add : ❌\n\n"
                #--------------------------------------------------------
                if wait["protect"] == True: md+="✏ Protect : ✔\n\n"
                else:md+="✏ Protect : ❌\n\n"
                #--------------------------------------------------------
                if wait["linkprotect"] == True: md+="✏ Link Protect : ✔\n\n"
                else:md+="✏ Link Protect : ❌\n\n"
                #--------------------------------------------------------
                if wait["inviteprotect"] == True: md+="✏ Invitation Protect : ✔\n\n"
                else:md+="✏ Invitation Protect : ❌\n\n"
                #--------------------------------------------------------
                if wait["AutoKick"] == True: md+="✏ Autokick : ✔\n\n"
                else:md+="✏ Autokick : ❌\n\n"                
                #--------------------------------------------------------
                if wait["cancelprotect"] == True: md+="✏ Cancel Protect : ✔\n\n\n  ⚓ T⃟E⃟A⃟M⃟ L⃟O⃟N⃟G⃟O⃟R⃟  ⚓"
                else:md+="✏ Cancel Protect : ❌   \n\n\n  ⚓ T⃟E⃟A⃟M⃟ L⃟O⃟N⃟G⃟O⃟R⃟  ⚓"
                #--------------------------------------------------------
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
#-----------------------------------------------------------------                
            elif "Album:" in msg.text:
                gid = msg.text.replace("Album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
#-----------------------------------------------------------------
            elif msg.text.lower() == 'all out':
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Is Out In all groups ✅")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
#-----------------------------------------------------------------                    
            elif msg.text.lower() == 'gcancel':
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"I declined all invitations")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
 #-----------------------------------------------------------------                   
            elif "Hapus:" in msg.text:
                gid = msg.text.replace("Hapus:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album")
            elif msg.text.lower() == 'add on':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Auto add already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'add off':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to off")
                    else:
                        cl.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to off")
                    else:
                        cl.sendText(msg.to,"Auto add already off")
            #elif "Pesan set:" in msg.text:
                wait["message"] = msg.text.replace("Pesan set:","")
                cl.sendText(msg.to,"We changed the message")
            #elif msg.text.lower() == 'pesan cek':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di")
                    else:
                        cl.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["come on"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Come","Comment"]:
                cl.sendText(msg.to,"         THANKS FOR ADD\n Creator: line.me/R/ti/p/~addtapigakpc\n           ~-™TEAM LONGOR™-~" + str(wait["comment"]))
            elif msg.text.lower() == 'url':
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
#-----------------------------------------------------------------                        
            elif msg.text.lower() == 'url1':
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        ki.updateGroup(g)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"It can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Can not be used for groups other than")
#-----------------------------------------------------------------                        
            elif 'Gurl ' in msg.text.lower():
                if msg.toType == 2:
                    gid = msg.text.replace("Gurl ","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text in ["Come bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”")
            elif msg.text in ["Come hapus"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”")
            elif msg.text in ["Come cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
#-----------------------------------------------------------------
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ki.getGroup(msg.to)
                       ginfo = ki.getGroup(msg.to)
                       #gs.preventJoinByTicket = False
                       #cl.updateGroup(gs)
                       invsend = 0
                       #Ticket = cl.reissueGroupTicket(msg.to)
                       #cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    #cl.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)                       	    
#-----------------------------------------------------------
            elif ("Fuck " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Limited ❌")
            elif ("Fuck1 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Limited ❌")

            elif ("Fuck2 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Limited ❌")
            elif ("Fuck3 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki3.kickoutFromGroup(msg.to,[target])
                       except:
                           ki3.sendText(msg.to,"Limited ❌")
#-----------------------------------------------------------------
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)
#-----------------------------------------------------------------
            elif "Gc" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"old user")
#-----------------------------------------------------------------
            elif msg.text in ["Invitgc"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif msg.text in ["1Invitgc"]:
              if msg.toType == 2:
                 ginfo = ki.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    ki.findAndAddContactsByMid(gCreator)
                    ki.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif msg.text in ["2Invitgc"]:
              if msg.toType == 2:
                 ginfo = ki2.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    ki2.findAndAddContactsByMid(gCreator)
                    ki2.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif msg.text in ["3Invitgc"]:
              if msg.toType == 2:
                 ginfo = ki3.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    ki3.findAndAddContactsByMid(gCreator)
                    ki3.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
#-----------------------------------------------------------------
            elif "Mayhem" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n' abort' to abort♪")
                    ki.sendText(msg.to,"「 Mayhem 」\n46 victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[cl,ki,ki2]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki.sendText(msg.to,"Mayhem done")
#-----------------------------------------------------------------
            elif "Invitme:" in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitme:","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                            ki.findAndAddContactsByMid(msg.from_)
                            ki.inviteIntoGroup(gid,[msg.from_])
                            ki2.findAndAddContactsByMid(msg.from_)
                            ki2.inviteIntoGroup(gid,[msg.from_])
                            ki3.findAndAddContactsByMid(msg.from_)
                            ki3.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Not In The Group")
                            ki.sendText(msg.to,"Not In The Group")
                            ki2.sendText(msg.to,"Not In The Group")
                            ki3.sendText(msg.to,"Not In The Group")      
   #-----------------------------------------------------------------
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))    
#-----------------------------------------------------------------		        		  
            elif msg.text in ["Kalender"]:
	    	      wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
	              cl.sendText(msg.to, "•KALENDER\n\n" + (wait2['setTime'][msg.to]))                              #-----------------------------------------------------------------
            elif 'wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))	              		        
#-----------------------------------------------------------------
            elif "Cleanse" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    ki.sendText(msg.to,"             Maaf\nGrub Kamu Saya Bersihkan\nKarna Mengandung Unsur Porno")
                    ki.sendText(msg.to,"Salam Dari TEAM LONGGOR")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[cl,ki,ki2]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki.sendText(msg.to,"Cleanse done") 
#-----------------------------------------------------------------
            elif "Spamunicode @" in msg.text:
                _name = msg.text.replace("Spamunicode @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.")
                       ki.sendText(g.mid,"40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.")
                       ki2.sendText(g.mid,"40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.")
                       ki3.sendText(g.mid,"40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.")
                       cl.sendText(msg.to, "Done")
                       print                       "40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.400.00440.04.400.004.40.04.400.00440.04.400.00440.04.400.00440.04.400.00440.04.400.004.40.04.400.00440.04.400.00404.40.04.400.004.40.04.400.00440.04.400.00440.04.400."
#-----------------------------------------------------------------                    
            elif "Spam @" in msg.text:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"Spammed !")
                       ki.sendText(g.mid,"Spammed !")  
                       ki2.sendText(g.mid,"Spammed !")
                       ki3.sendText(g.mid,"Spammed !")
                       cl.sendText(g.mid,"KAPOK TAK SPAM 🐶")
                       ki.sendText(g.mid,"KAPOK TAK SPAM 🐶")  
                       ki2.sendText(g.mid,"KAPOK TAK SPAM 🐶")
                       ki3.sendText(g.mid,"KAPOK TAK SPAM 🐶")   
                       cl.sendText(msg.to, "Done ✅")
                       print " Spammed !"
#-----------------------------------------------------------------
                
            elif msg.text in ["Creator"]:
              if msg.from_:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ufc7b7bd9cf929f01d7d1c7c2f3719368'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ua8174484291b3dcf35003ac4a4b7e58c'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ucff516dccd288fcc2fc3276da914db36'}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"INFO CREATOR\n╔════════════════════════\n╠Instagram: PC aja ya\n╠LINE: addtapigakpc\n╠WhatsApp: PC aja ya \n╠Nama: Hendrah Ary \n╚════════════════════════")                         
#-----------------------------------------------------------------                
            elif "Ulti " in msg.text:
              if msg.from_ in admin:
                ulti0 = msg.text.replace("Ulti ","")
                ulti1 = ulti0.rstrip()
                ulti2 = ulti1.replace("@","")
                ulti3 = ulti2.rstrip()
                _name = ulti3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                                try:
                                        ki.kickoutFromGroup(msg.to,[target])
                                        ki.leaveGroup(msg.to)
                                        ki2.kickoutFromGroup(msg.to,[target])
                                        ki2.leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        ki.sendText(msg.t,"Ter ELIMINASI....")
                                        ki.sendText(msg.to,"WOLES brooo....!!!")
                                        ki.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        cl.uldateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        cl.updateGroup(gs)
#-----------------------------------------------------------------
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': ginfo.creator.mid}
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,">> GROUP NAME <<\n" + str(ginfo.name) + "\n\n>> GIT <<\n" + msg.to + "\n\n>> GROUP CREATOR <<\n" + gCreator + "\n\nPROFIL STATUS\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\n•MEMBERS : " + str(len(ginfo.members)) + "•MEMBERS\n•PENDINGAN : " + sinvitee + " PEOPLE\n•URL : " + u + " IT IS INSIDE")
                        cl.sendMessage(msg)
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)               
#-----------------------------------------------------------
	    elif "Ban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                cl.sendText(msg.to,_nametarget + " Hy")
                            except:
                                cl.sendText(msg.to,"Error")
#----------------------------------------------------------                                
	    elif "Unban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                cl.sendText(msg.to,_nametarget + " Hapus")
                            except:
                                cl.sendText(msg.to,_nametarget + " No Bl")
#-----------------------------------------------------------------
            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,_name + "Cek Sider")
                                except:
                                    cl.sendText(msg.to,"Error")
#-----------------------------------------------------------------
            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,_name + " Hapus")
                                except:
                                    cl.sendText(msg.to,_name + " No Bl")                                    
#-----------------------------------------------------------
            elif msg.text in ["Respon","absen"]:
                ki.sendText(msg.to,"Hadir")
                ki2.sendText(msg.to,"Hadir")
                ki3.sendText(msg.to,"Hadir")
                ki4.sendText(msg.to,"Hadir")
                ki5.sendText(msg.to,"Hadir")
                ki6.sendText(msg.to,"Hadir")
                ki7.sendText(msg.to,"Hadir")
                ki8.sendText(msg.to,"Hadir")
                ki9.sendText(msg.to,"Hadir")
                ki10.sendText(msg.to,"Hadir")
#-----------------------------------------------------------speed
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
#-----------------------------------------------------------------                
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
#-----------------------------------------------------------------                
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No blacklist")
                else:
                    cl.sendText(msg.to,"Wait...")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "💨" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
#-----------------------------------------------------------------                    
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "►" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "Black list")
#-----------------------------------------------------------------                     
            elif msg.text in ["Clear ban"]:
                if msg.from_ in admin:
                 wait["blacklist"] = {}   
                 cl.sendText(msg.to,"Clear ✅")                
#-----------------------------------------------------------------                    
            elif msg.text.lower() == 'kill':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"User blacklist does not have")
                        return
                    for jj in matched_list:
                        try:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#-------------------------------------------------------------                            
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled")
#-----------------------------------------------------------------                    
            elif "Spam album:" in msg.text:
                try:
                    albumtags = msg.text.replace("Spam album:","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,"We created an album" + name)
                except:
                    cl.sendText(msg.to,"Error")
#-----------------------------------------------
            elif msg.text.lower() == 'in':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text.lower() == 'backup':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

#-----------------------------------------------
            elif "1in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "2in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "3in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G) 
#-----------------------------------------------
            elif "4in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki4.updateGroup(G)
#-----------------------------------------------
            elif "5in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "6in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif "7in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
#-----------------------------------------------
            elif "8in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
#-----------------------------------------------
            elif "9in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
#-----------------------------------------------
            elif "10in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)                                                                                                                                                                       
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text.lower() == 'out':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "1out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "2out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "3out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "4out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "5out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "6out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "7out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "8out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "9out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "10out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Leave" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Kb Key" in msg.text:
                ki.sendText(msg.to,"""      􀠁􀆩􏿿􀠁􀆩􏿿 BOT [KB] 􀠁􀆩􏿿􀠁􀆩􏿿  \n\n 􀠁􀆩􏿿 key Only Kicker 􀠁􀆩􏿿 \n\n􀠁􀆩􏿿[Kb1 in]\n􀠁􀆩􏿿[1name:]\n􀠁􀆩􏿿[B Cancel]\n􀠁􀆩􏿿[kick @]\n􀠁􀆩􏿿[Ban @]\n􀠁􀆩􏿿[kill]\n􀠁􀆩􏿿[BotChat]\n􀠁􀆩􏿿[Respons]\n􀠁􀆩􏿿[Kb1 Gift]\n􀠁􀆩􏿿[Kb1 bye]\n\n   
  
        
  
TEAM LONGOR WAS HERE



""")
#-----------------------------------------------
            elif msg.text.lower() == 'Kam':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"✏Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"✏Owner Grup " + str(ginfo.name) + "  \n" + ginfo.creator.displayName )

            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                    else:
                        G = ki.getGroup(op.param1)
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True
                       
                        
                elif op.param3 in kimid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)                        
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)


                elif op.param3 in ki2mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                    else:
                        G = ki3.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        
                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                    else:
                        G = ki4.getGroup(op.param1)
                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)

                elif op.param3 in ki4mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                    else:
                        G = ki5.getGroup(op.param1)
                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                    else:
                        G = ki6.getGroup(op.param1)
                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                    else:
                        G = ki7.getGroup(op.param1)
                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                    else:
                        G = ki8.getGroup(op.param1)
                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)

                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                    else:
                        G = ki9.getGroup(op.param1)
                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)

                elif op.param3 in ki9mid:
                    if op.param2 in ki8mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                    else:
                        G = ki10.getGroup(op.param1)
                        
                        ki10.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket =ki8.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)

                elif op.param3 in ki10mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket =ki9.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
            except:
                pass


        if op.type == 19:
                if not op.param2 in admin:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        gs = ki3.getGroup(op.param1)
                        gs = ki4.getGroup(op.param1)
                        gs = ki5.getGroup(op.param1)
                        gs = ki6.getGroup(op.param1)
                        gs = ki7.getGroup(op.param1)
                        gs = ki8.getGroup(op.param1)
                        gs = ki9.getGroup(op.param1)
                        gs = ki10.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            return


                    except Exception, e:
                        print e


        if op.type == 11:
                if not op.param2 in admin:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            return


                    except Exception, e:
                        print e
        
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			ki.kickoutFromGroup(op.param1,[op.param2])
			ki2.kickoutFromGroup(op.param1,[op.param2])
			ki3.kickoutFromGroup(op.param1,[op.param2])
			ki4.kickoutFromGroup(op.param1,[op.param2])
			ki5.kickoutFromGroup(op.param1,[op.param2])
			ki6.kickoutFromGroup(op.param1,[op.param2])
			ki7.kickoutFromGroup(op.param1,[op.param2])
			ki8.kickoutFromGroup(op.param1,[op.param2])
			ki9.kickoutFromGroup(op.param1,[op.param2])
			ki10.kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(cl).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki10.updateGroup(G)
			ki5.kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    ki.kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(cl).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(ki).updateGroup(G)
			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    ki.kickoutFromGroup(op.param1,[op.param2])
		    ki2.kickoutFromGroup(op.param1,[op.param2])
		    ki3.kickoutFromGroup(op.param1,[op.param2])
		    ki4.kickoutFromGroup(op.param1,[op.param2]) 
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    ki.cancelGroupInvitation(op.param1,[op.param3])
		    ki2.cancelGroupInvitation(op.param1,[op.param3])
		    ki3.cancelGroupInvitation(op.param1,[op.param3])
		    ki4.cancelGroupInvitation(op.param1,[op.param3])
		    ki5.cancelGroupInvitation(op.param1,[op.param3])
		    ki6.cancelGroupInvitation(op.param1,[op.param3])
		    ki7.cancelGroupInvitation(op.param1,[op.param3])
		    ki8.cancelGroupInvitation(op.param1,[op.param3])
		    ki9.cancelGroupInvitation(op.param1,[op.param3])
		    ki10.cancelGroupInvitation(op.param1,[op.param3])
		    random.choice(ki).kickoutFromGroup(op.param1,[op.param2])
            if op.param2 not in Bots:
       	        if op.param2 in Bots:
       	           pass
                elif wait["cancelprotect"] == True:
                   cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    ki2.updateGroup(G)
		    ki3.updateGroup(G)
		    ki4.updateGroup(G)
		    ki5.updateGroup(G)
		    ki6.updateGroup(G)
		    ki7.updateGroup(G)
		    ki8.updateGroup(G)
		    ki9.updateGroup(G)
		    ki10.updateGroup(G)
		    random.choice.kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

	if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・ " + Name + datetime.today().strftime('   %d - %H:%M:%S')
                        wait2['ROM'][op.param1][op.param2] = "・ " + Name
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    pass
            except:
                pass                

        if op.type == 26:
            msg = op.message
            try:
                if msg.contentType == 0:
                    try:
                        if msg.to in wait2['readPoint']:
                            if msg.from_ in wait2["ROM"][msg.to]:
                                del wait2["ROM"][msg.to][msg.from_]
                        else:
                            pass
                    except:
                        pass
                else:
                    pass

            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as error:
                print error
                print ("\n\nRECEIVE_MESSAGE\n\n")
                return

        if op.type == 59:
            print op


    except Exception as error:
        print error



        if op.type == 59:
            print op


    except Exception as error:
        print error

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)