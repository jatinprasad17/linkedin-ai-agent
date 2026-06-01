import time
import streamlit as st

def extract_job_titles(page):

    time.sleep(5)

    # proper ul selector
    ul = page.locator("div.scaffold-layout__list > div ul").first

    all_li = ul.locator("li")

    total_li = all_li.count()

    st.write(f"Total LI Tags: {total_li}")

    for i in range(min(total_li, 20)):

        try:

            li = all_li.nth(i)

            anchor = li.locator("a").first

            href = anchor.get_attribute("href")

            st.write("------------")
            st.write(f"LI INDEX: {i}")
            st.write(href)

        except Exception as e:

            st.write(f"ERROR IN LI {i}: {e}")