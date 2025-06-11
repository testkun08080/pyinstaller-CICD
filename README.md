# 概要
Pyinstallerを使ったPyQtのパッケージ作成から、  
github actionsを使ってタグの作成に応じて、windows/macようにビルドして配布するまでの工程をここに残します。

## 開発環境
- macOS Sequoia 15.5
- VsCode
- zsh 5.9 (arm64-apple-darwin24.0)

## 前提条件

システムに以下がインストールされていることを確認してください:

- Python 3.10
- uv pip (インストールは[こちら](https://docs.astral.sh/uv/getting-started/installation/))


## ローカルでのセットアップ

1. プロジェクトフォルダの作成
   ```
   mkdir pyinstaller-CICD
   cd pyinstaller-CICD
   ```

2. UVを使ってプロジェクトの作成
    ```zsh
    uv init -p 3.10
    uv add pyqt5 pyinstaller
    ```
3. app.pyの作成
   ```
   cat <<EOL > app.py
   import sys
   from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

   class HelloWindow(QWidget):
      def __init__(self):
         super().__init__()
         self.setWindowTitle("Hello PyQt5")
         self.setGeometry(100, 100, 300, 100)

         layout = QVBoxLayout()
         label = QLabel("Hello from PyQt5!")
         layout.addWidget(label)
         self.setLayout(layout)


   if __name__ == "__main__":
      app = QApplication(sys.argv)
      window = HelloWindow()
      window.show()
      sys.exit(app.exec_())
   EOL
   ```

4. ローカル起動テスト
   ```zsh
   uv run app.py
   ```
5. ローカルパッケージ作成テスト
   ```zsh
   uv run pyinstaller app.py
   ```
6. パッケージ起動のテスト
   ```
   uv run dist/app/app 
   ```

## GitHub ActionsでCI/CDを組む

1. `.github/workflows/oldpyinstaller-build.yml`のダウンロード  
   ```zsh
   # 保存先ディレクトリ
   TARGET_DIR=".github/workflows"

   # 保存先ディレクトリを作成（存在しない場合のみ）
   mkdir -p "$TARGET_DIR"

   # ダウンロードするファイルの正しいURL
   FILE_URL="https://raw.githubusercontent.com/testkun08080/pyinstaller-CICD/main/.github/workflows/pyinstaller-build.yml"

   # ファイルをダウンロード
   curl -o "$TARGET_DIR/pyinstaller-build.yml" "$FILE_URL"

   # 結果の確認
   if [ -f "$TARGET_DIR/pyinstaller-build.yml" ]; then
      echo "ファイルが正常に保存されました: $TARGET_DIR/pyinstaller-build.yml"
   else
      echo "ダウンロードに失敗しました。"
      exit 1
   fi
   ```

2. 新しいレポジトリの作成とコミット
   ```bash
   git init .
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/username/pyinstaller-CICD.git
   git branch -M main
   git push -u origin main
   ```

3. タグの作成
   ```
   git tag -a v1.0.0 -m "Release version 1.0.0"
   ```
4. リリース
   ```
   git push origin v1.0.0
   ```
5. ご自身のリリースページへ行って以下の様にリリースされていれば成功です。

   <img src="https://github.com/testkun08080/pyinstaller-CICD/blob/main/docs/sample-release.png">
   
   このレポのリリースページは[こんな感じ](https://github.com/testkun08080/pyinstaller-CICD/releases)です。

