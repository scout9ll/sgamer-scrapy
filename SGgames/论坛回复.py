from bs4 import BeautifulSoup
import requests
import re,json
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie':'U6IV_2132_auth=2b114JkisabQda3jAwUevVCSLDiukVXuF8XYX1oMkwRNFtZVvrAQl8P9MkKkRpYmAE%2BNfzMUgaUE1rL8%2FBdiI0NuqxQO; U6IV_2132_nofavfid=1; U6IV_2132_home_readfeed=1515230279; U6IV_2132_ulastactivity=1517429545%7C0; U6IV_2132_connect_is_bind=0; U6IV_2132_smile=1D1; pgv_pvi=9922863860; U6IV_2132_atarget=1; U6IV_2132_saltkey=xF7oFubF; U6IV_2132_lastvisit=1520176558; U6IV_2132_visitedfid=44; U6IV_2132_st_t=0%7C1520241726%7C84a77cec2bff2159dadabaef87bc4a74; U6IV_2132_forum_lastvisit=D_44_1520241726; U6IV_2132_secqaa=385067.d60cd5c3bf3db8d11a; U6IV_2132_st_p=0%7C1520242697%7C3eeea960d8792435138ff509744bf67e; U6IV_2132_viewid=tid_13670810; U6IV_2132_lastact=1520242699%09connect.php%09check; Hm_lvt_bcf12fa2ce69a5732226b5052e39a17a=1520002885,1520050018,1520180165,1520240862; Hm_lpvt_bcf12fa2ce69a5732226b5052e39a17a=1520242704'
}
def comments(url):

	data=requests.get(url,verify=False,headers=headers)


	soup=BeautifulSoup(data.text, 'lxml')
	c=soup.findAll("div",id=re.compile("post_[0-9]+"))
	title =soup.find("span",id="thread_subject").get_text()
	try:
		next_page = soup.find("a", attrs={"class": "nxt"}).get("href")
	except:
		next_page=None
	print(title)
	for x in c:
		a = x.find("td",attrs={"class":"t_f"})
		try:
			q=a.get_text().replace("\n", "").replace("\r", "")#string返回的是单个TAG下的text,而get_text返回TAG及TAG里面所有的text,str是字节串，，，，，text返回的是unicode字符串
		except:													#PY3中Str字节串 读取自动解码（默认utf-8），所以不能decode，只有输出的时候会再encode输出保存
			q="muted"
		b = x.find("a",target="_blank").get_text()
		e=int(re.findall(r"http://fj2.sgamer.com/attachment/common/.+?/common_(.+?)_usergroup_icon.png",str(x))[0])


		print(q,b,e)

	if next_page is not None:
		comments("https://bbs.sgamer.com/" + next_page)

comments("https://bbs.sgamer.com/thread-13658244-1-1.html")
"""
for i in range(2):
	url = 'https://bbs.sgamer.com/forum-44-%d.html' % (i+1)
	data = requests.get(url, verify=False, headers=headers)
	soup = BeautifulSoup(data.text, 'lxml')
	urls = soup.findAll("a", onclick = "atarget(this)")
		#onclick = "atarget(this)"
	for x in urls:
		print(x.get("href"))

#soup=BeautifulSoup(data.text, 'lxml')

#a=soup.findAll("td",id=re.compile("postmessage"))
#b=soup.findAll("strong")
#commends=[]
#names=[]
db=[]
#print(b)


#	print([names[i],commends[i]])
#with open("回复集.json","w") as f:
#	json.dump(db,f)
#"""