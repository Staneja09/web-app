import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import os

def generate_handwritten_image(text, font_path, font_size):
    # Create a blank white image
    image = Image.new("RGB", (800, 400), "white")
    draw = ImageDraw.Draw(image)

    # Load the handwriting font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except OSError:
        st.error("Font file not found. Please check the font path.")
        return None

    # Draw the text on the image
    draw.text((20, 100), text, font=font, fill="black")

    return image

def handwriting_tool():
    st.title("Text to Human Handwriting Tool")
    st.write("Convert your text to human-like handwriting on a blank white paper.")

    # Input for the text to convert
    user_text = st.text_area("Enter the text you want to convert to handwriting:", height=150)

    # Font settings
    font_size = st.slider("Font Size", 20, 100, 40)
    
    # Update the font path to your font file
    font_path = r"C:\Users\Samarth Taneja\Downloads\weddingday-font\WeddingdayPersonalUseRegular-1Gvo0.ttf"  # Ensure this path is correct

    if st.button("Generate Handwriting Image"):
        if user_text.strip() == "":
            st.warning("Please enter some text to generate handwriting.")
        else:
            # Generate the handwritten text image
            handwritten_image = generate_handwritten_image(user_text, font_path, font_size)

            if handwritten_image is not None:
                # Display the image
                st.image(handwritten_image, caption="Handwritten Text", use_column_width=True)

                # Provide a download button
                buf = io.BytesIO()
                handwritten_image.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download Handwritten Image",
                    data=byte_im,
                    file_name="handwritten_text.png",
                    mime="image/png"
                )

