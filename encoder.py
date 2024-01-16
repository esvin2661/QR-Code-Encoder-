import qrcode

def generate_qr_code(data, file_name):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(file_name)

if __name__ == "__main__":
    # Example usage
    data_to_encode = "Hello, QR Code!"
    output_file_name = "my_qr_code.png"

    generate_qr_code(data_to_encode, output_file_name)
    print(f"QR Code generated and saved as {output_file_name}")
