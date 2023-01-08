# Plagiarism-Check

Create a TURNITIN equivalent free software to do plagiarism checking of research articles / thesis etc.

### How to run?

1. Move to `<project-dir>`, create virual environment and then activate it as

```sh
$ cd <project-dir>
$ python3 -m venv .venv
$ source .venv/bin/activate
```

2. Edit configuration under `settings.py`. i.e. provide configuration/settings related to DB and other constants.

> If you are using PyCharm then environment variables can be specified under `run configuration`.

3. Add project to `PYTHONPATH` as

```sh
$ export PYTHONPATH="$PYTHONPATH:." # . corresponds to current directory(project-dir)
```

4. Under `<project-dir>` install requirements/dependencies as

```sh
$ pip3 install -r requirements.txt
```

5. Then run test cases as -

```sh
$ python -m unittest discover -s 'tests' -p '*.py'
```

6. Run server as -

```sh
$ python app.py
```

> Now you can access the application by visiting `{protocol}://{host}:{port}`. For localhost it is `http://localhost:5000`.

### Applications & Endpoints

There are following three APIs -

#### 1. Adding a new document -

> POST `{host}:{port}/api/v1/plagiarism/documents`.

_Request body_

```python
{
  "abstract": "Beamforming, user scheduling and transmit power on existing interference management schemes in multi-cell mmWave networks have been independently controlled due to the high computational complexity of the problem. In this paper, we formulate a long-term utility maximization problem where beam activation, user scheduling and transmit power are incorporated in a single framework. To develop a low-co...",
  "articleNumber": "9973235",
  "articleTitle": "Three Steps Toward Low-Complexity: Practical Interference Management in NOMA-Based mmWave Networks",
  "authors": [
    {
      "preferredName": "Joonpyo Hong",
      "normalizedName": "J. Hong",
      "firstName": "Joonpyo",
      "lastName": "Hong",
      "searchablePreferredName": "Joonpyo Hong"
    },
    .
    .
    .
  ],
  "doi": "10.1109/ACCESS.2022.3227444",
  "publicationTitle": "IEEE Access",
  "publicationYear": "2022",
  "publicationVolume": null,
  "publicationIssue": null,
  "volume": "10",
  "issue": null,
  "documentLink": "/document/9973235/",
  "xml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r..."
}
```

_Response_

```javascript
{
     "success": true,
     "message": "Document added successfully!",
     "data": null,
     "errors": []
}
```

#### 2. Detecting plagiarism -

> POST `{host}:{port}/api/v1/plagiarism/detect`.

_Request body_

```python
{
    "text": "Beamforming is a technique used in wireless communication to control the directionality of the transmitted signal. By carefully designing the phase and amplitude of the signals transmitted by each antenna, the beamforming algorithm can focus the transmitted energy in a particular direction, improving the signal-to-noise ratio at the intended receiver.",
}
```

_Response_

```javascript
{
    "success": true,
    "message": "Input text is 25.5% similar to the doc `articleNumber`: `9973235` with similarity score of 0.25499620385104793",
    "data": {
        "similarity_score": 0.25499620385104793,
        "similarity_percentage": 25.5,
        "doc": {
            ...
        }
    },
    "errors": []
}
```

#### 3. Fetch all documents -

> GET `{host}:{port}/api/v1/plagiarism/documents?page=1&per_page=10`.

_Response_

```javascript
{
    "success": true,
    "message": "",
    "data": {
        "data": [
            {
            "abstract": "Beamforming, user scheduling and transmit power on existing interference management schemes in multi-cell mmWave networks have been independently controlled due to the high computational complexity of the problem. In this paper, we formulate a long-term utility maximization problem where beam activation, user scheduling and transmit power are incorporated in a single framework. To develop a low-co...",
            "articleNumber": "9973235",
            "articleTitle": "Three Steps Toward Low-Complexity: Practical Interference Management in NOMA-Based mmWave Networks",
            "authors": [
                {
                "preferredName": "Joonpyo Hong",
                "normalizedName": "J. Hong",
                "firstName": "Joonpyo",
                "lastName": "Hong",
                "searchablePreferredName": "Joonpyo Hong"
                },
            .
            .
            .
            ],
            "doi": "10.1109/ACCESS.2022.3227444",
            "publicationTitle": "IEEE Access",
            "publicationYear": "2022",
            "publicationVolume": null,
            "publicationIssue": null,
            "volume": "10",
            "issue": null,
            "documentLink": "/document/9973235/",
            "xml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r..."
            }
            ,
            {......},
            {......}
         ],
         "count": 72
      }
}
```
