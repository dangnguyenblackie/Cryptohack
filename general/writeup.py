#!/bin/python3 -f
from functools import reduce
import base64
from Crypto.PublicKey import RSA
import OpenSSL
###### FERMAT LITTLE THEOREM
# a and p is coprime -> a^(p-1) = 1 mod p
#######

###### Euler Criterion
# a^(p-1)/2 = 1 if there exist x that a == x^2 mod p else -1
######

# lengendre 
def lengendre(a,p):
    return pow(a,(p-1)//2,p)

#tonelli shanks
def tonelli_shanks(a, p):
    assert lengendre(a, p) == 1
    q = p- 1
    s = 0
    while q%2 == 0:
        s = s+1    
        q//=2
    
    if s == 1: return pow(a,(p-1)//4,p)     #p = 3 mod 4
    
    #find z
    for z in range(2,p):
        if p-1 == lengendre(z, p): break

    #assign
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q+1)//2, p)

    while (t-1)%p != 0:
        t2 = (t*t)%p
        for i in range(1,m):
            if (t2-1)%p == 0:
                break
            t2 = (t2*t2)%p
        b = pow(c, 1 << (m-i-1), p)
        r = (r*b)%p
        c = (b*b)%p
        t = (t*c)%p
        m = i   
    return r

#chinese_remainder
def chinese_remainder(r, p):
    res = 0
    p_prod = reduce(lambda a,b: a*b, p) # N = n1*n2*n3*...
    for r_i,p_i in zip(r,p):
        N = (p_prod//p_i)
        if inv(N, p_i):
            res += (r_i*N*inv(N, p_i))
    return res

# general/gcd
def gcd(number1, number2):
    if(number1 == 0): return number2
    return gcd(number2%number1, number1)

# a = 66528
# b = 52920
# print(gcd(a, b))


# extended Euclide
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

def mulMod(number1,number2, number3):
    return (number1*number2)%number3

def powMod(number1,number2, number3):
    assert number2 >= 0 
    res = 1
    while number2 > 0:
        if(number2 & 1 == 1): res = mulMod(res, number1, number3)
        number1 = mulMod(number1, number1, number3)
        number2 = number2 >> 1
    return res
# mod 1
# p = 8146798528947
# q = 17
# print(p%q)



# mod 2
# print(gcd(273246787654,65537))

# mod inverting
# res = [x for x in range(13) if int((13*x+1)%3) == 0 and int((13*x+1)/3) < 13]
# print(int((13*res[0]+1)/3))

# Quadratic Residues: square root modulo
'''
This feels good, but now let's think about the square root of 18. From the above, we know we need to find some integer a such that a2 = 18

Your first idea might be to start with a = 1 and loop to a = p-1. In this discussion p isn't too large and we can quickly look.

Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all a ∈ Fp* you never find an a such that a2 = 18.
'''

# p = 29
# ints = [14, 6, 11] 
# res = []
# for items in ints:
#     for i in range(29):
#         if i*i % p == items: 
#             res += [items]
#             print(i)
#             break

# print(res)


# Legendre Symbol:
'''
Quadratic Residue * Quadratic Residue = Quadratic Residue
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue 
'''

'''
So what's the trick? The Legendre Symbol gives an efficient way to determine whether an integer is a quadratic residue modulo an odd prime p.

Legendre's Symbol: (a / p) ≡ a(p-1)/2 mod p obeys:

(a / p) = 1 if a is a quadratic residue and a ≢ 0 mod p
(a / p) = -1 if a is a quadratic non-residue mod p
(a / p) = 0 if a ≡ 0 mod p

Which means given any integer a, calculating pow(a,(p-1)//2,p) is enough to determine if a is a quadratic residue.
'''


########
# p = 3 mod 4
# p = 3 mod 4
# p = 3 mod 4
########
# p = 101524035174539890485408575671085261788758965189060164484385690801466167356667036677932998889725476582421738788500738738503134356158197247473850273565349249573867251280253564698939768700489401960767007716413932851838937641880157263936985954881657889497583485535527613578457628399173971810541670838543309159139

# ints = [
# 25081841204695904475894082974192007718642931811040324543182130088804239047149283334700530600468528298920930150221871666297194395061462592781551275161695411167049544771049769000895119729307495913024360169904315078028798025169985966732789207320203861858234048872508633514498384390497048416012928086480326832803, 
# 45471765180330439060504647480621449634904192839383897212809808339619841633826534856109999027962620381874878086991125854247108359699799913776917227058286090426484548349388138935504299609200377899052716663351188664096302672712078508601311725863678223874157861163196340391008634419348573975841578359355931590555, 
# 17364140182001694956465593533200623738590196990236340894554145562517924989208719245429557645254953527658049246737589538280332010533027062477684237933221198639948938784244510469138826808187365678322547992099715229218615475923754896960363138890331502811292427146595752813297603265829581292183917027983351121325, 
# 14388109104985808487337749876058284426747816961971581447380608277949200244660381570568531129775053684256071819837294436069133592772543582735985855506250660938574234958754211349215293281645205354069970790155237033436065434572020652955666855773232074749487007626050323967496732359278657193580493324467258802863, 
# 4379499308310772821004090447650785095356643590411706358119239166662089428685562719233435615196994728767593223519226235062647670077854687031681041462632566890129595506430188602238753450337691441293042716909901692570971955078924699306873191983953501093343423248482960643055943413031768521782634679536276233318, 
# 85256449776780591202928235662805033201684571648990042997557084658000067050672130152734911919581661523957075992761662315262685030115255938352540032297113615687815976039390537716707854569980516690246592112936796917504034711418465442893323439490171095447109457355598873230115172636184525449905022174536414781771, 
# 50576597458517451578431293746926099486388286246142012476814190030935689430726042810458344828563913001012415702876199708216875020997112089693759638454900092580746638631062117961876611545851157613835724635005253792316142379239047654392970415343694657580353333217547079551304961116837545648785312490665576832987, 
# 96868738830341112368094632337476840272563704408573054404213766500407517251810212494515862176356916912627172280446141202661640191237336568731069327906100896178776245311689857997012187599140875912026589672629935267844696976980890380730867520071059572350667913710344648377601017758188404474812654737363275994871, 
# 4881261656846638800623549662943393234361061827128610120046315649707078244180313661063004390750821317096754282796876479695558644108492317407662131441224257537276274962372021273583478509416358764706098471849536036184924640593888902859441388472856822541452041181244337124767666161645827145408781917658423571721, 
# 18237936726367556664171427575475596460727369368246286138804284742124256700367133250078608537129877968287885457417957868580553371999414227484737603688992620953200143688061024092623556471053006464123205133894607923801371986027458274343737860395496260538663183193877539815179246700525865152165600985105257601565]
# # res = [i for i in ints if (powMod(i, int((p-1)/2), p)==1 and i%p!=0)]
# # print((res))

# res = [i for i in ints if (pow(i, int((p-1)/2), p)==1 and i%p!=0)]

# quad = res[0]

# print(pow(quad,(p+1)/4,p))


# Modular Square Root

# a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
# p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161

# print(tonelli_shanks(a,p))


# CHINESE REMAINDER THEOREM
'''
 This means, that given a set of arbitrary integers ai, and pairwise coprime integers ni, such that the following linear congruences hold:

Note "pairwise coprime integers" means that if we have a set of integers {n1, n2, ..., ni}, all pairs of integers selected from the set are coprime: gcd(ni, nj) = 1.

x ≡ a1 mod n1
x ≡ a2 mod n2
...
x ≡ an mod nn


There is a unique solution x ≡ a mod N where N = n1 * n2 * ... * nn
'''

'''
x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17

Find the integer a such that x ≡ a mod 935
'''

# 935 = 5*11*17

# 935k + a - 2 % 5 = 0 
# 935k + a - 3 % 11 = 0 
# 935k + a - 5 % 17 = 0 

# a = [2,3,5]
# b = [5,11,17]

# prod = reduce(lambda a,b: a*b,b)

# print(chinese_remainder(a, b)%prod)


# Privacy-Enhanced Mail?


# c = open("./general/privacy_enhanced_mail.pem", "r").read()
# p = RSA.import_key(c)
# print(p.d)

# CERTainly not
# c = open("general/2048b-rsa-example-cert.der", "rb").read()
# p = RSA.import_key(c)
# print(p.n)

# Bruce-RSA
''' 
ssh-keygen -f bruce_rsa.pub -e -m pem > bruce_rsa.pem
'''
# c = open("general/bruce_rsa.pem", "rb").read()
# p = RSA.import_key(c)
# print(p.n)

# Transparency
''' 
When you connect to a website over HTTPS, the first TLS message sent by the server is the ServerHello containing the server TLS certificate. 
Your browser verifies that the TLS certificate is valid, and if not, will terminate the TLS handshake. Verification includes ensuring that:

- the name on the certificate matches the domain

- the certificate has not expired

- the certificate is ultimately signed (via a "chain of trust") by a root key of a Certificate Authority (CA) that's trusted by your browser or operating system

Since CAs have the power to sign any certificate, the security of the internet depends upon these organisations to issue TLS certificates to the correct people: they must only issue certificates to the real domain owners. 
However with Windows trusting root certificates from over 100 organisations by default, there's a number of opportunities for hackers, politics, or incompetence to break the whole model. If you could trick just a single CA to issue you a certificate for microsoft.com, 
you could use the corresponding private key to sign malware and bypass trust controls on Windows. CAs are strongly incentivised to be careful since their business depends upon people trusting them, however in practice they have failed several times.
'''

import requests, json, sys
target = 'cryptohack.org'
req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))

json_data = json.loads(req.text)
for (key,value) in enumerate(json_data):
    url = str(value['name_value'])
    if url.endswith(target):
        try:
            response_req = requests.get('https://' +url).text
        
            if(response_req.startswith('crypto')):
                print('URL : ' + url)
                print('KEY : ' +response_req)
                break         
        except:
            continue