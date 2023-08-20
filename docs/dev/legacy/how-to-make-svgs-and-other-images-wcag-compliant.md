## Overview
Using the `alt` property in `img` HTML tags or Accessible Rich Internet Applications ([ARIA](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/)) labels with Scalable Vector Graphics (SVGs) and other images is important so that all images on the Hack for LA website are Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) compliant. This pages explains how the Website Team deals with SVGs and other images to make them WCAG compliant.

## Methods

### Use an `img` HTML tag with the SVG or image as for the `src` and an `alt` attribute
#### When to use it
- Any new images added to the website repo, which are added to [/assets/images](https://github.com/hackforla/website/tree/gh-pages/assets/images) directory or in a subdirectory of it
- Images already in [/assets/images](https://github.com/hackforla/website/tree/gh-pages/assets/images) directory or in a subdirectory of it

#### Notes
- For SVGs, see the pros and cons detailed in [_The quick way: img element_](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Adding_vector_graphics_to_the_Web#the_quick_way_img_element) section in MDN Web Docs _Adding vector graphics to the web_.

#### Example of an image in an `img` tag that needs an `alt` attribute: 
```
<img class="header-hero-image" src="/assets/images/toolkit/toolkit-hero.svg">
```
#### Steps:
In an `img` HTML tag, 
1. The image needs to be in the [/assets/images](https://github.com/hackforla/website/tree/gh-pages/assets/images) directory or be in a subdirectory of it  
2. Set `src` to the path to the SVG or image
3. Add an `alt` attribute with an appropriate descriptive text. (Depending on the image, the `alt` attribute will either be an empty `alt` attribute (`alt=""`) or will have an appropriate descriptive text. You can use this [alt Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/) to help you decide what the `alt` attribute should contain.)

```
<img class="header-hero-image" src="/assets/images/toolkit/toolkit-hero.svg" alt="" >
```

### Use an ARIA label in the `div` HTML tag wrapping the SVG
#### When to use it
- Any existing images in the [_includes](https://github.com/hackforla/website/tree/gh-pages/_includes) in the website repo

#### Notes
- For SVGs, see the pros and cons detailed in [_How to include SVG code inside your HTML_](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Adding_vector_graphics_to_the_Web#how_to_include_svg_code_inside_your_html) section in MDN Web Docs _Adding vector graphics to the web_. This section discusses inline SVG, which is what this method does using [Jekyll's include tag](https://jekyllrb.com/docs/includes/) to insert an SVG into a HTML file and the result of this is an inline SVG when the site is generated.

#### Example of an SVG wrapped in a `div` tag that needs an ARIA label: 
```
<div>
  {% include svg/logo-hfla-small.svg %}
</div>
```
#### Steps:
In an `div` HTML tag, 
1. Add a `role="img"`
2. Add an `aria-label` with an appropriate descriptive text.

```
<div role="img" aria-label="Hack for LA">
  {% include svg/logo-hfla-small.svg %}
</div>
```

#### Accessible names/descriptions
Review the w3.org document about accessible names and descriptions [here](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/).

> Naming:
> * Naming with child content.
> * Naming with a string attribute via aria-label.
> * Naming by referencing content with aria-labelledby.
> * Naming form controls with the label element.
> * Naming fieldsets with the legend element.
> * Naming tables and figures with captions.
> * Fallback names derived from titles and placeholders.

> Describing:
> * Describing by referencing content with aria-describedby.
> * Describing tables and figures with captions.
> * Descriptions derived from titles.


### Resources
* [MDN: aria-label](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label)
* [MDN: ARIA, img role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/img_role)
* [a11y-101: Accessible SVGs](https://a11y-101.com/development/svg)
* [w3.org: Accessible Names and Descriptions](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/)
* [WCAG 2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/) 