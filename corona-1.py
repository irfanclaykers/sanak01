import os,sys
os.system('xdg-open https://m.youtube.com/channel/UCzWOSICWhsyn9rH3siTDtuQ')
os.system('clear')
print """\033[31m------------------------------------------------------
\033[00m\033[41m                  CEK CORONA MATI 2020                \033[00m
\033[31m------------------------------------------------------"""
print "\033[31m[\033[00m+\033[31m]\033[00m Authour : Sanakkambang01"
print "\033[31m[\033[00m+\033[31m]\033[00m My Team : Termux Comunity"
print "\033[31m[\033[00m+\033[31m]\033[00m Github  :\033[32m https://github.com/Sanakkambang01"
print
exec('import requests,re,os\nos.system("")\nfrom difflib import get_close_matches as caris\na=requests.get("https://api.kawalcorona.com/").text\nnamanegara=re.findall(\'"Country_Region":"(.*?)"\',a)\n\nwhile True:\n\task=raw_input("\033[31m[\033[00m+\033[31m] \033[00mCountry +> \033[32m")\n\tcari="".join(caris(ask,namanegara,n=1,cutoff=0))\n\ta=requests.get("https://api.kawalcorona.com/").text\n\tpat= r\'{"OBJECTID":.*?,"Country_Region":"\'+cari+\'","Last_Update":.*?,"Lat":.*?,"Long_":.*?,"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),"Active":(.*?)}}\'\n\tb=re.search(pat,a)\n\tprint ("\\x1b[1;35m\\n\033[31m[\033[00m+\033[31m] \033[00mNama Negara +> {}").format(cari)\n\tprint ("""\\x1b[1;31m[\033[00m+\033[31m]\033[00m Infected :\033[32m {}\n\\x1b[1;31m[\033[00m+\033[31m] \033[00mDied : \033[31m{}\n\\x1b[1;31m[\033[00m+\033[31m]\033[00m Recovered : \033[33m{}\n\\x1b[1;31m[\033[00m+\033[31m] \033[00mActive :\033[36m {}\\x1b[1;38m\n""".format(b.group(1),b.group(2),b.group(3),b.group(4)))\n\tif cari.lower() == "indonesia":\n\t\twhile True:\n\t\t\taska=raw_input("\\n\\x1b[1;31m[\033[00m#\033[31m]\033[00m Tampilkan Provinsi (\\x1b[1;32my\\x1b[1;36m/\\x1b[1;31mn\\x1b[1;36m) : \\x1b[1;39m").lower()\n\t\t\tif aska == "y":\n\t\t\t\ta=requests.get("https://api.kawalcorona.com/indonesia/provinsi/").text\n\t\t\t\tpat = re.findall(r\'"Provinsi":"(.*?)","Kasus_Posi":(.*?),"Kasus_Semb":(.*?),"Kasus_Meni":(.*?)}}\',a)\n\t\t\t\tfor i in pat:\n\t\t\t\t\tprint ("\\n\033[31m[\033[00m+\033[31m] \033[00mNama Negara +>\033[35m "+i[0]+"")\n\t\t\t\t\tprint ("\\x1b[1;31m[\033[00m+\033[31m] \033[00mTerinfeksi : \033[33m"+str(i[1]))\n\t\t\t\t\tprint ("\\x1b[1;31m[\033[00m+\033[31m] \033[00mSembuh     :\033[32m "+str(i[2]))\n\t\t\t\t\tprint ("\\x1b[1;31m[\033[00m+\033[31m] \033[00mMati       :\033[31m "+str(i[3])+"\\x1b[1;39m")\n\t\t\t\tprint("\\n\\n");break\n\t\t\telif aska == "n":\n\t\t\t\tbreak\n')
