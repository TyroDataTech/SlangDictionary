from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from fuzzywuzzy import fuzz
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#slang = input("Enter muhavara/slang:")
def searchDict(slang):
	slang = slang.lower()
	slang_dev = transliterate(slang, sanscript.ITRANS, sanscript.DEVANAGARI)
	df = pd.read_csv("database.csv")
	ratio = []
	for x in df["Muhavara"]:
		ratio.append(fuzz.ratio(slang_dev,x))
	df_new = pd.DataFrame({"Muhavara":df["Muhavara"],"Meaning":df["Meaning"],"Example":df["Example"],"Matching Ratio":ratio})
	df_new = df_new.sort_values(by="Matching Ratio",ascending=False)
	print(df_new.head())
	return df_new.head()
x = searchDict("mar mitna")
