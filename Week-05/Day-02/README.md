# Week 05 - Day 02 - HTML Foundations

**Date:** 2026-08-24

## Overview

Learned the basic structure of HTML pages and how HTML elements are used to organize web content. The lesson focused on page structure, tags, attributes, lists, links, images, and semantic HTML.

## Topics Covered

- HTML document structure
- `<head>` and `<body>`
- Tags and elements
- Attributes and values
- Headings and paragraphs
- Links and images
- Ordered and unordered lists
- Nested elements
- Semantic HTML
- Basic DOM structure

## Key Concepts

### HTML Structure

A basic HTML page contains:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>My Page</title>
</head>

<body>
    <!-- Visible page content -->
</body>

</html>
```

- `<head>` → information about the page
- `<body>` → visible page content

### Tags, Content, and Attributes

Example:

```html
<a href="/contact">Contact Us</a>
```

- `a` → tag
- `href` → attribute
- `/contact` → attribute value
- `Contact Us` → content

### Common HTML Elements

```html
<h1>Main Heading</h1>
<h2>Section Heading</h2>

<p>Paragraph</p>

<a href="https://example.com">Link</a>

<img src="image.png" alt="Image description">
```

Lists:

```html
<ul>
    <li>Item</li>
</ul>

<ol>
    <li>Item</li>
</ol>
```

### Semantic HTML

Semantic elements describe the purpose of each part of the page.

```html
<header>
<nav>
<main>
<section>
<footer>
```

Example structure:

```text
header
   ↓
nav
   ↓
main
   ↓
section
   ↓
footer
```

Semantic HTML makes the page structure easier to understand than using only `<div>` elements.

## Labs Summary

The lesson included practice on:

- Building the first HTML page
- Finding errors in HTML structure
- Deciding whether elements belong in `<head>` or `<body>`
- Identifying tags, content, attributes, and values
- Building a profile page
- Converting `<div>` layouts into semantic HTML
- Building a basic website skeleton

## Important Syntax / Patterns

```html
<tag>Content</tag>

<tag attribute="value">Content</tag>
```

Basic structure:

```text
html
├── head
└── body
```

Semantic structure:

```text
header
nav
main
section
footer
```

## Quick Review

- HTML defines the structure of a web page
- `<head>` contains page information
- `<body>` contains visible content
- Tags define HTML elements
- Attributes provide extra information
- `href` is used with links
- `src` defines an image source
- `alt` describes an image
- `<ul>` → unordered list
- `<ol>` → ordered list
- `<li>` → list item
- Semantic HTML gives meaning to page sections
- Common semantic tags include `<header>`, `<nav>`, `<main>`, `<section>`, and `<footer>`