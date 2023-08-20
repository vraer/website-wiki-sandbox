# Duplicate Style Classes

This guide provides the procedure for handling duplicate style classes by employing the bootstrap method of [Standardized Components](standardized-components.md), which incorporates reusable styling components, like `_buttons.scss`, assigned to specific folders and applicable across multiple pages. This reduces duplication and improves consistency, project performance, and facilitates code referencing.

## Locate the Reusable Styling Components Folder

Navigate to `_sass > components > elements`. Check if the duplicate style already has a reusable styling component in the elements folder.

  - If a reusable styling component exists, proceed to [Use a Reusable Styling Component](#use-a-reusable-styling-component).
  - If no reusable styling component exists, continue to [Create a Reusable Component for a Duplicate Style](#create-a-reusable-component-for-a-duplicate-style).

![Elements Folder](https://user-images.githubusercontent.com/101952500/195283854-33980af3-ada3-49e6-b80f-8421d6fa1054.png)

## Create a Reusable Component for a Duplicate Style

If you encounter a duplicate style that does not exist in the elements folder while working on an issue, create a reusable component:

1. Refer to the [Figma](https://www.figma.com/file/0RRPy1Ph7HafI3qOITg0Mr/Hack-for-LA-Website?node-id=3464%3A3) design for consistency with site principles.
2. Create a new file in the elements folder.
3. Name the new file following the existing format, such as `_button.scss` or `_color-styles.scss`.
4. In the new file, create your reusable component. Use the following naming conventions:
      - **Base Class**: Use for every instance of the component's style.
      - **Size Class**: Use when the size of the component changes.
      - **Color Class**: Use when the color of the component changes.
      - **Page-specific Class**: Use for page-specific component features.
5. Replace the duplicate style with the new reusable component.

## Use a Reusable Styling Component

Applying a style from a reusable component follows the bootstrap model. Some styles might not need a size, color, or page-specific class, and these can be omitted from the code.

![Button Class](https://user-images.githubusercontent.com/101952500/195679559-fafa8943-3f59-4ed0-b34a-720b95994647.png)

Refer to the Figma design to determine which classes to use.
