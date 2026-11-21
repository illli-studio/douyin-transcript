import asyncio
import re
from pathlib import Path

from local_asr import transcribe


async def extract_with_working_method(share_text: str) -> dict:
    """Use the verified browser-download and local-ASR workflow."""
    import importlib.util
    module_path = '/Users/elham/.hermes/skills/douyin-downloader/scripts/pipeline.py'
    spec = importlib.util.spec_from_file_location('douyin_pipeline_skill', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    urls = re.findall(r'https?://[^\s]+', share_text)
    if not urls:
        raise ValueError('未找到有效的分享链接')
    short_url = urls[0]
    import requests
    response = requests.get(short_url, allow_redirects=True, timeout=20)
    match = re.search(r'/video/(\d+)', response.url)
    if not match:
        raise ValueError('无法解析抖音视频 ID')
    video_url = f'https://www.douyin.com/video/{match.group(1)}'
    videos = await module.scrape_single_video(video_url)
    if not videos:
        raise RuntimeError('无法获取视频信息')
    video = videos[0]
    work = Path('/Users/elham/douyin-mcp-server/work')
    work.mkdir(exist_ok=True)
    audio = work / f"{video['video_id']}.mp3"
    ok = await module.download_with_retry(video_url, audio, asyncio.Semaphore(1))
    if not ok:
        raise RuntimeError('音频下载失败')
    text = await asyncio.to_thread(transcribe, audio)
    return {
        'success': True,
        'video_id': video['video_id'],
        'title': video['title'],
        'text': text,
        'download_url': video_url,
        'error': '',
    }
