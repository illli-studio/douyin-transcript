# 本机抖音口播转文字

贴一条抖音分享链接，下载音频，再用本机的 SenseVoiceSmall 转成文字。页面只开在 `127.0.0.1:18088`，不需要云端语音密钥。

## 安装

需要 Python 3.12。

```bash
git clone https://github.com/illli-studio/douyin-transcript.git
cd douyin-transcript
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e '.[web]' 'mcp<2' 'funasr==1.2.7' 'modelscope==1.29.0' 'torch==2.8.0' 'torchaudio==2.8.0' 'numpy<2'
```

第一次启动会下载 SenseVoiceSmall。模型约 900 MB，放在 `models/`，不进入 Git。

## 启动页面

```bash
HOST=127.0.0.1 PORT=18088 python web/app.py
```

打开 http://127.0.0.1:18088 。

1. 把整段分享文案，或一条 `https://v.douyin.com/` 短链，贴进输入框。
2. 点「提取文案」。程序先取视频编号，再下载音频，最后在本机转写。
3. 结果出现后，复制文字，或下载 Markdown。

一条视频通常要一两分钟。

## 不提交的文件

- `models/`：SenseVoiceSmall 模型。
- `work/`：下载下来的音频。
- `~/.douyin-cookies.json`：下载时使用的浏览器登录态。

## 来源

代码改自 [yzfly/douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)。原项目使用 Apache License 2.0。
