from preprocess_ncirar import utils 

__version__ = '0.0.1'

def get_wordcount(x):
	return utils._get_wordcount(x)

def get_charcount(x):
	return utils._get_charcount(x)

def get_avgwordlen(x):
	return utils._get_avgwordlen(x)

def get_stopwordscount(x)
	return utils._get_stopwordscount(x)

def get_hashtagcount(x):
	return utils._get_hashtagcount(x)

def get_mentioncount(x):
	return utils._get_mentioncount(x)

def get_digitcount(x):
	return utils._get_digitcount(x)

def get_uppercasecount(x):
	return utils._get_uppercasecount(x)

def get_cont_exp(x):
	return utils._get_cont_exp(x)

def get_lowercase(x):
	return utils._get_lowercase(x)

def get_emails(x):
	return utils._get_emails(x)

def remove_emails(x):
	return utils._remove_emails(x)

def get_urls(x):
	return utils._get_urls(x)

def remove_urls(x):
	return utils._remove_urls(x)

def remove_rts(x):
	return utils._remove_rts(x)

def remove_specialchars(x):
	return utils._remove_specialchars(x)

def remove_htmls(x):
	return utils._remove_htmls(x)

def remove_accentchars(x):
	return utils._remove_accentchars(x)

def remove_stopwords(x):
	return utils._remove_stopwords(x)

def convert_tobase(x):
	return utils._convert_tobase(x)

def remove_commonwords(x, n=20):
	return utils._remove_commonwords(x, n=20)

def remove_rarewords(x, n=20):
	return utils._remove_rarewords(x, n=20)

def spelling_correction(x):
	return utils._spelling_correction(x)