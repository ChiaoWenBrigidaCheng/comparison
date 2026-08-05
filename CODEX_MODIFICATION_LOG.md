# Codex 修改紀錄

本檔用來保留 Codex 對此資料夾做過的修改與產出，避免後續因使用量或對話中斷而失去脈絡。之後每次修改檔案或新增輸出，都應追加到本檔。

## 2026-07-22

### 1. 新增三組研究量能整理腳本

- 新增檔案：`build_research_capacity_dashboard.py`
- 目的：將 `../相似系所比較.xlsx` 的 SciVal / Scopus 研究指標，依使用者指定的三組比較對象重新整理。
- 三組比較對象：
  - `01 國際企業系 vs 企業管理系`
  - `02 電子工程系校區比較`
  - `03 財金會計稅務四系比較`
- 產出檔案：
  - `outputs/research_capacity/三組研究量能重整.xlsx`
  - `outputs/research_capacity/research_capacity_summary.json`
- 重要發現：
  - 目前 `相似系所比較.xlsx` 缺少 `金融系` 的研究量能資料。
  - 第 3 組只能先比較 `會計資訊系`、`財務管理系`、`財政稅務系`，並將 `金融系` 標示為資料缺口。

### 2. 新增研究量能資料更新模板腳本

- 新增檔案：`build_research_update_template.py`
- 目的：建立新版研究量能資料的補齊與更新模板，方便後續取得新版 SciVal / Scopus 資料後直接貼入或比對。
- 產出檔案：
  - `outputs/research_capacity/研究量能資料更新模板.xlsx`
  - `outputs/research_capacity/research_update_requirements.json`
- 模板內容：
  - `更新說明`
  - `待更新資料`
  - `目前資料檢核`
  - `指標清單`
- 目前檢核結果：
  - `金融系` 缺資料。
  - 其餘七個系所有舊版研究資料，但仍需以新版資料更新。

### 3. 驗證

- 已執行：
  - `python build_research_capacity_dashboard.py`
  - `python build_research_update_template.py`
  - `python -m py_compile build_research_update_template.py build_research_capacity_dashboard.py`
- 結果：
  - 腳本可正常編譯。
  - Excel 與 JSON 輸出已成功建立。
  - 未覆蓋原始 `相似系所比較.xlsx`。

## 後續待辦

- 重新取得包含 `金融系` 的最新版研究量能資料。
- 更新 `相似系所比較.xlsx` 或將新版資料填入 `研究量能資料更新模板.xlsx`。
- 重新產出三組研究量能分析。
- 後續若修改招生、課程、研究或整併報告相關檔案，請追加紀錄到本檔。

## 2026-07-22 下午更新

### 1. 改讀新版研究資料

- 新版來源檔：`../相似系所研究表現評比.xlsx`
- 舊版來源檔：`../old_相似系所比較.xlsx`
- 新版來源檔已包含 `金融系`。
- 新版來源檔欄位與舊版不同：
  - `Overall` 欄位位置改變。
  - 年度欄位讀到的是 `2018.0` 至 `2025.0`。
  - 指標清單由舊版 9 項改為新版 10 項。

### 2. 更新研究量能整理腳本

- 修改檔案：`build_research_capacity_dashboard.py`
- 調整內容：
  - 自動優先讀取 `相似系所研究表現評比.xlsx`。
  - 若新版檔不存在，才回頭找舊版或其他含 `Data` 工作表的 Excel。
  - 改為依欄名尋找 `Entity`、`Tags`、`Metric Name`、`Overall`，不再假設欄位位置固定。
  - 支援 `2018.0` 這類年度欄位。
  - 依新版來源檔自動偵測研究指標。
  - 第 3 組已可納入 `金融系`。
- 重新產出：
  - `outputs/research_capacity/三組研究量能重整.xlsx`
  - `outputs/research_capacity/research_capacity_summary.json`
- 檢核結果：
  - `data_gaps` 已為空陣列。

### 3. 更新研究資料模板腳本

- 修改檔案：`build_research_update_template.py`
- 調整內容：
  - 自動優先讀取 `相似系所研究表現評比.xlsx`。
  - 改為自動偵測年度與研究指標。
  - 新增 Excel 檔案被開啟時的另存保護。
- 原 `outputs/research_capacity/研究量能資料更新模板.xlsx` 疑似正在 Excel 中開啟，無法覆蓋。
- 因此另存新檔：
  - `outputs/research_capacity/研究量能資料更新模板_新版.xlsx`
- 更新 JSON：
  - `outputs/research_capacity/research_update_requirements.json`
- 檢核結果：
  - `missing_departments` 已為空陣列。

### 4. 驗證

- 已執行：
  - `python build_research_capacity_dashboard.py`
  - `python build_research_update_template.py`
  - `python -m py_compile build_research_capacity_dashboard.py build_research_update_template.py`
- 結果：
  - 腳本可正常編譯。
  - `金融系` 已納入新版研究資料。
  - 研究量能重整檔已使用新版來源重產。

## 2026-07-22 資料清理

### 1. 已刪除檔案

- `../old_相似系所比較.xlsx`
  - 原因：舊版研究資料已由 `../相似系所研究表現評比.xlsx` 取代。
- `_1_6各系新生入學前學校統計__202510171632.xlsx`
  - 原因：疑似重複或暫存來源檔，正式同類資料已保留。
- `__pycache__/`
  - 原因：Python 執行快取，可由腳本重新產生。
- `outputs/dept_merge_strategy/~$科系整併策略分析報告.docx`
  - 原因：Word 暫存鎖定檔，非正式成果。
- `outputs/record_count_source_dashboard/~$NKUST_學生人數加總_扣除NA_115_116招生決策儀表板_個別學制_含首頁目錄.xlsx`
  - 原因：Excel 暫存鎖定檔，非正式成果。
- `outputs/research_capacity/研究量能資料更新模板.xlsx`
  - 原因：已由新版輸出 `outputs/research_capacity/研究量能資料更新模板_新版.xlsx` 取代。

### 2. 保留檔案

- `../相似系所研究表現評比.xlsx`
  - 目前研究量能正式來源檔，已包含 `金融系`。
- `outputs/research_capacity/三組研究量能重整.xlsx`
  - 目前三組研究量能重整結果。
- `outputs/research_capacity/研究量能資料更新模板_新版.xlsx`
  - 新版研究資料更新模板。
- `../114評鑑報告自我改善執行情形.png`
  - 專案核心依據之一：用於比較三組系所的異同，並評估合併性質雷同系所的可行性。
  - 不列入後續清理刪除範圍。
- 各系課表、招生名額、學生人數與既有報告成果檔
  - 仍屬本次相似系所比較分析所需資料，先保留。

### 3. 檢核結果

- 已確認刪除範圍限於本專案資料夾內。
- 本次刪除無失敗項目。

## 2026-07-22 依據資料定位補充

- 依使用者說明，`../114評鑑報告自我改善執行情形.png` 是本專案的主要依據資料。
- 該圖檔用途：
  - 比較三組相似系所的異同。
  - 評估合併性質雷同系所的可行性。
- 後續整理、刪除或搬移資料時，應保留此檔案並維持其可追溯性。

## 2026-07-22 互動分析網站建立

### 1. 新增網站產生腳本

- 新增檔案：`build_comparison_site.py`
- 產出檔案：`outputs/comparison_site/index.html`
- 網站內容：
  - 三個頁面按鈕：
    - 第1組：國際企業系與企業管理系。
    - 第2組：電子工程系建工/燕巢校區與第一校區。
    - 第3組：財務管理系、財政稅務系、金融系、會計資訊系。
  - 每組包含：
    - 分析總覽。
    - 招生與入學趨勢。
    - 研究量能。
    - 課程與專業差異。
    - 處理方案、風險與下一步。
- 網站為單一靜態 HTML 檔，可直接用瀏覽器開啟，不需啟動伺服器。

### 2. 修正課表抽取腳本

- 修改檔案：`extract_curricula.py`
- 調整內容：
  - 改讀目前 `課表/` 子資料夾。
  - 支援目前帶編號的課表檔名。
  - 支援 PDF 與 DOCX 課表抽取。
- 重新產出課表文字檔至 `_curriculum_extract/`。
- 抽取狀態：
  - 可讀：`企業管理系`、`國際企業系`、`電子工程系`、`金融系`、`財務管理系`、`會計資訊系`。
  - 需人工對照原檔：`電子工程系[建工燕巢校區]`、`財政稅務系`，兩者 PDF 文字抽取量偏低，可能為掃描型 PDF。

### 3. 驗證

- 已執行：
  - `python extract_curricula.py`
  - `python build_comparison_site.py`
  - `python -m py_compile extract_curricula.py build_comparison_site.py`
  - `node --check` 檢查網站內嵌 JavaScript 語法。
- 檢查結果：
  - `outputs/comparison_site/index.html` 已成功產出。
  - 三組頁面資料已嵌入網站。
  - 網站文字未使用使用者指定避免使用的詞。
  - Playwright 未安裝，因此未做瀏覽器截圖驗證。

## 2026-07-22 報告產出與網站文字調整

### 1. 網站調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 調整內容：
  - 依使用者指示，移除網站頁面中的判斷提示說明區塊。
  - 保留三個頁面按鈕與各組資料表、趨勢圖、研究量能、課程與處理方案內容。

### 2. 新增正式報告產生腳本

- 新增檔案：`build_comparison_report.py`
- 報告資料來源：
  - 與網站共用 `build_comparison_site.py` 的整理後資料。
  - 避免網站與報告使用不同資料造成前後不一致。
- 產出檔案：
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.docx`
- 報告內容：
  - 報告目的。
  - 資料來源與限制。
  - 三組比較摘要。
  - 三組個別分析：招生、研究量能、課程差異、處理方向、風險與下一步。
  - 整體建議。

### 3. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python build_comparison_report.py`
  - `python -m py_compile build_comparison_site.py build_comparison_report.py`
  - `node --check` 檢查網站內嵌 JavaScript 語法。
- 檢查結果：
  - 網站仍包含三組頁面。
  - 網站已無被移除的說明區塊。
  - 報告 Markdown、HTML、DOCX 均已產出。
  - DOCX 壓縮結構與 `word/document.xml` 可正常解析。
  - 相關輸出與腳本均未出現使用者指定避免使用的詞。

## 2026-07-22 分析總覽補強數據依據

### 1. 網站分析總覽調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 調整內容：
  - 將「分析總覽」文字改為由資料自動生成支撐依據。
  - 每個總覽項目新增「依據」欄位。
  - 支撐資料包含：
    - 115年預測入學合計。
    - 115年招生名額合計。
    - 115年預測缺口。
    - 110至114年入學變動範圍。
    - 115年預測是否足額。
    - 研究論文量、國際合作占比、Top 10%期刊占比、Top 10%引用占比。
    - 課表文字可讀比例與需人工對照之系所。

### 2. 報告同步調整

- 修改檔案：`build_comparison_report.py`
- 重新產出：
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.docx`
- 調整內容：
  - 報告中各組「分析重點」同步加入數據依據。
  - 網站與報告共用同一份整理後資料，避免兩者判讀不一致。

### 3. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python build_comparison_report.py`
  - `python -m py_compile build_comparison_site.py build_comparison_report.py`
  - `node --check` 檢查網站內嵌 JavaScript 語法。
- 檢查結果：
  - 網站總覽卡片已出現「依據」與對應數據。
  - 報告分析重點已出現「依據」與對應數據。
  - DOCX 壓縮結構與 `word/document.xml` 可正常解析。
  - 相關輸出與紀錄檔均未出現使用者指定避免使用的詞。

## 2026-07-22 新生來源樣態分析新增

### 1. 網站新增生源分析

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 新增內容：
  - 在每一組系所頁面加入「新生來源樣態」區塊。
  - 每個系呈現 114 年日間部四技新生人數、來源學校數、主要來源學校、戶籍縣市、畢業學校地理區域與入學管道。
  - 補充 110 至 114 年日間部四技累計主要來源學校，協助觀察來源學校是否集中或分散。
  - 來源學校空白或缺值統一顯示為「未填」，避免輸出技術性缺值文字。

### 2. 報告同步新增

- 修改檔案：`build_comparison_report.py`
- 重新產出：
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.docx`
- 新增內容：
  - 報告各組新增「新生來源樣態」小節。
  - 以表格列出各系 114 年生源分布與 110 至 114 年累計來源學校。
  - 在表格後加入各系簡短生源觀察。

### 3. 使用資料

- `入學年114年日間部四技學生.xlsx`
  - 用於 114 年個人層級生源分析。
- `1-6各系新生入學前學校統計.xlsx`
  - 用於 110 至 114 年來源學校累計分析。

### 4. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python build_comparison_report.py`
  - `python -m py_compile build_comparison_site.py build_comparison_report.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - Python 檢查 DOCX 壓縮結構與 `word/document.xml` 可正常解析。
- 檢查結果：
  - 網站與報告已出現「新生來源樣態」區塊。
  - `nan` 缺值字樣已自輸出檔移除。
  - 相關輸出與紀錄檔均未出現使用者指定避免使用的詞。

## 2026-07-22 交接與紀錄規則

- 使用者要求：後續每個實質檔案更動都必須同步更新本 MD 檔，方便 Codex credits 用完後由其他 AI 或人工接手。
- 後續紀錄至少包含：
  - 更動日期與主題。
  - 修改或重新產出的檔案。
  - 更動原因與主要內容。
  - 使用資料來源。
  - 已完成的驗證或尚未完成的事項。
- 適用範圍：
  - 修改 Python 腳本。
  - 重新產出網站、Markdown、HTML、DOCX 或簡報素材。
  - 新增、刪除、搬移或整理資料檔。
  - 修正資料缺值、欄位對應、文字呈現或分析架構。

## 2026-07-22 公開網站移除內部資料檢查狀態

### 1. 公開網站調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 調整內容：
  - 從網站的課程卡片移除「資料狀態」欄位。
  - 從網站 KPI 與分析依據移除課表文字抽取狀態。
  - 課程區塊改為只顯示學分結構、核心課程與特色方向。
  - 沒有正式學分結構文字的系所，網站不顯示該列，不放內部檢查原因。
  - 網站內嵌資料移除未展示用途的研究資料狀態欄位。

### 2. 正式報告同步調整

- 修改檔案：`build_comparison_report.py`
- 重新產出：
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.docx`
- 調整內容：
  - 三組比較摘要移除課表文字抽取狀態欄。
  - 「課程與專業差異」表格移除「資料狀態」欄。
  - 資料使用提醒移除公開展示不需要的課表抽取狀態說明。

### 3. 內部抽檢清單新增

- 新增檔案：`build_manual_review_checklist.py`
- 新增輸出：`outputs/manual_review/人工對照抽檢清單.md`
- 清單內容：
  - 課程資料抽檢：列出來源檔案、內部狀態、優先度與需要核對的項目。
  - 招生資料抽檢：列出 110、114、115 預測、115 名額與缺口。
  - 生源資料抽檢：列出 114 人數、來源學校數、主要來源學校、戶籍縣市與入學管道。
  - 研究資料抽檢：列出論文量、國際合作、Top 10%期刊與 Top 10%引用。
- 必檢項目：
  - 電子工程系[建工／燕巢校區]課表。
  - 財政稅務系課表。

### 4. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python build_comparison_report.py`
  - `python build_manual_review_checklist.py`
  - `python -m py_compile build_comparison_site.py build_comparison_report.py build_manual_review_checklist.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - Python 檢查 DOCX 壓縮結構與 `word/document.xml` 可正常解析。
- 檢查結果：
  - 公開網站與正式報告不再顯示內部資料檢查狀態。
  - 抽檢清單已產出，並保留需要人工核對的項目。
  - 公開輸出未出現 `nan` 缺值字樣。
  - 相關公開輸出與抽檢清單均未出現使用者指定避免使用的詞。

## 2026-07-23 招生趨勢改用原始 Excel 重算

### 1. 招生資料來源調整

- 修改檔案：`build_comparison_site.py`
- 調整內容：
  - 不再讀取 `outputs/record_count_source_dashboard/student_count_no_na_source_summary.json` 作為招生趨勢來源。
  - 新增從 `1-6各系新生入學前學校統計.xlsx` 彙整 110 至 114 年日間部四技實際入學人數。

## 2026-08-03 新增每師平均研究量能輸出與前端整合

### 1. 新增後端腳本

- 新增檔案：`系所雷同比較Raw data/build_research_per_teacher.py`
- 目的：整合 `outputs/research_capacity/research_capacity_summary.json` 中之論文量與產學資料表（`產學_每師平均產學收入.xlsx`）的專任教師數，計算每系「每師論文數（papers_per_teacher）」，並輸出 `comparison/data/research_per_teacher.json`。

### 2. 前端調整

- 修改檔案：`comparison/index.html`
- 調整內容：
  - 預載 `comparison/data/research_per_teacher.json` 為 `RESEARCH_PER_TEACHER_MAP`，以便在研究量能表格中新增欄位「每師平均量能」。
  - 在研究量能表格（`researchTable`）新增欄位 `每師平均量能` 並以 `RESEARCH_PER_TEACHER_MAP` 填值；不存在資料則顯示「無資料」。
  - 移除原本獨立的「研究量能每師平均」視覺區塊，保留輕量初始化以維持資料檢視器移動行為（當群組有每師資料時，將資料檢視器移至頁面底部）。

### 3. 產出

- 產出檔案：`comparison/data/research_per_teacher.json`（由 `build_research_per_teacher.py` 產生）。

### 4. 驗證

- 已執行：`python "系所雷同比較Raw data\build_research_per_teacher.py"`，並寫入 `comparison/data/research_per_teacher.json`。
- 已在 `comparison/index.html` 預載資料並顯示於研究量能表格，且保留資料檢視器移動邏輯。

### 5. 後續建議

- 若需讓前端在名稱不完全相同時也可匹配，建議將 `build_research_per_teacher.py` 的對應表輸出（例如 `department_keymap`），並讓 `SITE_DATA` 或前端使用該對應表做穩健查找。

  - 新增從 `111-115學年度招生名額.xlsx` 彙整 115 年四技日間部招生名額。
  - 115 與 116 入學值改為以 110 至 114 年實際入學做線性趨勢推估。
  - 新增招生名額檔之系名對應，特別處理電子工程系第一校區與建工校區各組別。

### 2. 公開輸出文字調整

- 修改檔案：
  - `build_comparison_site.py`
  - `build_comparison_report.py`
- 重新產出：
  - `outputs/comparison_site/index.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.docx`
- 調整內容：
  - 網站與報告的招生欄位改為「115推估」「116推估」「115推估名額比」「115推估缺口」。
  - KPI 改為「115趨勢推估入學合計」與「115推估缺口」。
  - 資料來源說明新增：招生趨勢由原始 Excel 彙整 110 至 114 年實際入學，115 至 116 年為固定公式之趨勢推估。
  - 公開輸出已移除舊招生摘要來源與舊欄位名稱。

### 3. 內部抽檢清單同步調整

- 修改檔案：`build_manual_review_checklist.py`
- 重新產出：`outputs/manual_review/人工對照抽檢清單.md`
- 調整內容：
  - 招生資料抽檢改用 `load_enrollment_data()`，與網站、報告共用同一份原始 Excel 彙整結果。
  - 招生抽檢欄位改為 110 入學、114 入學、115 推估、115 名額、115 推估缺口。
  - 新增「114人數跨表一致性抽檢」，比較招生趨勢使用的 114 年彙總人數與生源樣態使用的 114 年個人層級人數。
  - 研究資料抽檢提醒改為依比較組顯示，金融系納入提醒只放在第三組。

### 4. 本次主要推估結果

- 第1組：115趨勢推估入學合計 113.0 人，115名額合計 90 人，推估缺口 0.0 人。
- 第2組：115趨勢推估入學合計 231.8 人，115名額合計 214 人，推估缺口 0.0 人。
- 第3組：115趨勢推估入學合計 302.5 人，115名額合計 277 人，推估缺口 1.9 人。

### 5. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python build_comparison_report.py`
  - `python build_manual_review_checklist.py`
  - `python -m py_compile build_comparison_site.py build_comparison_report.py build_manual_review_checklist.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - Python 檢查 DOCX 壓縮結構與 `word/document.xml` 可正常解析。
- 檢查結果：
  - 公開網站、正式報告與抽檢清單未再讀取舊招生摘要 JSON。
  - 公開輸出未出現舊招生摘要來源路徑與舊欄位名稱。
  - 相關公開輸出與抽檢清單均未出現使用者指定避免使用的詞。

## 2026-07-23 網站新增趨勢推估公式提示

### 1. 網站互動提示調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 調整內容：
  - 新增 tooltip 樣式，滑鼠移過或鍵盤聚焦時可顯示說明。
  - 在 KPI「115趨勢推估入學合計」與其註記加入公式提示。
  - 在招生表格欄位「115推估」「116推估」加入公式提示。
  - 提示文字說明：115/116 推估採 110 至 114 實際入學人數做線性趨勢，公式為 `入學人數 = a + b × 學年度`，`b` 為平均變動斜率，`a` 為截距，再代入 115 或 116；若推估值小於 0，顯示為 0。

### 2. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python -m py_compile build_comparison_site.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - 搜尋確認網站輸出含公式說明與 tooltip 樣式。
- 檢查結果：
  - 網站已加入滑鼠移過後顯示公式說明的提示。

## 2026-07-23 側欄主要資料檔名換行修正

### 1. 網站版面修正

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 調整內容：
  - 修正左側欄「主要資料」長檔名超出側欄寬度的問題。
  - `.sidebar` 新增必要時可垂直捲動。
  - `.source-box` 新增寬度限制與隱藏外溢。
  - `#sourceFiles div` 新增 `overflow-wrap: anywhere` 與 `word-break: break-word`，讓長路徑可自動換行。

### 2. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python -m py_compile build_comparison_site.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - 搜尋確認輸出 HTML 已包含 `#sourceFiles` 換行樣式。
- 檢查結果：
  - 側欄主要資料長檔名已可自動換行，不會突出到主內容區。

## 2026-07-23 網站新增互動式資料檢視器

### 1. 網站功能新增

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 新增內容：
  - 在每一組系所頁面 KPI 下方新增「資料檢視器」區塊。
  - 新增資料類型下拉選單，可切換：
    - 招生趨勢。
    - 新生來源。
    - 研究量能。
    - 課程專業。
  - 新增系所勾選器，可即時選擇要顯示哪些系所。
  - 資料表會依選擇即時更新，不需重新整理頁面。
  - 招生趨勢檢視保留 115 與 116 推估欄位的公式提示。

### 2. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python -m py_compile build_comparison_site.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - 搜尋確認輸出 HTML 已包含「資料檢視器」、`dataTypeSelect`、互動資料列渲染函式。
- 檢查結果：
  - 網站已新增互動式選資料功能。

## 2026-07-23 移除側欄主要資料區塊

### 1. 網站側欄調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 調整內容：
  - 移除左側欄「主要資料」標題與資料來源清單。
  - 移除 `sourceFiles` 的畫面填入程式與相關 CSS。
  - 網站輸出時不再把 `sourceFiles` 清單放入內嵌資料。
  - `build_site_data()` 仍保留 `sourceFiles` 給正式報告產生器使用。

### 2. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python -m py_compile build_comparison_site.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - 搜尋確認網站輸出 HTML 不再包含「主要資料」、`sourceFiles`、`#sourceFiles`。
- 檢查結果：
  - 網站左側欄只保留資料日期，不再顯示主要資料清單。

## 2026-07-23 新增115招生名額樣本與補充說明

### 1. 網站調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 調整內容：
  - `load_enrollment_data()` 新增 `quota_detail_rows`，保留 115 招生名額的明細列。
  - 每組分析資料新增 `quotaRows`，供網站顯示樣本表。
  - 在「招生與入學趨勢」表格下方新增「115招生名額樣本與補充說明」。
  - 補充說明包含資料來源、使用資料、加總方式，以及電子工程系建工校區組別合併方式。
  - 樣本表欄位包含「分析系所」、「原始系所/組別」、「學制」、「名額」。

### 2. 報告同步調整

- 修改檔案：`build_comparison_report.py`
- 重新產出：
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.docx`
- 調整內容：
  - 在正式報告的「招生與入學趨勢」小節同步加入「115招生名額樣本與補充說明」。
  - 報告內同步列出各組系所的 115 招生名額樣本表。

### 3. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python build_comparison_report.py`
  - `python -m py_compile build_comparison_site.py build_comparison_report.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - Python 檢查 DOCX 內部 XML 可正常解析。
  - 搜尋確認網站與報告輸出已包含「115招生名額樣本與補充說明」、「四技日間部-技高生」、「電子工程系資訊與數位IC設計組」。
- 檢查結果：
  - 網站與正式報告已可看到 115 招生名額的樣本與補充說明。

## 2026-07-23 複製最新網站與Markdown報告至comparison資料夾

### 1. 檔案搬移

- 來源檔案：
  - `outputs/comparison_site/index.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
- 目的檔案：
  - `../comparison/index.html`
  - `../comparison/三組相似系所比較分析報告.md`
- 調整內容：
  - 以最新產出的網站覆蓋 `comparison/index.html`。
  - 將最新 Markdown 報告複製到 `comparison` 資料夾，方便與網站一起整理或上傳。

### 2. 待確認

- 若要更新 GitHub Pages，仍需從 `comparison` 資料夾將上述檔案 commit 並 push 到 GitHub。

## 2026-07-23 複製正式報告HTML至comparison資料夾

### 1. 檔案搬移

- 來源檔案：
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
- 目的檔案：
  - `../comparison/三組相似系所比較分析報告.html`
- 調整內容：
  - 將最新正式報告 HTML 複製到 `comparison` 資料夾，與網站 `index.html` 及 Markdown 報告放在同一處。

### 2. 待確認

- 若此檔也要在 GitHub 上保存，需從 `comparison` 資料夾將新增 HTML 報告 commit 並 push 到 GitHub。

## 2026-07-23 調整研究提示、來源排版、招生名額hover說明與字體

### 1. 網站調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 同步覆蓋：`../comparison/index.html`
- 調整內容：
  - 移除研究量能區塊中的指定研究提示文字。
  - 移除資料使用提醒中的研究資料更新提示，避免網站再顯示同類文字。
  - 將「115招生名額樣本與補充說明」改為滑鼠移至「115招生名額合計」KPI 卡片時顯示。
  - 移除招生表格下方原本直接展開的「115招生名額樣本與補充說明」區塊。
  - 將資料檢視器中的來源學校、戶籍縣市、入學管道等分布資料改為一列一項。
  - CSS 字體加入 `"微軟正黑體"`，並保留 `"Microsoft JhengHei"` 作為同一字體的英文名稱。

### 2. 報告同步調整

- 修改檔案：`build_comparison_report.py`
- 重新產出：
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.docx`
- 同步覆蓋：
  - `../comparison/三組相似系所比較分析報告.md`
  - `../comparison/三組相似系所比較分析報告.html`
- 調整內容：
  - Markdown 與 HTML 報告中的新生來源分布資料改為以 `<br>` 換行呈現。
  - 報告 HTML 字體加入 `"微軟正黑體"`。

### 3. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python build_comparison_report.py`
  - `python -m py_compile build_comparison_site.py build_comparison_report.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - 搜尋確認 `comparison` 內的網站與報告已不含指定刪除文字。
  - 搜尋確認 `comparison` 內已包含 `mini-list`、`微軟正黑體` 與 hover 說明文字。
- 檢查結果：
  - `comparison` 資料夾已更新為最新可上傳版本。

## 2026-07-23 新增各分析區塊下方參考資料註記

### 1. 網站調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 同步覆蓋：`../comparison/index.html`
- 調整內容：
  - 新增 `SECTION_SOURCES` 與 `sourceNote()`，統一管理各區塊下方的參考資料文字。
  - 在 KPI、資料檢視器、分析總覽、招生與入學趨勢、新生來源樣態、研究量能、課程與專業差異、處理方案等區塊下方加入「參考資料」註記。
  - 新增 `.section-source` 樣式，讓來源註記以較小字級、分隔線方式呈現。
  - 各區塊依內容標示對應資料來源，例如招生 Excel、新生來源 Excel、研究量能彙整資料與課表資料。

### 2. 報告同步調整

- 修改檔案：`build_comparison_report.py`
- 重新產出：
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.docx`
- 同步覆蓋：
  - `../comparison/三組相似系所比較分析報告.md`
  - `../comparison/三組相似系所比較分析報告.html`
- 調整內容：
  - 新增 `SOURCE_NOTES` 與 `append_source_note()`，在報告各主要小節下方加入「參考資料」。
  - 報告 HTML 新增 `.source-note` 樣式，使來源註記與正文區隔。
  - Markdown、HTML、DOCX 皆重新產出。

### 3. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python build_comparison_report.py`
  - `python -m py_compile build_comparison_site.py build_comparison_report.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - 搜尋確認 `comparison` 內的網站與報告已包含「參考資料」註記。
  - 搜尋確認 `comparison` 內未重新出現先前指定刪除的研究提示文字。
- 檢查結果：
  - 網站與報告已在各主要區塊下方補上可供追溯的參考資料來源。

## 2026-07-23 補齊掃描課表學分欄位與缺漏檢查

### 1. 問題原因

- 財政稅務系課表 PDF 為掃描型或接近掃描型檔案，文字抽取結果只留下頁面標記，導致網站與報告中的學分結構先前顯示為空白。
- 電子工程系[建工／燕巢校區]課表也有相同狀況，文字抽取量偏低，因此原先同樣未能自動帶出學分結構。

### 2. 本次補值

- 修改檔案：`build_comparison_site.py`
- 財政稅務系：依 `_curriculum_extract/財政稅務系_page3.png` 人工讀圖，補入 `132學分；財稅行政模組必修69學分、選修35學分；財富規劃模組必修71學分、選修33學分`。
- 電子工程系[建工／燕巢校區]：依 `_curriculum_extract/電子工程系建工燕巢_page9.png` 人工讀圖，補入 `128學分；必修63學分、選修37學分`。
- 修改檔案：`build_manual_review_checklist.py`
  - 「必檢」課表說明新增提醒：即使網站或報告已有補值，仍需對照掃描頁影像確認。
  - 新增「生源缺值與欄位值異常抽檢」表，列出 114 年個人層級資料中的空白值，以及 `公私立別` 欄位出現非公立/私立/未填的異常值。

### 3. 重新產出與同步

- 已重新產出：
  - `outputs/comparison_site/index.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.docx`
  - `outputs/manual_review/人工對照抽檢清單.md`
- 已同步覆蓋：
  - `../comparison/index.html`
  - `../comparison/三組相似系所比較分析報告.md`
  - `../comparison/三組相似系所比較分析報告.html`

### 4. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python build_comparison_report.py`
  - `python build_manual_review_checklist.py`
  - `python -m py_compile build_comparison_site.py build_comparison_report.py build_manual_review_checklist.py`
  - Node 檢查網站內嵌 JavaScript 可正常解析。
  - 搜尋確認報告已帶出財政稅務系與電子工程系[建工／燕巢校區]學分資料，且不再顯示為空白。
  - 搜尋確認先前指定刪除的研究提示文字未被重新帶入。
  - 搜尋確認人工抽檢清單已新增「生源缺值與欄位值異常抽檢」表。

### 5. 仍需人工確認

- 課表：財政稅務系與電子工程系[建工／燕巢校區]仍列為必檢，因來源課表是掃描型或接近掃描型 PDF。
- 114人數跨表一致性：企業管理系差1人、電子工程系[建工／燕巢校區]差5人、財政稅務系差2人、金融系差6人、會計資訊系差2人，需確認兩份原始表的涵蓋範圍與系所歸類。
- 生源資料：部分系所來源學校、畢業學校地理區域或公私立別欄位在原始資料中為空白，網站與報告以「未填」呈現；需人工確認空白是否合理。
- 生源資料欄位值異常：電子工程系[建工／燕巢校區]的 `公私立別` 出現「樟樹」2人與「治平」1人；財政稅務系的 `公私立別` 出現「台中」1人，需回原始個人檔確認是否為欄位填寫或整理時放錯欄。

## 2026-07-23 網站柔和圓邊視覺調整

### 1. 網站樣式調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 同步覆蓋：`../comparison/index.html`
- 調整內容：
  - 新增 `--surface-soft`、`--radius`、`--radius-pill`、`--shadow-subtle` 等樣式變數，統一柔和底色、圓角與陰影。
  - 側欄、KPI、分析區塊、資料卡、表格框與提示框改用較淡邊框與較輕陰影。
  - 導覽按鈕、資料檢視器下拉選單、系所勾選項目與手機版選單改為較圓的膠囊形。
  - 標題字重調整為較柔和的 700，並移除主標題以視窗寬度變動字級的設定，改為固定桌機字級與既有手機字級。
  - 表格加入淡色隔列底色，提升閱讀性但不更動資料。

### 2. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python -m py_compile build_comparison_site.py`
  - Node 檢查 `comparison/index.html` 內嵌 JavaScript 可正常解析。
  - 搜尋確認 `comparison/index.html` 已包含新的柔和樣式變數與表格隔列樣式。
  - 搜尋確認先前指定刪除的研究提示文字未被重新帶入。

## 2026-07-23 重新抽取更新版課表

### 1. 課表抽取腳本調整

- 修改檔案：`extract_curricula.py`
- 調整內容：
  - 新增 HTML 課表抽取功能，支援從 `課表/*.html` 讀取可見文字。
  - 電子工程系[建工／燕巢校區]來源改指向 `課表/02 電子工程[建工].docx`。
  - 財政稅務系來源改指向 `課表/財政稅務系課表(更新).html`。

### 2. 重新抽取結果

- 已執行：`python extract_curricula.py`
- 財政稅務系：成功抽取約 7,094 字，輸出至 `_curriculum_extract/財政稅務系.txt`。
- 電子工程系[建工／燕巢校區]：新 DOCX 抽取結果仍為 0 字。檢查 DOCX 結構後，檔內有 61 個圖片媒體，`word/document.xml` 沒有可用文字節點，判斷目前仍是圖片型 Word 檔。
- 本機未找到 `tesseract` 執行檔，因此目前無法用本機 OCR 自動讀取電子工程系[建工／燕巢校區]的新 DOCX 圖片內容。

### 3. 網站與報告資料更新

- 修改檔案：
  - `build_comparison_site.py`
  - `build_comparison_report.py`
  - `build_manual_review_checklist.py`
- 調整內容：
  - 課程資料來源說明新增 `課表/*.html`。
  - 財政稅務系學分依更新版 HTML 課表修正為：`132學分；財稅行政模組必修69學分、選修35學分；財富規劃模組必修67學分、選修37學分`。
  - 人工抽檢清單的課表來源檔名改為更新版檔案。
  - 課表抽取量偏低的說明改為「可能為掃描型PDF或圖片型DOCX」。
  - 必檢課表說明改為需對照原始檔影像確認。

### 4. 重新產出與同步

- 已重新產出：
  - `outputs/comparison_site/index.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.md`
  - `outputs/comparison_report/三組相似系所比較分析報告.html`
  - `outputs/comparison_report/三組相似系所比較分析報告.docx`
  - `outputs/manual_review/人工對照抽檢清單.md`
- 已同步覆蓋：
  - `../comparison/index.html`
  - `../comparison/三組相似系所比較分析報告.md`
  - `../comparison/三組相似系所比較分析報告.html`

### 5. 驗證

- 已執行：
  - `python -m py_compile extract_curricula.py build_comparison_site.py build_comparison_report.py build_manual_review_checklist.py`
  - Node 檢查 `comparison/index.html` 內嵌 JavaScript 可正常解析。
  - 搜尋確認網站與報告已更新財政稅務系學分。
  - 搜尋確認人工抽檢清單中財政稅務系為「可讀」，電子工程系[建工／燕巢校區]仍為「需人工對照」。
  - 搜尋確認先前指定刪除的研究提示文字未被重新帶入。

## 2026-07-23 趨勢圖對比色與外部PDF可讀性檢查

### 1. 趨勢圖色票調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 同步覆蓋：`../comparison/index.html`
- 調整內容：
  - 將趨勢圖共用色票改為高對比色組：`#0072B2`、`#D55E00`、`#009E73`、`#CC79A7`、`#E69F00`、`#6A3D9A`、`#E7298A`、`#4D4D4D`。
  - 趨勢圖線條與圖例會同步使用新色票。

### 2. 外部PDF檢查

- 檢查連結：`https://ec.nkust.edu.tw/var/file/122/1122/img/2208/359178138.pdf`
- 本機下載測試成功，檔案大小約 888 KB、共 9 頁。
- 使用 `pdfplumber` 測試文字抽取，9 頁皆為 0 字，判斷為圖片型 PDF，不能直接用目前文字抽取流程讀入。
- 檢查用暫存檔 `outputs/manual_review/359178138.pdf` 已刪除，避免留下未使用資料。

### 3. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python -m py_compile build_comparison_site.py`
  - Node 檢查 `comparison/index.html` 內嵌 JavaScript 可正常解析。
  - 搜尋確認 `comparison/index.html` 已包含新高對比色票。
  - 搜尋確認先前指定刪除的研究提示文字未被重新帶入。

## 2026-07-23 移除網站上方部分KPI卡片

### 1. 網站調整

- 修改檔案：`build_comparison_site.py`
- 重新產出：`outputs/comparison_site/index.html`
- 同步覆蓋：`../comparison/index.html`
- 調整內容：
  - 網站每組上方 KPI 卡片不再顯示「115推估缺口」。
  - 網站每組上方 KPI 卡片不再顯示「研究論文量合計」。
  - KPI 網格改為兩欄排列，避免刪除卡片後留下大片空白。
  - 招生缺口與研究論文量資料仍保留在下方表格、研究量能與報告資料中。

### 2. 驗證

- 已執行：
  - `python build_comparison_site.py`
  - `python -m py_compile build_comparison_site.py`
  - Node 檢查 `comparison/index.html` 內嵌 JavaScript 可正常解析。
  - 搜尋確認 `comparison/index.html` 已套用 KPI 顯示過濾與兩欄網格。
  - 搜尋確認先前指定刪除的研究提示文字未被重新帶入。

## 2026-07-23 本機電子工程建工PDF可讀性檢查

### 1. 檢查檔案

- 檢查檔案：`課表/02 電子工程[建工].pdf`
- 比對檔案：`課表/02 電子工程系[建工燕巢校區課表.pdf`

### 2. 檢查結果

- `課表/02 電子工程[建工].pdf` 可開啟，共 9 頁。
- 使用 `pdfplumber` 測試文字抽取，9 頁皆為 0 字。
- 與既有 `課表/02 電子工程系[建工燕巢校區課表.pdf` 的 SHA256 雜湊相同，判斷兩者為同一份圖片型 PDF。
- 因此這份 PDF 仍不能直接用目前文字抽取流程讀入；若要引用其內容，需用人工讀圖或 OCR。

### 3. 注意

- 中斷前曾依使用者貼上的截圖，在 `build_comparison_site.py` 暫時補入電子組可辨識之學分文字；`outputs/comparison_site/index.html` 與 `outputs/comparison_report/三組相似系所比較分析報告.md` 已重產，但尚未同步覆蓋 `comparison/三組相似系所比較分析報告.md`。
- 若後續要公開使用該電子組數字，需確認是否只代表「電子組」，不要誤當整個建工／燕巢校區所有組別共同數字。

## 2026-07-23 趨勢推估說明浮層修正

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者指出「115推估」「116推估」欄位滑鼠移過去應出現的公式說明被表格區塊擋住。
- 原本的說明框是 `.tooltip::after`，會受到表格外層橫向捲動容器或其他區塊邊界影響，導致顯示位置被裁切。

### 3. 修改內容

- 將公式說明改為全頁共用的 `#floatingTooltip` 浮動提示框。
- 新增 `.floating-tooltip` CSS，使用 `position: fixed` 與較高的 `z-index`，避免被表格、卡片或捲動容器擋住。
- 新增 `initFloatingTooltips()`、`showFloatingTooltip()`、`hideFloatingTooltip()`、`positionFloatingTooltip()`。
- 保留滑鼠 hover 與鍵盤 focus 兩種觸發方式。
- 提示框會依畫面空間自動放在欄位上方或下方，並限制左右邊界不超出視窗。

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步 `outputs/comparison_site/index.html` 至 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已使用 Node 檢查 `../comparison/index.html` 內嵌 JavaScript 可正常解析。

## 2026-07-23 新生來源資料來源標示修正

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 查核結果

- 資料計算本身未發現用錯來源。
- `114主要來源學校`、`戶籍縣市`、`畢業學校地理區域`、`入學管道` 由 `入學年114年日間部四技學生.xlsx` 計算。
- `110-114累計主要來源學校` 由 `1-6各系新生入學前學校統計.xlsx` 計算，篩選條件為 `日間部四技` 且 `入學年` 為 110 至 114，再依 `入學前畢業學校` 加總 `學生總數`。

### 3. 修改內容

- 將新生來源區塊標題改為：
  - `114主要來源學校（114個人資料）`
  - `110-114累計主要來源學校（1-6統計）`
- 將底部參考資料註記改為分項說明：
  - `114主要來源學校、戶籍縣市、畢業學校地理區域、入學管道：入學年114年日間部四技學生.xlsx`
  - `110-114累計主要來源學校：1-6各系新生入學前學校統計.xlsx`

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步 `outputs/comparison_site/index.html` 至 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已使用 Node 檢查 `../comparison/index.html` 內嵌 JavaScript 可正常解析。

## 2026-07-23 網站移除處理方案並改置分析報告

### 1. 修改檔案

- `build_comparison_site.py`
- `build_name_similarity_strategy_docx.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`
- `outputs/comparison_report/115_名稱雷同之系所比較分析_處理方案.md`
- `../115_名稱雷同之系所比較分析_含處理方案.docx`

### 2. 修改原因

- 使用者指示「處理方案」先不要放在網站裡，改置於 `115_名稱雷同之系所比較分析`。

### 3. 網站修改內容

- 移除網站底部「處理方案」整個區塊。
- 從網站輸出的內嵌資料中移除 `proposal`、`options`、`risks`、`nextSteps` 欄位，避免處理方案仍留在 `index.html` 原始碼中。
- 重新產生 `outputs/comparison_site/index.html`，並同步至 `../comparison/index.html`。

### 4. 分析報告處理

- 新增 `build_name_similarity_strategy_docx.py`。
- 因根目錄 `115_名稱雷同之系所比較分析.docx` 目前被 Word 或其他處理序鎖定，未直接覆蓋原檔。
- 已由原檔複製並附加「處理方案」章節，產出：
  - `../115_名稱雷同之系所比較分析_含處理方案.docx`
- 同步產出處理方案文字稿：
  - `outputs/comparison_report/115_名稱雷同之系所比較分析_處理方案.md`

### 5. 驗證

- 已執行 `python build_comparison_site.py`。
- 已執行 `python build_name_similarity_strategy_docx.py`。
- 已執行 `python -m py_compile build_comparison_site.py build_name_similarity_strategy_docx.py`。
- 已使用 Node 檢查 `../comparison/index.html` 內嵌 JavaScript 可正常解析。
- 已確認 `../comparison/index.html` 與 `outputs/comparison_site/index.html` 不含「處理方案」「可採方案」「主要風險」。
- 已確認 `../115_名稱雷同之系所比較分析_含處理方案.docx` 是有效 docx，且包含「處理方案」與「可採方案」文字。

## 2026-07-28 推估說明提示與圖表單位修正

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者回報 `115推估`、`116推估` 的公式說明仍未出現。
- 使用者指出「招生與入學趨勢」折線圖未標示單位，容易無法判讀數值代表什麼。

### 3. 修改內容

- 強化推估說明 tooltip：
  - 新增 `tooltipTargetFromEvent()`，避免事件目標不是 Element 時 tooltip 無法觸發。
  - tooltip 元素同步加入 `title` 屬性，作為瀏覽器原生提示的後備機制。
  - 新增 click 觸發，可點擊 `115推估` 或 `116推估` 固定顯示說明，再點一次或點其他地方關閉。
  - 保留滑鼠 hover 與鍵盤 focus 顯示。
- 補上趨勢圖單位：
  - 圖框上方新增 `單位：入學人數（人）；橫軸：學年度`。
  - 圖內 y 軸上方新增 `入學人數（人）`。
  - 資料點標籤改為顯示 `xx人`。

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步 `outputs/comparison_site/index.html` 至 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已使用 Node 檢查 `../comparison/index.html` 內嵌 JavaScript 可正常解析。
- 已確認 `../comparison/index.html` 與 `outputs/comparison_site/index.html` 含圖表單位文字，且未重新出現「處理方案」「可採方案」「主要風險」。

## 2026-07-28 趨勢區塊改為可見單位與公式說明

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者回報仍未看到 `115推估`、`116推估` 說明與趨勢圖單位。
- 判斷可能是使用者沒有滑到表格欄名、瀏覽器預覽仍在舊狀態，或 hover 提示不夠直覺，因此改成直接顯示於趨勢圖區塊。

### 3. 修改內容

- 在「招生與入學趨勢」標題旁新增 `單位：人` 徽章。
- 將段落改為明確說明：
  - `110至114為原始資料實績，115至116為依110至114實績計算之趨勢推估；本區所有趨勢數值皆為入學人數。`
- 在趨勢圖上方新增可見說明列：
  - `單位：入學人數（人）`
  - `橫軸：學年度`
  - `115-116：趨勢推估值`
- 在圖表上方新增可點開的 `推估公式說明`，不再只依賴滑鼠 hover。

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步 `outputs/comparison_site/index.html` 至 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已使用 Node 檢查 `../comparison/index.html` 內嵌 JavaScript 可正常解析。
- 已確認 `../comparison/index.html` 與 `outputs/comparison_site/index.html` 含 `單位：人`、`推估公式說明`、`115-116：趨勢推估值`。
- 已確認 `../comparison/index.html` 未重新出現「處理方案」「可採方案」「主要風險」。

## 2026-07-28 新增產學合作收入網站區塊

### 1. 新增資料來源

- `../產學_每師平均產學收入.xlsx`
- 工作表：`TableData`
- 欄位：
  - `學院`
  - `系所`
  - `類別`
  - `年度`
  - `產學計畫總金額(元)`
  - `專任教師數`
  - `每師平均產學收入`

### 2. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 3. 修改內容

- 新增 `INDUSTRY_XLSX` 與 `INDUSTRY_YEARS`。
- 新增 `load_industry_data()`，讀取 `產學_每師平均產學收入.xlsx`，篩選 `類別=系所` 且年度為 110-114。
- 新增 `clean_industry_rows()`，整理各系：
  - 114產學總額（萬元）
  - 114每師平均（萬元）
  - 114專任教師數
  - 110-114累計總額（萬元）
  - 110-114年均每師平均（萬元）
  - 110-114每師平均變化
  - 原始系所名稱
- 新增 `make_industry_note()`，產出每組簡要判讀。
- 網站新增「產學合作收入」區塊，位置在「研究量能」之後、「課程與專業差異」之前。
- 互動資料選單新增 `產學收入`。
- 產學收入區塊新增每師平均產學收入折線圖，單位為 `萬元/師`。
- 將研究量能表中的 `產學合作` 欄名改為 `產學合作占比`，避免與產學收入混淆。
- 來源註記新增 `產學_每師平均產學收入.xlsx`。

### 4. 重要資料處理說明

- 電子工程系名稱對應：
  - `電子工程系(建工/燕巢校區)` 對應網站的 `電子工程系[建工|燕巢校區]`
  - `電子工程系(第一校區)` 對應網站的 `電子工程系[第一]`
- 第三組使用使用者指定的 `金融系`，未將原始資料中的 `金融資訊系` 混入本次比較。
- 金額由元轉為萬元呈現，避免表格數字過長。

### 5. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步 `outputs/comparison_site/index.html` 至 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已使用 Node 檢查 `../comparison/index.html` 內嵌 JavaScript 可正常解析。
- 已確認 `../comparison/index.html` 與 `outputs/comparison_site/index.html` 含 `產學合作收入`、`產學_每師平均產學收入.xlsx`、`114每師平均`、`萬元/師`、`產學合作占比`。
- 已確認 `../comparison/index.html` 未出現 `金融資訊系`。
- 已確認 `../comparison/index.html` 未重新出現「處理方案」「可採方案」「主要風險」。

## 2026-07-28 折線圖節點數值標示

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者指出折線圖節點應顯示數值，或至少滑鼠移過去時應顯示。

### 3. 修改內容

- 新增 `.chart-point-label` 樣式，使用白色描邊提升折線圖數值標籤可讀性。
- 新增 `chartValueLabel()` 共用函式，將節點數值標籤稍微上下錯開，降低多條線同年度數值重疊。
- 「招生與入學趨勢」圖：
  - 每個節點旁直接顯示入學人數數值。
  - 原有節點 `<title>` 保留，滑鼠移過節點仍可看到系所、年度與人數。
- 「產學合作收入」圖：
  - 每個節點旁直接顯示每師平均產學收入數值。
  - 原有節點 `<title>` 保留，滑鼠移過節點仍可看到系所、年度與 `萬元/師` 數值。

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步 `outputs/comparison_site/index.html` 至 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已使用 Node 檢查 `../comparison/index.html` 內嵌 JavaScript 可正常解析。
- 已確認 `../comparison/index.html` 與 `outputs/comparison_site/index.html` 含 `chart-point-label` 與 `chartValueLabel()`。
- 已確認 `../comparison/index.html` 未重新出現「處理方案」「可採方案」「主要風險」。

## 2026-07-28 移除重疊 tooltip 說明

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者指出滑鼠移到推估說明項目時會同時出現兩個說明框。
- 原因是 tooltip 元素同時有自訂浮層使用的 `data-tip`，以及瀏覽器原生提示使用的 `title`。

### 3. 修改內容

- 保留自訂浮層 `data-tip`。
- 移除 tooltip span 的 `title` 屬性，改用 `aria-label` 保留輔助閱讀資訊。
- 節點圖表中的 SVG `<title>` 保留，因為它只在滑鼠移到圖表節點時顯示單一節點數值提示，不會與自訂浮層重疊。

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步 `outputs/comparison_site/index.html` 至 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已使用 Node 檢查 `../comparison/index.html` 內嵌 JavaScript 可正常解析。
- 已確認 tooltip 函式輸出含 `data-tip` 與 `aria-label`，不再含 `title`。
- 已確認 `../comparison/index.html` 未重新出現「處理方案」「可採方案」「主要風險」。

## 2026-07-28 趨勢圖 y 軸與節點標籤調整

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者指出趨勢圖 y 軸數值應以整數為主，避免出現 42.3、126.8 等不易閱讀的刻度。
- 使用者要求在 y 軸加入一條基準直線，讓圖表座標參照更清楚。
- 使用者要求節點數值直接標在 nodes 旁邊，而不是離節點太遠。

### 3. 修改內容

- 新增 `integerAxis()`，依資料最大值產生 0 起算的整數 y 軸刻度，並將最大刻度上修到整數級距。
- 招生與入學趨勢圖、產學合作收入趨勢圖皆改用整數 y 軸刻度。
- 兩張折線圖皆在 y 軸位置新增垂直基準線。
- 調整 `chartValueLabel()`，讓節點數值依點位顯示在右側或左側，最後一個節點改靠左避免超出版面。

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步輸出到 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已用 Node 解析 `../comparison/index.html` 內嵌 JavaScript，結果為 `JS parse OK`。
- 已確認新版 `../comparison/index.html` 不再包含舊截圖中的 `42.3`、`126.8` 小數 y 軸刻度。

## 2026-07-28 趨勢圖常駐數值標籤移除

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者指出圖表上方已標示單位，因此圖內左上角不需再放「入學人數（人）」或「萬元/師」。
- 使用者希望節點數值不要常駐顯示，改為滑鼠游標移到節點時再顯示。

### 3. 修改內容

- 移除 `.chart-point-label` 樣式與 `chartValueLabel()` 函式。
- 招生與入學趨勢圖、產學合作收入趨勢圖不再輸出節點旁的常駐數值。
- 移除 SVG 圖內左上角的單位文字。
- 保留節點 `<title>`，讓滑鼠移到節點時仍可顯示系所、年度與數值。

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步輸出到 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已用 Node 解析 `outputs/comparison_site/index.html` 與 `../comparison/index.html` 內嵌 JavaScript，結果皆為 `JS parse OK`。
- 已確認新版 `../comparison/index.html` 不再包含 `chart-point-label`、`chartValueLabel()`、圖內左上角單位文字；節點 hover 用 `<title>` 仍保留。

## 2026-07-28 研究量能資料期間註記

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者要求研究量能部分需註記資料期間為 `2018-2025`。

### 3. 修改內容

- 在網站「研究量能」區塊標題旁新增 `資料期間：2018-2025` 標籤。
- 更新研究量能參考資料說明為 `outputs/research_capacity/research_capacity_summary.json；資料期間：2018-2025。`
- 同步更新 KPI、資料檢視器與分析總覽的參考資料文字，凡提到研究量能資料檔時補充 `2018-2025`。

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步輸出到 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已用 Node 解析 `../comparison/index.html` 內嵌 JavaScript，結果為 `JS parse OK`。
- 已確認 `build_comparison_site.py`、`outputs/comparison_site/index.html`、`../comparison/index.html` 均包含 `資料期間：2018-2025` 或 `研究量能資料期間：2018-2025`。

## 2026-07-28 研究量能參考資料文字調整

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者要求研究量能參考資料改補為 `擷取自SciVal (2018-2025)`。

### 3. 修改內容

- 將研究量能區塊下方參考資料改為 `擷取自SciVal (2018-2025)。`，畫面呈現為 `參考資料：擷取自SciVal (2018-2025)。`
- 將 KPI、資料檢視器與分析總覽中提及研究量能來源的文字同步改為 SciVal 來源說明。
- 保留研究量能標題旁的 `資料期間：2018-2025` 標籤。

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步輸出到 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已用 Node 解析 `../comparison/index.html` 內嵌 JavaScript，結果為 `JS parse OK`。
- 已確認 `outputs/comparison_site/index.html` 與 `../comparison/index.html` 均包含 `擷取自SciVal (2018-2025)`。

## 2026-07-29 研究量能指標英文 hover 說明

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者要求網站中「資料類型：研究量能」的指標，在游標移到指標名稱時顯示英文。

### 3. 修改內容

- 新增 `RESEARCH_INDICATOR_TIPS`，建立中文研究量能指標與 SciVal 英文名稱對照。
- 新增 `researchIndicator()`，沿用既有 tooltip 浮動提示機制。
- 資料檢視器的研究量能欄位標題改為可 hover 顯示英文。
- 下方「研究量能」表格欄位標題同步改為可 hover 顯示英文。
- 英文對照包含：
  - 論文量：Scholarly Output
  - 國際合作：International Collaboration (%)
  - 產學合作占比：Academic-Corporate Collaboration (%)
  - Top 10%期刊：Publications in Top 10% Journal Percentiles by CiteScore Percentile (%)
  - Top 10%引用：Output in Top 10% Citation Percentiles (%)
  - 主題廣度：Subject Area Main Category Count
  - 瀏覽影響力：Field-Weighted Views Impact

### 4. 驗證

- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步輸出到 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py`。
- 已用 Node 解析 `../comparison/index.html` 內嵌 JavaScript，結果為 `JS parse OK`。
- 已確認 `outputs/comparison_site/index.html` 與 `../comparison/index.html` 均包含 `Scholarly Output`、`Academic-Corporate Collaboration (%)`、`Field-Weighted Views Impact`。

## 2026-07-29 管理雙系招生3D趨勢圖

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改原因

- 使用者要求針對「國際企業系下降、企業管理系上升」這段招生分析，製作相對應的 3D 趨勢圖。
- 重新產生網站前發現 `產學_每師平均產學收入.xlsx` 目前位於 `系所雷同比較Raw data/`，產生器仍先找上一層資料夾，會造成產學資料錯誤歸零，因此一併修正資料路徑。

### 3. 修改內容

- 新增 `management3DTrendChart()`，僅在第1組「國際企業系與企業管理系」頁面顯示。
- 3D 趨勢圖呈現 110-114 年實際入學人數，不納入 115-116 推估值。
- 圖中以立體底板、年份軸、入學人數軸、兩條不同深度折線呈現：
  - 國際企業系：70人降至60人，變化 -14.3%。
  - 企業管理系：54人增至60人，變化 +11.1%。
- 圖表下方補一句文字說明：兩系不是同步衰退，而是招生吸引力呈不同方向變化。
- 新增 `.trend3d-wrap`、`.trend3d-title`、`.trend3d-chart`、`.trend3d-caption` 樣式。
- 修正 `INDUSTRY_XLSX` 路徑，優先讀取 `ROOT / "產學_每師平均產學收入.xlsx"`，若不存在再回退到上一層資料夾。

### 4. 驗證

- 已執行 `python -m py_compile build_comparison_site.py`。
- 已確認產學 Excel 路徑讀到 `系所雷同比較Raw data/產學_每師平均產學收入.xlsx`。
- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步輸出到 `../comparison/index.html`。
- 已用 Node 解析 `../comparison/index.html` 內嵌 JavaScript，結果為 `JS parse OK`。
- 已確認 `../comparison/index.html` 包含 `trend3d-wrap`、`trend3d-chart` 與圖表文字 `3D趨勢圖：110-114實際入學人數`。
- 本機未安裝 Playwright，因此未執行瀏覽器截圖驗證；目前採 HTML/JavaScript 解析與內容確認。

## 2026-07-29 移除網站3D圖並改產報告用圖檔

### 1. 修改檔案

- `build_comparison_site.py`
- `build_report_figures.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`
- `outputs/comparison_report/figures/管理雙系_招生趨勢3D圖.png`
- `outputs/comparison_report/figures/管理雙系_招生趨勢3D圖.svg`

### 2. 修改原因

- 使用者說明 3D 趨勢圖是要用在報告，不是放在網站頁面中。
- 因此需將網站恢復為原本的招生趨勢折線圖與表格呈現，另將 3D 圖輸出為報告可插入的圖檔。

### 3. 修改內容

- 從網站產生器移除 `.trend3d-*` CSS、`management3DTrendChart()` 函式與招生趨勢區塊中的呼叫。
- 新增 `build_report_figures.py`，用於產出報告用圖檔。
- 報告用 3D 圖呈現第1組管理雙系 110-114 年實際入學趨勢：
  - 國際企業系：70人降至60人，變化 -14.3%。
  - 企業管理系：54人增至60人，變化 +11.1%。
- 圖檔輸出：
  - `outputs/comparison_report/figures/管理雙系_招生趨勢3D圖.png`
  - `outputs/comparison_report/figures/管理雙系_招生趨勢3D圖.svg`
- 產圖腳本使用 Matplotlib 的 `Agg` backend，避免本機 Tcl/Tk 不完整時無法產圖。

### 4. 驗證

- 已執行 `python build_report_figures.py`，成功產出 PNG 與 SVG。
- 已執行 `python build_comparison_site.py` 重新產生網站。
- 已同步輸出到 `../comparison/index.html`。
- 已執行 `python -m py_compile build_comparison_site.py build_report_figures.py`。
- 已用 Node 解析 `../comparison/index.html` 內嵌 JavaScript，結果為 `JS parse OK`。
- 已確認 `build_comparison_site.py`、`outputs/comparison_site/index.html`、`../comparison/index.html` 不再包含 `trend3d`、`management3DTrendChart` 或 `3D趨勢圖`。
- 已使用圖片檢視工具檢查 `管理雙系_招生趨勢3D圖.png`，圖中文字與折線內容可辨識。

## 2026-07-29 報告圖檔由 3D 改為 2D

### 1. 修改檔案

- `build_report_figures.py`
- `outputs/comparison_report/figures/管理雙系_招生趨勢2D圖.png`
- `outputs/comparison_report/figures/管理雙系_招生趨勢2D圖.svg`

### 2. 刪除檔案

- `outputs/comparison_report/figures/管理雙系_招生趨勢3D圖.png`
- `outputs/comparison_report/figures/管理雙系_招生趨勢3D圖.svg`

### 3. 修改內容

- 依使用者要求刪除報告用 3D 版本，改產出 2D 折線趨勢圖。
- 2D 圖保留國際企業系與企業管理系 110-114 入學人數趨勢。
- 每個節點旁直接標示入學人數數值。
- 右側以線尾標籤補充兩系 110 至 114 的變化：
  - 國際企業系：70 人降至 60 人，變化 -14.3%。
  - 企業管理系：54 人增至 60 人，變化 +11.1%。
- 移除下方圖例，避免與資料說明文字重疊。

### 4. 驗證

- 已執行 `python -m py_compile build_report_figures.py`，語法檢查通過。
- 已執行 `python build_report_figures.py`，重新產生 2D PNG 與 SVG 圖檔。
- 已檢視 `管理雙系_招生趨勢2D圖.png`，確認節點數值可辨識且底部說明未重疊。
- 已確認圖檔資料夾不再保留 `管理雙系_招生趨勢3D圖.png` 與 `管理雙系_招生趨勢3D圖.svg`。
- 已用 `rg` 確認網站輸出與網站產生器未殘留 `trend3d`、`management3DTrendChart`、`3D趨勢圖` 或 `招生趨勢3D圖` 字串。

## 2026-07-29 新增電子工程雙校區與第三組四系招生趨勢圖

### 1. 修改檔案

- `build_report_figures.py`
- `outputs/comparison_report/figures/管理雙系_招生趨勢2D圖.png`
- `outputs/comparison_report/figures/管理雙系_招生趨勢2D圖.svg`
- `outputs/comparison_report/figures/電子工程雙校區_招生趨勢2D圖.png`
- `outputs/comparison_report/figures/電子工程雙校區_招生趨勢2D圖.svg`
- `outputs/comparison_report/figures/第三組四系_招生趨勢2D圖.png`
- `outputs/comparison_report/figures/第三組四系_招生趨勢2D圖.svg`

### 2. 修改內容

- 將報告圖檔產生器整理為共用的 `build_enrollment_trend_2d()`，三組比較都使用同一套 2D 折線圖邏輯。
- 原管理雙系圖仍保留同樣呈現方式：110-114 實際入學人數、節點數值、線尾起訖變化。
- 新增 `電子工程雙校區_招生趨勢2D圖`，比較電子工程系[建工/燕巢校區]與電子工程系[第一]。
- 新增 `第三組四系_招生趨勢2D圖`，比較財務管理系、財政稅務系、金融系、會計資訊系。
- 三張圖均於 y 軸標示「入學人數（人）」、x 軸標示「學年度」，且節點旁直接標出人數。

### 3. 驗證

- 已執行 `python -m py_compile build_report_figures.py`，語法檢查通過。
- 已執行 `python build_report_figures.py`，成功輸出三組 PNG 與 SVG 圖檔。
- 已檢視 `電子工程雙校區_招生趨勢2D圖.png`，確認節點數值與線尾標籤可辨識。
- 已檢視 `第三組四系_招生趨勢2D圖.png`，確認四系折線、節點數值與底部資料說明可辨識。

## 2026-07-29 修正 FWCI/FWVI 指標翻譯

### 1. 修改檔案

- `build_comparison_site.py`
- `build_comparison_report.py`
- `build_research_capacity_dashboard.py`
- `build_research_update_template.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`
- `outputs/comparison_report/三組相似系所比較分析報告.md`
- `outputs/comparison_report/三組相似系所比較分析報告.html`
- `outputs/comparison_report/三組相似系所比較分析報告.docx`
- `../comparison/三組相似系所比較分析報告.md`
- `../comparison/三組相似系所比較分析報告.html`

### 2. 修改原因

- 使用者指出 FWCI 不應翻為「瀏覽影響力」。
- 經檢查，目前網站研究量能表使用的數值來源為 `Field-Weighted Views Impact`，不是 `Field-Weighted Citation Impact`。
- 因此將網站與報告中的表頭由容易誤解的「瀏覽影響力」改為「領域加權瀏覽影響力（FWVI）」。
- hover 英文補充為 `Field-Weighted Views Impact (FWVI)`。
- 同時於 tooltip 字典保留 `領域加權引用影響力（FWCI）` 對應 `Field-Weighted Citation Impact (FWCI)`，避免後續若改用 FWCI 欄位時混淆。

### 3. 修改內容

- `build_comparison_site.py`
  - 研究量能資料檢視器與各組研究表表頭改為「領域加權瀏覽影響力（FWVI）」。
  - hover 英文說明改為 `Field-Weighted Views Impact (FWVI)`。
  - `viewsImpact` 讀值增加新舊欄名相容：優先讀 `領域加權瀏覽影響力(FWVI)`，若無則讀既有 `領域權重瀏覽影響力`。
- `build_comparison_report.py`
  - 報告研究量能表頭改為「領域加權瀏覽影響力（FWVI）」。
- `build_research_capacity_dashboard.py`
  - `Field-Weighted Views Impact` 中文整理欄名改為 `領域加權瀏覽影響力(FWVI)`。
  - `Field-Weighted Citation Impact` 中文整理欄名改為 `領域加權引用影響力(FWCI)`。
- `build_research_update_template.py`
  - 更新模板中的 FWVI/FWCI 翻譯同步修正。

### 4. 驗證與限制

- 已執行 `python -m py_compile build_research_update_template.py build_research_capacity_dashboard.py build_comparison_site.py build_comparison_report.py`，語法檢查通過。
- 已執行 `python build_comparison_site.py`，重新產生網站。
- 已將網站同步至 `../comparison/index.html`。
- 已執行 `python build_comparison_report.py`，重新產生報告 md/html/docx。
- 已將報告 md/html 同步至 `../comparison/`。
- 已用 Node 檢查 `../comparison/index.html` JavaScript，結果為 `JS parse OK`。
- 已搜尋確認網站、報告與產生器中不再有舊表頭 `| 瀏覽影響力 |`、`<th>瀏覽影響力</th>` 或 `FWCI領域權重引用影響力`。
- 嘗試重跑 `build_research_capacity_dashboard.py` 時，程式回報找不到含 `Data` 工作表的研究量能 Excel 原始檔；因此本次未重建 `outputs/research_capacity/research_capacity_summary.json`，網站仍沿用既有摘要數值，但呈現名稱已改為 FWVI。

## 2026-07-29 修正第三組四系招生趨勢圖節點標籤重疊

### 1. 修改檔案

- `build_report_figures.py`
- `outputs/comparison_report/figures/第三組四系_招生趨勢2D圖.png`
- `outputs/comparison_report/figures/第三組四系_招生趨勢2D圖.svg`
- `outputs/comparison_report/figures/管理雙系_招生趨勢2D圖.png`
- `outputs/comparison_report/figures/管理雙系_招生趨勢2D圖.svg`
- `outputs/comparison_report/figures/電子工程雙校區_招生趨勢2D圖.png`
- `outputs/comparison_report/figures/電子工程雙校區_招生趨勢2D圖.svg`

### 2. 修改內容

- 因第三組四系招生趨勢圖中，113與114年度部分節點數值與線尾標籤過近，造成閱讀困難。
- 於 `build_report_figures.py` 新增第三組專用的 `point_label_offsets`，針對財務管理系、財政稅務系、金融系、會計資訊系在113與114年度的節點數值進行左右與上下微調。
- 新增第三組專用 `tail_label_offsets` 與 `tail_x_offset`，將線尾說明向右及上下錯開。
- 節點數值與線尾標籤加上淡白底，降低與折線、格線重疊時的干擾。
- 重新輸出三組招生趨勢 PNG/SVG 圖檔，維持整套報告圖檔格式一致。

### 3. 驗證

- 已執行 `python -m py_compile build_report_figures.py`，語法檢查通過。
- 已執行 `python build_report_figures.py`，重新產生三組招生趨勢 PNG/SVG 圖檔。
- 已檢視 `第三組四系_招生趨勢2D圖.png`，確認113與114年度節點數值已錯開，整體可辨識性改善。

## 2026-07-30 新生來源樣態新增互動式圓餅圖

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改內容

- 在網站「新生來源樣態」區塊新增互動式圓餅圖。
- 新增三個篩選器：
  - 系所
  - 分類
  - 資料年度
- 來源學校分類使用 `1-6各系新生入學前學校統計.xlsx`，可切換：
  - 110年
  - 111年
  - 112年
  - 113年
  - 114年
  - 110-114綜合
- 114年個人層級資料分類使用 `入學年114年日間部四技學生.xlsx`，可切換分類：
  - 戶籍縣市
  - 戶籍區域
  - 畢業學校區域
  - 入學管道
  - 公私立別
- 圓餅圖資料改採前幾名加「其他」方式呈現，避免只顯示前幾名而造成比例加總不到100%。
- 圓餅圖右側新增圖例，顯示各分類人數與百分比。
- 圖下方新增資料說明，指出該分類使用的原始 Excel 檔案與年度限制。

### 3. 資料限制

- 110-114逐年與綜合年度目前可完整切換的是「來源學校」，資料來源為 `1-6各系新生入學前學校統計.xlsx`。
- 戶籍縣市、戶籍區域、畢業學校區域、入學管道、公私立別目前只有114年個人層級資料，資料來源為 `入學年114年日間部四技學生.xlsx`。

### 4. 驗證

- 已執行 `python -m py_compile build_comparison_site.py`，語法檢查通過。
- 已執行 `python build_comparison_site.py`，重新產生網站。
- 已將網站同步至 `../comparison/index.html`。
- 已用 Node 檢查 `../comparison/index.html` 內嵌 JavaScript，結果為 `JS parse OK`。
- 已搜尋確認 `outputs/comparison_site/index.html` 與 `../comparison/index.html` 包含 `sourceCharts`、`sourcePieDashboard`、`sourcePieDept`、`source-pie-layout` 與 `110-114綜合`。

## 2026-07-30 研究量能指標改為 Field-weighted citation index

### 1. 修改檔案

- `build_research_capacity_dashboard.py`
- `build_research_update_template.py`
- `build_comparison_site.py`
- `build_comparison_report.py`
- `outputs/research_capacity/research_capacity_summary.json`
- `outputs/research_capacity/三組研究量能重整.xlsx`
- `outputs/comparison_site/index.html`
- `outputs/comparison_report/三組相似系所比較分析報告.md`
- `outputs/comparison_report/三組相似系所比較分析報告.html`
- `outputs/comparison_report/三組相似系所比較分析報告.docx`
- `../comparison/index.html`
- `../comparison/三組相似系所比較分析報告.md`
- `../comparison/三組相似系所比較分析報告.html`

### 2. 修改內容

- 研究量能網站欄位由原先的 `領域加權瀏覽影響力（FWVI）` 改為 `Field-weighted citation index`。
- `build_comparison_site.py` 的研究資料物件欄位由 `viewsImpact` 改為 `citationIndex`，讀取順序為 `Field-weighted citation index`，並保留 `領域加權引用影響力(FWCI)` 與 `Field-Weighted Citation Impact` 作為相容來源名稱。
- `build_research_capacity_dashboard.py` 與 `build_research_update_template.py` 將 SciVal 原始指標 `Field-Weighted Citation Impact` 輸出顯示為 `Field-weighted citation index`。
- 研究資料整理腳本改為同時搜尋 `系所雷同比較Raw data` 與上一層資料夾，確保能讀取目前放在 Raw data 內的 `相似系所研究表現評比.xlsx`。
- 報告產生器同步改用 `citationIndex` 與 `Field-weighted citation index` 表頭，避免報告 MD/HTML/DOCX 殘留舊 FWVI 欄位。

### 3. 資料來源與抽查

- 使用來源：`系所雷同比較Raw data/相似系所研究表現評比.xlsx`。
- 使用工作表：`Data`。
- 使用原始 SciVal 指標：`Field-Weighted Citation Impact`。
- 重建後 JSON 欄位：`Field-weighted citation index`。
- 抽查值：國際企業系 0.75、企業管理系 1.12、電子工程系[建工|燕巢校區] 0.80、電子工程系[第一] 0.44、財務管理系 0.29、財政稅務系 0.47、金融系 1.18、會計資訊系 0.73。

### 4. 驗證

- 已執行 `python -m py_compile` 檢查四個修改腳本，通過。
- 已執行 `python build_research_capacity_dashboard.py`，成功重建研究量能 JSON/XLSX，`data_gaps` 為空。
- 已執行 `python build_comparison_site.py`，成功重建 `outputs/comparison_site/index.html`。
- 已執行 `python build_comparison_report.py`，成功重建報告 MD/HTML/DOCX。
- 已同步更新 `comparison/index.html`、`comparison/三組相似系所比較分析報告.md`、`comparison/三組相似系所比較分析報告.html`。
- 已用 Node 檢查 `comparison/index.html` 的 JavaScript，可解析，結果為 `JS parse OK`。
- 已搜尋 `comparison` 資料夾，未找到 `FWVI`、`領域加權瀏覽`、`瀏覽影響力`、`viewsImpact` 舊字樣。

## 2026-07-30 新生來源樣態報告圖產製

### 1. 新增與更新檔案

- `build_source_profile_figures.py`
- `outputs/comparison_report/figures/source_profiles/*.png`
- `outputs/comparison_report/figures/source_profiles/*.svg`
- `outputs/comparison_report/新生來源樣態比較圖清單.md`
- `../comparison/figures/source_profiles/*.png`
- `../comparison/figures/source_profiles/*.svg`
- `../comparison/新生來源樣態比較圖清單.md`

### 2. 圖表內容

- 依三組相似系所產製新生來源樣態比較圖。
- 每組包含6類分類圖：
  - 來源學校：110-114綜合年度。
  - 戶籍縣市：114年度。
  - 戶籍區域：114年度。
  - 畢業學校區域：114年度。
  - 入學管道：114年度。
  - 公私立別：114年度。
- 共產出18張PNG與18張SVG。
- 圖型採橫向分組長條圖，同一分類下直接比較各系所占比；標籤格式為「人數/占比」。
- 來源學校與戶籍縣市等高類別數圖表保留主要項目與「其他」；區域與公私立別保留全部項目。

### 3. 資料來源

- 來源學校使用 `1-6各系新生入學前學校統計.xlsx`，範圍為110-114日間部四技加總資料。
- 戶籍縣市、戶籍區域、畢業學校區域、入學管道、公私立別使用 `入學年114年日間部四技學生.xlsx`，範圍為114日間部四技個人層級資料。
- 圖表資料由 `build_comparison_site.py` 的 `build_site_data()` 取得，與網站新生來源樣態資料一致。

### 4. 驗證

- 已執行 `python -m py_compile build_source_profile_figures.py`，語法檢查通過。
- 已執行 `python build_source_profile_figures.py`，成功產出18張報告圖並同步到 `comparison/figures/source_profiles/`。
- 已確認 `comparison/figures/source_profiles/` 內有18個PNG與18個SVG。
- 已用 PIL 抽查圖像尺寸與非空白像素比例，確認圖檔非空白。
- 已檢查 `comparison/新生來源樣態比較圖清單.md` 內36個PNG/SVG連結，缺漏數為0。

## 2026-07-30 FWCI 顯示名稱改為中文

### 1. 修改檔案

- `build_research_capacity_dashboard.py`
- `build_research_update_template.py`
- `build_comparison_site.py`
- `build_comparison_report.py`
- `outputs/research_capacity/research_capacity_summary.json`
- `outputs/research_capacity/三組研究量能重整.xlsx`
- `outputs/comparison_site/index.html`
- `outputs/comparison_report/三組相似系所比較分析報告.md`
- `outputs/comparison_report/三組相似系所比較分析報告.html`
- `outputs/comparison_report/三組相似系所比較分析報告.docx`
- `../comparison/index.html`
- `../comparison/三組相似系所比較分析報告.md`
- `../comparison/三組相似系所比較分析報告.html`

### 2. 修改內容

- 將網站與報告中的 `Field-weighted citation index` 顯示名稱改為 `領域加權引用影響力 (FWCI)`。
- hover 英文說明保留為 `Field-Weighted Citation Impact (SciVal)`，讓指標來源可對回 SciVal 原始名稱。
- 修正 `build_comparison_site.py` 的 `clean_research_row()`，優先讀取 `領域加權引用影響力 (FWCI)` 欄位，並保留舊英文欄名與舊中文無空格欄名作為相容讀取。
- 重新產製研究量能 JSON/XLSX、網站 HTML、報告 MD/HTML/DOCX，並同步至 `comparison` 資料夾。

### 3. 驗證

- 已執行 `python -m py_compile` 檢查修改腳本，通過。
- 已執行 `python build_research_capacity_dashboard.py`，成功重建研究量能資料，`data_gaps` 為空。
- 已執行 `python build_comparison_site.py` 與 `python build_comparison_report.py`，成功重建網站與報告。
- 已同步更新 `comparison/index.html`、`comparison/三組相似系所比較分析報告.md`、`comparison/三組相似系所比較分析報告.html`。
- 已確認 `comparison/index.html` 的 JavaScript 可解析，結果為 `JS parse OK`。
- 已抽查網站資料內 FWCI 數值：國際企業系 0.75、企業管理系 1.12、電子工程系[建工|燕巢校區] 0.80、電子工程系[第一] 0.44、財務管理系 0.29、財政稅務系 0.47、金融系 1.18、會計資訊系 0.73。
- 已搜尋 `comparison` 資料夾，未找到 `Field-weighted citation index`、`FWVI`、`領域加權瀏覽`、`瀏覽影響力`、`viewsImpact` 舊字樣。

## 2026-07-30 新生來源樣態報告圖改為圓餅圖

### 1. 修改檔案

- `build_source_profile_figures.py`
- `outputs/comparison_report/figures/source_profiles/*.png`
- `outputs/comparison_report/figures/source_profiles/*.svg`
- `outputs/comparison_report/新生來源樣態比較圖清單.md`
- `../comparison/figures/source_profiles/*.png`
- `../comparison/figures/source_profiles/*.svg`
- `../comparison/新生來源樣態比較圖清單.md`

### 2. 修改內容

- 將新生來源樣態報告圖由橫向分組長條圖改為多圓餅圖，樣式配合網站的圓餅圖呈現。
- 每張圖仍以三組相似系所與6類分類產出：來源學校、戶籍縣市、戶籍區域、畢業學校區域、入學管道、公私立別。
- 每一系所在同一張圖內各自顯示一個圓餅圖，標籤直接標示「分類名稱、人數、占比」。
- 小比例項目改採圓餅旁的文字標示與引線，降低文字重疊；主要項目則保留於圓餅區塊上。
- 修正前次產圖腳本中少數中文標題、註腳與檔名被轉成 `?` 的問題，避免 Windows 輸出檔名無效。
- 本節更新後，前段「新生來源樣態報告圖產製」中的「橫向分組長條圖」描述已由本次圓餅圖版本取代。

### 3. 驗證

- 已執行 `python -m py_compile build_source_profile_figures.py`，語法檢查通過。
- 已執行 `python build_source_profile_figures.py`，成功重新產生18張PNG與18張SVG，並同步至 `comparison/figures/source_profiles/`。
- 已確認 `comparison/figures/source_profiles/` 內有18個PNG與18個SVG。
- 已用 PIL 檢查18張PNG尺寸與非空白像素變異，`blank=0`。
- 已檢查 `comparison/新生來源樣態比較圖清單.md` 內36個PNG/SVG連結，缺漏數為0。

## 2026-07-30 併入110-113個人層級新生來源資料並更新網站名稱

### 1. 修改檔案

- `build_comparison_site.py`
- `build_comparison_report.py`
- `outputs/comparison_site/index.html`
- `outputs/comparison_report/三組相似系所比較分析報告.md`
- `outputs/comparison_report/三組相似系所比較分析報告.html`
- `outputs/comparison_report/三組相似系所比較分析報告.docx`
- `../comparison/index.html`
- `../comparison/三組相似系所比較分析報告.md`
- `../comparison/三組相似系所比較分析報告.html`
- `../comparison/三組相似系所比較分析報告.docx`

### 2. 新增資料使用

- 新增讀取 `入學年110-113日間部四技學生.xlsx`，並與既有 `入學年114年日間部四技學生.xlsx` 併成110-114日間部四技個人層級資料。
- 個人層級新生來源分類更新為可切換 `110`、`111`、`112`、`113`、`114` 與 `110-114綜合`。
- 更新分類包含：戶籍縣市、戶籍區域、畢業學校區域、入學管道、公私立別。
- 來源學校分類仍使用 `1-6各系新生入學前學校統計.xlsx` 的110-114日間部四技加總資料，維持與招生來源學校統計表一致。

### 3. 網站名稱更新

- 網站 `<title>` 與側欄主標題已改為 `名稱及課程相似系所比較分析儀表板`。
- 新生來源區塊說明與各區參考資料文字已同步改為110-114個人層級資料。
- 資料檢視器的新生來源欄位改為顯示 `110-114人數` 與 `114人數`，方便同時看累計量體與最新年度。

### 4. 抽查結果

- 110-114個人層級資料筆數抽查：
  - 國際企業系：312人；114年60人。
  - 企業管理系：280人；114年61人。
  - 電子工程系[建工|燕巢校區]：833人；114年168人。
  - 電子工程系[第一]：351人；114年68人。
  - 財務管理系：297人；114年50人。
  - 財政稅務系：301人；114年60人。
  - 金融系：544人；114年103人。
  - 會計資訊系：549人；114年108人。
- 抽查國際企業系 `戶籍縣市` 的110-114綜合前三項為：高雄市57人/18.3%、台中市48人/15.4%、彰化縣37人/11.9%。

### 5. 驗證

- 已執行 `python -m py_compile build_comparison_site.py`，通過。
- 已執行 `python -m py_compile build_comparison_report.py`，通過。
- 已執行 `python build_comparison_site.py`，成功重建網站。
- 已執行 `python build_comparison_report.py`，成功重建報告 MD/HTML/DOCX。
- 已同步 `comparison/index.html` 與 `comparison/三組相似系所比較分析報告.*`。
- 已解析 `comparison/index.html` 內嵌資料，確認8個系所在5個個人層級新生來源分類中皆具備 `110`、`111`、`112`、`113`、`114`、`110-114` 年度資料鍵，缺漏數為0。
- 已用 Node 檢查 `comparison/index.html` 的 JavaScript，可解析，結果為 `JS parse OK`。
- 已搜尋 public 輸出，未找到舊網站名稱 `相似系所比較分析網站`、`114個人層級樣態使用`、`114年個人層級資料` 等舊說明。

## 2026-07-30 網站新生來源圓餅圖圖例距離調整

### 1. 修改檔案

- `build_comparison_site.py`
- `outputs/comparison_site/index.html`
- `../comparison/index.html`

### 2. 修改內容

- 調整網站「新生來源樣態」互動圓餅圖的圖例排版。
- 原本圖例列使用 `grid-template-columns: 14px minmax(0, 1fr) auto`，會把人數與百分比推到容器最右側，截圖放入報告時距離太遠。
- 改為 `grid-template-columns: 14px minmax(120px, max-content) max-content`，並增加 `justify-items: start`、`justify-content: start`、`width: fit-content`、`max-width: 560px`。
- 修改後圖例呈現為「色點／分類名稱／人數與占比」三欄緊湊排列，數字會靠近分類名稱，較適合截圖放入報告。

### 3. 驗證

- 已執行 `python -m py_compile build_comparison_site.py`，通過。
- 已執行 `python build_comparison_site.py`，成功重建網站。
- 已同步 `outputs/comparison_site/index.html` 至 `comparison/index.html`。
- 已搜尋 `comparison/index.html`，確認包含新版 CSS：`grid-template-columns: 14px minmax(120px, max-content) max-content`、`width: fit-content`、`max-width: 560px`。
- 已用 Node 檢查 `comparison/index.html` 的 JavaScript，可解析，結果為 `JS parse OK`。

## 2026-07-30 重新產出產學合作收入報告圖

### 1. 修改與新增檔案

- `build_industry_income_figures.py`
- `outputs/comparison_report/figures/industry_income/*.png`
- `outputs/comparison_report/figures/industry_income/*.svg`
- `outputs/comparison_report/產學合作收入圖清單.md`
- `../comparison/figures/industry_income/*.png`
- `../comparison/figures/industry_income/*.svg`
- `../comparison/產學合作收入圖清單.md`

### 2. 修改原因

- 使用者指出先前產學合作收入圖看起來有錯。
- 重新比對 `產學_每師平均產學收入.xlsx` 後，確認先前截圖中的部分趨勢數值與原始 Excel 不一致，例如：
  - 國際企業系110-114每師平均產學收入正確值為約23.9、171.3、49.4、35.4、21.8萬元/師。
  - 企業管理系110-114正確值為約1.5、3.0、0.5、3.5、1.6萬元/師。
  - 財務管理系110-114正確值為約21.5、14.4、21.6、17.7、0.4萬元/師。
  - 財政稅務系110-114正確值為約3.3、4.0、0.8、0.9、7.2萬元/師。
- 因此新增程式化產圖流程，不使用圖像生成方式重繪數字，避免視覺圖表與原始資料不一致。

### 3. 新圖設計

- 產出三張報告用主圖：
  - `產學合作收入_第1組管理雙系.png/svg`
  - `產學合作收入_第2組電子工程雙校區.png/svg`
  - `產學合作收入_第3組財金會稅四系.png/svg`
- 每張圖以小倍數折線圖呈現各系110-114每師平均產學收入，並在下方加入摘要表。
- 各小圖採各系自身尺度，避免電子工程系第一校區114年極端值壓縮其他系線條，使報告截圖更易讀。
- 圖上明列公式：每師平均產學收入（萬元/師）= 產學計畫總金額(元) ÷ 專任教師數 ÷ 10,000。
- 下方表格列出110-114各年每師平均、114總額、114教師數、110-114累計總額、110-114年均每師平均與110-114變化。

### 4. 驗證

- 已執行 `python -m py_compile build_industry_income_figures.py`，通過。
- 已執行 `python build_industry_income_figures.py`，成功產出3張PNG與3張SVG，並同步至 `comparison/figures/industry_income/`。
- 已確認 `comparison/figures/industry_income/` 內有3個PNG與3個SVG。
- 已用 PIL 檢查3張PNG尺寸與非空白像素變異，`blank_png=[]`。
- 已檢查 `comparison/產學合作收入圖清單.md` 內6個PNG/SVG連結，缺漏數為0。

## 2026-08-03 下午 - 網站 index.html：新生來源配色、研究每師平均、學生群與生源變化

- 修改 `comparison/index.html`，並同步至 `系所雷同比較Raw data/outputs/comparison_site/index.html`。
- 新生來源樣態圓餅圖改為固定分類配色：同一分類標籤在不同系所、年度與分類切換時使用一致顏色；未列入固定表的來源學校以標籤 hash 指派穩定備用色。
- 研究量能表新增「每師平均發表量」欄位，放在「論文量」旁；滑鼠移至欄名時顯示公式「每師平均發表量 = 論文量 ÷ 專任教師數」與該組各系專任教師數。
- 資料檢視器的研究量能同步新增「每師平均發表量」欄位；新生來源檢視器同步修正 110-114 人數、114 人數、110-114 來源學校數、114 來源學校數的欄位對應。
- 新增 `comparison/data/student_group_data.json`，並同步至 `系所雷同比較Raw data/outputs/comparison_site/data/student_group_data.json`。
- 學生群資料處理方式：以 `1-6各系新生入學前學校統計.xlsx` 的 110-114 日間部四技來源學校，對照 `5_110-114學年度技術型高中各校日間部各群類學生人數.xlsx`；依來源學校在各群類分頁的高三人數比例換算「推估來源群類」。此結果不是個別學生實際群類，網站已於表格下方註明。
- 新生來源區塊新增「學生群與生源變化」表，顯示各系推估來源群類、群類對照率、110-114 年來源學生數、110-114 變化與主要來源學校。
- 驗證：抽出 `comparison/index.html` 的 `<script>` 區塊後執行 `node --check`，語法檢查通過。

### 重要交接提醒

- 這次嘗試修改 `系所雷同比較Raw data/build_comparison_site.py` 時，PowerShell 寫入曾使該檔案原始碼被截斷；已將該檔改為明確的 recovery stub，避免後續誤以為可直接執行。
- 目前可用網站來源以 `comparison/index.html` 為準；在未從備份復原或重建 `build_comparison_site.py` 前，請勿從該 `.py` 重新產生網站，以免覆蓋目前 direct-edit 版本。
- 仍可找到 compiled cache：`系所雷同比較Raw data/__pycache__/build_comparison_site.cpython-313.pyc`，可作為後續復原線索，但不是可維護原始碼。

## 2026-08-03 下午 - 網站版面：資料檢視器移至最下方

- 修改 `comparison/index.html`：在 `renderGroup(group)` 中移除 KPI 下方的 `${dataExplorer(group)}`，改放到「課程與專業差異」section 之後，成為頁面最下方區塊。
- 同步更新 `系所雷同比較Raw data/outputs/comparison_site/index.html`。
- 驗證：抽出 `comparison/index.html` 的 `<script>` 區塊執行 `node --check`，語法檢查通過。

## 2026-08-03 下午 - 網站說明：學生群與生源變化新增計算方式

- 修改 `comparison/index.html` 的「學生群與生源變化」區塊，在表格上方新增「群類對照與來源推估計算方式」說明框。
- 說明內容包含：使用 `1-6各系新生入學前學校統計.xlsx` 取得來源學校與人數、使用 `5_110-114學年度技術型高中各校日間部各群類學生人數.xlsx` 對照同年度同來源學校的技高群類高三人數、無法對照資料的處理方式，以及兩個公式：推估來源群類人數、群類對照率。
- 調整表格下方註記，明確說明推估來源群類是來源學校層級推估，非個別學生實際群類。
- 同步更新 `系所雷同比較Raw data/outputs/comparison_site/index.html`。
- 驗證：抽出 `comparison/index.html` 的 `<script>` 區塊執行 `node --check`，語法檢查通過。

## 2026-08-03 下午 - 網站呈現：學生群與生源變化改為圖示卡片

- 修改 `comparison/index.html` 的「學生群與生源變化」區塊，將原本的表格呈現改為每系一張視覺化卡片。
- 每張卡片包含：群類對照率圓形指標、推估來源群類橫條圖、110-114 生源變化迷你長條圖。
- 移除原表格中的「110-114主要來源學校」欄位，避免與上方「新生來源樣態」中的來源學校分析重複。
- 保留「群類對照與來源推估計算方式」說明框與下方資料限制註記。
- 同步更新 `系所雷同比較Raw data/outputs/comparison_site/index.html`。
- 驗證：抽出 `comparison/index.html` 的 `<script>` 區塊執行 `node --check`，語法檢查通過。

## 2026-08-03 下午 - 調整學生群與來源群類變化區塊

- 更新 `comparison/data/student_group_data.json`，新增各系 `annualGroups` 欄位，保留110至114年各來源群類推估人數與百分比。
- 修改 `comparison/index.html`，將「學生群與來源群類變化」移至「招生與入學趨勢」下方，並自「新生來源樣態」段落移除重複插入。
- 依使用者要求移除原本過大的生源變化 bar 與主要來源學校欄位；本區改為聚焦「推估來源群類」與「群類年度變化（推估人數）」。
- 縮小群類橫條與卡片視覺，新增年度矩陣呈現110至114群類變化，避免與上方招生趨勢圖重複。
- 同步更新 `系所雷同比較Raw data/outputs/comparison_site/index.html` 與 `系所雷同比較Raw data/outputs/comparison_site/data/student_group_data.json`。
- 驗證：抽出 `comparison/index.html` 內 `<script>` 執行 `node --check`，結果通過。

### 追加文字修正
- 微調「新生來源樣態」說明，移除與新區塊重複的「生源變化與推估來源群類」描述，讓該段只聚焦戶籍、學校區域、入學管道、公私立別與來源學校。
- 已重新同步 `comparison/index.html` 至 `系所雷同比較Raw data/outputs/comparison_site/index.html`，並以 `node --check` 驗證腳本通過。

### 追加清理
- 移除 `comparison/index.html` 中三處先前樣式替換殘留的獨立 `$1` 字元。
- 重新確認「學生群與來源群類變化」只於「招生與入學趨勢」下方呼叫一次，且在「新生來源樣態」之前。
- 已再次同步 `comparison/index.html` 與 `comparison/data/student_group_data.json` 至輸出網站資料夾，並以 `node --check` 驗證腳本通過。

## 2026-08-03 下午 - 學生群年度矩陣改為 Heatmap

- 修改 `comparison/index.html` 的「學生群與來源群類變化」區塊，將原本年度矩陣的小色塊 highlight 改為整格 heatmap。
- Heatmap 設計：顏色沿用來源群類分類色；同一組比較中，可見群類的最大年度推估人數作為高值基準，格子越深代表該年度推估來源人數越多。
- 新增 heatmap 圖例：「顏色＝來源群類；深淺＝推估人數」，並保留滑鼠移至格子時顯示群類、年度與推估人數。
- 移除舊的 `annual-group-value` 小色塊呈現方式，改用 `.annual-heat-cell` 全格上色。
- 同步更新 `系所雷同比較Raw data/outputs/comparison_site/index.html`；`student_group_data.json` 也同步至輸出資料夾。
- 驗證：抽出 `comparison/index.html` 內 `<script>` 執行 `node --check`，結果通過。

## 2026-08-05 - 移除學生群推估來源群類 Bar

- 依使用者建議，修改 `comparison/index.html` 的「學生群與來源群類變化」區塊，刪除「110-114 推估來源群類」小橫條圖，只保留「群類年度變化（推估人數）」heatmap。
- 移除 `studentGroupBars()` 函式，以及 `.group-bar-*` 相關 CSS，避免網站保留未使用的視覺元件。
- 保留各系「群類對照率」圓環與年度 heatmap；heatmap 仍以顏色代表來源群類、深淺代表推估人數。
- 同步更新 `系所雷同比較Raw data/outputs/comparison_site/index.html` 與 `系所雷同比較Raw data/outputs/comparison_site/data/student_group_data.json`。
- 驗證：抽出 `comparison/index.html` 內 `<script>` 執行 `node --check`，結果通過。

## 2026-08-05 - Heatmap 顯示全部已推估群類

- 修改 `comparison/index.html` 的 `annualGroupMatrix()`，將原本 `annualGroups.slice(0, 3)` 改為顯示 `annualGroups` 中全部已推估群類。
- 更新「學生群與來源群類變化」卡片標題為「群類年度變化（全部已推估群類，推估人數）」，避免誤解為只顯示前三大群類。
- 目前 `comparison/data/student_group_data.json` 中各系 `annualGroups` 已包含目前整理出的可推估群類，例如管理與財金會稅組會顯示餐旅群；本次未重算原始數值，以維持既有資料計算結果一致。
- 同步更新 `系所雷同比較Raw data/outputs/comparison_site/index.html` 與 `系所雷同比較Raw data/outputs/comparison_site/data/student_group_data.json`。
- 驗證：抽出 `comparison/index.html` 內 `<script>` 執行 `node --check`，結果通過。

## 2026-08-05 - 補充群類對照與來源推估說明

- 修改 `comparison/index.html` 的「學生群與來源群類變化」區塊，將「群類對照與來源推估計算方式」移到該區塊最下方，作為補充說明。
- 補充說明內容包含資料來源、來源學校對照方式、無法對照情形，以及推估來源群類人數與群類對照率公式。
- 新增白話說明：例如群類對照率 85.7% 表示 85.7% 可完成群類推估，其餘 14.3% 因未填、非技高或無法自動對照而未納入群類推估。
- 同步更新 `系所雷同比較Raw data/outputs/comparison_site/index.html` 與 `系所雷同比較Raw data/outputs/comparison_site/data/student_group_data.json`。
- 驗證：抽出 `comparison/index.html` 內 `<script>` 執行 `node --check`，結果通過。

## 2026-08-05 - MD 修改紀錄格式修正

- 整理 `CODEX_MODIFICATION_LOG.md` 的 Markdown 段落間距，確保 `##` 與 `###` 標題前保留空行，避免標題黏在上一段項目後方。
- 以 `系所雷同比較Raw data/CODEX_MODIFICATION_LOG.md` 作為主檔修正後，同步覆蓋 `comparison/CODEX_MODIFICATION_LOG.md`，維持兩份紀錄一致。
- 修正前次整理時殘留的字面換行標記，改回真正的 Markdown 空行。

## 2026-08-05 - 刪除學生群區塊說明文字

- 修改 `comparison/index.html` 的「學生群與來源群類變化」區塊，刪除段落開頭文字「置於招生趨勢之後，」。
- 同步更新 `系所雷同比較Raw data/outputs/comparison_site/index.html` 與 `系所雷同比較Raw data/outputs/comparison_site/data/student_group_data.json`。
- 驗證：抽出 `comparison/index.html` 內 `<script>` 執行 `node --check`，結果通過。
## 2026-08-05 - 新生來源縣市圓餅圖配色修正

- 修改 `comparison/index.html` 的 `sourceColorOverrides`，新增常見縣市固定配色，避免戶籍縣市與來源地區圓餅圖使用 fallback 顏色時出現過於相近的色塊。
- 重點修正：`新北市` 固定為藍色 `#0072B2`，`台南市` 固定為橘色 `#E69F00`，使兩者在圓餅圖與圖例中更容易區分。
- 同步更新 `系所雷同比較Raw data/outputs/comparison_site/index.html` 與 `系所雷同比較Raw data/outputs/comparison_site/data/student_group_data.json`。
- 驗證：抽出 `comparison/index.html` 內 `<script>` 執行 `node --check`，結果通過。