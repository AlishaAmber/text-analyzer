import streamlit as st

# Function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# Function to analyze text
def analyze_text():
    # Streamlit UI
    st.title("📑 Text Analyzer")

    # User input
    paragraph = st.text_area("Enter your paragraph:", "")

    if paragraph:  # Validate non-empty input
        words = paragraph.split()
        total_words = len(words)
        total_characters = len(paragraph)
        vowels_count = count_vowels(paragraph)

        # Check if "Python" is in the text
        contains_python = "Python" in paragraph

        # Display statistics
        st.subheader("📊 Text Analysis Results")
        st.write(f"**Total Words:** {str(total_words)}")
        st.write(f"**Total Characters (including spaces):** {str(total_characters)}")
        st.write(f"**Number of Vowels:** {str(vowels_count)}")
        st.write(f"**Does the paragraph contain 'Python'?** {'Yes' if contains_python else 'No'}")

        # Search and Replace
        search_word = st.text_input("Enter a word to search for:")
        replace_word = st.text_input("Enter a word to replace it with:")

        if st.button("Replace Word"):
            modified_paragraph = paragraph.replace(search_word, replace_word)
            st.subheader("📝 Modified Paragraph:")
            st.write(modified_paragraph)

        # Uppercase & Lowercase Conversion
        st.subheader("🔠 Uppercase & Lowercase Conversion")
        st.write("**Uppercase:**", paragraph.upper())
        st.write("**Lowercase:**", paragraph.lower())

        # Calculate average word length
        average_word_length = total_characters / total_words if total_words else 0
        st.write(f"**Average Word Length:** {round(average_word_length, 2)}")

# Run the text analyzer
analyze_text()
