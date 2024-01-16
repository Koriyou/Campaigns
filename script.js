    // Function to fetch the card title from index.html and set it as the page title
    function setCardTitle() {
        // Fetch the title from index.html
        fetch('index.html')
            .then(response => response.text())
            .then(data => {
                // Use DOM manipulation to extract the title
                const parser = new DOMParser();
                const doc = parser.parseFromString(data, 'text/html');
                const cardTitleElement = doc.querySelector('.flip-card-front .card-title');
                const cardTitle = cardTitleElement.textContent;

                // Set the fetched title as the title of this page
                document.title = cardTitle;
            })
            .catch(error => console.error(error));
    }

    // Call the function to set the card title when the page loads
    setCardTitle();
