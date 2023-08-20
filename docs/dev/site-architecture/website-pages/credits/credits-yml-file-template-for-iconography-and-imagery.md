# Template for images

Use this to describe the attribution/credit for any images used on the HfLA website that would go under the Iconography and Imagery section of the [Credits page](https://www.hackforla.org/credits/). 
 
Entries are placed in the [_data/internal/credits](https://github.com/hackforla/website/tree/gh-pages/_data/internal/credits) folder. Jekyll pulls them into the cards on the [Credits](https://www.hackforla.org/credits/) page.


```yaml
---
# The title from the source provider
title: 
# The url where you can get direct access to the image on the provider site
title-link: 
# The type of content - image, audio, or video 
content-type: 
# The page it's used on
used-in: 
# Name of the artist
artist: 
# Name of the image database you found it on
provider: 
# Please give the general site URL, not the link to the image
provider-link: 
# Location in our GitHub repo
image-url:
# Alt text for the image on the Credits page
alt: ''
# If an image was altered, please give the name of the HfLA designer that altered the image
altered-by:
# If an image was altered, please give the LinkedIn URL of the HfLA designer that altered the image
altered-by-link:
---
```

[Sample](https://github.com/hackforla/website/blob/gh-pages/_data/internal/credits/act.yml) credit.yml file

****