import streamlit as st
from openai import OpenAI

# 从 Streamlit 安全存储中读取 API Key（不是写在代码里！）
client = OpenAI(
    api_key=st.secrets["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"
)

# 页面标题
st.title("🤖 AI 聊天机器人")

# 对话历史
if "history" not in st.session_state:
    st.session_state.history = []

# 显示之前的对话
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.write(f"**你：** {msg['content']}")
    else:
        st.write(f"**AI：** {msg['content']}")

# 输入框
user_input = st.text_input("请输入你的问题：")

# 按钮
if st.button("发送"):
    if user_input:
        st.session_state.history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=st.session_state.history
        )
        answer = response.choices[0].message.content

        st.session_state.history.append({"role": "assistant", "content": answer})
        st.rerun()
    else:
        st.write("请先输入问题哦～")
