import pandas as pd

df = pd.read_csv("gk_questions/rail-gk.csv")

for index, row in df.iterrows():
    print(index, row)
    break











































# import requests
# from bs4 import BeautifulSoup
#
# try:
#     r = requests.get("https://gk-hindi.in", params={'address': "kolkata"})
#     print("hi")
#     soup = BeautifulSoup(r.content, 'html.parser')
#     print(soup)
#     x = soup.find_all("a", class_="list-group-item")
#     print(x)
#     # for t in x:
#     #     soup2 = BeautifulSoup(str(t), 'html.parser')
#     #     p = soup2.find('a')
#     #     print(p.attrs)
# except Exception as e:
#     print(e)
# ff = [
#     ["india-gk", 66],
#     ["world-gk", 23],
#     ["gk-questions", 48],
#     ["gk-quiz", 36],
#     ["biology-gk", 71],
#     ["science-gk", 37],
#     ["physics-gk", 124],
#     ["chemistry-gk", 121],
#     ["general-awareness", 12],
#     ["computer-gk", 52],
#     ["political-gk", 42],
#     ["economics-gk", 1],
#     ["history-gk", 1],
#     ["sports-gk", 1],
#     ["geography-gk", 1],
#     ["teaching-aptitude-in-hindi", 1],
#     ["ctet-gk-in-hindi", 1],
#     ["bed-entrance-gk-in-hindi", 1],
#     ["bank-gk", 1],
#     ["ssc-gk-in-hindi", 1],
#     ["rail-gk", 1],
#     ["upsc-gk-in-hindi", 1],
#     ["indian-army-gk-in-hindi", 1],
#     ["hindi-grammar-gk", 1],
#     ["hindi-grammar-mcq", 1],
#     ["reasoning-in-hindi", 1],
#     ["bihar-gk-in-hindi", 1],
#     ["rajasthan-gk-in-hindi", 1],
#     ["jharkhand-gk-in-hindi", 1],
#     ["mp-gk-in-hindi", 1],
#     ["up-gk-in-hindi", 1],
#     ["chhattisgarh-gk-in-hindi", 1],
#     ["haryana-gk-in-hindi", 1],
#     ["himachal-pradesh-gk-in-hindi", 1],
#     ["electronics-gk-in-hindi", 1],
#     ["agriculture-gk", 1],
#     ["current-affairs-2018-in-hindi", 1],
#     ["current-affairs-2019-in-hindi", 1],
#     ["math-gk", 1],
#     ["states-capitals-gk", 1],
#     ["kbc-gk-in-hindi", 1],
#     ["bollywood-gk", 1],
#     ["ramayan-gk", 1],
#     ["author-name", 1],
#     ["computer-in-hindi", 1], ]

















# from moviepy.editor import TextClip
# for x in TextClip.list("font"):
#     print(x)

# Courier
# Helvetica-Narrow-BoldOblique
# AvantGarde-Book
# AvantGarde-BookOblique
# AvantGarde-Demi
# AvantGarde-DemiOblique
# Bookman-Demi
# Bookman-DemiItalic
# Bookman-Light
# Bookman-LightItalic
# Courier-Bold
# Courier-BoldOblique
# Courier-Oblique
# fixed
# Helvetica
# Helvetica-Bold
# Helvetica-BoldOblique
# Helvetica-Narrow
# Helvetica-Narrow-Bold
# Helvetica-Narrow-Oblique
# Helvetica-Oblique
# NewCenturySchlbk-Bold
# NewCenturySchlbk-BoldItalic
# NewCenturySchlbk-Italic
# NewCenturySchlbk-Roman
# Palatino-Bold
# Palatino-BoldItalic
# Palatino-Italic
# Palatino-Roman
# Symbol
# Times-Bold
# Times-BoldItalic
# Times-Italic
# Times-Roman
# aakar
# Abyssinica-SIL
# Ani
# AnjaliOldLipi
# Bitstream-Charter
# Bitstream-Charter-Bold
# Bitstream-Charter-Bold-Italic
# Bitstream-Charter-Italic
# C059-BdIta
# C059-Bold
# C059-Bold-Italic
# C059-Italic
# C059-Roman
# Century-Schoolbook-L-Bold
# Century-Schoolbook-L-Bold-Italic
# Century-Schoolbook-L-Italic
# Century-Schoolbook-L-Roman
# Chandas
# Chilanka-Regular
# Courier-10-Pitch
# Courier-10-Pitch-Bold
# Courier-10-Pitch-Bold-Italic
# Courier-10-Pitch-Italic
# D050000L
# DejaVu-Sans
# DejaVu-Sans-Bold
# DejaVu-Sans-Bold-Oblique
# DejaVu-Sans-Condensed
# DejaVu-Sans-Condensed-Bold
# DejaVu-Sans-Condensed-Bold-Oblique
# DejaVu-Sans-Condensed-Oblique
# DejaVu-Sans-ExtraLight
# DejaVu-Sans-Mono
# DejaVu-Sans-Mono-Bold
# DejaVu-Sans-Mono-Bold-Oblique
# DejaVu-Sans-Mono-Oblique
# DejaVu-Sans-Oblique
# DejaVu-Serif
# DejaVu-Serif-Bold
# DejaVu-Serif-Bold-Italic
# DejaVu-Serif-Condensed
# DejaVu-Serif-Condensed-Bold
# DejaVu-Serif-Condensed-Bold-Italic
# DejaVu-Serif-Condensed-Italic
# DejaVu-Serif-Italic
# DejaVuMathTeXGyre-Regular
# Devanagari-MT
# Devanagari-MT-Bold
# Dhurjati
# Dingbats
# Droid-Sans-Fallback
# Dyuthi
# FreeMono
# FreeMono-Bold
# FreeMono-Bold-Oblique
# FreeMono-Oblique
# FreeSans
# FreeSans-Bold
# FreeSans-Bold-Oblique
# FreeSans-Oblique
# FreeSerif
# FreeSerif-Bold
# FreeSerif-Bold-Italic
# FreeSerif-Italic
# Gargi
# Garuda
# Garuda-Bold
# Garuda-Bold-Oblique
# Garuda-Oblique
# Gayathri
# Gayathri-Bold
# Gayathri-Regular
# Gentium
# Gentium-Basic
# Gentium-Basic-Bold
# Gentium-Basic-Bold-Italic
# Gentium-Basic-Italic
# Gentium-Book-Basic
# Gentium-Book-Basic-Bold
# Gentium-Book-Basic-Bold-Italic
# Gentium-Book-Basic-Italic
# Gentium-Italic
# GentiumAlt
# GentiumAlt-Italic
# Gidugu
# Gubbi
# Gurajada
# Jamrul
# KacstArt
# KacstBook
# KacstDecorative
# KacstDigital
# KacstFarsi
# KacstLetter
# KacstNaskh
# KacstOffice
# KacstOne
# KacstOne-Bold
# KacstPen
# KacstPoster
# KacstQurn
# KacstScreen
# KacstTitle
# KacstTitleL
# Kalapi
# Kalimati
# Karumbi
# Keraleeyam-Regular
# Khmer-OS
# Khmer-OS-System
# Kinnari
# Kinnari-Bold
# Kinnari-Bold-Italic
# Kinnari-Bold-Oblique
# Kinnari-Italic
# Kinnari-Oblique
# Kruti-Dev-010
# LakkiReddy
# Laksaman
# Laksaman-Bold
# Laksaman-Bold-Italic
# Laksaman-Italic
# Liberation-Mono
# Liberation-Mono-Bold
# Liberation-Mono-Bold-Italic
# Liberation-Mono-Italic
# Liberation-Sans
# Liberation-Sans-Bold
# Liberation-Sans-Bold-Italic
# Liberation-Sans-Italic
# Liberation-Sans-Narrow
# Liberation-Sans-Narrow-Bold
# Liberation-Sans-Narrow-Bold-Italic
# Liberation-Sans-Narrow-Italic
# Liberation-Serif
# Liberation-Serif-Bold
# Liberation-Serif-Bold-Italic
# Liberation-Serif-Italic
# Likhan
# LKLUG
# Lohit-Assamese
# Lohit-Bengali
# Lohit-Devanagari
# Lohit-Gujarati
# Lohit-Gurmukhi
# Lohit-Kannada
# Lohit-Malayalam
# Lohit-Odia
# Lohit-Tamil
# Lohit-Tamil-Classical
# Lohit-Telugu
# Loma
# Loma-Bold
# Loma-Bold-Oblique
# Loma-Oblique
# Mallanna
# Mandali
# Manjari
# Manjari-Bold
# Manjari-Thin
# Meera
# Mitra-Mono
# mry_KacstQurn
# Mukti
# Mukti-Bold
# Nakula
# NATS
# Navilu
# Nimbus-Mono-L
# Nimbus-Mono-L-Bold
# Nimbus-Mono-L-Bold-Oblique
# Nimbus-Mono-L-Regular-Oblique
# Nimbus-Mono-PS
# Nimbus-Mono-PS-Bold
# Nimbus-Mono-PS-Bold-Italic
# Nimbus-Mono-PS-Italic
# Nimbus-Roman
# Nimbus-Roman-Bold
# Nimbus-Roman-Bold-Italic
# Nimbus-Roman-Italic
# Nimbus-Roman-No9-L
# Nimbus-Roman-No9-L-Medium
# Nimbus-Roman-No9-L-Medium-Italic
# Nimbus-Roman-No9-L-Regular-Italic
# Nimbus-Sans
# Nimbus-Sans-Bold
# Nimbus-Sans-Bold-Italic
# Nimbus-Sans-Italic
# Nimbus-Sans-L
# Nimbus-Sans-L-Bold
# Nimbus-Sans-L-Bold-Condensed
# Nimbus-Sans-L-Bold-Condensed-Italic
# Nimbus-Sans-L-Bold-Italic
# Nimbus-Sans-L-Regular-Condensed
# Nimbus-Sans-L-Regular-Condensed-Italic
# Nimbus-Sans-L-Regular-Italic
# Nimbus-Sans-Narrow
# Nimbus-Sans-Narrow-Bold
# Nimbus-Sans-Narrow-Bold-Oblique
# Nimbus-Sans-Narrow-Oblique
# NimbusMonoPS-Bold
# NimbusMonoPS-BoldItalic
# NimbusMonoPS-Italic
# NimbusMonoPS-Regular
# NimbusRoman-Bold
# NimbusRoman-BoldItalic
# NimbusRoman-Italic
# NimbusRoman-Regular
# NimbusSans-Bold
# NimbusSans-BoldItalic
# NimbusSans-Italic
# NimbusSans-Regular
# NimbusSansNarrow-Bold
# NimbusSansNarrow-BoldOblique
# NimbusSansNarrow-Oblique
# NimbusSansNarrow-Regular
# Norasi
# Norasi-Bold
# Norasi-Bold-Italic
# Norasi-Bold-Oblique
# Norasi-Italic
# Norasi-Oblique
# Noto-Color-Emoji
# Noto-Mono
# Noto-Sans-CJK-HK
# Noto-Sans-CJK-HK-Bold
# Noto-Sans-CJK-JP
# Noto-Sans-CJK-JP-Bold
# Noto-Sans-CJK-KR
# Noto-Sans-CJK-KR-Bold
# Noto-Sans-CJK-SC
# Noto-Sans-CJK-SC-Bold
# Noto-Sans-CJK-TC
# Noto-Sans-CJK-TC-Bold
# Noto-Sans-Mono-Bold
# Noto-Sans-Mono-CJK-HK
# Noto-Sans-Mono-CJK-HK-Bold
# Noto-Sans-Mono-CJK-JP
# Noto-Sans-Mono-CJK-JP-Bold
# Noto-Sans-Mono-CJK-KR
# Noto-Sans-Mono-CJK-KR-Bold
# Noto-Sans-Mono-CJK-SC
# Noto-Sans-Mono-CJK-SC-Bold
# Noto-Sans-Mono-CJK-TC
# Noto-Sans-Mono-CJK-TC-Bold
# Noto-Sans-Mono-Regular
# Noto-Serif-CJK-HK
# Noto-Serif-CJK-HK-Bold
# Noto-Serif-CJK-JP
# Noto-Serif-CJK-JP-Bold
# Noto-Serif-CJK-KR
# Noto-Serif-CJK-KR-Bold
# Noto-Serif-CJK-SC
# Noto-Serif-CJK-SC-Bold
# Noto-Serif-CJK-TC
# Noto-Serif-CJK-TC-Bold
# NTR
# OpenSymbol
# ori1Uni-Medium
# P052-Bold
# P052-Bold-Italic
# P052-BoldItalic
# P052-Italic
# P052-Roman
# Padauk
# Padauk-Bold
# Padauk-Book
# Padauk-Book-Bold
# padmaa
# padmaa-Bold.1.1
# padmaa-normal-indictrans
# Pagul
# Peddana-Regular
# Phetsarath-OT
# Ponnala
# Pothana2000
# Potti-Sreeramulu
# Purisa
# Purisa-Bold
# Purisa-Bold-Oblique
# Purisa-Oblique
# Rachana
# RaghuMalayalamSans-Regular
# Ramabhadra
# Ramaraja-Regular
# Rasa-Bold
# Rasa-Light
# Rasa-Medium
# Rasa-Regular
# Rasa-SemiBold
# RaviPrakash
# Rekha
# Saab
# Sahadeva
# Samanata
# Samyak-Devanagari
# Samyak-Gujarati
# Samyak-Malayalam
# Samyak-Tamil
# Sarai
# Sawasdee
# Sawasdee-Bold
# Sawasdee-Bold-Oblique
# Sawasdee-Oblique
# Sree-Krushnadevaraya
# Standard-Symbols-L
# Standard-Symbols-PS
# Suranna
# Suravaram
# Suruma
# Syamala-Ramana
# TenaliRamakrishna
# Tibetan_Machine_Uni
# Timmana
# Tlwg-Mono
# Tlwg-Mono-Bold
# Tlwg-Mono-Bold-Oblique
# Tlwg-Mono-Oblique
# Tlwg-Typewriter
# Tlwg-Typewriter-Bold
# Tlwg-Typewriter-Bold-Oblique
# Tlwg-Typewriter-Oblique
# Tlwg-Typist
# Tlwg-Typist-Bold
# Tlwg-Typist-Bold-Oblique
# Tlwg-Typist-Oblique
# Tlwg-Typo
# Tlwg-Typo-Bold
# Tlwg-Typo-Bold-Oblique
# Tlwg-Typo-Oblique
# Ubuntu
# Ubuntu-Bold
# Ubuntu-Bold-Italic
# Ubuntu-Condensed
# Ubuntu-Italic
# Ubuntu-Light
# Ubuntu-Light-Italic
# Ubuntu-Medium
# Ubuntu-Medium-Italic
# Ubuntu-Mono
# Ubuntu-Mono-Bold
# Ubuntu-Mono-Bold-Italic
# Ubuntu-Mono-Italic
# Ubuntu-Thin
# Umpush
# Umpush-Bold
# Umpush-Bold-Oblique
# Umpush-Light
# Umpush-Light-Oblique
# Umpush-Oblique
# Uroob-Regular
# URW-Bookman-Demi
# URW-Bookman-Demi-Italic
# URW-Bookman-L-Demi-Bold
# URW-Bookman-L-Demi-Bold-Italic
# URW-Bookman-L-Light
# URW-Bookman-L-Light-Italic
# URW-Bookman-Light
# URW-Bookman-Light-Italic
# URW-Chancery-L-Medium-Italic
# URW-Gothic-Book
# URW-Gothic-Book-Oblique
# URW-Gothic-Demi
# URW-Gothic-Demi-Oblique
# URW-Gothic-L-Book
# URW-Gothic-L-Book-Oblique
# URW-Gothic-L-Demi
# URW-Gothic-L-Demi-Oblique
# URW-Palladio-L-Bold
# URW-Palladio-L-Bold-Italic
# URW-Palladio-L-Italic
# URW-Palladio-L-Roman
# URWBookman-Demi
# URWBookman-DemiItalic
# URWBookman-Light
# URWBookman-LightItalic
# URWGothic-Book
# URWGothic-BookOblique
# URWGothic-Demi
# URWGothic-DemiOblique
# Vemana2000
# Waree
# Waree-Bold
# Waree-Bold-Oblique
# Waree-Oblique
# Yrsa-Bold
# Yrsa-Bold-Italic
# Yrsa-Italic
# Yrsa-Light
# Yrsa-Light-Italic
# Yrsa-Medium
# Yrsa-Medium-Italic
# Yrsa-Regular
# Yrsa-SemiBold
# Yrsa-SemiBold-Italic
# Z003-Medium-Italic
# Z003-MediumItalic
