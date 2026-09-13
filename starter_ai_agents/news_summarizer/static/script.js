const button = document.getElementById("summarizeBtn");

const category = document.getElementById("category");
const limit = document.getElementById("limit");

const newsContainer = document.getElementById("newsContainer");
const loading = document.getElementById("loading");
const resultsTitle = document.getElementById("resultsTitle");


button.addEventListener("click", async () => {

    const selectedCategory = category.value;
    const selectedLimit = Number(limit.value);

    // Clear previous results
    newsContainer.innerHTML = "";
    resultsTitle.textContent = "";

    // Show loading
    loading.classList.remove("hidden");

    // Disable button while request is running
    button.disabled = true;
    button.textContent = "Loading...";


    try {

        const response = await fetch("/news", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                category: selectedCategory,
                limit: selectedLimit
            })

        });


        if (!response.ok) {
            throw new Error("Failed to fetch news");
        }


        const data = await response.json();


        // Display category heading
        resultsTitle.textContent =
            `${capitalize(data.category)} News`;


        // Display articles
        displayNews(data.articles);


    } catch (error) {

        newsContainer.innerHTML = `
            <div class="error">
                <strong>Error:</strong>
                ${error.message}
            </div>
        `;

    } finally {

        // Hide loading
        loading.classList.add("hidden");

        // Enable button
        button.disabled = false;
        button.textContent = "Get News";
    }

});


function displayNews(articles) {

    if (!articles || articles.length === 0) {

        newsContainer.innerHTML = `
            <div class="error">
                No news articles found.
            </div>
        `;

        return;
    }


    articles.forEach((article, index) => {

        const card = document.createElement("article");

        card.className = "news-card";


        card.innerHTML = `

            <div class="article-number">
                ${index + 1}
            </div>

            <div class="article-content">

                <h2>
                    ${escapeHTML(article.title)}
                </h2>

                <p>
                    ${escapeHTML(article.summary)}
                </p>

                <a
                    href="${article.link}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Read full article →
                </a>

            </div>

        `;


        newsContainer.appendChild(card);

    });

}


function capitalize(text) {

    if (!text) {
        return "";
    }

    return text.charAt(0).toUpperCase() + text.slice(1);

}


/*
    Prevent article content from being interpreted as HTML.
*/
function escapeHTML(text) {

    if (!text) {
        return "";
    }

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;

}