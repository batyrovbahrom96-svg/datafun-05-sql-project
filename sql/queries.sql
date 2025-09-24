-- Show all authors
SELECT * FROM authors;

-- Show all books
SELECT * FROM books;

-- Join authors and books
SELECT books.title, authors.first, authors.last
FROM books
JOIN authors ON books.author_id = authors.author_id;

-- Update a book
UPDATE books SET title = "Emma" WHERE book_id = "3";

-- Delete a book
DELETE FROM books WHERE book_id = "4";