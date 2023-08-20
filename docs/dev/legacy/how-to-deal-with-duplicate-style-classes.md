# Overview

This guideline will expand on how to deal with duplicate style classes using the bootstrap method of [Standardized Components](https://github.com/hackforla/website/wiki/Standardized-Components) that was already set in place. The method currently implemented uses a reusable styling component, such as `_buttons.scss`, that is **dedicated to one specific folder** and **can be applied to multiple page**s rather than being limited to one page and found in many folders. This prevents the unnecessary duplication of having to recreate styles for every single page and have it limited for that one specific page.

As you may guess, duplication can create formatting inconsistencies, may impact our project performances, and can makes it difficult for any type of code referencing. This is why we are encouraging developers to assist in fixing duplications they find while working on their assigned issues. 

Below you will find a step by step guide on how to handle duplicate style classes which include the folder/file location of our reusable styling components, how to create a reusable styling component, and how to replace the duplicate styles by replacing it with a reusable styling component.


***



# Follow these steps below if you come across a duplicate style. 

## Step 1 - Check the reusable styling components folder


Begin by checking to see if the duplicated style has a reusable styling component in the elements folder.

- You can find the reusable components in the element folder via this path: _sass > components > elements

   <img src='https://user-images.githubusercontent.com/101952500/195283854-33980af3-ada3-49e6-b80f-8421d6fa1054.png' alt='elements folder' width='200px' />

- If there is a reusable styling component, then jump down to [Step 3 - How to use a reusable styling component](#step-3---how-to-use-a-reusable-styling-component)

- If there is **NOT** a reusable styling component, then continue below to create one. [Step 2 - Create a reusable component to replace the duplicate style](#step-2---create-a-reusable-component-to-replace-the-duplicate-style)





<br/>

***

## Step 2 - Create a reusable component to replace the duplicate style

Consider creating a reusable component if you discover an existing duplicate style while working on an issue and it is **NOT** in the elements folder.

   1. First, refer to the [Figma](https://www.figma.com/file/0RRPy1Ph7HafI3qOITg0Mr/Hack-for-LA-Website?node-id=3464%3A3) design to stay consistent with our site principles.

   1. Once you understand the design format, begin by creating a new file under the elements folder.
      - Right click on the elements folder and select 'New File'
      <img src='https://user-images.githubusercontent.com/101952500/195460269-6acb384d-a897-4b96-ad7b-a2b22b0bcd55.png' alt='elements folder click' width='300px' />

   1. Name your file using the format already in place.
      - Please stay consistent with the naming principles like the ones displayed here. `_button.scss`, `_color-styles.scss`, etc.

   1. After successfully creating your file, begin to create your reusable component.
      - **Please make sure to leave detailed comments describing the styling features you create.**
      - Style names must follow:

          - Base Class -- should be used for every instance of the component's style and must describe the component in general. (ex: `.btn` is for buttons, `.page-card` is for page cards) 

          - Size Class -- should be added for every instance where the size of the component is changed. Typically includes sm, md, lg, and xl. (ex: `.btn-lg`, `.page-card-xl`)

          - Color Class -- should be added on for every instance where the color of the component is changed. (ex: `.btn-primary`, `.page-card-secondary`)

          - Page-specific Class -- Any feature related to the component that is specific to a page. (ex: `.btn--about-us`)


<br/>
Your code should look something similar to the image below.
<br/>

  <img width="400" alt="Screen Shot 2022-10-13 at 2 43 22 PM" src="https://user-images.githubusercontent.com/101952500/195716753-eadd2d30-bb87-41ac-9b48-3135497fc9ef.png"><img width="400" alt="Screen Shot 2022-10-13 at 2 43 04 PM" src="https://user-images.githubusercontent.com/101952500/195716762-ffe0b61c-522e-4961-abde-8717e83847b9.png">


   5. Once you've successfully created your styles, **begin replacing the duplicate style with the reusable component**.
       - To use the component created, simply include the name of the style needed in your class. See [Step 3 - How to use a reusable styling component](#step-3---how-to-use-a-reusable-styling-component) for a visual breakdown.


<br/>

***

## Step 3 - How to use a reusable styling component

Using a style is fairly simple and takes after the bootstrap model. Some styles may not need a size, color, or page specific class and can be simply removed from the code. For an example, see below.

<img src='https://user-images.githubusercontent.com/101952500/195679559-fafa8943-3f59-4ed0-b34a-720b95994647.png' alt='button class' width='800px' /> <br />

Base Class (`page-card`) - sets our page-card component.

Color Class (`card-primary`) - sets our page-card component color to primary (white page card).

Size Class (`page-card-lg`) - sets our page-card component size to large.

Page-specific Class (`page-card--project-description-page`) - used for a specific page page-card component.

- Again, please refer to the Figma design to determine what must be used. Some may have sizing, colors, etc and some may not.