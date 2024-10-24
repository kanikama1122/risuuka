# Streamlitライブラリをインポート
import streamlit as st
import random


def main():
    st.title("今日の自己啓発アプリ")
    st.write("名前を入力して自己啓発してください")

name = st.text_input('あなたの名前を入力してください')



jikokeihatu =["スマホばかり見るな",
              "勉強しないとまずいって",
              "厳しいって",
              ]
if st.button("自己啓発をする"):
    if name:
        random.seed(name)
        jikokeihatu =random.choice(jikokeihatu)
        st.write({jikokeihatu})
    else:
        st.write("名前を入力してください")

if __name__=="__main__":
    main()            
