# CBOE PITCH Viewer
> A tool for viewing/debugging PITCH messages

DEMO: [cboe.haydenbickerton.com](http://cboe.haydenbickerton.com/)

Here is a screenshot of the web interface:

![viewer](https://drive.google.com/uc?export=view&id=15KgEKh51IWeQcE7jn7xWy1QARKsuy8bi)

## Run the compiled viewer
```sh
$ cd /client/dist
$ python3 -m http.server 8080
...
```
Then open your browser to [http://localhost:8080/ ](http://localhost:8080/ ) to see the viewer.

## Installation & Development

OS X & Linux:

```sh
$ cd /client
$ yarn install
yarn install v1.7.0
[1/4] Resolving packages...
[2/4] Fetching packages...
...
$ npm run serve
...
  App running at:
  - Local:   http://localhost:8080/
  - Network: http://10.0.0.200:8080/
```

# Notes
The code is in one of two steps:

 1. Converting the PITCH Message Specifications into usage python/javascript parsers/models
	 - `/structs/specs` - YAML's extracted from PDF using [tabula]([https://tabula.technology/](https://tabula.technology/))
	 -  `/notebooks/Building Structs.ipynb` - Notebook to build YAMLs into py/js models
 2. Web interface/app/viewer to view uploaded message data
	 - `/client/` - Vue.js app (pictured above)
	 - `/structs/compiled/Cboe.js` - Generated in  step 1 , imported by web app


Initially I went the route of making the python models and types for a backend parsing service, as I'm primarily a python developer. But copy-pasting each value into hardcoded classes when there's clearly an existing spec *somewhere* isn't what I'd normally do. So I did the YAMLs, and referenced those as the specs in the vue app. More about this in `Building Structs.ipynb`. I left code from initial run in `/cboe-sdk/` and `/notebooks/Modeling.ipynb`.


### Other
This feels very similar to [ACORD AL3]([https://www.acord.org/standards-architecture/acord-data-standards/Property_Casualty_Data_Standards#AL3](https://www.acord.org/standards-architecture/acord-data-standards/Property_Casualty_Data_Standards#AL3)), which is a popular [fixed length messaging standard]([https://www.ibm.com/support/knowledgecenter/en/SSMKHH_10.0.0/com.ibm.etools.mft.doc/ad09530_.htm](https://www.ibm.com/support/knowledgecenter/en/SSMKHH_10.0.0/com.ibm.etools.mft.doc/ad09530_.htm)) used by insurance software for the transmission of policies and claims. I created the AL3 implementation during my time at [BriteCore]([https://www.britecore.com/](https://www.britecore.com/)) .

The idea for the viewer comes from working with AL3, as there are thousands of different data/message types and no straightforward tool for displaying a feed of messages and their fields.







