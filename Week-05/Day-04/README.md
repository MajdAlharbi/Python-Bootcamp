# Week 05 - Day 04 - CSS Layout and Responsive Design

**Date:** 2026-08-26

## Overview

Learned how to organize page layouts using Flexbox and Grid, and how to make layouts responsive for different screen sizes using media queries.

## Topics Covered

- Flexbox
- `justify-content`
- `align-items`
- `flex-direction`
- `flex-wrap`
- `gap`
- CSS Grid
- `fr`
- `auto-fit`
- `minmax()`
- Flexbox vs Grid
- Responsive design
- Media queries

## Key Concepts

### Flexbox

Flexbox is useful for arranging elements in one direction.

```css
.container {
    display: flex;
    gap: 20px;
}
```

Common properties:

```css
justify-content: center;
align-items: center;
flex-direction: row;
flex-wrap: wrap;
```

### CSS Grid

Grid is useful for rows and columns.

```css
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}
```

- `1fr` → one fraction of the available space
- `gap` → space between grid items

### Responsive Grid

```css
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
```

- `auto-fit` → automatically adjusts the number of columns
- `minmax()` → sets the minimum and maximum size of each column

### Flexbox vs Grid

```text
Flexbox → one direction
Grid    → rows and columns
```

Typical use:

```text
Navbar → Flexbox
Cards  → Grid
```

### Media Queries

Media queries change the layout based on screen size.

```css
@media (max-width: 768px) {
    .hero {
        flex-direction: column;
    }
}
```

This can change a desktop layout into a mobile layout.

## Labs Summary

- Flexbox Navbar
- Responsive Card Grid
- Project Layout Upgrade

## Homework

Build a responsive page including:

- Header
- Hero section
- Features
- Courses
- Media query

## Important Syntax / Patterns

```css
display: flex;
display: grid;

gap: 20px;

grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));

@media (max-width: 768px) {
    /* responsive styles */
}
```

## Quick Review

- Flexbox → arrange items in one direction
- Grid → arrange items in rows and columns
- `gap` → space between items
- `flex-wrap` → allows items to move to a new line
- `1fr` → fraction of available space
- `auto-fit` → automatically fits columns
- `minmax()` → defines minimum and maximum sizes
- Responsive design → adapts to screen size
- Media query → applies styles based on screen width