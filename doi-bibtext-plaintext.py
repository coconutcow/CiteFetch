import requests


def get_citation_from_doi(doi):
    url = f"https://api.crossref.org/works/{doi}"
    data = requests.get(url).json()["message"]

    if "author" in data:
        authors = data["author"]
        author_names = []
        for author in authors:
            author_names.append(f"{author['given']} {author['family']}")
        authors_str = ', '.join(author_names)
    else:
        authors_str = "No authors listed"

    if "title" in data:
        title = data["title"][0]
    else:
        title = "No title listed"

    if "published-print" in data:
        date = data["published-print"]["date-parts"][0][0]
    else:
        date = "No date listed"

    if "container-title" in data:
        container_title = data["container-title"][0]
    else:
        container_title = "No container title listed"

    citation = f"{authors_str} ({date}). {title}. {container_title}. https://doi.org/{doi}"
    return citation


# you can test the function with the DOI from our lab
print(get_citation_from_doi('10.3389/fpsyg.2019.02441'))
