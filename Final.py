import Tkinter
from Tkinter import *
import os
from open import browse
import tkMessageBox
from transfer import *
#import nltk
tx=[]
tg=[]
dict1={'a': u'\u0d05',
	 'aa': u'\u0d06',
	 'i': u'\u0d07',
	 'ii': u'\u0d08',
	 'u': u'\u0d09',
	 'uu': u'\u0d0a',
	 'rh': u'\u0d0b',
	 'e': u'\u0d0e',
	 'ee': u'\u0d0f',
	 'ai': u'\u0d10',
	 'o': u'\u0d12',
	 'oo': u'\u0d13',
	 'au': u'\u0d14',
	 'k': u'\u0d15\u0d4d',
	 'kh': u'\u0d16\u0d4d',
	 'g': u'\u0d17\u0d4d',
	 'gh': u'\u0d18\u0d4d',
	 'ng': u'\u0d19\u0d4d',
	 'ch': u'\u0d1a\u0d4d',
	 'chh': u'\u0d1b\u0d4d',
	 'j': u'\u0d1c\u0d4d',
	 'jh': u'\u0d1d\u0d4d',
	 'nj': u'\u0d1e\u0d4d',
	 't': u'\u0d1f\u0d4d',
	 'tt': u'\u0d20\u0d4d',
	 'd': u'\u0d21\u0d4d',
	 'dd': u'\u0d22\u0d4d',
	 'nh': u'\u0d23\u0d4d',
	 'th': u'\u0d24\u0d4d',
	 'tth': u'\u0d25\u0d4d',
	 'dh': u'\u0d26\u0d4d',
	 'ddh': u'\u0d27\u0d4d',
	 'n': u'\u0d28\u0d4d',
	 'p': u'\u0d2a\u0d4d',
	 'ph': u'\u0d2b\u0d4d',
	 'b': u'\u0d2c\u0d4d',
	 'bh': u'\u0d2d\u0d4d',
	 'm': u'\u0d2e\u0d4d',
	 'y': u'\u0d2f\u0d4d',
	 'r': u'\u0d30\u0d4d',
	 'rr': u'\u0d31\u0d4d',
	 'l': u'\u0d32\u0d4d',
	 'll': u'\u0d33\u0d4d',
	 'v': u'\u0d35\u0d4d',
	 'sh': u'\u0d36\u0d4d',
	 'ss': u'\u0d37\u0d4d',
	 's': u'\u0d38\u0d4d',
	 'h': u'\u0d39\u0d4d',
	 'zh': u'\u0d34\u0d4d',
	 'kaa': u'\u0d15\u0d3e',
	 'khaa': u'\u0d16\u0d3e',
	 'gaa': u'\u0d17\u0d3e',
	 'ghaa': u'\u0d18\u0d3e',
	 'ngaa': u'\u0d19\u0d3e',
	 'chaa': u'\u0d1a\u0d3e',
	 'chhaa': u'\u0d1b\u0d3e',
	 'jaa': u'\u0d1c\u0d3e',
	 'jhaa': u'\u0d1d\u0d3e',
	 'njaa': u'\u0d1e\u0d3e',
	 'taa': u'\u0d1f\u0d3e',
	 'ttaa': u'\u0d20\u0d3e',
	 'daa': u'\u0d21\u0d3e',
	 'ddaa': u'\u0d22\u0d3e',
	 'nhaa': u'\u0d23\u0d3e',
	 'thaa': u'\u0d24\u0d3e',
	 'tthaa': u'\u0d25\u0d3e',
	 'dhaa': u'\u0d26\u0d3e',
	 'ddhaa': u'\u0d27\u0d3e',
	 'naa': u'\u0d28\u0d3e',
	 'paa': u'\u0d2a\u0d3e',
	 'phaa': u'\u0d2b\u0d3e',
	 'baa': u'\u0d2c\u0d3e',
	 'bhaa': u'\u0d2d\u0d3e',
	 'maa': u'\u0d2e\u0d3e',
	 'yaa': u'\u0d2f\u0d3e',
	 'raa': u'\u0d30\u0d3e',
	 'rraa': u'\u0d31\u0d3e',
	 'laa': u'\u0d32\u0d3e',
	 'llaa': u'\u0d33\u0d3e',
	 'vaa': u'\u0d35\u0d3e',
	 'shaa': u'\u0d36\u0d3e',
	 'ssaa': u'\u0d37\u0d3e',
	 'saa': u'\u0d38\u0d3e',
	 'haa': u'\u0d39\u0d3e',
	 'zhaa': u'\u0d34\u0d3e',
	 'ki': u'\u0d15\u0d3f',
	 'khi': u'\u0d16\u0d3f',
	 'gi': u'\u0d17\u0d3f',
	 'ghi': u'\u0d18\u0d3f',
	 'ngi': u'\u0d19\u0d3f',
	 'chi': u'\u0d1a\u0d3f',
	 'chhi': u'\u0d1b\u0d3f',
	 'ji': u'\u0d1c\u0d3f',
	 'jhi': u'\u0d1d\u0d3f',
	 'nji': u'\u0d1e\u0d3f',
	 'ti': u'\u0d1f\u0d3f',
	 'tti': u'\u0d20\u0d3f',
	 'di': u'\u0d21\u0d3f',
	 'ddi': u'\u0d22\u0d3f',
	 'nhi': u'\u0d23\u0d3f',
	 'thi': u'\u0d24\u0d3f',
	 'tthi': u'\u0d25\u0d3f',
	 'dhi': u'\u0d26\u0d3f',
	 'ddhi': u'\u0d27\u0d3f',
	 'ni': u'\u0d28\u0d3f',
	 'pi': u'\u0d2a\u0d3f',
	 'phi': u'\u0d2b\u0d3f',
	 'bi': u'\u0d2c\u0d3f',
	 'bhi': u'\u0d2d\u0d3f',
	 'mi': u'\u0d2e\u0d3f',
	 'yi': u'\u0d2f\u0d3f',
	 'ri': u'\u0d30\u0d3f',
	 'rri': u'\u0d31\u0d3f',
	 'li': u'\u0d32\u0d3f',
	 'lli': u'\u0d33\u0d3f',
	 'vi': u'\u0d35\u0d3f',
	 'shi': u'\u0d36\u0d3f',
	 'ssi': u'\u0d37\u0d3f',
	 'si': u'\u0d38\u0d3f',
	 'hi': u'\u0d39\u0d3f',
	 'zhi': u'\u0d34\u0d3f',
	 'kii': u'\u0d15\u0d40',
	 'khii': u'\u0d16\u0d40',
	 'gii': u'\u0d17\u0d40',
	 'ghii': u'\u0d18\u0d40',
	 'ngii': u'\u0d19\u0d40',
	 'chii': u'\u0d1a\u0d40',
	 'chhii': u'\u0d1b\u0d40',
	 'jii': u'\u0d1c\u0d40',
	 'jhii': u'\u0d1d\u0d40',
	 'njii': u'\u0d1e\u0d40',
	 'tii': u'\u0d1f\u0d40',
	 'ttii': u'\u0d20\u0d40',
	 'dii': u'\u0d21\u0d40',
	 'ddii': u'\u0d22\u0d40',
	 'nhii': u'\u0d23\u0d40',
	 'thii': u'\u0d24\u0d40',
	 'tthii': u'\u0d25\u0d40',
	 'dhii': u'\u0d26\u0d40',
	 'ddhii': u'\u0d27\u0d40',
	 'nii': u'\u0d28\u0d40',
	 'pii': u'\u0d2a\u0d40',
	 'phii': u'\u0d2b\u0d40',
	 'bii': u'\u0d2c\u0d40',
	 'bhii': u'\u0d2d\u0d40',
	 'mii': u'\u0d2e\u0d40',
	 'yii': u'\u0d2f\u0d40',
	 'rii': u'\u0d30\u0d40',
	 'rrii': u'\u0d31\u0d40',
	 'lii': u'\u0d32\u0d40',
	 'llii': u'\u0d33\u0d40',
	 'vii': u'\u0d35\u0d40',
	 'shii': u'\u0d36\u0d40',
	 'ssii': u'\u0d37\u0d40',
	 'sii': u'\u0d38\u0d40',
	 'hii': u'\u0d39\u0d40',
	 'zhii': u'\u0d34\u0d40',
	 'ku': u'\u0d15\u0d41',
	 'khu': u'\u0d16\u0d41',
	 'gu': u'\u0d17\u0d41',
	 'ghu': u'\u0d18\u0d41',
	 'ngu': u'\u0d19\u0d41',
	 'chu': u'\u0d1a\u0d41',
	 'chhu': u'\u0d1b\u0d41',
	 'ju': u'\u0d1c\u0d41',
	 'jhu': u'\u0d1d\u0d41',
	 'nju': u'\u0d1e\u0d41',
	 'tu': u'\u0d1f\u0d41',
	 'ttu': u'\u0d20\u0d41',
	 'du': u'\u0d21\u0d41',
	 'ddu': u'\u0d22\u0d41',
	 'nhu': u'\u0d23\u0d41',
	 'thu': u'\u0d24\u0d41',
	 'tthu': u'\u0d25\u0d41',
	 'dhu': u'\u0d26\u0d41',
	 'ddhu': u'\u0d27\u0d41',
	 'nu': u'\u0d28\u0d41',
	 'pu': u'\u0d2a\u0d41',
	 'phu': u'\u0d2b\u0d41',
	 'bu': u'\u0d2c\u0d41',
	 'bhu': u'\u0d2d\u0d41',
	 'mu': u'\u0d2e\u0d41',
	 'yu': u'\u0d2f\u0d41',
	 'ru': u'\u0d30\u0d41',
	 'rru': u'\u0d31\u0d41',
	 'lu': u'\u0d32\u0d41',
	 'llu': u'\u0d33\u0d41',
	 'vu': u'\u0d35\u0d41',
	 'shu': u'\u0d36\u0d41',
	 'ssu': u'\u0d37\u0d41',
	 'su': u'\u0d38\u0d41',
	 'hu': u'\u0d39\u0d41',
	 'zhu': u'\u0d34\u0d41',
	 'kuu': u'\u0d15\u0d42',
	 'khuu': u'\u0d16\u0d42',
	 'guu': u'\u0d17\u0d42',
	 'ghuu': u'\u0d18\u0d42',
	 'nguu': u'\u0d19\u0d42',
	 'chuu': u'\u0d1a\u0d42',
	 'chhuu': u'\u0d1b\u0d42',
	 'juu': u'\u0d1c\u0d42',
	 'jhuu': u'\u0d1d\u0d42',
	 'njuu': u'\u0d1e\u0d42',
	 'tuu': u'\u0d1f\u0d42',
	 'ttuu': u'\u0d20\u0d42',
	 'duu': u'\u0d21\u0d42',
	 'dduu': u'\u0d22\u0d42',
	 'nhuu': u'\u0d23\u0d42',
	 'thuu': u'\u0d24\u0d42',
	 'tthuu': u'\u0d25\u0d42',
	 'dhuu': u'\u0d26\u0d42',
	 'ddhuu': u'\u0d27\u0d42',
	 'nuu': u'\u0d28\u0d42',
	 'puu': u'\u0d2a\u0d42',
	 'phuu': u'\u0d2b\u0d42',
	 'buu': u'\u0d2c\u0d42',
	 'bhuu': u'\u0d2d\u0d42',
	 'muu': u'\u0d2e\u0d42',
	 'yuu': u'\u0d2f\u0d42',
	 'ruu': u'\u0d30\u0d42',
	 'rruu': u'\u0d31\u0d42',
	 'luu': u'\u0d32\u0d42',
	 'lluu': u'\u0d33\u0d42',
	 'vuu': u'\u0d35\u0d42',
	 'shuu': u'\u0d36\u0d42',
	 'ssuu': u'\u0d37\u0d42',
	 'suu': u'\u0d38\u0d42',
	 'huu': u'\u0d39\u0d42',
	 'zhuu': u'\u0d34\u0d42',
	 'ke': u'\u0d46\u0d15',
	 'khe': u'\u0d46\u0d16',
	 'ge': u'\u0d46\u0d17',
	 'ghe': u'\u0d46\u0d18',
	 'nge': u'\u0d46\u0d19',
	 'che': u'\u0d46\u0d1a',
	 'chhe': u'\u0d46\u0d1b',
	 'je': u'\u0d46\u0d1c',
	 'jhe': u'\u0d46\u0d1d',
	 'nje': u'\u0d46\u0d1e',
	 'te': u'\u0d46\u0d1f',
	 'tte': u'\u0d46\u0d20',
	 'de': u'\u0d46\u0d21',
	 'dde': u'\u0d46\u0d22',
	 'nhe': u'\u0d46\u0d23',
	 'the': u'\u0d46\u0d24',
	 'tthe': u'\u0d46\u0d25',
	 'dhe': u'\u0d46\u0d26',
	 'ddhe': u'\u0d46\u0d27',
	 'ne': u'\u0d46\u0d28',
	 'pe': u'\u0d46\u0d2a',
	 'phe': u'\u0d46\u0d2b',
	 'be': u'\u0d46\u0d2c',
	 'bhe': u'\u0d46\u0d2d',
	 'me': u'\u0d46\u0d2e',
	 'ye': u'\u0d46\u0d2f',
	 're': u'\u0d46\u0d30',
	 'rre': u'\u0d46\u0d31',
	 'le': u'\u0d46\u0d32',
	 'lle': u'\u0d46\u0d33',
	 've': u'\u0d46\u0d35',
	 'she': u'\u0d46\u0d36',
	 'sse': u'\u0d46\u0d37',
	 'se': u'\u0d46\u0d38',
	 'he': u'\u0d46\u0d39',
	 'zhe': u'\u0d46\u0d34',
	 'kee': u'\u0d47\u0d15',
	 'khee': u'\u0d47\u0d16',
	 'gee': u'\u0d47\u0d17',
	 'ghee': u'\u0d47\u0d18',
	 'ngee': u'\u0d47\u0d19',
	 'chee': u'\u0d47\u0d1a',
	 'chhee': u'\u0d47\u0d1b',
	 'jee': u'\u0d47\u0d1c',
	 'jhee': u'\u0d47\u0d1d',
	 'njee': u'\u0d47\u0d1e',
	 'tee': u'\u0d47\u0d1f',
	 'ttee': u'\u0d47\u0d20',
	 'dee': u'\u0d47\u0d21',
	 'ddee': u'\u0d47\u0d22',
	 'nhee': u'\u0d47\u0d23',
	 'thee': u'\u0d47\u0d24',
	 'tthee': u'\u0d47\u0d25',
	 'dhee': u'\u0d47\u0d26',
	 'ddhee': u'\u0d47\u0d27',
	 'nee': u'\u0d47\u0d28',
	 'pee': u'\u0d47\u0d2a',
	 'phee': u'\u0d47\u0d2b',
	 'bee': u'\u0d47\u0d2c',
	 'bhee': u'\u0d47\u0d2d',
	 'mee': u'\u0d47\u0d2e',
	 'yee': u'\u0d47\u0d2f',
	 'ree': u'\u0d47\u0d30',
	 'rree': u'\u0d47\u0d31',
	 'lee': u'\u0d47\u0d32',
	 'llee': u'\u0d47\u0d33',
	 'vee': u'\u0d47\u0d35',
	 'shee': u'\u0d47\u0d36',
	 'ssee': u'\u0d47\u0d37',
	 'see': u'\u0d47\u0d38',
	 'hee': u'\u0d47\u0d39',
	 'zhee': u'\u0d47\u0d34',
	 'kai': u'\u0d48\u0d15',
	 'khai': u'\u0d48\u0d16',
	 'gai': u'\u0d48\u0d17',
	 'ghai': u'\u0d48\u0d18',
	 'ngai': u'\u0d48\u0d19',
	 'chai': u'\u0d48\u0d1a',
	 'chhai': u'\u0d48\u0d1b',
	 'jai': u'\u0d48\u0d1c',
	 'jhai': u'\u0d48\u0d1d',
	 'njai': u'\u0d48\u0d1e',
	 'tai': u'\u0d48\u0d1f',
	 'ttai': u'\u0d48\u0d20',
	 'dai': u'\u0d48\u0d21',
	 'ddai': u'\u0d48\u0d22',
	 'nhai': u'\u0d48\u0d23',
	 'thai': u'\u0d48\u0d24',
	 'tthai': u'\u0d48\u0d25',
	 'dhai': u'\u0d48\u0d26',
	 'ddhai': u'\u0d48\u0d27',
	 'nai': u'\u0d48\u0d28',
	 'pai': u'\u0d48\u0d2a',
	 'phai': u'\u0d48\u0d2b',
	 'bai': u'\u0d48\u0d2c',
	 'bhai': u'\u0d48\u0d2d',
	 'mai': u'\u0d48\u0d2e',
	 'yai': u'\u0d48\u0d2f',
	 'rai': u'\u0d48\u0d30',
	 'rrai': u'\u0d48\u0d31',
	 'lai': u'\u0d48\u0d32',
	 'llai': u'\u0d48\u0d33',
	 'vai': u'\u0d48\u0d35',
	 'shai': u'\u0d48\u0d36',
	 'ssai': u'\u0d48\u0d37',
	 'sai': u'\u0d48\u0d38',
	 'hai': u'\u0d48\u0d39',
	 'zhai': u'\u0d48\u0d34',
	 'ko': u'\u0d46\u0d15\u0d3e',
	 'kho': u'\u0d46\u0d16\u0d3e',
	 'go': u'\u0d46\u0d17\u0d3e',
	 'gho': u'\u0d46\u0d18\u0d3e',
	 'ngo': u'\u0d46\u0d19\u0d3e',
	 'cho': u'\u0d46\u0d1a\u0d3e',
	 'chho': u'\u0d46\u0d1b\u0d3e',
	 'jo': u'\u0d46\u0d1c\u0d3e',
	 'jho': u'\u0d46\u0d1d\u0d3e',
	 'njo': u'\u0d46\u0d1e\u0d3e',
	 'to': u'\u0d46\u0d1f\u0d3e',
	 'tto': u'\u0d46\u0d20\u0d3e',
	 'do': u'\u0d46\u0d21\u0d3e',
	 'ddo': u'\u0d46\u0d22\u0d3e',
	 'nho': u'\u0d46\u0d23\u0d3e',
	 'tho': u'\u0d46\u0d24\u0d3e',
	 'ttho': u'\u0d46\u0d25\u0d3e',
	 'dho': u'\u0d46\u0d26\u0d3e',
	 'ddho': u'\u0d46\u0d27\u0d3e',
	 'no': u'\u0d46\u0d28\u0d3e',
	 'po': u'\u0d46\u0d2a\u0d3e',
	 'pho': u'\u0d46\u0d2b\u0d3e',
	 'bo': u'\u0d46\u0d2c\u0d3e',
	 'bho': u'\u0d46\u0d2d\u0d3e',
	 'mo': u'\u0d46\u0d2e\u0d3e',
	 'yo': u'\u0d46\u0d2f\u0d3e',
	 'ro': u'\u0d46\u0d30\u0d3e',
	 'rro': u'\u0d46\u0d31\u0d3e',
	 'lo': u'\u0d46\u0d32\u0d3e',
	 'llo': u'\u0d46\u0d33\u0d3e',
	 'vo': u'\u0d46\u0d35\u0d3e',
	 'sho': u'\u0d46\u0d36\u0d3e',
	 'sso': u'\u0d46\u0d37\u0d3e',
	 'so': u'\u0d46\u0d38\u0d3e',
	 'ho': u'\u0d46\u0d39\u0d3e',
	 'zho': u'\u0d46\u0d34\u0d3e',
	 'koo': u'\u0d47\u0d15\u0d3e',
	 'khoo': u'\u0d47\u0d16\u0d3e',
	 'goo': u'\u0d47\u0d17\u0d3e',
	 'ghoo': u'\u0d47\u0d18\u0d3e',
	 'ngoo': u'\u0d47\u0d19\u0d3e',
	 'choo': u'\u0d47\u0d1a\u0d3e',
	 'chhoo': u'\u0d47\u0d1b\u0d3e',
	 'joo': u'\u0d47\u0d1c\u0d3e',
	 'jhoo': u'\u0d47\u0d1d\u0d3e',
	 'njoo': u'\u0d47\u0d1e\u0d3e',
	 'too': u'\u0d47\u0d1f\u0d3e',
	 'ttoo': u'\u0d47\u0d20\u0d3e',
	 'doo': u'\u0d47\u0d21\u0d3e',
	 'ddoo': u'\u0d47\u0d22\u0d3e',
	 'nhoo': u'\u0d47\u0d23\u0d3e',
	 'thoo': u'\u0d47\u0d24\u0d3e',
	 'tthoo': u'\u0d47\u0d25\u0d3e',
	 'dhoo': u'\u0d47\u0d26\u0d3e',
	 'ddhoo': u'\u0d47\u0d27\u0d3e',
	 'noo': u'\u0d47\u0d28\u0d3e',
	 'poo': u'\u0d47\u0d2a\u0d3e',
	 'phoo': u'\u0d47\u0d2b\u0d3e',
	 'boo': u'\u0d47\u0d2c\u0d3e',
	 'bhoo': u'\u0d47\u0d2d\u0d3e',
	 'moo': u'\u0d47\u0d2e\u0d3e',
	 'yoo': u'\u0d47\u0d2f\u0d3e',
	 'roo': u'\u0d47\u0d30\u0d3e',
	 'rroo': u'\u0d47\u0d31\u0d3e',
	 'loo': u'\u0d47\u0d32\u0d3e',
	 'lloo': u'\u0d47\u0d33\u0d3e',
	 'voo': u'\u0d47\u0d35\u0d3e',
	 'shoo': u'\u0d47\u0d36\u0d3e',
	 'ssoo': u'\u0d47\u0d37\u0d3e',
	 'soo': u'\u0d47\u0d38\u0d3e',
	 'hoo': u'\u0d47\u0d39\u0d3e',
	 'zhoo': u'\u0d47\u0d34\u0d3e',
         'aM':u'\u0d05\u0d02',
	 'km': u'\u0d15\u0d02',
	 'khm': u'\u0d16\u0d02',
	 'gm': u'\u0d17\u0d02',
	 'ghm': u'\u0d18\u0d02',
	 'ngm': u'\u0d19\u0d02',
	 'chm': u'\u0d1a\u0d02',
	 'chhm': u'\u0d1b\u0d02',
	 'jm': u'\u0d1c\u0d02',
	 'jhm': u'\u0d1d\u0d02',
	 'njm': u'\u0d1e\u0d02',
	 'tm': u'\u0d1f\u0d02',
	 'ttm': u'\u0d20\u0d02',
	 'dm': u'\u0d21\u0d02',
	 'ddm': u'\u0d22\u0d02',
	 'nhm': u'\u0d23\u0d02',
	 'thm': u'\u0d24\u0d02',
	 'tthm': u'\u0d25\u0d02',
	 'dhm': u'\u0d26\u0d02',
	 'ddhm': u'\u0d27\u0d02',
	 'nm': u'\u0d28\u0d02',
	 'pm': u'\u0d2a\u0d02',
	 'phm': u'\u0d2b\u0d02',
	 'bm': u'\u0d2c\u0d02',
	 'bhm': u'\u0d2d\u0d02',
	 'mm': u'\u0d2e\u0d02',
	 'ym': u'\u0d2f\u0d02',
	 'rm': u'\u0d30\u0d02',
	 'rrm': u'\u0d31\u0d02',
	 'lm': u'\u0d32\u0d02',
	 'llm': u'\u0d33\u0d02',
	 'vm': u'\u0d35\u0d02',
	 'shm': u'\u0d36\u0d02',
	 'ssm': u'\u0d37\u0d02',
	 'sm': u'\u0d38\u0d02',
	 'hm': u'\u0d39\u0d02',
	 'zhm': u'\u0d34\u0d02',
	 'kow': u'\u0d15\u0d57',
	 'ka': u'\u0d15',
	 'khow': u'\u0d16\u0d57',
	 'kha': u'\u0d16',
	 'gow': u'\u0d17\u0d57',
	 'ga': u'\u0d17',
	 'ghow': u'\u0d18\u0d57',
	 'gha': u'\u0d18',
	 'ngow': u'\u0d19\u0d57',
	 'nga': u'\u0d19',
	 'chow': u'\u0d1a\u0d57',
	 'cha': u'\u0d1a',
	 'chhow': u'\u0d1b\u0d57',
	 'chha': u'\u0d1b',
	 'jow': u'\u0d1c\u0d57',
	 'ja': u'\u0d1c',
	 'jhow': u'\u0d1d\u0d57',
	 'jha': u'\u0d1d',
	 'njow': u'\u0d1e\u0d57',
	 'nja': u'\u0d1e',
	 'tow': u'\u0d1f\u0d57',
	 'ta': u'\u0d1f',
	 'ttow': u'\u0d20\u0d57',
	 'tta': u'\u0d20',
	 'dow': u'\u0d21\u0d57',
	 'da': u'\u0d21',
	 'ddow': u'\u0d22\u0d57',
	 'dda': u'\u0d22',
	 'nhow': u'\u0d23\u0d57',
	 'nha': u'\u0d23',
	 'thow': u'\u0d24\u0d57',
	 'tha': u'\u0d24',
	 'tthow': u'\u0d25\u0d57',
	 'ttha': u'\u0d25',
	 'dhow': u'\u0d26\u0d57',
	 'dha': u'\u0d26',
	 'ddhow': u'\u0d27\u0d57',
	 'ddha': u'\u0d27',
	 'now': u'\u0d28\u0d57',
	 'na': u'\u0d28',
	 'pow': u'\u0d2a\u0d57',
	 'pa': u'\u0d2a',
	 'phow': u'\u0d2b\u0d57',
	 'pha': u'\u0d2b',
	 'bow': u'\u0d2c\u0d57',
	 'ba': u'\u0d2c',
	 'bhow': u'\u0d2d\u0d57',
	 'bha': u'\u0d2d',
	 'mow': u'\u0d2e\u0d57',
	 'ma': u'\u0d2e',
	 'yow': u'\u0d2f\u0d57',
	 'ya': u'\u0d2f',
	 'row': u'\u0d30\u0d57',
	 'ra': u'\u0d30',
	 'rrow': u'\u0d31\u0d57',
	 'rra': u'\u0d31',
	 'low': u'\u0d32\u0d57',
	 'la': u'\u0d32',
	 'llow': u'\u0d33\u0d57',
	 'lla': u'\u0d33',
	 'vow': u'\u0d35\u0d57',
	 'va': u'\u0d35',
	 'show': u'\u0d36\u0d57',
	 'sha': u'\u0d36',
	 'ssow': u'\u0d37\u0d57',
	 'ssa': u'\u0d37',
	 'sow': u'\u0d38\u0d57',
	 'sa': u'\u0d38',
	 'how': u'\u0d39\u0d57',
	 'ha': u'\u0d39',
	 'zhow': u'\u0d34\u0d57',
	 'zha': u'\u0d34',
	'L': u'\u0d7d',
         'ttt':u'\u0d1f\u0d4d\u0d1f\u0d4d',
	 'ttti':u'\u0d1f\u0d4d\u0d1f\u0d3f',
	'ttto':u'\u0d1f\u0d4d\u0d1f\u0d4a',
         'ppa':u'\u0d2a\u0d4d\u0d2a',
          'chch':u'\u0d1a\u0d4d\u0d1a',
          'kka':u'\u0d15\u0d4d\u0d15',
	  'ngnga':u'\u0d19\u0d4d\u0d19',
		'ngngi':u'\u0d19\u0d4d\u0d19\u0d3f',
           'swa':u'\u0d38\u0d4d\u0d35\u0d3e',
           'dhra':u'\u0d26\u0d4d\u0d30',
	   'kra':u'\u0d15\u0d4d\u0d30',
	   'gra':u'\u0d17\u0d4d\u0d30',
	   'thra':u'\u0d24\u0d4d\u0d30',
	 'dhhra':u'\u0d27\u0d4d\u0d30',
          'pra':u'\u0d2a\u0d4d\u0d30',
           'bra':u'\u0d2c\u0d4d\u0d30',
           'bhra':u'\u0d2d\u0d4d\u0d30',
           'mra':u'\u0d2e\u0d4d\u0d30',
	'hra':u'\u0d39\u0d4d\u0d30',
	'shra':u'\u0d27\u0d4d\u0d30',
	'sra':u'\u0d28\u0d4d\u0d30',
	'AM':u'\u0d02',
	'LL':u'\u0d7e',
	'NH':u'\u0d7a',
        'N':u'\u0d7b',
	'R':u'\u0d7c',
	'nna':u'\u0d6c',
	'nn':u'\u0d6c\u0d4d',
	'nni':u'\u0d6c\u0d3f',
	'nnaa':u'\u0d6c\u0d3e',
	'nnii':u'\u0d6c\u0d40',
	'nnu':u'\u0d6c\u0d41',
	'nnuu':u'\u0d6c\u0d42',
	'nne':u'\u0d46\u0d6c',
	'nnee':u'\u0d47\u0d6c',
	'nno':u'\u0d46\u0d6c\u0d3e',
	'nnoo':u'\u0d47\u0d6c\u0d3e',
	'nnm':u'\u0d6c\u0d02',

	 'kr': u'\u0d15\u0d43',
	 'khr': u'\u0d16\u0d43',
	 'gr': u'\u0d17\u0d43',
	 'ghr': u'\u0d18\u0d43',
	 'chr': u'\u0d1a\u0d43',
	 'chhr': u'\u0d1b\u0d43',
	 'jr': u'\u0d1c\u0d43',
	 'jhr': u'\u0d1d\u0d43',
	
	 'thr': u'\u0d24\u0d43',
	 'dhr': u'\u0d26\u0d43',
	 'ddhr': u'\u0d27\u0d43',
	 'nr': u'\u0d28\u0d43',
	 'pr': u'\u0d2a\u0d43',
	 
	 'mr': u'\u0d2e\u0d43',
	 'yr': u'\u0d2f\u0d43',
	 'll': u'\u0d33\u0d4d',
	 'vr': u'\u0d35\u0d43',
	 'shr': u'\u0d36\u0d43',
	 'ssr': u'\u0d37\u0d43',
	 'sr': u'\u0d38\u0d43',
	 'hr': u'\u0d39\u0d43'
	 
	
         }
#******************************************************** 
temp=""
flag=0
def convert(value):
	global temp
	global flag
	
	b=[]
	malayalam=""
	
	j=0
	no=1
	
	d=value.split()	
	for k in range(len(d)):
		l=len(d[k])
		print l
		i=0
		no=0
		pl=5
		
		while(i<=l):
			
			p=d[k][i:pl]
			print p
			if " " in p:
				if i<pl:
					print "true"
					
					pl=pl-1
					temp=temp+malayalam
					flag=1
					malayalam=malayalam+" "	
				else: 
					i=i+1
							
	
			elif p in dict1:
				malayalam=malayalam+dict1[p].encode('UTF-8')
				#print malayalam
				i=pl
				pl=pl+5
				no=no+1
	
			elif pl>0:			
				pl=pl-1
			else:
				print "n=",no
				d[k]=d[k][no:]
				l-=1
				i=0
				pl=5
				no=0
		malayalam=malayalam+" "
		
		
			

			
	j=j+1
	'''
	if flag==1:
		
		flag=0
		return temp+" "+malayalam

	else:
		return temp+malayalam
	'''
	return malayalam
	

#*****************************************************************************************
def OnKeyPress(event):
	value = event.widget.get()
	print len(value),"  ",value
	if (ord(value[len(value)-1])>64 and ord(value[len(value)-1])<91)  or (ord(value[len(value)-1])>96 and ord(value[len(value)-1])<123):
		m=convert(value)
		print ord(value[len(value)-1])
		
		
	
		string=m
		status.configure(text=string)

	else:
		print "problem"



def display_in_lab():
	f=open("output","r")
	text=f.read().split("\n")
	f.close()	
	global tg
	global tx
	ts=[]
	s=""
	for i in range(len(text)):
		if not text[i]=="":
			tx.append(text[i].decode('utf-8'))
			tx[i].split()

			tg.append(tx[i].split()[1])
			ts.append(tx[i].split()[0])
	for i in range(len(tx)):
		s=s+ tx[i]+"\n"
	status_op.configure(text=s)
def display_in_lab2(s):
	
	f=open("output","r")
	text=f.read().split("\n")
	f.close()	
	global tg
	global tx
	ts=[]
	tg=[]
	tx=[]
	for i in range(len(text)):
		if not text[i]=="":
			tx.append(text[i].decode('utf-8'))
			tx[i].split()

			tg.append(tx[i].split()[1])
			ts.append(tx[i].split()[0])
	print ts
	print "s=", len(s),"  ts=",len(ts)

	a=""
	for j in range(len(s)):
		k=""
		for i in range(len(s[j])):
			k=k+s[j][i]+", "
		k=k[:-1]
		print k

		a=a+"["+k+"....]   "+ts[j] +"\n"
	status_op.configure(text=a)
	ts=[]
	s=[[]]
	

def browse_cmd():
	file_path=browse()
	r.set(file_path)
	string=read_file(file_path)
	status.configure(text=string)
	print file_path
def tagg():
	string1= status.cget("text")
	xx=r1.get()
	path=r.get()
	if not xx=="" and not path=="":
		tkMessageBox.showinfo("Input Error", "You cannot enter into both fields:")
		r.set("")
		r1.set("")
	elif not xx=="":
		read_in_text(string1)
		tnt_tagging()
		in_file_tagging()
		display_in_lab()
	elif not path=="":
		string=read_in_file(path)
		
		tnt_tagging()
		in_file_tagging()
		display_in_lab()	
	return
def trasfer():
	string1= status.cget("text")
	path=r.get()
	xx=r1.get()
	if not xx=="" and not path=="":
		tkMessageBox.showinfo("Input Error", "You cannot enter into both fields:")
		r.set("")
		r1.set("")
	elif not xx=="":
		read_in_text(string1)
		tnt_tagging()
		in_file_tagging()
		tx=create_KB_tag_lst()
		s=create_KB_sub_obj(tx)
		display_in_lab2(s)
	elif not path=="":
		string=read_in_file(path)

		tnt_tagging()
		in_file_tagging()
		tx=create_KB_tag_lst()
		print tx
		s=create_KB_sub_obj(tx)
		display_in_lab2(s)	
	return

root = Tkinter.Tk()
root.geometry('950x400+200+200')
widget = Tkinter.Label(root)
root.configure(bg='white')
r=StringVar()
r1=StringVar()
l1v=StringVar()
l2v=StringVar()
entry1 = Tkinter.Entry(root, width=30, name="entry1",xscrollcommand=30,textvariable=r)
entry2 = Tkinter.Entry(root, width=30, name="entry2",xscrollcommand=30,textvariable=r1)
#entry3 = Tkinter.Entry(root, name="entry3")

#entry1.bindtags(('.entry1', 'Entry', '.', 'all'))
#entry2.bindtags(('Entry', '.entry1', '.', 'all'))
#entry3.bindtags(('.entry1','Entry','post-class-bindings', '.', 'all'))

#btlabel1 = Tkinter.Label(text="bindtags: %s" % " ".join(entry1.bindtags()))
#btlabel2 = Tkinter.Label(text="bindtags: %s" % " ".join(entry2.bindtags()))
#btlabel3 = Tkinter.Label(text="bindtags: %s" % " ".join(entry3.bindtags()))
btlabel1 = Tkinter.Label(text="Enter file path", bg='white',fg='black')
btlabel1.grid(row=3, column=10 ,columnspan=5)
btlabel2 = Tkinter.Label(text="Enter text", bg='white',fg='black')
btlabel2.grid(row=4, column=10 ,columnspan=5)
cmdBrowse = Tkinter.Button(text="Browse",width=5,height=1,command = browse_cmd, bg='blue',fg='black')

status = Tkinter.Label(wraplength=200,width=30,pady=3,padx=3,anchor="w",bg='white',fg='black')
status_op = Tkinter.Label(wraplength=300,width=30,pady=3,padx=3,anchor="w",bg='white',fg='red')
cmdtagg = Tkinter.Button(text="Tagging",width=5,command = tagg, bg='blue',fg='black')
cmdtrans = Tkinter.Button(text="Interlingua",width=7,command = trasfer, bg='blue',fg='black')
btlabel3 = Tkinter.Label(text="NEWS PAPER ARTICLE TEXT SUMMARIZER FOR MALAYALAM", bg='red',fg='black')
btlabel3.grid(row=0, column=100 ,columnspan=5)
entry1.grid(row=3,column=40)
entry2.grid(row=4,column=40, sticky='EW')
cmdBrowse.grid(row=3,column=90)
cmdtagg.grid(row=6,column=260)
cmdtrans.grid(row=6,column=360)
status.grid(row=13,column=40, columnspan=2, sticky='EW')
status_op.grid(row=13,column=460, columnspan=2, sticky='E')
#btlabel1.grid(row=0,column=1, padx=10, sticky="w")
#entry2.grid(row=1,column=0)
#btlabel2.grid(row=1,column=1, padx=10, sticky="w")
#entry3.grid(row=2,column=0)
#btlabel3.grid(row=2,column=1, padx=10)
#status.grid(row=3, columnspan=2, sticky="w")
#entry1.bind("<KeyPress>", OnKeyPress)
entry2.bind("<KeyPress>", OnKeyPress)
#entry3.bind_class("post-class-bindings", "<KeyPress>", OnKeyPress)
root.mainloop()
