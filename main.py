import streamlit as st

st.set_page_config(
    page_title = "Streamlit Playground",
    page_icon = "favicon.ico",
    layout = "centered",     # centered, wide
    initial_sidebar_state = "expanded",    # expanded, collapsed, auto
    menu_items = {
        "Get Help": "https://docs.streamlit.io/",
        "About": "Streamlit Playground"
    }
)

st.sidebar.title("Streamlit Playground")

st.title('Streamlit Playground')

print("STEP-1: reenter dashboard..")

# Initialize chat history
if "messages" not in st.session_state:
    print(f'new session messages added!')
    st.session_state.messages = []
else:
    msgs = st.session_state.messages
    print(f'msg not empty: {len(msgs)}')


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    print(f'msg: {message["content"]}')
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

print("STEP-2: finish showing messages..")

# React to user input
if prompt := st.chat_input("What is up?"):
    print(f'getting prompt: {prompt}')

    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    print("prompt added to messages session")

print("STEP-3: leaving page")