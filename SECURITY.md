# Security Notes

RoadLens Australia is a static coursework prototype. Its present controls are intentionally proportionate to that scope.

- Every HTML page declares a restrictive Content Security Policy.
- No third-party JavaScript libraries, analytics, advertising scripts, logins, or tracking pixels are loaded.
- External links use `rel="noopener noreferrer"` where a new tab is opened.
- The About feedback form is local-only; it does not transmit or persist user-entered feedback.
- The site does not claim database or API encryption because the submitted prototype has no remote application backend.

For production hosting, use HTTPS/TLS, HSTS, routine dependency/vulnerability checks, secure server configuration and server-side validation for any future API or form endpoint.
