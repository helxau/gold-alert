import os, requests, yfinance as yf

df = yf.download("GC=F", period="5d", interval="5m", progress=False)
c = df["Close"].squeeze()
f, s = c.rolling(8).mean(), c.rolling(21).mean()
prev = f.iloc[-3] - s.iloc[-3]
cur = f.iloc[-2] - s.iloc[-2]

msg = None
if prev <= 0 < cur:
    msg = f"🟢 کراس صعودی طلا XAU (SMA 8/21، ۵ دقیقه)\nقیمت: {c.iloc[-2]:.2f}"
elif prev >= 0 > cur:
    msg = f"🔴 کراس نزولی طلا XAU (SMA 8/21، ۵ دقیقه)\nقیمت: {c.iloc[-2]:.2f}"

if msg:
    requests.post(
        f"https://api.telegram.org/bot{os.environ['TOKEN']}/sendMessage",
        data={"chat_id": os.environ["CHAT_ID"], "text": msg},
    )
