import boto3
import streamlit as st

# Initialize the S3 client
s3 = boto3.client('s3')

# Function to read file from S3 bucket
def read_from_s3(bucket_name, file_name):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        contents = response['Body'].read().decode('utf-8')
        return contents
    except Exception as e:
        st.error(f"Error reading file from S3: {e}")
        return None

# Main function to run the SecurityChatBot
def run_security_chatbot():
    # Set the title and description
    st.title("Security ChatBot")
    st.write("Welcome to the Security ChatBot!")

    # Get the S3 bucket and file name from the user
    bucket_name = st.text_input("Enter S3 bucket name:")
    file_name = st.text_input("Enter file name to read from S3:")

    # Read the file from S3
    if st.button("Read File"):
        if bucket_name and file_name:
            file_contents = read_from_s3(bucket_name, file_name)
            if file_contents:
                st.success("File read successfully!")
                st.code(file_contents)
        else:
            st.warning("Please enter the S3 bucket name and file name.")

# Run the SecurityChatBot
if __name__ == "__main__":
    run_security_chatbot()
