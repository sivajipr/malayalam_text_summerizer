import Tkinter
#import nltk
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
	 'ke': u'\u0d15\u0d46',
	 'khe': u'\u0d16\u0d46',
	 'ge': u'\u0d17\u0d46',
	 'ghe': u'\u0d18\u0d46',
	 'nge': u'\u0d19\u0d46',
	 'che': u'\u0d1a\u0d46',
	 'chhe': u'\u0d1b\u0d46',
	 'je': u'\u0d1c\u0d46',
	 'jhe': u'\u0d1d\u0d46',
	 'nje': u'\u0d1e\u0d46',
	 'te': u'\u0d1f\u0d46',
	 'tte': u'\u0d20\u0d46',
	 'de': u'\u0d21\u0d46',
	 'dde': u'\u0d22\u0d46',
	 'nhe': u'\u0d23\u0d46',
	 'the': u'\u0d24\u0d46',
	 'tthe': u'\u0d25\u0d46',
	 'dhe': u'\u0d26\u0d46',
	 'ddhe': u'\u0d27\u0d46',
	 'ne': u'\u0d28\u0d46',
	 'pe': u'\u0d2a\u0d46',
	 'phe': u'\u0d2b\u0d46',
	 'be': u'\u0d2c\u0d46',
	 'bhe': u'\u0d2d\u0d46',
	 'me': u'\u0d2e\u0d46',
	 'ye': u'\u0d2f\u0d46',
	 're': u'\u0d30\u0d46',
	 'rre': u'\u0d31\u0d46',
	 'le': u'\u0d32\u0d46',
	 'lle': u'\u0d33\u0d46',
	 've': u'\u0d35\u0d46',
	 'she': u'\u0d36\u0d46',
	 'sse': u'\u0d37\u0d46',
	 'se': u'\u0d38\u0d46',
	 'he': u'\u0d39\u0d46',
	 'zhe': u'\u0d34\u0d46',
	 'kee': u'\u0d15\u0d47',
	 'khee': u'\u0d16\u0d47',
	 'gee': u'\u0d17\u0d47',
	 'ghee': u'\u0d18\u0d47',
	 'ngee': u'\u0d19\u0d47',
	 'chee': u'\u0d1a\u0d47',
	 'chhee': u'\u0d1b\u0d47',
	 'jee': u'\u0d1c\u0d47',
	 'jhee': u'\u0d1d\u0d47',
	 'njee': u'\u0d1e\u0d47',
	 'tee': u'\u0d1f\u0d47',
	 'ttee': u'\u0d20\u0d47',
	 'dee': u'\u0d21\u0d47',
	 'ddee': u'\u0d22\u0d47',
	 'nhee': u'\u0d23\u0d47',
	 'thee': u'\u0d24\u0d47',
	 'tthee': u'\u0d25\u0d47',
	 'dhee': u'\u0d26\u0d47',
	 'ddhee': u'\u0d27\u0d47',
	 'nee': u'\u0d28\u0d47',
	 'pee': u'\u0d2a\u0d47',
	 'phee': u'\u0d2b\u0d47',
	 'bee': u'\u0d2c\u0d47',
	 'bhee': u'\u0d2d\u0d47',
	 'mee': u'\u0d2e\u0d47',
	 'yee': u'\u0d2f\u0d47',
	 'ree': u'\u0d30\u0d47',
	 'rree': u'\u0d31\u0d47',
	 'lee': u'\u0d32\u0d47',
	 'llee': u'\u0d33\u0d47',
	 'vee': u'\u0d35\u0d47',
	 'shee': u'\u0d36\u0d47',
	 'ssee': u'\u0d37\u0d47',
	 'see': u'\u0d38\u0d47',
	 'hee': u'\u0d39\u0d47',
	 'zhee': u'\u0d34\u0d47',
	 'kai': u'\u0d15\u0d48',
	 'khai': u'\u0d16\u0d48',
	 'gai': u'\u0d17\u0d48',
	 'ghai': u'\u0d18\u0d48',
	 'ngai': u'\u0d19\u0d48',
	 'chai': u'\u0d1a\u0d48',
	 'chhai': u'\u0d1b\u0d48',
	 'jai': u'\u0d1c\u0d48',
	 'jhai': u'\u0d1d\u0d48',
	 'njai': u'\u0d1e\u0d48',
	 'tai': u'\u0d1f\u0d48',
	 'ttai': u'\u0d20\u0d48',
	 'dai': u'\u0d21\u0d48',
	 'ddai': u'\u0d22\u0d48',
	 'nhai': u'\u0d23\u0d48',
	 'thai': u'\u0d24\u0d48',
	 'tthai': u'\u0d25\u0d48',
	 'dhai': u'\u0d26\u0d48',
	 'ddhai': u'\u0d27\u0d48',
	 'nai': u'\u0d28\u0d48',
	 'pai': u'\u0d2a\u0d48',
	 'phai': u'\u0d2b\u0d48',
	 'bai': u'\u0d2c\u0d48',
	 'bhai': u'\u0d2d\u0d48',
	 'mai': u'\u0d2e\u0d48',
	 'yai': u'\u0d2f\u0d48',
	 'rai': u'\u0d30\u0d48',
	 'rrai': u'\u0d31\u0d48',
	 'lai': u'\u0d32\u0d48',
	 'llai': u'\u0d33\u0d48',
	 'vai': u'\u0d35\u0d48',
	 'shai': u'\u0d36\u0d48',
	 'ssai': u'\u0d37\u0d48',
	 'sai': u'\u0d38\u0d48',
	 'hai': u'\u0d39\u0d48',
	 'zhai': u'\u0d34\u0d48',
	 'ko': u'\u0d15\u0d4a',
	 'kho': u'\u0d16\u0d4a',
	 'go': u'\u0d17\u0d4a',
	 'gho': u'\u0d18\u0d4a',
	 'ngo': u'\u0d19\u0d4a',
	 'cho': u'\u0d1a\u0d4a',
	 'chho': u'\u0d1b\u0d4a',
	 'jo': u'\u0d1c\u0d4a',
	 'jho': u'\u0d1d\u0d4a',
	 'njo': u'\u0d1e\u0d4a',
	 'to': u'\u0d1f\u0d4a',
	 'tto': u'\u0d20\u0d4a',
	 'do': u'\u0d21\u0d4a',
	 'ddo': u'\u0d22\u0d4a',
	 'nho': u'\u0d23\u0d4a',
	 'tho': u'\u0d24\u0d4a',
	 'ttho': u'\u0d25\u0d4a',
	 'dho': u'\u0d26\u0d4a',
	 'ddho': u'\u0d27\u0d4a',
	 'no': u'\u0d28\u0d4a',
	 'po': u'\u0d2a\u0d4a',
	 'pho': u'\u0d2b\u0d4a',
	 'bo': u'\u0d2c\u0d4a',
	 'bho': u'\u0d2d\u0d4a',
	 'mo': u'\u0d2e\u0d4a',
	 'yo': u'\u0d2f\u0d4a',
	 'ro': u'\u0d30\u0d4a',
	 'rro': u'\u0d31\u0d4a',
	 'lo': u'\u0d32\u0d4a',
	 'llo': u'\u0d33\u0d4a',
	 'vo': u'\u0d35\u0d4a',
	 'sho': u'\u0d36\u0d4a',
	 'sso': u'\u0d37\u0d4a',
	 'so': u'\u0d38\u0d4a',
	 'ho': u'\u0d39\u0d4a',
	 'zho': u'\u0d34\u0d4a',
	 'koo': u'\u0d15\u0d4b',
	 'khoo': u'\u0d16\u0d4b',
	 'goo': u'\u0d17\u0d4b',
	 'ghoo': u'\u0d18\u0d4b',
	 'ngoo': u'\u0d19\u0d4b',
	 'choo': u'\u0d1a\u0d4b',
	 'chhoo': u'\u0d1b\u0d4b',
	 'joo': u'\u0d1c\u0d4b',
	 'jhoo': u'\u0d1d\u0d4b',
	 'njoo': u'\u0d1e\u0d4b',
	 'too': u'\u0d1f\u0d4b',
	 'ttoo': u'\u0d20\u0d4b',
	 'doo': u'\u0d21\u0d4b',
	 'ddoo': u'\u0d22\u0d4b',
	 'nhoo': u'\u0d23\u0d4b',
	 'thoo': u'\u0d24\u0d4b',
	 'tthoo': u'\u0d25\u0d4b',
	 'dhoo': u'\u0d26\u0d4b',
	 'ddhoo': u'\u0d27\u0d4b',
	 'noo': u'\u0d28\u0d4b',
	 'poo': u'\u0d2a\u0d4b',
	 'phoo': u'\u0d2b\u0d4b',
	 'boo': u'\u0d2c\u0d4b',
	 'bhoo': u'\u0d2d\u0d4b',
	 'moo': u'\u0d2e\u0d4b',
	 'yoo': u'\u0d2f\u0d4b',
	 'roo': u'\u0d30\u0d4b',
	 'rroo': u'\u0d31\u0d4b',
	 'loo': u'\u0d32\u0d4b',
	 'lloo': u'\u0d33\u0d4b',
	 'voo': u'\u0d35\u0d4b',
	 'shoo': u'\u0d36\u0d4b',
	 'ssoo': u'\u0d37\u0d4b',
	 'soo': u'\u0d38\u0d4b',
	 'hoo': u'\u0d39\u0d4b',
	 'zhoo': u'\u0d34\u0d4b',
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
	'R':u'\u0d7c'}
#******************************************************** 
temp=""
flag=0
def convert(value):
	global temp
	global flag
	#dict1['k']=u'\u0d15\u0d3e'
	#dict1['a']=u'\u0d3e'
	#dict1['T']=u'\u0d7b'
	#print dict1
	b=[]
	malayalam=""
	#f=open("maldict","w")
	#f.write("aaa")
	j=0
	no=1
	#if d[0]=='a'or'e'or'i' or 'o' or 'u'
	#b[0].append(d[0])
	#print dict1
	#print b
	#print dict1[d]
	d=value.split()	
	for k in range(len(d)):
		l=len(d[k])
		print l
		i=0
		no=0
		pl=5
		#f.write(str(no)+" ")
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
	#f.write("\n")
	#print b

#*****************************************************************************************
def OnKeyPress(event):
	value = event.widget.get()
	if (ord(value[len(value)-1])>64 and ord(value[len(value)-1])<91)  or (ord(value[len(value)-1])>96 and ord(value[len(value)-1])<123):
		m=convert(value)
		print ord(value[len(value)-1])
	#string="value of %s is '%s'" % (event.widget._name, value)
		string=m
		status.configure(text=string)
	else:
		print "problem"

root = Tkinter.Tk()

entry1 = Tkinter.Entry(root, name="entry1")
entry2 = Tkinter.Entry(root, name="entry2")
entry3 = Tkinter.Entry(root, name="entry3")

entry1.bindtags(('.entry1', 'Entry', '.', 'all'))
entry2.bindtags(('Entry', '.entry1', '.', 'all'))
entry3.bindtags(('.entry1','Entry','post-class-bindings', '.', 'all'))

btlabel1 = Tkinter.Label(text="bindtags: %s" % " ".join(entry1.bindtags()))
btlabel2 = Tkinter.Label(text="bindtags: %s" % " ".join(entry2.bindtags()))
btlabel3 = Tkinter.Label(text="bindtags: %s" % " ".join(entry3.bindtags()))
status = Tkinter.Label(anchor="w")

entry1.grid(row=0,column=0)
btlabel1.grid(row=0,column=1, padx=10, sticky="w")
entry2.grid(row=1,column=0)
btlabel2.grid(row=1,column=1, padx=10, sticky="w")
entry3.grid(row=2,column=0)
btlabel3.grid(row=2,column=1, padx=10)
status.grid(row=3, columnspan=2, sticky="w")
entry1.bind("<KeyPress>", OnKeyPress)
entry2.bind("<KeyPress>", OnKeyPress)
entry3.bind_class("post-class-bindings", "<KeyPress>", OnKeyPress)
root.mainloop()
