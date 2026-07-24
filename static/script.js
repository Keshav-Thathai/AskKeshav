// js
async function sendMessage() {
  

    let message = document.getElementById("message").value;

    if (message == "") {
        alert("Please enter a question");
        return;
    }

    let response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    let data = await response.json();

    document.getElementById("chat-box").innerHTML += `
        <p><b>You:</b> ${message}</p>
        <p><b>AskKeshav:</b> ${data.reply}</p>
        <hr>
    `;

    document.getElementById("message").value = "";
}