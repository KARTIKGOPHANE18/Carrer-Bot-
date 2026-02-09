const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

function sendMessage() {
    const message = userInput.value.trim();
    if (message === "") return;

    addMessage(message, "user");
    userInput.value = "";

    showTyping();

    setTimeout(() => {
        removeTyping();
        const reply = fakeAIReply(message);
        addMessage(reply, "bot");
    }, 1200);
}

function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.className = `message ${sender}`;
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function showTyping() {
    const typing = document.createElement("div");
    typing.className = "message bot typing";
    typing.id = "typing";
    typing.innerText = "CareerBot is typing...";
    chatBox.appendChild(typing);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTyping() {
    const typing = document.getElementById("typing");
    if (typing) typing.remove();
}

function fakeAIReply(userText) {
    const replies = [
        "That’s a great question about your career.",
        "Based on your interest, I suggest improving core technical skills.",
        "You can focus on projects and internships to grow faster.",
        "Would you like a roadmap for this career path?",
        "I can help you with resume and interview preparation."
    ];
    return replies[Math.floor(Math.random() * replies.length)];
}

