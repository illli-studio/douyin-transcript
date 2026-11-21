# douyin-transcript

本机把抖音口播转成文字。贴一条分享链接，下载音频后用 SenseVoiceSmall 识别，不需要云端语音密钥。

页面只监听 `127.0.0.1:18088`。

## 准备

需要 Python 3.12。

```bash
git clone https://github.com/illli-studio/douyin-transcript.git
cd douyin-transcript
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e '.[web]' 'mcp<2' 'funasr==1.2.7' 'modelscope==1.29.0' 'torch==2.8.0' 'torchaudio==2.8.0' 'numpy<2'
```

首次启动会下载 SenseVoiceSmall，大约 900 MB，放在 `models/`。

## 启动

```bash
HOST=127.0.0.1 PORT=18088 python web/app.py
```

打开 http://127.0.0.1:18088 ，粘贴整段分享文案或短链，然后点「提取文案」。

识别通常要一两分钟。结果可以复制，也可以下载为 Markdown。

## 说明

- 语音识别在本机运行，不需要硅基流动或百炼密钥。
- 模型和下载缓存不进入 Git。
- 下载依赖本机浏览器登录态，cookie 保存在 `~/.douyin-cookies.json`，不要提交。

基于 [yzfly/douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) 修改，原项目使用 Apache License 2.0。
