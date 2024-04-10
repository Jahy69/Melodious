import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
import pandas as pd  # type: ignore
import re


def clean_text(text):
    text = re.sub(r"\[\d+\]|\[citation needed\]", "", text)
    text = re.sub(r"\(.*?\)", "", text)

    return text.strip()


def get_first_paragraph(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        content_area = soup.find("div", class_="mw-parser-output")
        if content_area:
            first_paragraph = content_area.find("p", recursive=False)
            if first_paragraph and first_paragraph.text.strip():
                return clean_text(first_paragraph.text)
            else:
                return "Descripción no encontrada"
        else:
            return "Descripción no encontrada"
    except Exception as e:
        return "Descripción no encontrada"


def main():
    url = "https://fr.wikipedia.org/wiki/Liste_de_styles_musicaux"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    content_areas = soup.find_all(["div", "section"], class_=["mw-parser-output"])
    genres_descriptions = []

    for area in content_areas:
        li_elements = area.find_all("li")
        for li in li_elements:
            a = li.find("a")
            if a and "href" in a.attrs:
                link = "https://fr.wikipedia.org" + a["href"]
                description = get_first_paragraph(link)
                genres_descriptions.append(
                    {"Genre": a.text, "Description": description}
                )
    df = pd.DataFrame(genres_descriptions)
    df.to_csv("genres_musicaux_descriptions.csv", index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    main()
