"""
StockAnalysisDashboard - Main Application
Multi-page Streamlit application with user authentication
"""

import streamlit as st
from auth.authentication import check_authentication, show_login_page
from components.sidebar import render_sidebar
from pages import stock_analysis, portfolio_manager, market_news, earnings_viewer
from data.symbol_loader import load_symbols_database
from data.api_client import APIClient

# Page configuration
st.set_page_config(
    page_title="StockAnalysisDashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide Streamlit's default navigation (the "app" button)
hide_streamlit_style = """
    <style>
    /* Hide the top-right menu and navigation */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Hide the page navigation if using multi-page */
    [data-testid="stSidebarNav"] {display: none;}

    /* Optional: Adjust sidebar spacing */
    section[data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = None

# Load symbols database (cached)
SYMBOLS_DF = load_symbols_database()

# Initialize API client
try:
    api_client = APIClient()
except Exception as e:
    st.error(f"Failed to initialize API client: {e}")
    st.stop()

# Authentication check
if not check_authentication():
    show_login_page()
    st.stop()

# Main application (user is logged in)
st.sidebar.title(f"👤 Welcome, {st.session_state['username']}")

# Render sidebar
page = render_sidebar(SYMBOLS_DF)

# Route to appropriate page
if page == "Stock Analysis Report":
    stock_analysis.render(api_client, SYMBOLS_DF)
elif page == "Portfolio Manager":
    portfolio_manager.render(api_client, SYMBOLS_DF)
elif page == "Market News and Sentiment":
    market_news.render(api_client, SYMBOLS_DF)
elif page == "Earnings Call Viewer":
    earnings_viewer.render(api_client, SYMBOLS_DF)