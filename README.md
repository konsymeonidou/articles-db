# articles-db
This is an assignment for a technical interview as Backend Engineer

# Junior Back-end Engineer Technical Assignment: Articles Database

## Description

Create a proof of concept app of an "Articles database" where users can perform CRUD (Create, Read, Update, Delete) operations on Articles, comment on them, and filter based on their properties.

## Required Functionality

### Article Management
- **Upload an Article**: Users can upload an article with the following attributes:
  - Identifier
  - Publication date
  - Authors (multiple authors allowed)
  - Abstract
  - Title
  - Tags (multiple tags allowed, e.g., `Meat, Beef, Grill`)

- **List Articles**: Users can get a list of all articles uploaded by any user.
  - **Filtering**: Users can filter the list by:
    - Year
    - Month
    - Author(s)
    - Tag(s)
    - Keywords (search in abstract and title)
  - Keyword search can simply check its existence on the abstract and title - feel free to implement any kind of search mechanism you like.
    - Optional - check out more advanced full text search implementations.
    Some databases offer such functionality, which usually includes some
    kind of tokenization and stemming.
  - **Pagination**: The view must be paginated, with a maximum of 100 rows per page.

- **Download CSV**: Users can download a CSV of articles by providing a list of identifiers or by applying the same filters as when listing articles.

- **Update and Delete**: Users can update and delete their own articles.

### Comment Management
- Users can perform CRUD operations on comments for any article.
  - Users can only update and delete their own comments.

## Technical Specifications

- **API Only**: Provide only the API, no UI is required.
- **RESTful API**: Design and implement a RESTful API.
- **Framework**: Use a framework of your choice (preferably in Python).
- **Database**: Use a database of your choice.
- **Code Quality**: Provide working and tested code.

## Notes

- The specifications are flexible. Feel free to add or change details based on common sense.
- The project should be designed and implemented in a way that showcases your technical skills.
- Over-engineering some parts to demonstrate technical skills, patterns, and designs is acceptable.
- Simplifying some parts is also okay if needed.
- The goal is not just to have a project that runs, but to understand the depth of your skills.
