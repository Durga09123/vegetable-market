```javascript
document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const button = document.querySelector(".predict-btn");

    if (form && button) {

        form.addEventListener("submit", function () {

            button.disabled = true;

            const text =
                button.querySelector(".btn-text");

            const icon =
                button.querySelector(".btn-icon");

            if (text) {
                text.textContent = "Predicting...";
            }

            if (icon) {
                icon.textContent = "⏳";
            }

        });

    }


    // Smooth scroll to results after prediction

    const results =
        document.querySelector(".results-section");

    if (results) {

        setTimeout(function () {

            results.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        }, 250);

    }

});
```
