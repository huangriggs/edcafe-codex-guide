# Edcafe × Codex 教學操作指南

讓Codex根據你的教學需求，協助選擇Edcafe工具、準備素材、操作網站、核對內容及測試回應。這套公開教材整理了一天的真實合作：10題數學測驗 → 網站操作索引 → 12工具教學顧問指南 → 原創影片與影片測驗 → 概念補救Chatbot。

**適用：** 繁體中文教師；國中數學案例可改成其他學科。**版本：** 1.0.1，實測基準2026-10-04。**性質：** 社群教學指南，非Edcafe或OpenAI官方產品、API、CLI或自動登入工具。

## 下載後，先把這段貼給Codex

```text
請先讀這個repo的AGENTS.md、README.md、教學指南.md，以及skills/edcafe-operations/SKILL.md。
依我的教學目標，幫我選一個主要Edcafe方案，包含素材、提示詞、操作路徑和完成檢核。
先確認你有沒有可用的瀏覽器控制能力；有的話檢查目前畫面，登入由我自行完成。
要製作時請完成保存與重開核對，不只給建議。未要求公開的教材儲存Private。
分開說明已實測、只確認介面和未完成部分，並更新我的專案交接檔。
我的需求是：【填年級／科目／章節、學生主要困難、活動時間與希望產出的教材】。
```

例如：「八上平方根，學生把√25寫成±5，要做10分鐘概念補救，請先建立Chatbot並用合成對話測試。」

## 三種使用方式

1. **整個repo當工作區：** GitHub Code→Download ZIP→解壓縮→Codex開啟此資料夾，貼上啟動提示。
2. **放進既有專案：** 把本套件放在`工具/edcafe-codex-guide/`，在原AGENTS.md追加指向本指南的段落，保留原規則。不要覆蓋既有AGENTS.md。
3. **選配安裝skill：** 將`skills/edcafe-operations/`整個資料夾複製到自己的Codex skills位置；例如使用預設位置的Windows使用者為`%USERPROFILE%\.codex\skills\`。若已存在同名技能先比較、合併，不覆蓋。重新開啟對話後是否自動發現依環境而定；也可直接要求Codex讀本地SKILL.md，不需安裝。

Codex實際是否能操作網站，取決於使用者環境的瀏覽器工具、登入狀態和Edcafe方案。本repo不會安裝瀏覽器工具、購買訂閱或授予權限；只有文字／CLI環境時，可由Codex引導你逐步操作。

## 導覽

| 需求 | 文件 |
|---|---|
| 從登入到教材完成 | [教學指南](教學指南.md) |
| 今天整段合作歷程、決策和結果 | [對話實作紀錄](docs/對話實作紀錄.md) |
| 快速找按鈕、路徑和已知欄位 | [操作索引](skills/edcafe-operations/references/操作索引.md) |
| 12工具設計卡、8種課堂方案 | [教學顧問指南](skills/edcafe-operations/references/教學顧問指南.md) |
| 遇到卡住、字幕、選項或Chatbot偏離 | [困難與注意事項](docs/困難與注意事項.md) |
| 命題、影片與補救指示範例 | [案例目錄](examples/README.md) |
| 如何在自己專案維護經驗 | [專案接手與索引維護](docs/專案接手與索引維護.md) |
| 公開包來源、驗證和未測界限 | [發布驗證](docs/發布驗證.md) |

**已實作：** Quiz建立／校對／Private保存／重開；原創影片＋YouTube CC＋五題影片測驗；Chatbot建立與教師Preview試聊。**尚未完整驗證：** 正式學生交卷／評分、一般Quiz三模式、Word下載、語音／白板等；完整矩陣見顧問指南。

操作索引能減少重複探索；沒有速度前後基準，不能宣稱固定加速倍率。Chatbot提示詞也不是程式狀態機，仍會偏離；範例保留失敗與限制。

## 離線查找

有PowerShell時，於repo根目錄執行：

```powershell
powershell -NoProfile -File .\skills\edcafe-operations\references\查詢操作.ps1 -關鍵字 補救
```

只讀本機JSON，不會操作網站或傳送資料。Python使用者可執行`python scripts/query.py Chatbot`。需要檢查套件完整性時執行`python scripts/validate_package.py`。

## 內容與授權

本套件含自編教學文件、原創數學範例及合成測試對話；不含課本PDF／掃描頁、個人帳號畫面、登入資訊、私人教材或不公開影片連結。範例保留原課本檔名與頁碼作來源註記，需自行取得合法教材，不能當成附件已提供。

依[MIT授權](LICENSE)可下載、修改及分享本repo自編內容；外部網站、課本及工具各自的權利與使用條件仍適用。公開repo含教師答案；正式測驗請改題並將答案留在教師端。
