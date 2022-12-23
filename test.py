

for index in range(_page_size):
    paper = dict()
    paper['abstract'] = records[index].get("abstract")
    paper['articleNumber'] = records[index].get("articleNumber")
    paper['articleTitle'] = records[index].get("articleTitle")
    paper['authors'] = records[index].get("authors")
    paper['doi'] = records[index].get("doi")
    paper['publicationTitle'] = records[index].get("publicationTitle")
    paper['publicationYear'] = records[index].get("publicationYear")
    paper['publicationVolume'] = records[index].get("publicationVolume")
    paper['publicationIssue'] = records[index].get("publicationIssue")
    paper['volume'] = records[index].get("volume")
    paper['issue'] = records[index].get("issue")
    paper['documentLink'] = records[index].get("documentLink")
    resp = get_xml(paper['articleNumber'])
    if resp.status_code == 200:
        paper['xml'] = resp.text
        with open(f'./data/{paper["publicationYear"]}/{paper["articleNumber"]}.json', 'w') as f:
            f.write(json.dumps(paper, indent=4))
