import cv2
import streamlit as st
import numpy as np


def resize_image(image, scale_percent):
    try:
        # Decode the uploaded image
        image_array = np.frombuffer(image.read(), np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        # Check if the image was successfully loaded
        if img is None:
            raise ValueError("Image not found or cannot be opened")

        # Calculate new dimensions based on scaling percentage
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dsize = (width, height)

        # Resize the image
        resized_image = cv2.resize(img, dsize)

        # Return the resized image
        return resized_image

    except Exception as e:
        st.error(f"Error occurred: {e}")
        return None


def main():
    st.title("Image Resizer")

    # Upload the image file
    uploaded_image = st.file_uploader("Upload an image", type=["jpeg", "jpg", "png", "bmp"])

    if uploaded_image is not None:
        # Input for scale percentage
        scale_percent = st.slider("Select scale percentage", 1, 100, 50)

        # Input for output file name
        output_name = st.text_input("Enter the name of the resized image (without extension)")

        # Input for output format
        output_format = st.selectbox("Select the format for the resized image", ["jpg", "png", "bmp"])

        if st.button("Resize Image"):
            # Perform image resizing
            resized_image = resize_image(uploaded_image, scale_percent)

            if resized_image is not None:
                # Save the resized image as a temporary file
                output_path = f"{output_name}.{output_format}"
                cv2.imwrite(output_path, resized_image)

                # Show success message
                st.success(f"Image resized and saved as {output_path}")
                st.image(resized_image, channels="BGR", caption="Resized Image")


if __name__ == "__main__":
    main()
