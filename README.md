AI Company Stock Analysis Dashboard

This project builds an interactive stock analysis dashboard using Python, designed to visualize and analyze stock performance for major AI companies. It integrates technical indicators such as SMA, EMA, and RSI for informed decision-making.

================================================================================================================================================

Features

Real-time Data: Fetches stock data from Yahoo Finance for top AI companies.

Technical Indicators: Calculates and visualizes Simple Moving Average (SMA), Exponential Moving Average (EMA), and Relative Strength Index (RSI).

Interactive Widgets: Select companies and date ranges using dropdowns and date pickers.

Dynamic Plotting: Visualize closing prices with overlaid technical indicators.

Cursor Interaction: Hover over plots to see detailed values and dates.

================================================================================================================================================

Requirements

Ensure the following packages are installed:

!pip install yfinance ta ipywidgets mplcursors
================================================================================================================================================

Usage

Clone the repository or copy the script into Google Colab.

Run the script to install dependencies and fetch stock data.

Use the dropdown and date pickers to select the company and date range.

Analyze price trends and indicators on an interactive plot.

================================================================================================================================================


How It Works

Stock Data Retrieval: The script downloads historical stock data for AI giants like NVIDIA, Tesla, Google, Microsoft, Meta, AMD, Intel, IBM, Cisco, and Oracle.

Indicator Calculation: SMA (50-day), EMA (20-day), and RSI (14-day) are computed for each company.

Visualization: The dashboard plots closing prices and overlays indicators with distinct neon colors for better visualization.

Interactive Elements: Use widgets to dynamically adjust the company and date, updating plots in real-time.

================================================================================================================================================


Demo

Select a company from the dropdown.

Choose start and end dates.

View dynamic stock price plots with overlaid technical indicators.

Example Companies

NVIDIA (NVDA)

Tesla (TSLA)

Google (GOOGL)

Microsoft (MSFT)

Meta (META)

================================================================================================================================================


Contributions

Feel free to fork, improve, and submit pull requests.

================================================================================================================================================


License

MIT License.

