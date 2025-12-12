import streamlit as st
# 修改标签页的文字和图标
st.set_page_config(page_title="相册", page_icon="🐾")
st.title("我的相册")

# 如果内存中没有ind，才需要设置为0，否则不要设置ind
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

images = [
    {
        'url': "https://img1.baidu.com/it/u=2528176158,3706650567&fm=253&fmt=auto&app=138&f=JPEG?w=1200&h=800",
        'text': '猫'
    },
    {
        'url': "https://pic.616pic.com/photoone/00/02/40/618cf416207693898.jpg!/fw/1120",
        'text': 'dog'
    },
    {
        'url': "https://img95.699pic.com/photo/60017/6146.jpg_wh860.jpg",
        'text': 'lion'
    }
]

# url:图片的地址 caption:图片注释介绍
st.image(images[st.session_state['ind']]['url'], caption=images[st.session_state['ind']]['text'])

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)

# 分列容器 课本110页
c1, c2 = st.columns(2)
with c1:
    st.button("上一张", on_click=prevImg, use_container_width=True)
with c2:
    # 按钮 课本73页
    st.button("下一张", on_click=nextImg, use_container_width=True)
