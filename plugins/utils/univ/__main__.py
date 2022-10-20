"Checker UNIV"
import time, requests as req
from bs4 import BeautifulSoup as bs
from userge import userge, Message

#binus
@userge.on_cmd("binus", about={
	'header': "Untuk cek akun BINUS",
	'usage': "{tr}binus [nim]:[pass]\n"})
	
async def binus(message: Message):
	"""Untuk cek akun BINUS"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = "https://myclass.apps.binus.ac.id/Auth/Login"
	dat = {"Username":u, "Password":p}
	raw = ses.post(url, data=dat).text
	if "Login Success" in raw:
		await message.edit(f"BINUS\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
	else:
		await message.edit(f"BINUS\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)


#mercu
@userge.on_cmd("mercu", about={
	'header': "Untuk cek akun MERCU",
	'usage': "{tr}mercu [nim]:[pass]\n"})
	
async def mercu(message: Message):
	"""Untuk cek akun MERCU"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	res = ses.post("https://sso.mercubuana.ac.id", data={"username":u, "password":p, "_method":"POST" }).headers['Set-Cookie']
	try:
		mantap = bs(res, 'html.parser').findAll('td')[3].get_text() 
		await message.edit(f"MERCU\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
	except:
		await message.edit(f"MERCU\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)


#uajy
@userge.on_cmd("uajy", about={
	'header': "Untuk cek akun UAJY",
	'usage': "{tr}uajy [nim]:[pass]\n"})
	
async def uajy(message: Message):
	"""Untuk cek akun UAJY"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = "https://sikma.uajy.ac.id/Account/Login?ReturnUrl=%2F"
	raw = ses.get(url).text
	tok = bs(raw, 'html.parser').findAll('input')
	dat = { "__RequestVerificationToken":tok[4]['value'],
	"username":u,
	"password":p, }
	res = ses.post(url, data=dat).text 
	if "Gagal Login!" in res:
		await message.edit(f"UAJY\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)
	else:
		await message.edit(f"UAJY\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
	

		
#ub
@userge.on_cmd("ub", about={
	'header': "Untuk cek akun UB",
	'usage': "{tr}ub [nim]:[pass]\n"})
	
async def ub(message: Message):
	"""Untuk cek akun UB"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = 'https://siam.ub.ac.id/index.php'
	headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}
	dat = {'username':u, 'password':p, 'login':'submit' }
	raw = ses.post(url, headers=headers, data=dat, verify=False).text 
	yan = bs(raw, 'html.parser').find("title")
	if yan.text == "Sistem Informasi Akademik Mahasiswa":
		await message.edit(f"UB\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
	else:
		await message.edit(f"UB\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)



#ugm
@userge.on_cmd("ugm", about={
	'header': "Untuk cek akun UGM",
	'usage': "{tr}ugm [nim]:[pass]\n"})
	
async def ugm(message: Message):
	"""Untuk cek akun UGM"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = 'https://sso.ugm.ac.id/cas/login?service=http%3A%2F%2Fsimaster.ugm.ac.id%2Fugmfw%2Fsignin_simaster%2Fsignin_proses'
	raw = ses.get(url).text
	tok = bs(raw, 'html.parser').findAll('input')
	dat = { 'username':u, 'password':p, 'lt':tok[4]['value'], '_eventId':'submit', 'submit':'LOGIN'}
	res = ses.post(url, data=dat).text
	try:
		bs(res, 'html.parser').findAll('noscript')[0].get_text()
		await message.edit(f"UGM\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
	except:
		await message.edit(f"UGM\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)
		
		
#ui
@userge.on_cmd("ui", about={
	'header': "Untuk cek akun UI",
	'usage': "{tr}ui [nim]:[pass]\n"})
	
async def ui(message: Message):
	"""Untuk cek akun UI"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = 'https://sso.ui.ac.id/cas/login'
	raw = ses.get(url).text
	tok = bs(raw, 'html.parser').findAll('input')
	dat = {'username':u,  'password':p, 
	 'lt':tok[2]['value'], 
	 'execution':tok[3]['value'], 
	 '_eventId':'submit'}
	res = ses.post(url, data=dat).headers
	try:
		mantap = res['Set-Cookie']
		await message.edit(f"UI\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
	except:
		await message.edit(f"UI\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)


#uii
@userge.on_cmd("uii", about={
	'header': "Untuk cek akun UII",
	'usage': "{tr}uii [nim]:[pass]\n"})
	
async def uii(message: Message):
	"""Untuk cek akun UII"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = 'https://cloud-api.uii.ac.id/v1/login'
	ro = req.options(url, verify=False)
	headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
	'Referer': 'https://gateway.uii.ac.id/account/login'}
	data = {'kd_member': u, 'password': p}
	yan = req.post(url, headers=headers, data=data, verify=False)
	if "true" in yan.text :
		await message.edit(f"UII\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
	else:
		await message.edit(f"UII\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)

#ulm
@userge.on_cmd("ulm", about={
	'header': "Untuk cek akun ULM",
	'usage': "{tr}ulm [nim]:[pass]\n"})
	
async def ulm(message: Message):
	"""Untuk cek akun ULM"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = "https://portal.ulm.ac.id/mahasiswa"
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')[0]['value']
	login =  ses.post(url, data={ "csrf_test_name":tok, "username":u, "password":p, "Submit":"Login" }, verify=False).text
	if "Username tidak terdaftar" in login:
		await message.edit(f"ULM \nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)
	elif "Password anda salah" in login:
		await message.edit(f"ULM \nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)
	else:
		await message.edit(f"ULM\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
		

#unsyi
@userge.on_cmd("unsyi", about={
	'header': "Untuk cek akun UNSYIAH",
	'usage': "{tr}unsyi [nim]:[pass]\n"})
	
async def unsyi(message: Message):
	"""Untuk cek akun UNSYIAH"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = 'https://simkuliah.unsyiah.ac.id/index.php/login' 
	dat = { 'username':u, 'password':p }
	res = ses.post(url, data=dat).text
	if "Username atau Password Anda salah.." in res:
		await message.edit(f"UNSYIAH\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)
	else:
		await message.edit(f"UNSYIAH\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")





#uny
@userge.on_cmd("uny", about={
	'header': "Untuk cek akun UNY",
	'usage': "{tr}uny [nim]:[pass]\n"})
	
async def uny(message: Message):
	"""Untuk cek akun UNY"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = 'https://sso.uny.ac.id/login' 
	raw = ses.get(url).text
	tok = bs(raw, 'html.parser').findAll('input')[2]['value']
	dat = {'username':u,  'password':p, 'execution':tok, '_eventId':'submit', 'submit':'LOGIN'}
	res = ses.post(url, data=dat).text
	qn = bs(res, 'html.parser').find('title')
	if qn.text == 'Berhasil Masuk / Log In Successful - Single Sign On UNY':
		await message.edit(f"UNY\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
	else:
		await message.edit(f"UNY\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)


#upi
@userge.on_cmd("upi", about={
	'header': "Untuk cek akun UPI",
	'usage': "{tr}upi [nim]:[pass]\n"})
	
async def upi(message: Message):
	"""Untuk cek akun UPI"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = 'https://sso.upi.edu/cas/login' 
	raw = ses.get(url).text
	tok = bs(raw, 'html.parser').findAll('input')[2]['value']
	dat = {'username':u,  'password':p, 'execution':tok, '_eventId':'submit', 'submit':'LOGIN'}
	res = ses.post(url, data=dat, verify=False).text
	qn = bs(res, 'html.parser').findAll('div')[2]['class'][0]
	if qn == 'success':
		await message.edit(f"UPI\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
	else:
		await message.edit(f"UPI\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)
		
@userge.on_cmd("unair", about={
	'header': "Untuk cek akun UNAIR",
	'usage': "{tr}unair [nim]:[pass]\n"})
	
async def ub(message: Message):
	"""Untuk cek akun UNAIR"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = 'https://mahasiswa.unair.ac.id/'
	headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}
	dat = {'username':u, 'password':p, 'btnSubmit':'login' }
	raw = ses.post(url, headers=headers, data=dat, verify=False).text 
	yan = bs(raw, 'html.parser').find("title")
	if yan.text == "Mahasiswa - Universitas Airlangga":
		await message.edit(f"UNAIR\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)
	else:
		await message.edit(f"UNAIR\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
