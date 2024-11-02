## Basic URL Shortener API

This is a simple URL Shortener API that allows users to shorten long URLs for easier sharing and management.

### Endpoints

#### GET `/<code>`
Redirects to the original URL associated with the provided code.
- Success: HTTP 302 redirect to original URL
- Error: JSON `{"error": "Code not found"}` with 404 status

#### POST `/shorten`
Creates a short URL from a provided original URL.
- Input: JSON body with `{"url": "original_url"}` or query parameter `?url=original_url`
- Success: JSON response with shortened URL details
- Error: JSON `{"error": "URL is required"}` with 400 status if URL is missing
