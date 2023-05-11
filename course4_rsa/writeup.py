from Crypto.Util.number import *
import hashlib
from gmpy2 import iroot
from math import floor
import numpy as np
from fractions import Fraction
import owiener
import random

def gcd(number1, number2):
    if(number1 == 0): return number2
    return gcd(number2%number1, number1)

def get_p_q(phi, N):
    res = []
    for i in range(len(phi)):
        b = int(N-phi[i]+1)
        coeff = [1, b, N]
        res.append(np.roots(coeff))
    return res


def Wiener(e,N):
    cur = e/N
    e_N = []
    e_N.append(floor(cur))
    i = 0
    con = 1
    while con != 0:
        cur = 1/cur
        con = round(cur,6)
        
        new = int(round(cur,6))
        e_N.append(new)
        cur = cur - new
        con = con - new

    cur = e/N
    k_d = []
    k_d.append(e_N[0])
    for item in range(1, len(e_N)):
        den = 0
        for j in reversed(range(1, item+1)):
            den += e_N[j]
            den = 1/den
        k_d.append(e_N[0]+den)
    

    frac = [Fraction(f).limit_denominator() for f in k_d[1:]]
    phi = []
    for  i in range(len(frac)):
        cur = (e*frac[i].denominator - 1)/frac[i].numerator
        if cur - round(cur, 6) == 0:
            phi.append(cur)
    phi = [int(i) for i in phi]
    res = get_p_q(phi, N)

    return res

def  factorize_N_with_d_e(e,d,N):
    k = d*e - 1
    while True:
        g = random.randint(2, N-1)
        t = k 
        x = 1
        while t%2==0:
            t = t//2
            x = pow(g, t, N)
        if x > 1 and gcd(x-1, N) > 1:
            p = gcd(x-1, N)
            q = N//p
            return p,q

    

# ------------------------------------------------------------------------------------------------------------

# RSA Starter 1

# SageMath

# print(pow(101,17, 22663))

# ------------------------------------------------------------------------------------------------------------
# RSA Starter 2

# SageMath

# print(pow(12, 65537,17*23))

# ------------------------------------------------------------------------------------------------------------
# RSA Starter 3

# p = 857504083339712752489993810777

# q = 1029224947942998075080348647219

# print((p-1)*(q-1))

# ------------------------------------------------------------------------------------------------------------
# RSA Starter 4

def extended_gcd(a,b):
    s = 0
    old_s = 1
    r = b
    old_r = a

    bezout_t = None

    q = None
    while r!= 0:
        q = int(old_r / r)
        old_r, r = r, old_r - q*r
        old_s, s = s, old_s - q*s

    if b!=0 :
        bezout_t = int((old_r - old_s*a) / b)
    else: 
        bezout_t = 0
    
    print(old_s, bezout_t)
    print("GCD: " + str(old_r))
    return (old_s,bezout_t,old_r)

def inv(number1, number2):
    (old_s,bezout_t,old_r) = extended_gcd(number1, number2)
    if old_r > 1: return None
    if old_s < 0: old_s+=number2
    return old_s

# p = 857504083339712752489993810777

# q = 1029224947942998075080348647219

# e = 65537

# phi = (p-1)*(q-1)
# print(inv(e,phi))
# 121832886702415731577073962957377780195510499965398469843281


# ------------------------------------------------------------------------------------------------------------
# RSA Starter 5

# #======= Public K
# N = 882564595536224140639625987659416029426239230804614613279163

# e = 65537
# #======= 

# ######## Private K
# d = 121832886702415731577073962957377780195510499965398469843281

# # message
# c = 77578995801157823671636298847186723593814843845525223303932


# print(pow(c, d,N))


# ------------------------------------------------------------------------------------------------------------
# RSA Starter 6

# N = 15216583654836731327639981224133918855895948374072384050848479908982286890731769486609085918857664046075375253168955058743185664390273058074450390236774324903305663479046566232967297765731625328029814055635316002591227570271271445226094919864475407884459980489638001092788574811554149774028950310695112688723853763743238753349782508121985338746755237819373178699343135091783992299561827389745132880022259873387524273298850340648779897909381979714026837172003953221052431217940632552930880000919436507245150726543040714721553361063311954285289857582079880295199632757829525723874753306371990452491305564061051059885803
# d = 11175901210643014262548222473449533091378848269490518850474399681690547281665059317155831692300453197335735728459259392366823302405685389586883670043744683993709123180805154631088513521456979317628012721881537154107239389466063136007337120599915456659758559300673444689263854921332185562706707573660658164991098457874495054854491474065039621922972671588299315846306069845169959451250821044417886630346229021305410340100401530146135418806544340908355106582089082980533651095594192031411679866134256418292249592135441145384466261279428795408721990564658703903787956958168449841491667690491585550160457893350536334242689

# flag = b"crypto{Immut4ble_m3ssag1ng}"

# m = hashlib.sha256()
# m.update(flag)

# hash_m = bytes_to_long(m.digest()) #69523276807549773371481917516452638375664281433555793080445569568100703974091
# print(hash_m)

# print(pow(hash_m, d,N))


# ------------------------------------------------------------------------------------------------------------
# Factoring
# p = 510143758735509025530880200653196460532653147
# a = factor(p)
# b = a[0][0]
# c = a[1][0]
# print(b if b<c else c)


# ------------------------------------------------------------------------------------------------------------
# Monoprime
# n = 171731371218065444125482536302245915415603318380280392385291836472299752747934607246477508507827284075763910264995326010251268493630501989810855418416643352631102434317900028697993224868629935657273062472544675693365930943308086634291936846505861203914449338007760990051788980485462592823446469606824421932591                                                                  
# e = 65537
# ct = 161367550346730604451454756189028938964941280347662098798775466019463375610700074840105776873791605070092554650190486030367121011578171525759600774739890458414593857709994072516290998135846956596662071379067305011746842247628316996977338024343628757374524136260758515864509435302781735938531030576289086798942

# phi = n-1
# d = inv(e, phi)

# message = pow(ct, d, n)
# 44981230718212183184022261350591509650967020174777710365581497711727767219325
# print(long_to_bytes(44981230718212183184022261350591509650967020174777710365581497711727767219325))

# ------------------------------------------------------------------------------------------------------------
#  Manyprime
# n = 580642391898843192929563856870897799650883152718761762932292482252152591279871421569162037190419036435041797739880389529593674485555792234900969402019055601781662044515999210032698275981631376651117318677368742867687180140048715627160641771118040372573575479330830092989800730105573700557717146251860588802509310534792310748898504394966263819959963273509119791037525504422606634640173277598774814099540555569257179715908642917355365791447508751401889724095964924513196281345665480688029639999472649549163147599540142367575413885729653166517595719991872223011969856259344396899748662101941230745601719730556631637
# e = 65537
# ct = 320721490534624434149993723527322977960556510750628354856260732098109692581338409999983376131354918370047625150454728718467998870322344980985635149656977787964380651868131740312053755501594999166365821315043312308622388016666802478485476059625888033017198083472976011719998333985531756978678758897472845358167730221506573817798467100023754709109274265835201757369829744113233607359526441007577850111228850004361838028842815813724076511058179239339760639518034583306154826603816927757236549096339501503316601078891287408682099750164720032975016814187899399273719181407940397071512493967454225665490162619270814464

# fac = ecm.factor(n)
# phi = 1

# for i in fac:
#     phi = phi*(i-1)
# d = inv(e,phi)

# message = pow(ct,d,n)
# print(message)
# 686359111300845080969870766816838073152202927102297965376128501853336957

# print(long_to_bytes(686359111300845080969870766816838073152202927102297965376128501853336957))

# ------------------------------------------------------------------------------------------------------------
# Salty
# n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767                                                                  
# e = 1
# ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
# print(long_to_bytes(ct))

# ------------------------------------------------------------------------------------------------------------
# Modulus Inutilis
# n = 17258212916191948536348548470938004244269544560039009244721959293554822498047075403658429865201816363311805874117705688359853941515579440852166618074161313773416434156467811969628473425365608002907061241714688204565170146117869742910273064909154666642642308154422770994836108669814632309362483307560217924183202838588431342622551598499747369771295105890359290073146330677383341121242366368309126850094371525078749496850520075015636716490087482193603562501577348571256210991732071282478547626856068209192987351212490642903450263288650415552403935705444809043563866466823492258216747445926536608548665086042098252335883
# e = 3
# ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957
# message = (iroot(ct,3))       # ct = message^e % phi because of 1024 bits phi :)) so there is a chance to ci = message^e
# print(long_to_bytes(message[0]))

# ------------------------------------------------------------------------------------------------------------
# Inferius Prime
# n = 742449129124467073921545687640895127535705902454369756401331
# e = 3
# ct = 39207274348578481322317340648475596807303160111338236677373

# fac = factor(n)
# p = fac[0][0]         #p = 752708788837165590355094155871

# q = fac[1][0]         #q = 986369682585281993933185289261

# phi = (p-1)*(q-1)

# d = inv(e,phi)
# message = pow(ct,d,n)

# print(long_to_bytes(9525146106593233618825000042088863551831280763610019197))

# ------------------------------------------------------------------------------------------------------------
# Square Eyes
# n =     535860808044009550029177135708168016201451343147313565371014459027743491739422885443084705720731409713775527993719682583669164873806842043288439828071789970694759080842162253955259590552283047728782812946845160334801782088068154453021936721710269050985805054692096738777321796153384024897615594493453068138341203673749514094546000253631902991617197847584519694152122765406982133526594928685232381934742152195861380221224370858128736975959176861651044370378539093990198336298572944512738570839396588590096813217791191895941380464803377602779240663133834952329316862399581950590588006371221334128215409197603236942597674756728212232134056562716399155080108881105952768189193728827484667349378091100068224404684701674782399200373192433062767622841264055426035349769018117299620554803902490432339600566432246795818167460916180647394169157647245603555692735630862148715428791242764799469896924753470539857080767170052783918273180304835318388177089674231640910337743789750979216202573226794240332797892868276309400253925932223895530714169648116569013581643192341931800785254715083294526325980247219218364118877864892068185905587410977152737936310734712276956663192182487672474651103240004173381041237906849437490609652395748868434296753449
# # n is p^2
# e =     65537
# ct =    222502885974182429500948389840563415291534726891354573907329512556439632810921927905220486727807436668035929302442754225952786602492250448020341217733646472982286222338860566076161977786095675944552232391481278782019346283900959677167026636830252067048759720251671811058647569724495547940966885025629807079171218371644528053562232396674283745310132242492367274184667845174514466834132589971388067076980563188513333661165819462428837210575342101036356974189393390097403614434491507672459254969638032776897417674577487775755539964915035731988499983726435005007850876000232292458554577437739427313453671492956668188219600633325930981748162455965093222648173134777571527681591366164711307355510889316052064146089646772869610726671696699221157985834325663661400034831442431209123478778078255846830522226390964119818784903330200488705212765569163495571851459355520398928214206285080883954881888668509262455490889283862560453598662919522224935145694435885396500780651530829377030371611921181207362217397805303962112100190783763061909945889717878397740711340114311597934724670601992737526668932871436226135393872881664511222789565256059138002651403875484920711316522536260604255269532161594824301047729082877262812899724246757871448545439896

# p = iroot(n,2)[0]
# phi = (p-1)*p
# d = inv(e, phi)
# message = pow(ct, d, n)
# # 912327745903138317426723037632596080882852291533603076406890007888287805926165236318117298828527463941218685
# print(long_to_bytes(912327745903138317426723037632596080882852291533603076406890007888287805926165236318117298828527463941218685))

# ------------------------------------------------------------------------------------------------------------
# Everything is Big
# N = "b8af3d3afb893a602de4afe2a29d7615075d1e570f8bad8ebbe9b5b9076594cf06b6e7b30905b6420e950043380ea746f0a14dae34469aa723e946e484a58bcd92d1039105871ffd63ffe64534b7d7f8d84b4a569723f7a833e6daf5e182d658655f739a4e37bd9f4a44aff6ca0255cda5313c3048f56eed5b21dc8d88bf5a8f8379eac83d8523e484fa6ae8dbcb239e65d3777829a6903d779cd2498b255fcf275e5f49471f35992435ee7cade98c8e82a8beb5ce1749349caa16759afc4e799edb12d299374d748a9e3c82e1cc983cdf9daec0a2739dadcc0982c1e7e492139cbff18c5d44529407edfd8e75743d2f51ce2b58573fea6fbd4fe25154b9964d"
# e = "9ab58dbc8049b574c361573955f08ea69f97ecf37400f9626d8f5ac55ca087165ce5e1f459ef6fa5f158cc8e75cb400a7473e89dd38922ead221b33bc33d6d716fb0e4e127b0fc18a197daf856a7062b49fba7a86e3a138956af04f481b7a7d481994aeebc2672e500f3f6d8c581268c2cfad4845158f79c2ef28f242f4fa8f6e573b8723a752d96169c9d885ada59cdeb6dbe932de86a019a7e8fc8aeb07748cfb272bd36d94fe83351252187c2e0bc58bb7a0a0af154b63397e6c68af4314601e29b07caed301b6831cf34caa579eb42a8c8bf69898d04b495174b5d7de0f20cf2b8fc55ed35c6ad157d3e7009f16d6b61786ee40583850e67af13e9d25be3"
# c = "3f984ff5244f1836ed69361f29905ca1ae6b3dcf249133c398d7762f5e277919174694293989144c9d25e940d2f66058b2289c75d1b8d0729f9a7c4564404a5fd4313675f85f31b47156068878e236c5635156b0fa21e24346c2041ae42423078577a1413f41375a4d49296ab17910ae214b45155c4570f95ca874ccae9fa80433a1ab453cbb28d780c2f1f4dc7071c93aff3924d76c5b4068a0371dff82531313f281a8acadaa2bd5078d3ddcefcb981f37ff9b8b14c7d9bf1accffe7857160982a2c7d9ee01d3e82265eec9c7401ecc7f02581fd0d912684f42d1b71df87a1ca51515aab4e58fab4da96e154ea6cdfb573a71d81b2ea4a080a1066e1bc3474"

# N = bytes_to_long(bytes.fromhex(N))
# e = bytes_to_long(bytes.fromhex(e))
# c = bytes_to_long(bytes.fromhex(c))

# d = owiener.attack(e, N)
# message = pow(c,d, N)
# print(long_to_bytes(message))

# ------------------------------------------------------------------------------------------------------------
# Crossed Wires
# My_private_keys =  [21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 2734411677251148030723138005716109733838866545375527602018255159319631026653190783670493107936401603981429171880504360560494771017246468702902647370954220312452541342858747590576273775107870450853533717116684326976263006435733382045807971890762018747729574021057430331778033982359184838159747331236538501849965329264774927607570410347019418407451937875684373454982306923178403161216817237890962651214718831954215200637651103907209347900857824722653217179548148145687181377220544864521808230122730967452981435355334932104265488075777638608041325256776275200067541533022527964743478554948792578057708522350812154888097]
# My_Friend_public_keys = [[21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 106979], [21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 108533], [21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 69557], [21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 97117], [21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 103231]]
# Encrypted_flag = 20304610279578186738172766224224793119885071262464464448863461184092225736054747976985179673905441502689126216282897704508745403799054734121583968853999791604281615154100736259131453424385364324630229671185343778172807262640709301838274824603101692485662726226902121105591137437331463201881264245562214012160875177167442010952439360623396658974413900469093836794752270399520074596329058725874834082188697377597949405779039139194196065364426213208345461407030771089787529200057105746584493554722790592530472869581310117300343461207750821737840042745530876391793484035024644475535353227851321505537398888106855012746117

# message = Encrypted_flag
# e = 65537
# p,q = (factorize_N_with_d_e(e, My_private_keys[1], My_private_keys[0]))
# p,q = (134460556242811604004061671529264401215233974442536870999694816691450423689575549530215841622090861571494882591368883283016107051686642467260643894947947473532769025695530343815260424314855023688439603651834585971233941772580950216838838690315383700689885536546289584980534945897919914730948196240662991266027, 161469718942256895682124261315253003309512855995894840701317251772156087404025170146631429756064534716206164807382734456438092732743677793224010769460318383691408352089793973150914149255603969984103815563896440419666191368964699279209687091969164697704779792586727943470780308857107052647197945528236341228473)
# phi = (p-1)*(q-1)
# friend_private_key = []
# for key in range(len(My_Friend_public_keys)):
#     e_i = My_Friend_public_keys[key][1]
#     d_i = inv(e_i, My_Friend_public_keys[key][0])
#     friend_private_key.append([My_Friend_public_keys[key][0], d_i])

# for key in reversed(range(len(friend_private_key))):
#     message = pow(message, friend_private_key[key][1], friend_private_key[key][0])
# print(message)
# print(long_to_bytes(282351761401118367933191045054313718055580073791559536506841118001604417533527376824087507263144353230054685686578866914410695559969149))

# ------------------------------------------------------------------------------------------------------------
#  Everything is Still Big
# N = "0xb12746657c720a434861e9a4828b3c89a6b8d4a1bd921054e48d47124dbcc9cfcdcc39261c5e93817c167db818081613f57729e0039875c72a5ae1f0bc5ef7c933880c2ad528adbc9b1430003a491e460917b34c4590977df47772fab1ee0ab251f94065ab3004893fe1b2958008848b0124f22c4e75f60ed3889fb62e5ef4dcc247a3d6e23072641e62566cd96ee8114b227b8f498f9a578fc6f687d07acdbb523b6029c5bbeecd5efaf4c4d35304e5e6b5b95db0e89299529eb953f52ca3247d4cd03a15939e7d638b168fd00a1cb5b0cc5c2cc98175c1ad0b959c2ab2f17f917c0ccee8c3fe589b4cb441e817f75e575fc96a4fe7bfea897f57692b050d2b"
# e = "0x9d0637faa46281b533e83cc37e1cf5626bd33f712cc1948622f10ec26f766fb37b9cd6c7a6e4b2c03bce0dd70d5a3a28b6b0c941d8792bc6a870568790ebcd30f40277af59e0fd3141e272c48f8e33592965997c7d93006c27bf3a2b8fb71831dfa939c0ba2c7569dd1b660efc6c8966e674fbe6e051811d92a802c789d895f356ceec9722d5a7b617d21b8aa42dd6a45de721953939a5a81b8dffc9490acd4f60b0c0475883ff7e2ab50b39b2deeedaefefffc52ae2e03f72756d9b4f7b6bd85b1a6764b31312bc375a2298b78b0263d492205d2a5aa7a227abaf41ab4ea8ce0e75728a5177fe90ace36fdc5dba53317bbf90e60a6f2311bb333bf55ba3245f"
# c = "0xa3bce6e2e677d7855a1a7819eb1879779d1e1eefa21a1a6e205c8b46fdc020a2487fdd07dbae99274204fadda2ba69af73627bdddcb2c403118f507bca03cb0bad7a8cd03f70defc31fa904d71230aab98a10e155bf207da1b1cac1503f48cab3758024cc6e62afe99767e9e4c151b75f60d8f7989c152fdf4ff4b95ceed9a7065f38c68dee4dd0da503650d3246d463f504b36e1d6fafabb35d2390ecf0419b2bb67c4c647fb38511b34eb494d9289c872203fa70f4084d2fa2367a63a8881b74cc38730ad7584328de6a7d92e4ca18098a15119baee91237cea24975bdfc19bdbce7c1559899a88125935584cd37c8dd31f3f2b4517eefae84e7e588344fa5"


# ------------------------------------------------------------------------------------------------------------
#  Diffie-Hellman Starter 1
# p = 991
# g = 209
# print(inv(g, p))


# ------------------------------------------------------------------------------------------------------------
#  Diffie-Hellman Starter 2
'''We just need to detect Cycle :))'''
p = 28151

found = False
for i in range(2,p):
    found = True
    for j in range(2,p):
        a = pow(i, j, p)
        if a == i:
            found = False
            break
    if found:
        print("Found: " + str(i))
        


