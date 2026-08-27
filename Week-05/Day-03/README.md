# Week 05 - Day 03 - Forms and CSS Fundamentals

**Date:** 2026-08-25

## Overview

Learned how to create interactive HTML using forms and how to style web pages using CSS. The lesson focused on form structure, selectors, specificity, the box model, and external stylesheets.

## Topics Covered

- HTML forms
- Labels and input fields
- `name` and `id`
- Select, checkbox, and textarea
- Form submission
- CSS selectors
- Specificity
- Box model
- External CSS
- Basic styling
- `:hover`

## Key Concepts

### Forms

Forms collect data from the user.

```html
<form>
    <label for="email">Email</label>
    <input type="email" id="email" name="email">

    <button type="submit">Submit</button>
</form>
```

- `label` → describes the field
- `id` → connects the field with its label
- `name` → identifies the value when the form is submitted
- `submit` → sends the form

### CSS Selectors

CSS selectors choose which HTML elements to style.

```css
p {
    color: red;
}

.note {
    color: blue;
}

#main-note {
    color: green;
}
```

```text
element < class < id
```

### Specificity

Specificity decides which CSS rule wins when multiple rules target the same element.

```text
Element selector → lower priority
Class selector   → higher
ID selector      → highest
```

### Box Model

Every HTML element behaves like a box.

```text
Margin
 └── Border
      └── Padding
           └── Content
```

### External CSS

CSS can be stored in a separate file and linked inside `<head>`.

```html
<link rel="stylesheet" href="styles.css">
```

### Hover

`:hover` applies styling when the mouse moves over an element.

```css
button:hover {
    background-color: lightgray;
}
```

## Labs Summary

- Contact Form
- Specificity Challenge
- Style the Project
- Lab 04 — Group Project

## Important Syntax / Patterns

```html
<label for="name">Name</label>
<input type="text" id="name" name="name">
```

```css
selector {
    property: value;
}
```

```css
.class-name { }

#id-name { }

button:hover { }
```

## Quick Review

- `<form>` groups user input
- `for` should match the field `id`
- `name` is used when sending form data
- `type="submit"` submits the form
- CSS controls presentation and styling
- `element < class < id` in specificity
- `padding` → space inside the element
- `margin` → space outside the element
- External CSS is linked using `<link>`
- `:hover` styles an element when the pointer is over it