document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("question");
    const errorMsg = document.getElementById("error-msg");

    form.addEventListener("submit", (e) => {
        if (!input.value.trim()) {
            e.preventDefault();
            errorMsg.textContent = "Please type a message before sending!";
            input.focus();
        } else {
            errorMsg.textContent = "";
        }
    });
});
