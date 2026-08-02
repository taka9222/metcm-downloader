# GSDF MET-DLP

自衛隊演習場などの任意の地点について、FNL（Final Analysis）気象データを利用して、高度別の気象情報を取得・表示する Web アプリケーションです。

> **Status: Alpha**
>
> 現在も開発・整理を継続しています。
> UI、FNL データ取得、気象データ解析、設定機能などは今後変更される可能性があります。

## 🌐 Web App

**インストール不要で、ブラウザから利用できます。**

[GSDF MET-DLP を開く](https://gsdf-met-dlp.onrender.com/?utm_source=chatgpt.com)

スマートフォン・タブレット・PCなど、Webブラウザから利用できます。

---

## Features

### 🌦️ FNL 気象データ

NCAR / GDEX が提供する FNL GRIB2 データを利用し、指定した地点・時刻の気象情報を取得します。

* FNL データの検索
* 利用可能なデータの確認
* FNL GRIB2 データの取得
* GRIB2 データの解析
* 指定地点の気象データ取得
* 高度別の気象情報表示

FNL データは以下のデータセットを利用しています。

[NCAR / GDEX FNL Dataset (d083002)](https://gdex.ucar.edu/datasets/d083002/?utm_source=chatgpt.com)

### 📊 気象情報

指定地点について、主に以下の気象情報を取得します。

* 気温
* 気圧
* 空気密度
* 湿度
* 風速
* 風向
* U / V 風成分
* 高度

気圧面のデータを空間補間し、高度方向に補間することで、各高度の代表的な気象値を算出します。

### ⛰️ 大気層

地上付近から高高度までを複数の気層に分け、それぞれの代表値を表示します。

これにより、単一高度の気象情報だけでなく、高度による気温・密度・風などの変化を確認できます。

### 📍 演習場・試験場

あらかじめ登録された演習場・試験場から地点を選択して、気象データを取得できます。

国内だけでなく、国外の地点にも対応しています。

### 🗺️ Map

登録地点を地図上で確認できます。

地図表示では、地点の位置を確認しながら対象地点を選択できます。

### ⚙️ Settings

アプリケーションの外観や各種設定を変更できます。

---

## Usage

基本的な利用方法は以下の通りです。

```text
1. Web App を開く
       ↓
2. 地点を選択
       ↓
3. 利用可能な FNL データを検索
       ↓
4. 対象となる日時を選択
       ↓
5. FNL GRIB2 データを取得
       ↓
6. 気象データを解析
       ↓
7. 高度別の気象情報を表示
```

### Web App

[https://gsdf-met-dlp.onrender.com/](https://gsdf-met-dlp.onrender.com/?utm_source=chatgpt.com)

---

## Data Processing

FNL GRIB2 データから取得した気圧面の気象情報を使用して、指定地点の気象状態を計算します。

```text
FNL GRIB2
    │
    ▼
GRIB2 データ解析
    │
    ▼
気圧面データ取得
    │
    ▼
指定地点周辺の格子データ
    │
    ▼
空間補間
    │
    ▼
高度方向への補間
    │
    ▼
各気層の代表値
    │
    ▼
Web UI に表示
```

風については、GRIB2 の U / V 成分から風速および風向を計算します。

風向は**「風が吹いてくる方向」**として扱います。

---

## Technology

主な使用技術：

* Python
* NiceGUI
* NumPy
* SciPy
* ecCodes
* GRIB2 / pygrib
* Leaflet
* Render

Web UI は NiceGUI によって構築されています。

---

## Deployment

現在の Web アプリケーションは **Render** 上で公開しています。

```text
Browser
   │
   ▼
NiceGUI
   │
   ▼
Render
   │
   ├── FNL data search
   ├── GRIB2 download
   └── Meteorological analysis
```

FNL の GRIB2 ファイルはサイズが大きいため、取得したデータは永続的なストレージへの保存を前提とせず、実行環境の一時ファイルシステムを利用しています。

そのため、再デプロイやインスタンスの再起動などによってキャッシュされたデータが失われる場合があります。

---

## Local Development

Web アプリケーションは Render 上で公開されていますが、ソースコードを取得してローカル環境で実行することもできます。

```bash
git clone https://github.com/taka9222/metcm-downloader.git
cd metcm-downloader
```

仮想環境を作成します。

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

依存パッケージをインストールします。

```bash
pip install -r requirements.txt
```

アプリケーションを起動します。

```bash
python main.py
```

起動後、ブラウザから以下へアクセスします。

```text
http://localhost:8080
```

---

## Project Structure

現在のプロジェクトは、UI とデータ処理を分離する構成で整理しています。

```text
metcm-downloader/
│
├── components/      # 再利用可能な UI コンポーネント
├── config/          # アプリケーション設定
├── pages/           # 各 Web ページ
├── services/        # FNL取得・解析などのサービス
├── static/          # CSS / JavaScript / 静的ファイル
├── utils/           # ユーティリティ
│
├── main.py          # アプリケーションエントリポイント
├── settings.py      # アプリケーション設定
├── requirements.txt
└── README.md
```

---

## Disclaimer

本アプリケーションが提供する気象情報は、FNL の公開データをもとに計算・補間したものです。

実際の観測値とは異なる場合があります。

本アプリケーションによって提供される情報は、気象状況の把握・研究・開発等を目的としたものであり、実際の活動に使用する場合は、適切な公式情報・観測情報等と併用してください。

---

## License

現在、ライセンスは明示されていません。

---

## Links

* **Web App:** [GSDF MET-DLP](https://gsdf-met-dlp.onrender.com/?utm_source=chatgpt.com)
* **Source Code:** [GitHub Repository](https://github.com/taka9222/metcm-downloader?utm_source=chatgpt.com)
* **FNL Data:** [NCAR / GDEX d083002](https://gdex.ucar.edu/datasets/d083002/?utm_source=chatgpt.com)
