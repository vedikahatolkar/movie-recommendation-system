const input = document.getElementById("movieInput");
const suggestions = document.getElementById("suggestions");

input.addEventListener("input", function () {

    const value = this.value.toLowerCase();
    suggestions.innerHTML = "";

    if (!value) return;

    const filtered = movies.filter(movie =>
        movie.toLowerCase().includes(value)
    ).slice(0, 8);  // limit results

    filtered.forEach(movie => {
        const div = document.createElement("div");
        div.classList.add("suggestion-item");
        div.innerText = movie;

        div.onclick = () => {
            input.value = movie;
            suggestions.innerHTML = "";
        };

        suggestions.appendChild(div);
        div.innerHTML = movie.replace(
    new RegExp(value, "gi"),
    match => `<b>${match}</b>`
);
    });
});