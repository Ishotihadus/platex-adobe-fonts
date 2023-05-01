# Adobe Fonts for LaTeX

Adobe Fonts の日本語フォントを pLaTeX / upLaTeX で使えるようにするためのスクリプトなど。

現状 macOS のみ対応。

## 使い方

### 1. texmf.cnf の追記

`texmf.cnf` にある内容を `/usr/local/texlive/texmf-local/web2c/texmf.cnf` に追記する（ファイルがなければ作る）。

### 2. map ファイルのコピー

`ptex-fontmaps` ディレクトリ以下を `/usr/local/texlive/texmf-local/fonts/map/dvipdfmx/ptex-fontmaps/` にコピーする。

### 3. フォントの適用

`sudo mktexlsr` をする。

`sudo kanji-config-updmap-sys --jis2004 [name]` を叩くことでデフォルトの日本語フォントが反映される。`[name]` は `ryo-plusn` もしくは `shuei`。

`sudo kanji-config-updmap-sys status` で適用されているかを確認できる。

## 実装されている fontmaps

### ryo-plusn

りょう Text PlusN / りょう Display PlusN / りょうゴシック PlusN を使ったもの。丸ゴシックのみスーラ。

### shuei

DNP の秀英明朝 / 秀英四号太かな / 秀英角ゴシック金 / 秀英丸ゴシックを使ったもの。

## 自前で fontmaps を作る

`/usr/local/texlive/[year]/texmf-dist/fonts/map/dvipdfmx/ptex-fontmaps` にある fontmaps を参考にする。`morisawa-pr6n` が確実。

各フォントのファイル名と PostScript 名は `list.py` を実行すると得られる。
