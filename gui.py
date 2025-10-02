import streamlit as st

class AssistantGUI:
    def __init__(self, assistant):
        self.assistant = assistant
        self.messages = assistant.messages
        self.employee_information = assistant.employee_information

    
    def get_response(self, user_input):
        return self.assistant.get_response(user_input)


    def render_messages(self):
        messages = self.messages

        for message in messages:
            if message["role"] == "user":
                st.chat_message("human").markdown(message["content"])
            if message["role"] == "ai":
                st.chat_message("ai").markdown(message["content"])

    
    def set_state(self, key, value):
        st.session_state[key] = value


    def render_user_input(self):
        user_input = st.chat_input("Type here...", key="input")
        if user_input and user_input != "":
            st.chat_message("human").markdown(user_input)

            response_generator = self.get_response(user_input)

            with st.chat_message("ai"):
                response = st.write_stream(response_generator)

            self.messages.append({"role": "user", "content": user_input})
            self.messages.append({"role": "ai", "content": response})

            self.set_state("messages", self.messages)



    def render(self):
        with st.sidebar:
            st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGo0bTRwNDBmNXY5bHhxaDJ4ZTIwamxlMmEwdWVkZG14MXV4czJrbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GghGKaZ8JeHJx0apQC/giphy.gif",
                     width=80 )
            st.title("Interview Me")

            st.subheader("Employee Information")
            st.write(self.employee_information)

        self.render_messages()

        self.render_user_input()