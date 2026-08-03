from nicegui import ui

from components.page_header import page_header


HELP_CONTENT = """
## 基本的な使い方

GSDF MET-DLPでは、指定した地点・日時について、
FNL気象データから高度別の気象情報を取得できます。

### 1. 地点を選択

対象となる演習場・試験場を選択します。

### 2. FNLデータを検索

選択した地点に対応する利用可能なFNLデータを検索します。

### 3. 日時を選択

取得したい日時のデータを選択します。

### 4. 気象データを解析

FNL GRIB2データを取得し、指定地点の気象情報を計算します。

### 5. 結果を確認

高度別の気温・気圧・空気密度・湿度・風速・風向などを確認できます。

---

## 風向について

風向は **「風が吹いてくる方向」** として表示されます。

例えば、

- 北風 → 北から南へ吹く風
- 東風 → 東から西へ吹く風

となります。

---

## 表示される気象情報

主に以下の情報を表示します。

- 気層ごとの高度
- 気温
- 気圧
- 空気密度
- 湿度
- 風速
- 風向

---

## 高度について

気圧面のデータを空間補間し、
さらに高度方向へ補間することで、
各高度における代表的な気象値を算出しています。

そのため、表示値はFNLの直接観測値ではなく、
FNLデータから計算・補間した推定値です。

---

## 注意事項

本アプリケーションが提供する気象情報は、
FNLの公開データをもとに計算・補間したものです。

実際の観測値とは異なる場合があります。

実際の活動に使用する場合は、
適切な公式情報・観測情報等と併用してください。
"""


def open_help_page() -> None:
    """ヘルプページへ遷移する。"""
    ui.navigate.to("/help")


def help_page():

    ui.button(
        "戻る",
        icon="arrow_back",
        on_click=ui.navigate.back,
    ).props("flat no-caps")

    with ui.column().classes("page-content"):
        page_header("HELP", "操作のヒント")

        with ui.card().classes("glass-card w-full"):
            ui.markdown(
                HELP_CONTENT,
                extras=["fenced-code-blocks", "tables"],
            ).classes("help-content")