import tkinter as tk
import random
from tkinter import PhotoImage


def generate_key():

    letter_1 = chr(random.randint(ord('A'), ord('Z')))
    lettr_2 = chr(random.randint(ord('A'), ord('Z')))


    start_ord = min(ord(letter_1) - ord('A') + 1, ord(lettr_2) - ord('A') + 1)
    end_ord = max(ord(letter_1) - ord('A') + 1, ord(lettr_2) - ord('A') + 1)


    interval_letters = [chr(i + ord('A') - 1) for i in range(start_ord, end_ord + 1)]


    random.shuffle(interval_letters)


    block1 = f"{start_ord:02d}"
    block2 = ''.join(interval_letters[:7])
    block3 = f"{end_ord:02d}"

    generated_key = f"{block1} {block2} {block3}"


    key_label.config(text=generated_key)


window = tk.Tk()
window.title("Key Generator")


window.geometry("400x400")
window.configure(bg="white")

try:
    background_image = PhotoImage(file="encryption-key-generator.png")
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading background image: {e}")


key_label = tk.Label(window, text="Generated Key", font=("Helvetica", 16), bg="white", fg="black")
key_label.pack(pady=30)

generate_button = tk.Button(window, text="Generate Key", font=("Helvetica", 12), command=generate_key)
generate_button.pack(pady=20)


window.mainloop()