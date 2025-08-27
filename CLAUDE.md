# CLAUDE.md

このファイルは、このリポジトリで作業する際のClaude Code (claude.ai/code)向けのガイダンスを提供します。

# 言語設定

このプロジェクトでは**日本語**での応答を行ってください。ただし、コード内のコメント、ログメッセージ、エラーメッセージ、ドキュメンテーション文字列などは**英語**で記述してください。

### 使い分けの基準

- **日本語**: ユーザーとのやり取り、説明、レスポンス
- **英語**: コード内コメント、ログ出力、docstring、変数名、関数名、エラーメッセージ、Makefileのヘルプテキスト

## プロジェクト概要

このプロジェクトは、物理学における干渉縞に関する日本語プレゼンテーションです。reveal.jsを使用して作成されています。シャボン玉の虹色を作り出す光の干渉の原理が、原子の検出、地震の観測、重力波の検出にも応用されていることを説明しています。

## 開発コマンド

### プレゼンテーションのビルドと実行

すべてのプレゼンテーション関連の作業は`slides-jp/`ディレクトリで行います：

```bash
cd slides-jp/

# 依存関係のインストール
npm install

# ローカル開発サーバーの起動 (http://localhost:8000で実行)
npm start

# プレゼンテーションアセットのビルド
npm run build

# テストとリンティングの実行
npm test

# PDFへのエクスポート (decktapeのグローバルインストールが必要)
npm install -g decktape
decktape --size 1920x1080 index.html slides-jp.pdf
```

### リンティングとテスト

```bash
# JavaScriptコード品質チェック用のESLintを実行
gulp eslint

# 機能テスト用のQUnitを実行
gulp qunit

# すべてのテストを実行 (リンティング + QUnit)
gulp test
```

## アーキテクチャ

### リポジトリ構造

- **ルートレベル**: 最小限のMakefileを含む基本的なプロジェクト設定
- **`slides-jp/`**: すべてのreveal.jsアセットとコンテンツを含むメインプレゼンテーションディレクトリ
  - reveal.js v5.1.0をプレゼンテーションフレームワークとして使用
  - アセットコンパイルと開発サーバー用のGulpベースのビルドシステム
  - 数式用のKaTeXを使用したMarkdownベースのスライドをサポート

### 主要技術

- **プレゼンテーションフレームワーク**: カスタムSkyテーマを使用したreveal.js
- **ビルドツール**: JavaScriptバンドルとトランスパイル用のGulp、Rollup、Babel
- **スタイリング**: CSSコンパイル用のautoprefixerを使用したSass/SCSS
- **数式レンダリング**: スライド内の数式用のKaTeX
- **コードハイライト**: 構文ハイライト用のhighlight.js
- **テスティング**: 自動テスト用のPuppeteerを使用したQUnit

### コンテンツ構造

- **メインプレゼンテーションファイル**: `slides-jp/index.html` - Markdownを使用したスライド構造を含む
- **原稿**: `slides-jp/manuscript-jp.md` - プレゼンテーションのフルテキスト版
- **アセット**: `slides-jp/assets/images/` - すべてのプレゼンテーション画像を含む
- **カスタムスタイル**: `slides-jp/styles/custom-style.css` - プレゼンテーション固有のスタイリング

### ビルドパイプライン

Gulpビルドシステムは以下を処理します：

1. Rollupを介したJavaScriptバンドル（ES5およびES6モジュール）
2. SassコンパイルとCSS圧縮
3. reveal.js拡張機能用のプラグインコンパイル
4. 開発中のライブリロード
5. QUnitとESLintを使用したテスト

## 動画制作（Manim）

### 波の干渉アニメーション

`scripts/wave_interference/`ディレクトリには、YouTube動画用の波の干渉アニメーションが含まれています：

```bash
cd scripts

# Manimの依存関係をインストール
pip install -r requirements.txt

# 強め合う干渉の動画を生成（高画質）
manim -qh wave_interference/constructive_interference.py ConstructiveInterference --media_dir ../videos

# 弱め合う干渉の動画を生成（高画質）
manim -qh wave_interference/destructive_interference.py DestructiveInterference --media_dir ../videos

# 低画質版（テスト用）
manim -ql wave_interference/constructive_interference.py ConstructiveInterference --media_dir ../videos
```

### 出力される動画

- **強め合う干渉**: `videos/videos/constructive_interference/1080p60/ConstructiveInterference.mp4`
- **弱め合う干渉**: `videos/videos/destructive_interference/1080p60/DestructiveInterference.mp4`

これらの動画はPremiere Proでの編集に適したシンプルな構成で作成されています。

### Manimアニメーション内容

1. **ConstructiveInterference**: 同位相の2つの正弦波が重なり、振幅が2倍になる様子
2. **DestructiveInterference**: 位相が180度ずれた2つの正弦波が打ち消し合う様子

各アニメーションには波の動きとラベルが含まれ、物理現象の理解を助ける視覚的説明が提供されます。

## 重要な注意事項

- プレゼンテーションは日本語で、干渉パターンに関する物理概念をカバーしています
- すべてのスライド開発は`slides-jp/`ディレクトリで行う必要があります
- ビルドシステムはHTML、Markdown、JavaScript、CSSファイルの変更を監視します
- PDFエクスポートには`decktape`ツールのグローバルインストールが必要です
- Manimアニメーションは`videos/`ディレクトリに出力されます（.gitignoreで除外済み）

## コミット規則

### コミットメッセージ規則

- **形式**: `<emoji> <type>: <description>`
- **言語**: 英語（日本語プロジェクトでも統一）
- **分割原則**: 論理的変更単位ごと、1コミット1目的

### 絵文字プレフィックス

- ✨ **feat**: 新機能追加
- 🐛 **fix**: バグ修正
- 📚 **docs**: ドキュメント更新
- ♻️ **refactor**: リファクタリング
- ✅ **test**: テスト追加・修正
- 🔧 **chore**: 雑務・設定変更
- 🔒 **security**: セキュリティ関連
- 🚀 **perf**: パフォーマンス改善

### 必須フッター

すべてのコミットに以下を含める：

```text
🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### 例

```text
✨ feat: implement secure NASA Earthdata authentication system
📚 docs: add comprehensive EULA approval process  
♻️ refactor: consolidate Python scripts under src/ directory
🔒 security: remove personal client_ID from documentation
```