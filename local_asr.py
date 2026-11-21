from pathlib import Path
import re
import threading

MODEL_DIR = Path('/Users/elham/douyin-mcp-server/models/iic/SenseVoiceSmall')
_model = None
_lock = threading.Lock()


def transcribe(audio_path) -> str:
    """Transcribe an audio file with the local SenseVoice model."""
    global _model
    with _lock:
        if _model is None:
            from funasr import AutoModel
            _model = AutoModel(model=str(MODEL_DIR), disable_update=True)
        result = _model.generate(
            input=str(audio_path),
            language='zh',
            use_itn=True,
            batch_size_s=60,
        )
    text = result[0].get('text', '') if result else ''
    text = re.sub(r'<\|[^|]*\|>', '', text).strip()
    return text or '未识别到文本内容'
