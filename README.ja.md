# ResetSyncCommand

# Japanese
## 概要
Discord botのテスト時に発生する、古いスラッシュコマンドとの混同（表示の重複や不要なコマンドの残留）を解消するため、コマンドの同期・リセットを行うプログラムです。

## 使用技術
- 言語: Python 3.x
- ライブラリ/フレームワーク: discord.py, python-dotenv
- データベース: なし
- その他: なし

## 使い方

### 前提条件
Python 3.x がインストールされていること
Discord Botのトークンを取得済みであること

### インストール方法
以下の手順に従って、ご自身の環境にプロジェクトをセットアップしてください。

1. リポジトリをクローンします。
```bash
git clone https://github.com/ay2416/ResetSyncCommand.git
```

2. プロジェクトのディレクトリに移動します。
```bash
cd ResetSyncCommand
```

3. 必要なパッケージをインストールします。
```bash
pip install discord.py python-dotenv
```

### 基本的な使い方
```bash
python main.py
```

## 主な機能
- **グローバルコマンドおよびギルドコマンドの同期**
  新しいコマンドを反映させ、古いコマンドの残留を防ぎます。
- **`/test` コマンド**
  コマンドの同期が正常に完了したかを確認するためのテストコマンドを提供します。

## 設定
プロジェクトルートディレクトリに `.env` ファイルを作成し、以下の環境変数を設定してください。
- `token`: Discord Botのトークン

また、`main.py` 内の以下の変数を、テスト対象のサーバー（ギルド）IDに変更してください。
- `guild_id`: テスト用サーバーのID

## ライセンス
The Unlicense


# English
## Overview
This program performs a reset and synchronization of slash commands to eliminate mix-ups (such as duplicate displays or residual unnecessary commands) with old slash commands when testing a Discord bot.

## Tech Stack
- Language: Python 3.x
- Libraries/Frameworks: discord.py, python-dotenv
- Database: None
- Other: None

## Usage

### Prerequisites
Python 3.x must be installed.
A Discord Bot token must be obtained.

### Installation
Follow the steps below to set up the project in your local environment.

1. Clone the repository.
```bash
git clone https://github.com/ay2416/ResetSyncCommand.git
```

2. Navigate to the project directory.
```bash
cd ResetSyncCommand
```

3. Install the required packages.
```bash
pip install discord.py python-dotenv
```

### Basic Usage
```bash
python main.py
```

## Main Features
- **Global and Guild Command Synchronization**
  Applies new commands and prevents old commands from remaining.
- **`/test` Command**
  Provides a test command to verify that the command synchronization has been completed successfully.

## Configuration
Create a `.env` file in the project root directory and set the following environment variable:
- `token`: Your Discord Bot token.

Additionally, modify the following variable in `main.py` to the target test server (guild) ID:
- `guild_id`: The ID of the test server.

## License
The Unlicense
