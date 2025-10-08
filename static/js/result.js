document.addEventListener("DOMContentLoaded", () => {
    const chatBody = document.getElementById("chat-body");
    if (chatBody) {
        chatBody.scrollTop = chatBody.scrollHeight; // Auto scroll to bottom
    }

    const form = document.getElementById("chatForm");
    const input = document.getElementById("question");

    form.addEventListener("submit", (e) => {
        if (!input.value.trim()) {
            e.preventDefault();
            alert("Please type a message before sending!");
            input.focus();
        }
    });
});
