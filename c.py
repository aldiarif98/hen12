# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from gtts import gTTS
from bs4 import BeautifulSoup
import time,random,sys,re,goslate,requests,urllib,os,json,subprocess,codecs,threading,glob,wikipedia

cl = LINETCR.LINE()
#cl.login(qr=True)
cl.login(token="Ep1q9OvUF2SMHbCez2s8.+hT72C/sNWhx0CFc83gtAa.mhFBlJK2/a6ZqDmKlfuFL2X06bCrZz8mlUsVbDXGspI=")
cl.loginResult()

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""         ⚠彡 T⃟E⃟A⃟M⃟ L⃟O⃟N⃟G⃟O⃟R⃟ 彡⚠

╔═══════════════════
╠     ✍️MODIFIER✍️
╠❂͜͡➣ All:[text]
╠❂͜͡➣ Allbio:[text]
╠❂͜͡➣ Comment:[text]
╠❂͜͡➣ Message:[text]
╠❂͜͡➣ Group name:[text]
╚═══════════════════
╔═══════════════════
╠     ✍️PROMOTE/DEMOTE✍️
╠❂͜͡➣ Admin on @[name]
╠❂͜͡➣ Expel on @[name]
╠❂͜͡➣ Expelall
╚═══════════════════
╔═══════════════════
╠     ✍️STEALING✍️
╠❂͜͡➣ Steal name    @[name]
╠❂͜͡➣ Steal contact @[name]
╠❂͜͡➣ Ava cover   @[name]
╠❂͜͡➣ Ava    @[name]
╠❂͜͡➣ Ava group
╠❂͜͡➣ Midpict:[mid]
╠❂͜͡➣ Copy @[name]
╠❂͜͡➣ Mybackup
╚═══════════════════
╔═══════════════════
╠     ✍️GUARD MODE✍️
╠❂͜͡➣ Protect:low
╠❂͜͡➣ Protect:hight
╚═══════════════════
╔═══════════════════
╠     ✍️MARK TO LIST✍️
╠❂͜͡➣ Ban    @[name]
╠❂͜͡➣ Unban  @[name]
╠❂͜͡➣ Ban group:
╠❂͜͡➣ Del ban:
╠❂͜͡➣ List ban group
╠❂͜͡➣ Banned[send contact]
╠❂͜͡➣ Unbanned[send contact]
╠❂͜͡➣ Ban repeat @[name]
╠❂͜͡➣ Blacklist all
╠❂͜͡➣ Ban cek
╠❂͜͡➣ Clear banl
╠❂͜͡➣ Mimic target @[name]
╠❂͜͡➣ Mimic untarget @[name]
╠❂͜͡➣ Add friend @[name]
╠❂͜͡➣ Target @[name]
╠❂͜͡➣ Del target @[name]
╠❂͜͡➣ Target list
╚═══════════════════
╔═══════════════════
╠     ✍️INVITATION✍️
╠❂͜͡➣ Invite:[mid]
╠❂͜͡➣ Invite user[contact]
╠❂͜͡➣ Invite me
╠❂͜͡➣ Join all
╠❂͜͡➣ Join group
╚═══════════════════
╔═══════════════════
╠     ✍️LEAVE GROUP✍️
╠❂͜͡➣ All out
╠❂͜͡➣ Center @bye
╠❂͜͡➣ Bye allgroups[own]
╠❂͜͡➣ Leave group:
╚═══════════════════
╔═══════════════════
╠     ✍️BOT AUTO SETTINGS✍️
╠❂͜͡➣ Auto join:on/off
╠❂͜͡➣ Auto leave:on/off
╠❂͜͡➣ Auto like:on/off
╠❂͜͡➣ Welcome message:on/off
╠❂͜͡➣ Auto notice:on/off
╠❂͜͡➣ Blockinvite:on/off
╠❂͜͡➣ Auto blockqr:on/off
╠❂͜͡➣ Namelock:on/off
╠❂͜͡➣ Mimic:on/off
╠❂͜͡➣ Auto add:on/off
╠❂͜͡➣ Check message
╠❂͜͡➣ Add message:[text]
╠❂͜͡➣ Comment:on/off
╠❂͜͡➣ Add comment:[text]
╠❂͜͡➣ Check comment
╠❂͜͡➣ Backup:on/off
╠❂͜͡➣ Gcancel:[number]
╠❂͜͡➣ Update welcome:[text]
╠❂͜͡➣ Check welcome message
╚═══════════════════
╔═══════════════════
╠     ✍️CANCEL MODE✍️
╠❂͜͡➣ Rejectall
╠❂͜͡➣ Clean invites
╠❂͜͡➣ Clear invites
╚═══════════════════
╔═══════════════════
╠     ✍️SUPRISE GIFT✍️
╠❂͜͡➣ gift1-15
╠❂͜͡➣ Spam gift
╚═══════════════════
╔═══════════════════
╠    ✍️NOTIFICATION LIST✍️
╠❂͜͡➣ Group list
╠❂͜͡➣ Banlist
╠❂͜͡➣ Admin list
╠❂͜͡➣ Settings
╠❂͜͡➣ Ginfo
╠❂͜͡➣ TL:[text]
╠❂͜͡➣ Mimic list
╠❂͜͡➣ Details grup:
╠❂͜͡➣ Crash
╠❂͜͡➣ Add all
╚═══════════════════
╔═══════════════════
╠★ KICKER MODE ★
╠❂͜͡➣ Cleanse
╠❂͜͡➣ Vkick @
╠❂͜͡➣ Nk [name]
╠❂͜͡➣ Kick:[mid]
╠❂͜͡➣ Purge
╠❂͜͡➣ Ulti
╠❂͜͡➣ Recover
╚═══════════════════
╔═══════════════════
╠     ✍️CHAT RELATED✍️
╠❂͜͡➣ Spamg[on/off][no][txt]
╠❂͜͡➣ Spam add:[text]
╠❂͜͡➣ Spam change:[text]
╠❂͜͡➣ Spam start:[number]
╠❂͜͡➣ Say [text]
╠❂͜͡➣ Me
╠❂͜͡➣ Speed
╠❂͜͡➣ Debug speed
╠❂͜͡➣ My mid
╠❂͜͡➣ Gcreator
╠❂͜͡➣ Halo
╠❂͜͡➣ Bot contact
╠❂͜͡➣ Bot mid
╠❂͜͡➣ Creator
╠❂͜͡➣ System
╠❂͜͡➣ Iconfig
╠❂͜͡➣ Kernel
╠❂͜͡➣ Cpu
╠❂͜͡➣ Responsename
╠❂͜͡➣ Help
╠❂͜͡➣ Mc:[mid]
╚═══════════════════
╔═══════════════════
╠     ✍️UTILITY✍️
╠❂͜͡➣ Lurk
╠❂͜͡➣ View
╠❂͜͡➣ Setlastpoint
╠❂͜͡➣ Viewlastseen
╠❂͜͡➣ Link open
╠❂͜͡➣ Link close
╠❂͜͡➣ Gurl
╠❂͜͡➣ Remove chat
╠❂͜͡➣ Bot restart
╚═══════════════════
╔═══════════════════
╠     ✍️CHAT RELATED✍️
╠❂͜͡➣ Lyric [][]
╠❂͜͡➣ Music [][]
╠❂͜͡➣ Wiki [text]
╠❂͜͡➣ Vidio [text]
╠❂͜͡➣ Youtube [text]
╠❂͜͡➣ Instagram [text]
╠❂͜͡➣ .fb
╠❂͜͡➣ .google
╠❂͜͡➣ Translate-idn [text]
╠❂͜͡➣ Translate-eng [text]
╠❂͜͡➣ Translate-thai [text]
╠❂͜͡➣ Translate-japan [text]
╠❂͜͡➣ Emoji [expression]
╠❂͜͡➣ Info @[name]
╠❂͜͡➣ Ping
╠❂͜͡➣ Time
╠❂͜͡➣ apakah
╠❂͜͡➣ Sticker [expression]
╠❂͜͡➣ Mention all
╠❂͜͡➣ /say
╠❂͜͡➣ /say-en
╠❂͜͡➣ /say-jp
╠❂͜͡➣ Dosa @
╠❂͜͡➣ /
╠❂͜͡➣ Siapa
╚═══════════════════
╔═══════════════════
╠     ✍️BROADCASTING✍️
╠❂͜͡➣ Pm cast   [text]
╠❂͜͡➣ Broadcast [text]
╠❂͜͡➣ Spam @[name]
╚═══════════════════
╔═══════════════════
╠     ✍️special command✍️ 
╠❂͜͡➣ Turn off bots
╚═══════════════════
        ⚠彡 T⃟E⃟A⃟M⃟ L⃟O⃟N⃟G⃟O⃟R⃟ 彡⚠
"""
KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]
admin= ["ufc7b7bd9cf929f01d7d1c7c2f3719368"]
staff=[]
whitelist=[]

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add Me",
    "lang":"JP",
    "comment":"AutoLike by HendrahAry",
    "welmsg":"welcome to group",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "status":False,
    "likeOn":False,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "welcomemsg":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
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
    'ROM':{},
    'rom':{}
    }
    
res = {
    'num':{},
    'us':{},
    'au':{},
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

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

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

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

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
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
      
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

#=======================================================
            elif msg.text.lower() == "crash":
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ufc7b7bd9cf929f01d7d1c7c2f3719368"}
                cl.sendMessage(msg)
#-----------------=============================                   
#--------------------------------- TRANSLATE --------------------------------

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
            elif "Lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"cctv already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "Lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"cctv already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "View" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Sider:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Sider:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\ncctving time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Cctv has not been set.")
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
                        cl.sendText(msg.to, "URL Open" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "URL Open" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
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
                        cl.sendText(msg.to, "URL Close" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "URL Close" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
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
                    cl.sendText(msg.to, "Name Changed To " + string + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
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
                 cnt.text = "Jumlah :\n" + str(jml) +  " Members" + "\n\nWaktu :" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S')
                 cnt.to = msg.to
                 cl.sendMessage(cnt)

#---------------------------------------------------------------------------
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "      Done" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                except Exception as e:
                    cl.sendText(msg.to, str (e)) 
#-----------------------------------------------
            elif "/say-jp " in msg.text:
                say = msg.text.replace("/say-jp ","")
                lang = 'jp'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#------------------------------------------------
            elif "/say-en " in msg.text:
                say = msg.text.replace("/say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------
            elif "/say " in msg.text:
                 psn = msg.text.replace("/say ","")
                 tts = gTTS(psn, lang='id', slow=False)
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
			cl.sendText(msg.to, "      Done " + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
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
                
            elif "Steal mid @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Steal mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass            
                        
                                  
#---------------------------------------------------------------------------     
#-----------------------------------------------
            elif "Siapa " in msg.text:
    		tanya = msg.text.replace("Siapa ","")
    		jawab = ("Dia yg kebanyakan micin"," Dia gila")
    		jawaban = random.choice(jawab)
		tts = gTTS(text=jawaban, lang='en')
		tts.save('tts.mp3')
    		cl.sendAudio(msg.to,'tts.mp3')
#==========================================
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='en')
                tts.save('tts.mp3')
                cl.sendText(msg.to,"Dosanya adalah cek voie ini")
                cl.sendAudio(msg.to,'tts.mp3')

            elif msg.text in ["Center @bye"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     cl.sendMessage(msg.to,"bye-bye")
                     cl.leaveGroup(msg.to)
                except:
                     pass
           
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
            elif "Ava cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Ava cover @","")
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
                cl.sendText(msg.to, "Bot Restarted" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                restart_program()
                print "@Restart"        
                
            elif "Turn off" in msg.text:
               if msg.from_ in owner:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass          
                     
            elif msg.text.lower() == 'ifconfig':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")                                                   
            elif msg.text.lower() == 'system':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                    
            elif "Viewlastseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%d日 %H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        grp = '\n• '.join(str(f) for f in dataResult)
                        total = '\nThese %iuesrs have seen at the lastseen\npoint(｀・ω・´)\n\n%s' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "• %s %s" % (grp, total))
                    else:
                        cl.sendText(msg.to, "Sider ga bisa di read cek setpoint dulu bego tinggal ketik\nSetlastpoint\nkalo mau liat sider ketik\nViewlastseen")
                    print "Viewlastseen"   
                    
            elif "Setlastpoint" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                #cl.sendText(msg.to, "Checkpoint checked!")
                cl.sendText(msg.to, "Set the lastseens' point(｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                print "Setlastpoint"     
                
            elif "Lirik " in msg.text:
                songname = msg.text.replace("Lirik ","")
                params = {"songname": songname}
                r=requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data=r.text
                data=json.loads(data)
                for song in data:
                    songz = song[5].encode('utf-8')
                    lyric = songz.replace('ti:','Title -')
                    lyric = lyric.replace('ar:','Artist -')
                    lyric = lyric.replace('al:','Album -')
                    removeString = "[1234567890.:]"
                    for char in removeString:
                        lyric = lyric.replace(char,'')
                    cl.sendText(msg.to, "Judul: " + song[0].encode('utf-8') + "\n\n" + lyric)
                        
            elif "Info @" in msg.text:
              if msg.from_ in admin:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        gjh= cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + gjh.displayName + "\n[Mid]:\n" + gjh.mid + "\n[BIO]:\n" + gjh.statusMessage + "\n[pict profile]:\nhttp://dl.profile.line-cdn.net/" + gjh.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass                                                                            
#-----------------------------------------------------------------                        
            elif "youtube " in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'Vidio ' in msg.text:
	      if msg.from_ in admin:
                try:
                    textToSearch = (msg.text).replace('Vidio ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
		    cl.sendVideoWithURL(msg.to,ght)
                except:
                    cl.sendText(msg.to,"Could not find it")     
                    
#========================================
            elif ".fb" in msg.text:
                    a = msg.text.replace(".fb","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    cl.sendText(msg.to, "https://www.facebook.com" + b)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")                                                       
#========================================
            elif ".google " in msg.text:
                    a = msg.text.replace(".google ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    cl.sendText(msg.to, "https://www.google.com" + b)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")
#========================================                    
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
                                
            elif 'cari ' in msg.text.lower():
                  try:
                      shi = msg.text.lower().replace("cari ","")
                      kha = random.choice(items)
                      url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + shi
                      raw_html = (download_page(url))
                      items = items + (_images_get_all_items(raw_html))
                      items = []
                  except:
                      try:
                          cl.sendImageWithURL(msg.to,random.choice(items))
                          cl.sendText(msg.to,"Total Image Links ="+str(len(items)))
                      except Exception as e:
                          cl.sendText(msg.to,str(e))                                
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
#=================================================================
            elif msg.text in ["Protect:hight","protect:hight"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Auto blockqr:off","auto blockqr:off"]:
              if msg.from_ in admin:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Welcome message:on"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on")
            elif msg.text in ["Auto blockqr:on","auto blockqr:on"]:
              if msg.from_ in admin:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Welcome message:off"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Protect:low","Protect:low"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
#=======================================================
            elif msg.text.lower() == "crash":
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ufc7b7bd9cf929f01d7d1c7c2f3719368"}
                cl.sendMessage(msg)
#-----------------=============================                           
                        
#===============================================================
            
            elif msg.text in ["Auto like:on"]:
              if msg.from_ in admin:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Auto like:off"]:
              if msg.from_ in admin:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
#==========================================================
            elif msg.text in ["Invite"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")                        
                        
 #-----------------------------------------------------------------                       
            elif msg.text in ["Settings","Set"]:
              if msg.from_ in admin:
            	print "Setting pick up..."
                md="list of bot settings\n\n"
                if wait["likeOn"] == True: md+="Auto like : on\n"
                else:md+="Auto like : off\n"
                if wait["winvite"] == True: md+="Invite : on\n"
                else:md+="Invite : off\n"
                if wait["pname"] == True: md+="Namelock : on\n"
                else:md+="Namelock : off\n"
                if wait["contact"] == True: md+="Notice : on\n"
                else: md+="Notice : off\n"
                if wait["autoJoin"] == True: md+="Auto join : on\n"
                else: md +="Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="Auto leave : on\n"
                else: md+="Auto leave : off\n"
                if wait["clock"] == True: md+="Clock Name : on\n"
                else:md+="Clock Name : off\n"
                if wait["autoAdd"] == True: md+="Auto add : on\n"
                else:md+="Auto add : off\n"
                if wait["commentOn"] == True: md+="Comment : on\n"
                else:md+="Comment : off\n"
                if wait["Backup"] == True: md+="Backup : on\n"
                else:md+="Backup : off\n"
                if wait["qr"] == True: md+="Protect QR : on\n"
                else:md+="Protect QR : off\n"
                if wait["welcomemsg"] == True: md+="welcome message : on\n"
                else:md+="welcome message : off\n"
                if wait["protectionOn"] == True: md+="Protection : hight\n\n"+ datetime.today().strftime('%H:%M:%S')
                else:md+="Protection : low\n\n"+ datetime.today().strftime('%H:%M:%S')
                cl.sendText(msg.to,md)
                
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
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
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
              if msg.from_ in admin:
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
                        cl.sendAudioWithURL(msg.to, song[3])
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
                ki11.sendText(msg.to,"Hadir")
                ki12.sendText(msg.to,"Hadir")
                ki13.sendText(msg.to,"Hadir")
                ki13.sendText(msg.to, "Lengkap Bos" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
#-----------------------------------------------------------speed
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
#-----------------------------------------------------------------                
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
#-----------------------------------------------------------------                
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing") 
                else:
                    cl.sendText(msg.to,"blacklist user list")
                    mc = "[⎈]Blacklist User[⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
#-----------------------------------------------------------------                     
            elif msg.text in ["Clear ban"]:
                if msg.from_ in admin:
                 wait["blacklist"] = {}   
                 cl.sendText(msg.to, "      Clear " + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))                
            elif "Pm cast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Pm cast ", "")
					t = cl.getAllContactIds()
					for manusia in t:
						cl.sendText(manusia,(bctxt))        
						
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = cl.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = cl.getGroup(i).name
		            if h == ng:
		                cl.inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success join to ["+ h +"] group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Khusus Creator")
		except Exception as e:
		    cl.sendMessage(msg.to, str(e))				
		    
#-------------------------------------------------------
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)
#===========================================
            elif msg.text in ["Comment:on"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Comment:off"]:
              if msg.from_ in admin:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Check comment"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"message comment\n\n" + str(wait["comment"]))

            elif "Time" in msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))		    		         
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
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
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
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki13.updateGroup(G)
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki13.updateGroup(G)
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki2mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                    else:
                        G = ki3.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True
                        
                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])


                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki4mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki9mid:
                    if op.param2 in ki8mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki10mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                    else:
                        G = ki11.getGroup(op.param1)

                        
                        ki11.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket =ki9.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)

                elif op.param3 in ki11mid:
                    if op.param2 in ki10mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                    else:
                        G = ki12.getGroup(op.param1)

                        
                        ki12.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket =ki10.reissueGroupTicket(op.param1)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        
                elif op.param3 in ki12mid:
                    if op.param2 in ki11mid:
                        G = ki11.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                    else:
                        G = ki13.getGroup(op.param1)

                        
                        ki13.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket =ki11.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)

                elif op.param3 in ki13mid:
                    if op.param2 in ki12mid:
                        G = ki12.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket =ki12.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)



                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki2mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True
                        
                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])


                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki4mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki9mid:
                    if op.param2 in ki8mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki10mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                    else:
                        G = ki11.getGroup(op.param1)

                        
                        ki11.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket =ki9.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)

                elif op.param3 in ki11mid:
                    if op.param2 in ki10mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                    else:
                        G = ki12.getGroup(op.param1)

                        
                        ki12.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket =ki10.reissueGroupTicket(op.param1)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        
                elif op.param3 in ki12mid:
                    if op.param2 in ki11mid:
                        G = ki11.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                    else:
                        G = ki13.getGroup(op.param1)

                        
                        ki13.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket =ki11.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)

                elif op.param3 in ki13mid:
                    if op.param2 in ki12mid:
                        G = ki12.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket =ki12.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)

   

                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki20.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in kimid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki2mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True
                        
                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])


                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki4mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)

                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki10mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                    else:
                        G = ki11.getGroup(op.param1)

                        
                        ki11.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket =ki9.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)

                elif op.param3 in ki11mid:
                    if op.param2 in ki10mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                    else:
                        G = ki12.getGroup(op.param1)

                        
                        ki12.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket =ki10.reissueGroupTicket(op.param1)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        
                elif op.param3 in ki12mid:
                    if op.param2 in ki11mid:
                        G = ki11.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                    else:
                        G = ki13.getGroup(op.param1)

                        
                        ki13.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket =ki11.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)

                elif op.param3 in ki13mid:
                    if op.param2 in ki12mid:
                        G = ki12.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket =ki12.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)


                       
            except:
                pass
                
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			ki6.kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(cl).getGroup(op.param1)
			G.preventJoinByTicket = True
			random.choice(ki).updateGroup(G)
			ki6.kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    ki6.kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(cl).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(ki).updateGroup(G)
			    ki6.kickoutFromGroup(op.param1,[op.param2])
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
		    ki6.kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	if op.type == 13:
            if wait["inviteprotect"] == True:
                group = ki10.getGroup(op.param1)
                gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              ki10.cancelGroupInvitation(op.param1, gMembMids)
              ki10.sendText(op.param1, "Aku Cancel😛")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki5.updateGroup(G)
		    ki6.updateGroup(G)
		    ki7.updateGroup(G)
		    ki8.updateGroup(G)
		    ki9.updateGroup(G)
		    ki10.updateGroup(G)
		    ki11.updateGroup(G)
		    ki12.updateGroup(G)
		    ki13.updateGroup(G)
		    random.choice(ki).kickoutFromGroup(op.param1,[op.param2])
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

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
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
            
def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kc.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ks.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kt.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kk.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kc.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ks.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kt.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()            