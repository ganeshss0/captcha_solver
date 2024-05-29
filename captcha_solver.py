from PIL import Image
import pytesseract



def solve(image_path: str) -> str:
    '''
    Solve simple image captcha.
    # Parameters:
    image_path (str): Path to the image file.
    # Returns:
    text (str): The text in the captcha image.
    '''
    # Image file
    captcha_image = Image.open(image_path)
    
    
    # preprocess the image
    captcha_text = pytesseract.image_to_string(captcha_image, config='--psm 6')

    return captcha_text








if __name__ == '__main__':

    captcha_image_path = './Sample/captcha.png'

    solution = solve(captcha_image_path)

    print(solution)