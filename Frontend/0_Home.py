import i18n
import streamlit as st

from utils.init import init_once


if __name__ == '__main__':
    # Init
    init_once()

    # Show title
    st.title("원영적 사고를 해보자")

    # Show page description
    st.write("단순한 긍정적 사고를 넘어선, 초월적인 긍정적 사고\n\n장원영의 원영적 사고를 배워보자!")

    # Show github link
    st.write(f'* Github: {"https://github.com/Cubane0120/my-mobilex-project-team-10"}')
