
!pip install yfinance ta ipywidgets mplcursors

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import ta
import ipywidgets as widgets
from IPython.display import display
import mplcursors

ai_companies = [
    "NVDA",  # NVIDIA
    "TSLA",  # Tesla
    "GOOGL", # Google
    "MSFT",  # Microsoft
    "META",  # Meta
    "AMD",   # AMD
    "INTC",  # Intel
    "IBM",   # IBM
    "CSCO",  # Cisco
    "ORCL"   # Oracle
]

start_date = "2023-01-01"
end_date = pd.Timestamp.today().strftime('%Y-%m-%d')

stock_data = pd.DataFrame()
for company in ai_companies:
    temp_data = yf.download(company, start=start_date, end=end_date)
    temp_data['Company'] = company
    stock_data = pd.concat([stock_data, temp_data])

stock_data.reset_index(inplace=True)
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
pivot_data = stock_data.pivot_table(values='Close', index='Date', columns='Company')

sma_period = 50
ema_period = 20
rsi_period = 14

for company in ai_companies:
    if company in pivot_data.columns:
        close_prices = pivot_data[company].squeeze()
        pivot_data[f'{company}_SMA'] = ta.trend.sma_indicator(close_prices, window=sma_period)
        pivot_data[f'{company}_EMA'] = ta.trend.ema_indicator(close_prices, window=ema_period)
        pivot_data[f'{company}_RSI'] = ta.momentum.rsi(close_prices, window=rsi_period)

company_widget = widgets.Dropdown(
    options=ai_companies,
    value='NVDA',
    description='Company:'
)

start_widget = widgets.DatePicker(
    description='Start Date',
    value=pd.to_datetime('2024-01-01')
)

end_widget = widgets.DatePicker(
    description='End Date',
    value=pd.to_datetime(pd.Timestamp.today())
)

def plot_stock(company, start, end):

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)


    filtered_data = pivot_data.loc[(pivot_data.index >= start) & (pivot_data.index <= end)]

    if filtered_data.empty:
        print(f"No data available for {company} from {start.date()} to {end.date()}")
        return


    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15, 8))


    line_close, = ax.plot(filtered_data.index, filtered_data[company], label=f'{company} Close Price', color='#00FFFF', linewidth=2)  # Cyan (Neon)
    line_sma, = ax.plot(filtered_data.index, filtered_data[f'{company}_SMA'], label='SMA 50', color='#FF00FF', linewidth=2)  # Magenta (Neon)
    line_ema, = ax.plot(filtered_data.index, filtered_data[f'{company}_EMA'], label='EMA 20', color='#00FF00', linewidth=2)  # Green (Neon)
    line_rsi, = ax.plot(filtered_data.index, filtered_data[f'{company}_RSI'], label='RSI', color='#FFA500', linewidth=2)  # Orange (Neon)
    ax.axhline(y=80, color='#FF4500', linestyle='--', linewidth=1.5, label='RSI Overbought (80)')
    ax.axhline(y=20, color='#32CD32', linestyle='--', linewidth=1.5, label='RSI Oversold (20)')
    ax.set_title(f'{company} - Technical Indicators', color='white', fontsize=16)
    ax.set_xlabel('Date', color='white', fontsize=12)
    ax.set_ylabel('Price / RSI', color='white', fontsize=12)
    ax.legend(facecolor='black', framealpha=1, fontsize=10)
    ax.grid(color='#333333', linestyle='--', linewidth=0.5)
    cursor = mplcursors.cursor([line_close, line_sma, line_ema, line_rsi], hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{sel.artist.get_label()}\nDate: {filtered_data.index[sel.index].date()}\nValue: {sel.target[1]:.2f}"))
    plt.show()


ui = widgets.HBox([company_widget, start_widget, end_widget])
out = widgets.interactive_output(plot_stock, {
    'company': company_widget,
    'start': start_widget,
    'end': end_widget
})

display(ui, out)
