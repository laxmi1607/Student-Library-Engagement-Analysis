@echo off
echo Starting Student Library Dashboard...
python -c "import streamlit, pandas, openpyxl, matplotlib, numpy" >nul 2>&1
if errorlevel 1 (
  echo Installing required packages...
  python -m pip install streamlit pandas openpyxl matplotlib numpy
)
python -m streamlit run dashboard.py
pause
