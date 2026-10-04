# 平方根影片素材

八上2-1基礎概念｜2026-10-04｜六段、4:26.792、47段字幕的已完成案例素材。

來源課本04-115國中數學2上-課本-2-1-學用(115f231559).pdf，PDF5–8／14–17頁（課本58–61／67–70）。旁白、例題與動畫構想自編；未附課本或原帳號影片。

narration.json供腳本改作，captions.srt和timeline.json是原版本時間資料，quiz_questions.json／quiz_answers.json分離。若重製語音或修改腳本，必須重新對齊並驗證SRT，不能沿用時間就當同步。

給其他使用者的預設語音工具為 **edge-tts**，請依[影片語音與字幕流程](../../docs/影片語音與字幕.md)先生成台灣華語短段，核對後再製作完整影片。需要 Python 與網路，不要求 GPU 或 VoxCPM2。可用 `python -m pip install edge-tts` 安裝，透過 `edge-tts --list-voices` 確認語音，再以 `edge-tts --voice zh-TW-HsiaoChenNeural --text "旁白文字" --write-media narration.mp3` 產生音檔。字幕時間須依新音軌重算。

原案例製作環境：Python＋Pillow動畫、FFmpeg、Windows繁體字型、本機VoxCPM2聲音、large-v3 ASR輔助核對。VoxCPM2 僅是作者已安裝環境的選配；這些環境與音軌未隨repo安裝。

可給Codex：「讀這份旁白，先幫我做六段分鏡與短預覽；說明你的可用工具。製作後先完成字幕文字、自然斷句、同步、缺字和最終影片QA，再準備YouTube上傳和CC。」
