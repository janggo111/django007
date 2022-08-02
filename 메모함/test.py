16일차


# pip : pypi.org 에서 다른 개발자들이 개발해놓은 코드를 가져다 사용할 수 있도록 만든 프로그램

# import : 다른 파일의 클래스, 함수, 변수를 가져다 사용할 수 있도록 만든 구문!!

import googletrans
from googletrans import Translator

# print(googletrans.LANGUAGES)

text1 = "Hello welcome to my website!"
translator = Translator()
trans1 = translator.translate(text1, src='en', dest='ja')
print("English to Japanese: ", trans1.text)

d = {1:"one", 2:"two", 3:"three"}
d.items()
dict_items([(1:"one"), (2:"two"), (3:"three")])
# 키 밸류 조합 튜플들의 리스트
# 이방법으로만 템플렛에서 딕셔너리 사용 가능

a, b = 1, 2
a
1
b
2


for k, v in d.items():
    print(k, v)

1 one
2 two
3 three



fr 이 있을 때
    전송되는 나라코드에 맞춰 selected

fr 이 없을 때
    나라코드가 ~일 때 selected



17일차

TTS : 문자열을 읽어주는 라이브러리

from gtts import gTTS
tts = gTTS('hello')
tts.save('hello.mp3')