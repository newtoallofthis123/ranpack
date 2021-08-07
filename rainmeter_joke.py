from pathlib import Path
import pyjokes
joke = pyjokes.get_joke()
home_dir = Path.home()
ini_path = f'{home_dir}/Documents/Rainmeter/Skins/RanPack/joke/joke.ini'
file = open(ini_path, 'w')
content = f'[Rainmeter]\nUpdate=1000\n\n[Metadata]\nName=Quote\nAuthor=NoobScience\nInformation=Shows a Quote on the screen\nLicense=MIT\nVersion=1.0.0\n\n[Style]\nFontFace=Cascadia Code\nFontColor=255, 255, 255\nAntiAlias=1\n\n[QuoteMeter]\nMeter=String\nText={joke}\nMeterStyle=Style\nFontSize=12\nToolTipText=Joke'
file.write(content)
file.close()
