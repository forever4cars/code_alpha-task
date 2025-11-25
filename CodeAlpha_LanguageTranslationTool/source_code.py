import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator


class TranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Language Translator")
        self.geometry("1100x320")
        self.resizable(False, False)
        self.configure(bg="skyblue")

        # Load supported languages
        self.languages = GoogleTranslator().get_supported_languages()

        self._build_ui()

    def _build_ui(self):
        title_label = tk.Label(
            self,
            text="Language Translator",
            font=("Arial", 20, "bold"),
            bg="skyblue",
        )
        title_label.pack(pady=(10, 5))

        # Main frame
        main_frame = tk.Frame(self, bg="skyblue")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Input
        tk.Label(
            main_frame,
            text="Enter Text",
            font=("Arial", 13, "bold"),
            bg="white smoke",
        ).place(x=135, y=10)

        self.input_text = tk.Text(
            main_frame,
            font=("Arial", 10),
            height=5,
            wrap="word",
            padx=5,
            pady=5,
            width=50,
        )
        self.input_text.place(x=20, y=50)

        # Output
        tk.Label(
            main_frame,
            text="Output",
            font=("Arial", 13, "bold"),
            bg="white smoke",
        ).place(x=770, y=10)

        self.output_text = tk.Text(
            main_frame,
            font=("Arial", 10),
            height=5,
            wrap="word",
            padx=5,
            pady=5,
            width=50,
            state="disabled",
        )
        self.output_text.place(x=580, y=50)

        # Language selector
        tk.Label(
            main_frame,
            text="Target language",
            font=("Arial", 11),
            bg="skyblue",
        ).place(x=20, y=155)

        self.dest_lang = ttk.Combobox(
            main_frame,
            values=self.languages,
            width=25,
            state="readonly",
        )
        self.dest_lang.place(x=150, y=155)
        self.dest_lang.set("choose language")

        # Buttons
        ttk.Button(main_frame, text="Translate", command=self.translate_text).place(
            x=450, y=150
        )
        ttk.Button(main_frame, text="Clear", command=self.clear_text).place(
            x=450, y=190
        )

    def translate_text(self):
        text = self.input_text.get("1.0", tk.END).strip()
        lang = self.dest_lang.get()

        if not text:
            messagebox.showwarning("No text", "Please enter some text to translate.")
            return

        if lang == "choose language":
            messagebox.showwarning("No language", "Please select a target language.")
            return

        try:
            translated = GoogleTranslator(source="auto", target=lang).translate(text)
        except Exception as exc:
            messagebox.showerror("Translation error", f"An error occurred:\n{exc}")
            return

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, translated)
        self.output_text.config(state="disabled")

    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state="disabled")
        self.dest_lang.set("choose language")


if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()
