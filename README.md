# discordpy-railway

- railway.app で discord.py を始めるテンプレートです。
- Use Template からご利用ください。

## 各ファイル情報

### main.py
PythonによるDiscordBotのアプリケーション起点ファイルです。

### constant.py
DiscordBot(アプリケーション)で使用する定数を格納するファイルです。

### .env.example
プロジェクト内で使用する環境変数を定義する.envファイルのテンプレートです。  
ローカル開発の際にはこれをコピーして .env ファイルを追加してください。

### requirements.txt
使用しているPythonのライブラリ情報の設定ファイルです。

### Procfile
Railwayでのアプリケーション起動コマンドの設定です。

### .github/workflows/flake8.yaml
GitHub Actions による自動構文チェックの設定ファイルです。

### .gitignore
Git管理が不要なファイル/ディレクトリの設定ファイルです。

### LICENSE
このリポジトリのコードの権利情報です。MITライセンスの範囲でご自由にご利用ください。

### README.md
このドキュメントです。

## 各ディレクトリ情報

### /cogs
discord.py の Cog ファイルを置くディレクトリです。

### /extensions
discord.py の Extension ファイルを置くディレクトリです。

### /utils
DiscordBot(アプリケーション)で使用する汎用関数群を置くディレクトリです。
