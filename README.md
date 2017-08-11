# MT (Machine Translator)

English to Yoruba Translator.

## Motivation

Google has the best english to yoruba translator out there and doesnt do a very good job.

## Project objetive

Our end goal is to translate english to yoruba contextually, at the early stages we hope to achive translation based on the SVO (Subject Object Verb) structure of an english sentence to the SOV structure of a yoruba sentence, the approach being used for now is to break down an english sentence into words and identify the Subject,  Verb ad Object. We then find the equivalent words in our diction (an example can be found below) and then create a sentence in yoruba using the SOV structure.

`diction = {'NP': {1: 'N', 2: 'D'},		
 -               'VP': {1: 'V', 2: 'V.NP'},		
 -               'V': {'play': 'sere', 'cut': 'ge', 'plant': 'gbi', 'is': 'n', 'bought': 'ra'},		
 -               'N': {'boy': 'omokunrin', 'tree': 'igi', 'fruit': 'eso', 'cloth': 'aso', 'girl': 'omobinrin'},		
 -               'D': {'the': 'naa', 'a': 'kan', 'an': 'kan'},		
 -               'A': {'white': 'funfun', 'black': 'dudu'}		
 -               } 
 `
Try it here: https://serene-badlands-42335.herokuapp.com/

## Installing

- Install python 3

- Install pymongo3

- clone this repo

- enjoy!

## Contributing

- Please send a discussion to the owners telling them what you wish to add before starting work.

- If given the go ahead, fork the project and make a pull request to the repo.

## Milestones

We hope to see this repo progress over time and we would be having milestones until we hit a plateu. Please see our [MILESTONES.md](https://github.com/otaruMendez/MT/blob/master/MILESTONES.md) file for details.

## Versioning

We would be using [SemVer](http://semver.org/) for versioning, this would be ignored though till we hit our first milestone.

## Authors

* **Babatunde Otaru** - *Initial work*

* **Rasaq Kasali** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/otaruMendez/MT/blob/master/LICENSE.md) file for details

