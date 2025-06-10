# 概要
Pyinstallerを使ったPyQtのパッケージ作成から、
github actionsを使ってwindows/macようにビルドして配布するまでの工程をここに残します。

## 開発環境
- macOS Sequoia 15.5
- VsCode
- zsh 5.9 (arm64-apple-darwin24.0)

## 前提条件

システムに以下がインストールされていることを確認してください:

- Python 3.10
- uv pip (インストールは[こちら](https://docs.astral.sh/uv/getting-started/installation/))


## ローカルでのセットアップ

1. UVを使ってプロジェクトの作成
    ```zsh
    uv init -p 3.10
    uv add pyqt5 pyinstaller
    ```
2. app.pyの作成
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
1. ローカル起動テスト
   ```zsh
   uv run app.py
   ```
2. ローカルパッケージ作成テスト
   ```zsh
   uv run pyinstaller app.py
   ```
3. パッケージ起動のテスト
   ```
   uv run dist/app/app 
   ```