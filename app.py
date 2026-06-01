import streamlit as st
from scraper.linkedin_scraper import extract_job_titles
from browser.browser_manager import start_browser


st.title("LinkedIn AI Agent")


if "browser_opened" not in st.session_state:
    st.session_state.browser_opened = False


if st.button("Open LinkedIn"):
    if not st.session_state.browser_opened:
        playwright, browser, page = start_browser()
        st.session_state.browser_opened = True
        page.goto("https://www.linkedin.com/jobs/collections/easy-apply/")
        st.success("LinkedIn Opened!")
        extract_job_titles(page)
     
    else:
        st.warning("Browser already running!")