const API_URL = "http://localhost:5002/products";

async function loadProducts() {

    try {

        const response = await fetch(API_URL);

        const products = await response.json();

        const container =
            document.getElementById("product-container");

        container.innerHTML = "";

        products.forEach(product => {

            const card = document.createElement("div");

            card.className = "card";

            card.innerHTML = `
                <h3>${product.name}</h3>
                <p>Product ID: ${product.id}</p>
                <p class="price">₹${product.price}</p>
            `;

            container.appendChild(card);
        });

    } catch(error) {

        console.error(error);

        document.getElementById("product-container").innerHTML =
            "<p>Unable to load products.</p>";
    }
}

loadProducts();
