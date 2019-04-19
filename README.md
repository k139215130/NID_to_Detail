# NID_to_Detail

## 環境設定

```
pip install -r requirements.txt
```

## Code

### 單筆查詢

1. 執行 `single.py`
3. 輸入學號、密碼、欲查詢學號
4. 結果顯示於終端機上

![](https://i.imgur.com/09B3BXZ.png)


#### 錯誤資訊

+ 若出現 未使用校內網路 則有以下可能:
    + 網頁無回應，請檢察您的網路
    + 您為使用校內網路，請使用校內網路
+ 若出現 帳號密碼輸入錯誤 則有以下可能:
    + 您無權進入系統
    + 您的帳號輸入錯誤，密碼不一定
+ 若出現 密碼輸入錯誤 則有以下可能:
    + 您的密碼輸入錯誤，帳號是對的

### 多筆查詢

1. 於 `example.xlsx` 輸入欲查詢學號

2. 執行 `multi.py`

3. 若有資料查詢不到，則會詢問您 是否將無資料欄位標註為紅色，請輸入y或n來決定

4. 結果產生於 `ouput.xlsx`

> 檔名請勿更改

+ `example.xlsx`
    + ![](https://i.imgur.com/uMARdWx.png)
+ 執行 `multi.py`
    + ![](https://i.imgur.com/6NPYriA.png)
+ `output.xlsx`
    + ![](https://i.imgur.com/PFaSAH3.png)


#### 錯誤資訊

+ 若出現 未使用校內網路 則有以下可能:
    + 網頁無回應，請檢察您的網路
    + 您為使用校內網路，請使用校內網路
+ 若出現 帳號密碼輸入錯誤 則有以下可能:
    + 您無權進入系統
    + 您的帳號輸入錯誤，密碼不一定
+ 若出現 密碼輸入錯誤 則有以下可能:
    + 您的密碼輸入錯誤，帳號是對的

## Web

## 單筆查詢

+ 輸入帳號、密碼、欲查詢學號
    + ![](https://i.imgur.com/5gotIAt.png)
+ 結果展示在下方
    + ![](https://i.imgur.com/nVbM2jP.png)

## 多筆查詢

+ 輸入帳號、密碼、欲查詢學號之 `.xlsx` 檔
    + ![](https://i.imgur.com/A8hmiEI.png)
    > 檔名不限
+ 若要存至資料庫(可繪製圖表)
    + 請將 **是否將資料存置資料庫 打勾**
    + 並填上 **名稱**
+ 送出後會自動下載 `output.xlsx`

## Chart

+ 最上層的 button 固定有**社課總人數**，後續的為上傳資料(名稱為 mutli 所填之名稱)
+ 每個名稱下有
    + 男女人數
    + 各系人數
    + 各年級人數
    + 各學院人數(未完成)
    + 詳細資料
+ 每個圖表可獨自下載為 `.png`

## Edit

+ 最上方按鈕為各個名稱
+ 點擊後有該名稱知詳細資料
+ 最上方右邊刪除按鈕為刪除整個名稱
+ 下方之刪除按鈕為刪除該筆資料

## 畫面

+ 首頁
    + ![](https://i.imgur.com/wbh56Nk.png)
+ Single
    + ![](https://i.imgur.com/wB45uw6.png)
+ Multi
    + ![](https://i.imgur.com/Hja3f72.png)
+ Chart
    + ![](https://i.imgur.com/WhcxWAX.png)
    + ![](https://i.imgur.com/fYRHMsr.png)
+ Edit
    + ![](https://i.imgur.com/F647doR.png)
    + ![](https://i.imgur.com/tL9b1SG.png)