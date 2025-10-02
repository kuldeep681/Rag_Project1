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



    # def render(self):
    #     with st.sidebar:
    #         st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGo0bTRwNDBmNXY5bHhxaDJ4ZTIwamxlMmEwdWVkZG14MXV4czJrbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GghGKaZ8JeHJx0apQC/giphy.gif",
    #                  width=80 )
    #         st.title("Interview Me")

    #         st.subheader("Employee Information")
    #         st.write(self.employee_information)

    #     self.render_messages()

    #     self.render_user_input()



    

    def render(self):
        # --- CSS Injection to reduce top spacing in the sidebar ---
        st.markdown(
            """
            <style>
            section[data-testid="stSidebar"] {
            padding-top: 0rem !important;
            }
            div[data-testid="stSidebarContent"] {
            padding-top: 0rem !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        # --- END CSS Injection ---
    
        # Access the raw employee information dictionary directly
        employee_info = self.employee_information 

        orange_style = "color: #FFA500; font-weight: 500;"
        
        with st.sidebar:
            # --- START: Branding Header (Styled and Aligned) ---
            # Define columns to put the image and title side-by-side
            col1, col2 = st.columns([1, 3])  

            with col1:
                st.image(
                    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGo0bTRwNDBmNXY5bHhxaDJ4ZTIwamxlMmEwdWVkZG14MXV4czJrbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GghGKaZ8JeHJx0apQC/giphy.gif",
                    width=80 
                )

            with col2:
                # Custom Markdown for a stylish, vertically centered title
                st.markdown(
                    """
                    <div style="
                    display: flex; 
                    align-items: center; 
                    height: 80px;
                    padding-left: 20px; 
                    font-size: 26px; 
                    font-weight: 800; 
                    letter-spacing: 1px; 
                    color: #00BFFF; 
                    text-shadow: 1px 1px 2px #000000; 
                    ">INTERVIEW ME
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            # --- END: Branding Header ---
        
            # Add a custom styled separator line
            st.markdown("<hr style='border: 1px solid #444444; margin-top: 10px; margin-bottom: 20px;'>", unsafe_allow_html=True) 

        
            # --- START: Employee Profile Context Badge ---
            st.markdown(
                """
                <div style="
                background-color: #333333; 
                padding: 5px 10px; 
                border-radius: 5px; 
                font-weight: bold; 
                color: #FFFFFF; 
                margin-bottom: 15px;">
                PROFILE DETAILS
                </div>
                """, 
                unsafe_allow_html=True
            )
            # --- START: Structured Data Display ---
        
            # 1. Display Full Name (Value is Orange)
            name_value = employee_info.get('name', 'N/A') + " " + employee_info.get('lastname', '')
            st.markdown(f"**Name:** <span style='{orange_style}'>{name_value}</span>", unsafe_allow_html=True)

            # 2. Highlight the Goal (The st.info box is visually distinct, but we'll color the value)
            goal_value = employee_info.get('current_goal', 'N/A')
            st.markdown(f"**Goal:** <span style='{orange_style}'>{goal_value}</span>", unsafe_allow_html=True)

            # 3. Display Position (Value is Orange)
            position_value = employee_info.get('position', 'N/A')
            st.markdown(f"**Position:** <span style='{orange_style}'>*{position_value}*</span>", unsafe_allow_html=True)

            # 4. Display Department (Value is Orange)
            department_value = employee_info.get('department', 'N/A')
            st.markdown(f"**Department:** <span style='{orange_style}'>{department_value}</span>", unsafe_allow_html=True)

            # # Email (Value is Orange)
            # email_value = employee_info.get('email', 'N/A')
            # st.markdown(f"**Email:** <span style='{orange_style}'>{email_value}</span>", unsafe_allow_html=True)

            # Email (Value is Orange, NO UNDERLINE/BLUE LINK)
            email_value = employee_info.get('email', 'N/A')
            st.markdown(
                f"**Email:** <span style='color: #FFA500; font-weight: 500; text-decoration: none;'>{email_value}</span>", 
                unsafe_allow_html=True)
        
            # Phone (Value is Orange)
            phone_value = employee_info.get('phone_number', 'N/A')
            st.markdown(f"**Phone:** <span style='{orange_style}'>{phone_value}</span>", unsafe_allow_html=True)

            # 5. Display the Skills (0-indexed using st.json)
            st.subheader("Technical Skills:")
        
            # st.json is used to show the raw list, which displays the 0-indexed keys clearly
            st.json(employee_info.get('skills', []))
        
            # --- END: Structured Data Display ---
            
        # These functions render the main chat window content (outside the sidebar)
        self.render_messages()
        self.render_user_input()