from pyarabic.araby import (
    tokenize,
    is_arabicrange,
    strip_tashkeel,
    strip_tatweel,
    strip_shadda,
)


class DataReader:
    def __init__(self):
        pass

    # remove any non arabic words in the file
    def remove_non_arabic(self, data):
        tokens = tokenize(
            data,
            conditions=lambda x: is_arabicrange(x)
            and not x.isdigit()
            or x in ["٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"],
        )

        cleaned_data = " ".join(tokens)
        return cleaned_data

    # remove diacritics from arabic text and store the new data inside a new file
    def remove_diacritics(self, data):
        data_without_diactrics = strip_tashkeel(data)
        data_without_shadda = strip_shadda(data_without_diactrics)
        data_without_tatweel = strip_tatweel(data_without_shadda)
        return data_without_tatweel

    # remove all punctuation characters and store the result inside the output file
    def remove_tarkeem(self, data):
        arabic_punctuation = ["،", "٪", "؛", "؟", "ـ"]
        english_punctuation = [
            ",",
            ".",
            "%",
            ":",
            ";",
            "?",
            "!",
            "-",
            "_",
            "'",
            '"',
            "(",
            ")",
            "[",
            "]",
            "{",
            "}",
        ]
        data_without_tarkeem = ""
        for character in data:
            if (
                character not in arabic_punctuation
                and character not in english_punctuation
            ):
                data_without_tarkeem += character
        return data_without_tarkeem

    def remove_duplicate_words(self, input_file, output_file):
        with open(input_file, "r") as f:
            content = f.read()

        words = content.split()
        unique_words = set(words)

        with open(output_file, "w") as f:
            f.write("\n".join(unique_words))

    def store_data_cleaned(self, inputfile, outputfile):
        try:
            with open(inputfile, "r", encoding="utf-8") as f_input:
                with open(outputfile, "w", encoding="utf-8") as f_output:
                    for line in f_input:
                        cleaned_line = self.remove_non_arabic(line)
                        line_without_tarkeem = self.remove_tarkeem(cleaned_line)
                        line_without_diacritics = self.remove_diacritics(
                            line_without_tarkeem
                        )
                        f_output.write(line_without_diacritics + "\n")
            print("Text stored successfully!")

        except Exception as e:
            print(f"An error occurred: {e}")
