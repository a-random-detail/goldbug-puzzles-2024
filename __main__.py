#!/usr/bin/env/python3

import pymupdf
import fold_info


def extract_information(pdf_path):
    doc = pymupdf.open(pdf_path)

    for i in range(3, doc.page_count, 2):
        page_information(doc[i], i)
    return "fart noise"


def page_information(page, num):

    points = set()

    max_height = page.rect.height

    for drawing in page.get_drawings():
        for item in drawing["items"]:
            if item[1].x == 0:
                points.add(item[1])
            if item[2].x == 0:
                points.add(item[2])

    print_points(points, max_height)


def print_points(points, max_height):
    current_height = max_height
    y_values = []
    display_string = ""
    is_between = False

    for point in points:
        y_values.append(point.y)

    for val in sorted(y_values, reverse=True):
        while current_height >= val and current_height >= 0:
            if is_between:
                display_string = display_string + "."
            else:
                display_string = display_string + " "
            current_height = current_height - 5
        is_between = not is_between

    print(display_string)


if __name__ == '__main__':
    path = 'Etiquette_Book.pdf'
    extract_information(path)
