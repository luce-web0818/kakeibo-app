# 家計簿アプリ

## 概要
Python(Django)で作成した家計簿WEBアプリです。
日々の収入・支出を管理し、月ごとの合計金額を確認できます。

## 主な機能
- 支出・収入の記録
- 一覧表示（新しい順）
- 編集・削除機能
- 当月の合計金額・件数の表示

## 使用技術
- Python
- Django
- HTML / CSS

## 機能
- 支出の登録
- 支出一覧表示

## 工夫した点
- ユーザーが直感的に操作できるよう、シンプルで見やすいUIを意識

## 今後の改善予定
- カテゴリ分け機能
- グラフ表示
- デザインの改善
- ログイン機能の追加

## アプリ画面

### ホーム画面
![ホーム画面](https://github.com/user-attachments/assets/4afbbfac-9b3b-469d-813e-4ff67daabc7b)

### 支出一覧画面
![支出一覧](https://github.com/user-attachments/assets/573a5097-db38-4017-8a3f-5679fa169d80)

### 入力画面
![入力画面](https://github.com/user-attachments/assets/d1777093-044b-45b3-9920-7eda927fe7a4)


## 環境構築・起動方法

```bash
git clone https://github.com/luce-web0818/kakeibo-app.git
cd kakeibo-app
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py runserver




