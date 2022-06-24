from art import text2art
from colorama import Fore
from pathlib import Path
from gtts import gTTS # https://github.com/pndurette/gTTS

def main():
    print(Fore.BLUE + text2art('txt_to_mp3', font='buldhead'))
    print(Fore.RESET + "")

    file_path = input(Fore.RESET + "Enter a file's path: ")
    lang = input("Choose lang 'en' or 'ru': ")

    path = Path(file_path)

    if path.is_file() and path.suffix == '.txt' and lang in ['en', 'ru']:
        print(f'[+] Original path {path.name}')
        print(f'[+] Processing...')

        with open(file_path, encoding='utf-8') as f:
            text = f.read().replace('\n', ' ')

        audio = gTTS(text=text, lang=lang, slow=False)
        audio_path = str(path.parent) + '\\' + path.stem + '.mp3'
        audio.save(audio_path)

        print(f"[+] {path.stem}.mp3 saved successfully!")

    else:
        print('Something went worng')

if __name__ == '__main__':
    main()