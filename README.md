# 家計簿アプリ

## 概要
日々の支出を記録・一覧表示できるシンプルな家計簿アプリです。

## 使用技術
- Python
- Django
- HTML / CSS

## 機能
- 支出の登録
- 支出一覧表示

## 工夫した点
- シンプルで見やすいUIを意識
- 初心者でも扱いやすい構成

## 今後の改善予定
- カテゴリ分け機能
- 編集・削除機能
- グラフ表示

## アプリ画面

![ホーム画面](https://github.com/user-attachments/assets/4afbbfac-9b3b-469d-813e-4ff67daabc7b)
![支出一覧](https://github.com/user-attachments/assets/573a5097-db38-4017-8a3f-5679fa169d80)


## 環境構築・起動方法

```bash
git clone https://github.com/luce-web0818/kakeibo-app.git
cd kakeibo-app
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py runserver




