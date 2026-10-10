# 🤖 AI 聊天机器人（ai-chatbot）

你的第一个 AI 作品：一个带对话记忆的网页聊天机器人，DeepSeek 驱动，输入问题即答。

## ✨ 功能

- 网页聊天界面，输入问题点击"发送"即回答
- **记住对话历史**：多轮聊天有上下文，AI 知道你前面说过什么
- API Key 存在 Streamlit Secrets 里，**不写进代码**（不会随仓库泄露）

## 🚀 本地运行

```bash
pip install -r requirements.txt
streamlit run app.py
```

> 运行前需配置 Secrets：在 `.streamlit/secrets.toml` 里写入 `DEEPSEEK_API_KEY = "你的Key"`（该文件已被 .gitignore 拦截，不会上传）

## 🛠 技术栈

Python · Streamlit（界面与会话状态）· DeepSeek API（OpenAI 兼容接口）
