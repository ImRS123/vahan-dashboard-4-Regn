import streamlit as st

def main():
    st.title("Vahan Dashboard 4 Regn")

    # Read the content of your HTML file
    with open("Vahan Dashboard 4 Regn.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # Display the HTML content in the Streamlit app
    st.markdown(html_content, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
