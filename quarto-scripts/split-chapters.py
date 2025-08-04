import pypdf
import os

def chapter_name(x):
    x = x.lower()
    x = x.replace(" ", "-")
    return x

output = "_chapters"

reader = pypdf.PdfReader("docs/thesis.pdf")
outlines = reader.outline

if not os.path.exists(output):
    os.makedirs(output)

# keep only non-nested list (thus excluding level > 1 bookmarks)
bookmarks = [x for x in outlines if not isinstance(x, list)]

# get references index

titles = [x.title for x in bookmarks]
index_bib = titles.index("References")

for i, bookmark in enumerate(bookmarks):
    if i > index_bib:
        break

    title = bookmark.title
    start_page = reader.get_destination_page_number(bookmark)
    num_pages = len(reader.pages)

    if i + 1 < len(bookmarks):
        end_page = reader.get_destination_page_number(bookmarks[i + 1]) - 1
    else:
        end_page = num_pages - 1  # Last bookmark goes to end of PDF

    writer = pypdf.PdfWriter()
    for page_num in range(start_page, end_page + 1):
        writer.add_page(reader.pages[page_num])

    output_file = str(i + 1).zfill(2) + "-" + chapter_name(title) + ".pdf"
    output_path = os.path.join(output, output_file)

    with open(output_path, "wb") as f_out:
        writer.write(f_out)