# 波の干渉アニメーション

物理現象「波の干渉」を可視化するManimアニメーションです。

## 必要環境

- Python 3.8以上
- FFmpeg（動画出力に必要）

## インストール

```bash
# scriptsディレクトリに移動
cd scripts

# 依存関係のインストール
pip install -r requirements.txt
```

## アニメーション一覧

### 1. 強め合う干渉（Constructive Interference）
同位相の2つの正弦波が重なり、振幅が2倍になる様子を表示します。

```bash
manim -pql wave_interference/constructive_interference.py ConstructiveInterference
```

### 2. 弱め合う干渉（Destructive Interference）
位相が180度ずれた2つの正弦波が重なり、打ち消し合う様子を表示します。

```bash
manim -pql wave_interference/destructive_interference.py DestructiveInterference
```

## 出力オプション

### 画質の設定
- `-ql` : 低画質（480p）- テスト用
- `-qm` : 中画質（720p）
- `-qh` : 高画質（1080p）
- `-qk` : 4K画質（2160p）

### その他のオプション
- `-p` : レンダリング後に自動再生
- `-s` : 最後のフレームのみを出力（静止画）
- `--fps 60` : フレームレートを60fpsに設定

### 例：高画質でレンダリング
```bash
manim -pqh wave_interference/constructive_interference.py ConstructiveInterference
```

### 例：透過背景で出力
```bash
manim -pqh --transparent wave_interference/constructive_interference.py ConstructiveInterference
```

## 出力ファイルの場所

レンダリングされた動画は以下のディレクトリに保存されます：

```
media/videos/{ファイル名}/{画質}/
```

例：
```
media/videos/constructive_interference/1080p60/ConstructiveInterference.mp4
```

## カスタマイズ

各Pythonファイルを編集することで、以下の要素をカスタマイズできます：

- 波の色
- 振幅の大きさ
- アニメーションの速度
- テキストの内容
- 背景色

## トラブルシューティング

### FFmpegエラーが出る場合

MacOS:
```bash
brew install ffmpeg
```

Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

Windows:
FFmpegを[公式サイト](https://ffmpeg.org/download.html)からダウンロードし、PATHに追加してください。

### Manimのインストールに失敗する場合

```bash
# pipをアップグレード
pip install --upgrade pip

# Manimを再インストール
pip uninstall manim
pip install manim
```