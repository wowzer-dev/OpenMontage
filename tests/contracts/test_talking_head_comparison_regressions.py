from pathlib import Path

from tools.video.remotion_caption_burn import RemotionCaptionBurn


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_caption_words_use_a_visible_css_gap() -> None:
    source = (REPO_ROOT / "remotion-composer/src/components/CaptionOverlay.tsx").read_text()

    assert "marginRight:" in source
    assert 'wordSeparator === " "' in source
    assert '? "0.28em"' in source


def test_talking_head_supports_fade_through_black_and_source_duration() -> None:
    talking_head = (REPO_ROOT / "remotion-composer/src/TalkingHead.tsx").read_text()
    root = (REPO_ROOT / "remotion-composer/src/Root.tsx").read_text()

    assert "transitions?: TalkingHeadTransition[]" in talking_head
    assert "fade_through_black" in talking_head
    assert "calculateTalkingHeadMetadata" in talking_head
    assert "props.durationSeconds" in talking_head
    assert "calculateMetadata={calculateTalkingHeadMetadata}" in root


def test_caption_burn_parses_first_nonempty_probe_line() -> None:
    assert RemotionCaptionBurn._first_nonempty_line("\n1080x1920\n\n1080x1920\n") == "1080x1920"


def test_caption_burn_static_file_path_omits_public_prefix() -> None:
    source = (REPO_ROOT / "tools/video/remotion_caption_burn.py").read_text()

    assert '"videoSrc": f"talking-head/{video_filename}"' in source
    assert '"videoSrc": f"public/talking-head/{video_filename}"' not in source


def test_video_compose_stages_talking_head_video_src() -> None:
    source = (REPO_ROOT / "tools/video/video_compose.py").read_text()

    assert 'media_keys = {"source", "src", "backgroundSrc", "videoSrc"}' in source
