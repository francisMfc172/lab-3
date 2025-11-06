import tkinter as tk
import random


def generate_key():
    # pick two random uppercase letters
    letter_1 = chr(random.randint(ord('A'), ord('Z')))
    letter_2 = chr(random.randint(ord('A'), ord('Z')))

    # convert to 1-based positions (1..26) and determine interval
    start_ord = min(ord(letter_1) - ord('A') + 1, ord(letter_2) - ord('A') + 1)
    end_ord = max(ord(letter_1) - ord('A') + 1, ord(letter_2) - ord('A') + 1)

    # build the list of letters in the interval
    interval_letters = [chr(i + ord('A') - 1) for i in range(start_ord, end_ord + 1)]

    # choose 7 letters: if interval has >=7 letters pick sample without repeats, otherwise allow repeats
    if len(interval_letters) >= 7:
        block2 = ''.join(random.sample(interval_letters, 7))
    else:
        # if interval is small, allow repeats to fill 7 chars
        block2 = ''.join(random.choices(interval_letters, k=7))

    block1 = f"{start_ord:02d}"
    block3 = f"{end_ord:02d}"

    # show as three lines for readability
    generated_key = f"{block1}\n{block2}\n{block3}"

    key_label.config(text=generated_key)
    print("Generated Key:")
    print(generated_key)


window = tk.Tk()
window.title("Key Generator")

window.geometry("600x400")  # reduced height since we're using fewer lines
window.configure(bg="white")

try:
    background_image = tk.PhotoImage(file="encryption-key-generator.png")
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading background image: {e}")

key_label = tk.Label(window, text="Generated Key", font=("Helvetica", 18), bg="white", fg="black", justify="center")
key_label.pack(pady=30)

generate_button = tk.Button(window, text="Generate Key", font=("Helvetica", 12), command=generate_key)
generate_button.pack(pady=20)

# Generate a key on startup to show output
generate_key()

# keep a reference so PhotoImage isn't garbage-collected
_images_keep = (globals().get('background_image', None), )
