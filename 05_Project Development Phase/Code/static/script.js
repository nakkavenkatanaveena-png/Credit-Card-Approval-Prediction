document.addEventListener("DOMContentLoaded", function () {

    const inputs = document.querySelectorAll("input");

    inputs.forEach(input => {

        input.addEventListener("focus", function () {
            this.style.backgroundColor = "#eef8ff";
        });

        input.addEventListener("blur", function () {
            this.style.backgroundColor = "white";
        });

    });

    const form = document.querySelector("form");

    form.addEventListener("submit", function () {

        let valid = true;

        inputs.forEach(input => {

            if (input.value === "") {

                valid = false;

                input.style.border = "2px solid red";

            } else {

                input.style.border = "1px solid #ccc";

            }

        });

        if (!valid) {

            alert("Please fill all fields.");

        }

        return valid;

    });

});